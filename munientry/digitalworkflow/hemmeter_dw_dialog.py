"""Builder for Hemmeter Digital Workflow Dialog."""
import os
from loguru import logger

from munientry.builders import base_builders as base
from munientry.views.hemmeter_workflow_dialog_ui import Ui_HemmeterWorkflowDialog
from munientry.settings import DW_HEMMETER
from munientry.digitalworkflow.workflow_builder import PdfDialogView

class HemmeterWorkflowDialogViewModifier(base.BaseDialogViewModifier):
    """View builder for Hemeter Workflow Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.load_entry_list()

    def load_entry_list(self):
        entry_list = os.listdir(DW_HEMMETER)
        for file in entry_list:
            self.dialog.pending_entries_listWidget.addItem(file)


class HemmeterWorkflowDialogSlotFunctions(base.BaseDialogSlotFunctions):
    """Additional Functions for Hemmeter Workflow Dialog."""

    def open_entry(self):
        selected_entry = self.dialog.pending_entries_listWidget.selectedItems()[0]
        selected_entry = selected_entry.text()
        logger.debug(selected_entry)
        entry = f'{DW_HEMMETER}{selected_entry}'
        logger.debug(entry)
        self.dialog.entry_view = PdfDialogView(entry)

    def create_pdf_view(self, entry):
        return PdfDialogView(entry)


class HemmeterWorkflowDialogSignalConnector(base.BaseDialogSignalConnector):
    """Signal connector for Hemmeter Workflow Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_workflow_buttons()

    def connect_workflow_buttons(self):
        self.dialog.open_entry_Button.released.connect(self.dialog.functions.open_entry)


class HemmeterWorkflowDialog(base.BaseDialogBuilder, Ui_HemmeterWorkflowDialog):
    """Dialog builder class for Hemmeter Digital Workflow."""

    build_dict = {
        'dialog_name': 'Hemmeter Digital Workflow',
        'view': HemmeterWorkflowDialogViewModifier,
        'slots': HemmeterWorkflowDialogSlotFunctions,
        'signals': HemmeterWorkflowDialogSignalConnector,
    }