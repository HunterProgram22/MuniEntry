"""Builder for Hemmeter Digital Workflow Dialog."""
import os
import shutil
from loguru import logger

from munientry.builders import base_builders as base
from munientry.views.hemmeter_workflow_dialog_ui import Ui_HemmeterWorkflowDialog
from munientry.settings import DW_APPROVED_DIR, DW_HEMMETER
from munientry.digitalworkflow.workflow_builder import PdfDialogView

class HemmeterWorkflowDialogViewModifier(base.BaseDialogViewModifier):
    """View builder for Hemeter Workflow Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.load_pending_entries_list()

    def load_pending_entries_list(self):
        pending_entries_list = os.listdir(DW_HEMMETER)
        for file in pending_entries_list:
            self.dialog.pending_entries_listWidget.addItem(file)


class HemmeterWorkflowDialogSlotFunctions(base.BaseDialogSlotFunctions):
    """Additional Functions for Hemmeter Workflow Dialog."""

    def open_entry(self):
        selected_entry_widget = self.dialog.pending_entries_listWidget.selectedItems()[0]
        entry_name = selected_entry_widget.text()
        document = f'{DW_HEMMETER}{entry_name}'
        self.dialog.entry_view = PdfDialogView(document, selected_entry_widget, self.dialog)

    def complete_workflow(self):
        row_count = self.dialog.approved_entries_listWidget.count()
        row = 0
        while row < row_count:
            entry = self.dialog.approved_entries_listWidget.takeItem(0)
            entry_name = entry.text()
            document = f'{DW_HEMMETER}{entry_name}'
            shutil.move(document, DW_APPROVED_DIR)
            row +=1


class HemmeterWorkflowDialogSignalConnector(base.BaseDialogSignalConnector):
    """Signal connector for Hemmeter Workflow Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_workflow_buttons()

    def connect_workflow_buttons(self):
        self.dialog.open_entry_Button.released.connect(self.dialog.functions.open_entry)
        self.dialog.complete_workflow_Button.released.connect(
            self.dialog.functions.complete_workflow
        )


class HemmeterWorkflowDialog(base.BaseDialogBuilder, Ui_HemmeterWorkflowDialog):
    """Dialog builder class for Hemmeter Digital Workflow."""

    build_dict = {
        'dialog_name': 'Hemmeter Digital Workflow',
        'view': HemmeterWorkflowDialogViewModifier,
        'slots': HemmeterWorkflowDialogSlotFunctions,
        'signals': HemmeterWorkflowDialogSignalConnector,
    }