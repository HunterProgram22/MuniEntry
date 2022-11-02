"""Builder for Mattox Digital Workflow Dialog."""
import os

from loguru import logger

from munientry.builders import base_builders as base
from munientry.views.mattox_workflow_dialog_ui import Ui_MattoxWorkflowDialog
from munientry.widgets.message_boxes import InfoBox, RequiredBox
from munientry.appsettings.paths import DW_MATTOX


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
        """Opens the selected entry.

        Provides instructions if multiple entries or no entries are selected.
        """
        if (
            len(self.dialog.scram_gps_entries_listWidget.selectedItems()) == 0
            and len(self.dialog.community_control_entries_listWidget.selectedItems()) == 0
        ):
            message = 'No entry is selected. You must select an entry to open.'
            return RequiredBox(message).exec()
        if (
            len(self.dialog.scram_gps_entries_listWidget.selectedItems()) == 1
            and len(self.dialog.community_control_entries_listWidget.selectedItems()) == 1
        ):
            message = 'You have selected an entry in both lists. Please unselect an entry by ' \
                      'by clicking in blank space of the list for the entry you want to unselect.'
            return RequiredBox(message).exec()
        if len(self.dialog.scram_gps_entries_listWidget.selectedItems()) == 1:
            selected_entry_widget = self.dialog.scram_gps_entries_listWidget.selectedItems()[0]
            entry_name = selected_entry_widget.text()
            document = f'{DW_MATTOX}/Scram_GPS/{entry_name}'
        elif len(self.dialog.community_control_entries_listWidget.selectedItems()) == 1:
            selected_entry_widget = self.dialog.community_control_entries_listWidget.selectedItems()[0]
            entry_name = selected_entry_widget.text()
            document = f'{DW_MATTOX}/Comm_Control/{entry_name}'
        os.startfile(document)
        logger.info(f'{document} opened in workflow.')

    def delete_entry(self):
        if (
                len(self.dialog.scram_gps_entries_listWidget.selectedItems()) == 0
                and len(self.dialog.community_control_entries_listWidget.selectedItems()) == 0
        ):
            message = 'No entry is selected. You must select an entry to delete.'
            return RequiredBox(message).exec()
        if (
                len(self.dialog.scram_gps_entries_listWidget.selectedItems()) == 1
                and len(self.dialog.community_control_entries_listWidget.selectedItems()) == 1
        ):
            message = 'You have selected an entry in both lists. Please unselect an entry by ' \
                      'by clicking in blank space of the list for the entry you want to unselect.'
            return RequiredBox(message).exec()
        if len(self.dialog.scram_gps_entries_listWidget.selectedItems()) == 1:
            selected_entry_widget = self.dialog.scram_gps_entries_listWidget.selectedItems()[0]
            entry_name = selected_entry_widget.text()
            widget_list = self.dialog.scram_gps_entries_listWidget
            document = f'{DW_MATTOX}/Scram_GPS/{entry_name}'
        elif len(self.dialog.community_control_entries_listWidget.selectedItems()) == 1:
            selected_entry_widget = self.dialog.community_control_entries_listWidget.selectedItems()[0]
            entry_name = selected_entry_widget.text()
            widget_list = self.dialog.community_control_entries_listWidget
            document = f'{DW_MATTOX}/Comm_Control/{entry_name}'
        row = widget_list.row(selected_entry_widget)
        widget_list.takeItem(row)
        try:
            os.remove(document)
            logger.info(f'{document} deleted in workflow.')
        except PermissionError as error:
            message = 'The document is currently in use by another user and cannot be deleted until' \
                      ' they close the document.'
            InfoBox(message).exec()
            logger.warning(error)

    def load_new_entries(self):
        """Need to fix as message shows no cases loaded if one loads cases and other list doesnt."""
        pending_scram_gps_entries = os.listdir(f'{DW_MATTOX}/Scram_Gps//')
        pending_comm_control_entries = os.listdir(f'{DW_MATTOX}/Comm_Control//')
        if (
            len(pending_scram_gps_entries) == self.dialog.scram_gps_entries_listWidget.count()
            and len(pending_comm_control_entries) == self.dialog.community_control_entries_listWidget.count()
        ):
            message = 'There were no new entries availalbe to load.'
            return InfoBox(message, 'No Entries to Load').exec()
        if len(pending_scram_gps_entries) != self.dialog.scram_gps_entries_listWidget.count():
            scram_entry_count = self.dialog.scram_gps_entries_listWidget.count()
            while scram_entry_count >= 0:
                self.dialog.scram_gps_entries_listWidget.takeItem(0)
                scram_entry_count -= 1
            for file in pending_scram_gps_entries:
                self.dialog.scram_gps_entries_listWidget.addItem(file)
        if len(pending_comm_control_entries) != self.dialog.community_control_entries_listWidget.count():
            comm_entry_count = self.dialog.community_control_entries_listWidget.count()
            while comm_entry_count >= 0:
                self.dialog.community_control_entries_listWidget.takeItem(0)
                comm_entry_count -= 1
            for file in pending_comm_control_entries:
                self.dialog.community_control_entries_listWidget.addItem(file)


class MattoxWorkflowDialogSignalConnector(base.BaseDialogSignalConnector):
    """Signal connector for Mattox Workflow Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_workflow_buttons()

    def connect_workflow_buttons(self):
        self.dialog.open_entry_Button.released.connect(self.dialog.functions.open_entry)
        self.dialog.delete_entry_Button.released.connect(self.dialog.functions.delete_entry)
        self.dialog.load_new_entries_Button.released.connect(self.dialog.functions.load_new_entries)


class MattoxWorkflowDialog(base.BaseDialogBuilder, Ui_MattoxWorkflowDialog):
    """Dialog builder class for Mattox Digital Workflow."""

    build_dict = {
        'dialog_name': 'Mattox Digital Workflow',
        'view': MattoxWorkflowDialogViewModifier,
        'slots': MattoxWorkflowDialogSlotFunctions,
        'signals': MattoxWorkflowDialogSignalConnector,
    }
