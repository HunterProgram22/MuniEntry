"""Builder for Mattox Digital Workflow Dialog."""
import os

from munientry.digitalworkflow.workflow_tools import PdfViewer
from munientry.builders import base_builders as base
from munientry.views.mattox_workflow_dialog_ui import Ui_MattoxWorkflowDialog
from munientry.widgets.message_boxes import RequiredBox
from munientry.settings import DW_MATTOX


class MattoxWorkflowDialogViewModifier(base.BaseDialogViewModifier):
    """View builder for Mattox Workflow Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.load_pending_entries_list()

    def load_pending_entries_list(self):
        pending_scram_gps_entries = os.listdir(f'{DW_MATTOX}/Scram_Gps//')
        for file in pending_scram_gps_entries:
            self.dialog.scram_gps_entries_listWidget.addItem(file)
        pending_comm_control_entries = os.listdir(f'{DW_MATTOX}/Comm_Control//')
        for file in pending_comm_control_entries:
            self.dialog.community_control_entries_listWidget.addItem(file)


class MattoxWorkflowDialogSlotFunctions(base.BaseDialogSlotFunctions):
    """Additional Functions for Mattox Workflow Dialog."""

    def open_entry(self):
        if len(self.dialog.scram_gps_entries_listWidget.selectedItems()) == 1:
            selected_entry_widget = self.dialog.scram_gps_entries_listWidget.selectedItems()[0]
            entry_name = selected_entry_widget.text()
            document = f'{DW_MATTOX}/Scram_GPS/{entry_name}'
        elif len(self.dialog.community_control_entries_listWidget.selectedItems()) == 1:
            selected_entry_widget = self.dialog.community_control_entries_listWidget.selectedItems()[0]
            entry_name = selected_entry_widget.text()
            document = f'{DW_MATTOX}/Comm_Control/{entry_name}'
        else:
            message = 'No entry is selected. You must select an entry to open.'
            return RequiredBox(message).exec()
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
