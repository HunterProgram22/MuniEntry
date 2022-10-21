"""Builder for Probation Digital Workflow Dialog."""
import os
import shutil
from loguru import logger

from munientry.digitalworkflow.workflow_tools import add_approved_stamp, PdfViewer
from munientry.builders import base_builders as base
from munientry.views.probation_workflow_dialog_ui import Ui_ProbationWorkflowDialog
from munientry.settings import DW_PROBATION


class ProbationWorkflowDialogViewModifier(base.BaseDialogViewModifier):
    """View builder for Probation Workflow Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.load_pending_entries_list()

    def load_pending_entries_list(self):
        pending_entries_list = os.listdir(DW_PROBATION)
        for file in pending_entries_list:
            self.dialog.scram_gps_entries_listWidget.addItem(file)


class ProbationWorkflowDialogSlotFunctions(base.BaseDialogSlotFunctions):
    """Additional Functions for Probation Workflow Dialog."""

    def open_entry(self):
        selected_entry_widget = self.dialog.scram_gps_entries_listWidget.selectedItems()[0]
        entry_name = selected_entry_widget.text()
        document = f'{DW_PROBATION}{entry_name}'
        self.dialog.entry_view = PdfViewer(document, selected_entry_widget, self.dialog)


class ProbationWorkflowDialogSignalConnector(base.BaseDialogSignalConnector):
    """Signal connector for Probation Workflow Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_workflow_buttons()

    def connect_workflow_buttons(self):
        self.dialog.open_entry_Button.released.connect(self.dialog.functions.open_entry)


class ProbationWorkflowDialog(base.BaseDialogBuilder, Ui_ProbationWorkflowDialog):
    """Dialog builder class for Probation Digital Workflow."""

    build_dict = {
        'dialog_name': 'Probation Digital Workflow',
        'view': ProbationWorkflowDialogViewModifier,
        'slots': ProbationWorkflowDialogSlotFunctions,
        'signals': ProbationWorkflowDialogSignalConnector,
    }
