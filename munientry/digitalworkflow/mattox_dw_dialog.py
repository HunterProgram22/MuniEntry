"""Builder for Mattox Digital Workflow Dialog."""
import os

from munientry.digitalworkflow.workflow_tools import PdfViewer
from munientry.builders import base_builders as base
from munientry.views.mattox_workflow_dialog_ui import Ui_MattoxWorkflowDialog
from munientry.settings import DW_MATTOX


class MattoxWorkflowDialogViewModifier(base.BaseDialogViewModifier):
    """View builder for Mattox Workflow Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.load_pending_entries_list()

    def load_pending_entries_list(self):
        pending_entries_list = os.listdir(DW_MATTOX)
        for file in pending_entries_list:
            self.dialog.scram_gps_entries_listWidget.addItem(file)


class MattoxWorkflowDialogSlotFunctions(base.BaseDialogSlotFunctions):
    """Additional Functions for Mattox Workflow Dialog."""

    def open_entry(self):
        selected_entry_widget = self.dialog.scram_gps_entries_listWidget.selectedItems()[0]
        entry_name = selected_entry_widget.text()
        document = f'{DW_MATTOX}{entry_name}'
        self.dialog.entry_view = PdfViewer(document, selected_entry_widget, self.dialog)


class MattoxWorkflowDialogSignalConnector(base.BaseDialogSignalConnector):
    """Signal connector for Mattox Workflow Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_workflow_buttons()

    def connect_workflow_buttons(self):
        self.dialog.open_entry_Button.released.connect(self.dialog.functions.open_entry)


class MattoxWorkflowDialog(base.BaseDialogBuilder, Ui_MattoxWorkflowDialog):
    """Dialog builder class for Mattox Digital Workflow."""

    build_dict = {
        'dialog_name': 'Mattox Digital Workflow',
        'view': MattoxWorkflowDialogViewModifier,
        'slots': MattoxWorkflowDialogSlotFunctions,
        'signals': MattoxWorkflowDialogSignalConnector,
    }
