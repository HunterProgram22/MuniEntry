"""Builder for Pretrial Digital Workflow Dialog."""
import datetime
import os

from loguru import logger
from PyQt6.QtWidgets import QHeaderView, QTableWidgetItem

from munientry.appsettings.paths import DW_PROBATION
from munientry.builders import base_builders as base
from munientry.views.com_control_workflow_dialog_ui import Ui_ComControlWorkflowDialog
from munientry.views.pretrial_workflow_dialog_ui import Ui_PretrialWorkflowDialog
from munientry.widgets.message_boxes import InfoBox, RequiredBox

SCRAM_PATH = f'{DW_PROBATION}/Scram_Gps//'
COM_CONTROL_PATH = f'{DW_PROBATION}/Comm_Control//'


class ProbationWorkflowDialogViewModifier(base.BaseDialogViewModifier):
    """View builder for Probation Workflow Dialogs."""


class ProbationWorkflowDialogSignalConnector(base.BaseDialogSignalConnector):
    """Signal connector for Probation Workflow Dialogs."""

    def __init__(self, dialog):
        self.dialog = dialog
        self.connect_workflow_buttons()

    def connect_workflow_buttons(self):
        self.dialog.close_dialog_Button.released.connect(self.dialog.close)
        self.dialog.open_entry_Button.released.connect(self.dialog.functions.open_entry)
        self.dialog.delete_entry_Button.released.connect(self.dialog.functions.delete_entry)
        self.dialog.load_new_entries_Button.released.connect(self.dialog.functions.load_new_entries)


class ProbationWorkflowDialogSlotFunctions(base.BaseDialogSlotFunctions):
    """Additional Functions for Probation Workflow Dialog."""

    def create_table_on_dialog_load(self):
        self.dialog.entries_tableWidget.insertColumn(0)
        self.dialog.entries_tableWidget.insertColumn(1)
        self.dialog.entries_tableWidget.insertColumn(2)
        header = self.dialog.entries_tableWidget.horizontalHeader()
        self.dialog.entries_tableWidget.setHorizontalHeaderLabels(
            ['Case Entry', 'Date Created', 'Time Created'],
        )
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.load_pending_entries_list()

    def load_pending_entries_list(self):
        pending_entries = os.listdir(self.dialog.entry_path)
        row = 0
        for entry_name in pending_entries:
            entry_creation_time = os.path.getctime(f'{self.dialog.entry_path}{entry_name}')
            date_time_conversion = datetime.datetime.fromtimestamp(entry_creation_time)
            date = date_time_conversion.strftime('%b %d, %Y')
            time = date_time_conversion.strftime('%I:%M %p')
            self.dialog.entries_tableWidget.insertRow(row)
            self.dialog.entries_tableWidget.setItem(row, 0, QTableWidgetItem(entry_name))
            self.dialog.entries_tableWidget.setItem(row, 1, QTableWidgetItem(date))
            self.dialog.entries_tableWidget.setItem(row, 2, QTableWidgetItem(time))
            row += 1
        self.dialog.entries_tableWidget.setSortingEnabled(True)

    def open_entry(self):
        """Opens the selected entry.

        Provides instructions if no entry is selected.
        """
        if len(self.dialog.entries_tableWidget.selectedItems()) == 0:
            message = 'No entry is selected. You must select an entry to open.'
            return RequiredBox(message).exec()
        if len(self.dialog.entries_tableWidget.selectedItems()) == 1:
            if self.dialog.entries_tableWidget.selectedItems()[0].column() != 0:
                message = 'Must select a single from from the Case Entry column to open a document.'
                return RequiredBox(message).exec()
            selected_entry_widget = self.dialog.entries_tableWidget.selectedItems()[0]
            entry_name = selected_entry_widget.text()
            document = f'{self.dialog.entry_path}/{entry_name}'
            os.startfile(document)
            logger.info(f'{document} opened in workflow.')
        else:
            message = 'Must select only a single row from the Case Entry column to open a document.'
            return RequiredBox(message).exec()

    def delete_entry(self):
        if len(self.dialog.entries_tableWidget.selectedItems()) == 0:
            message = 'No entry is selected. You must select an entry to delete.'
            return RequiredBox(message).exec()
        if len(self.dialog.entries_tableWidget.selectedItems()) == 1:
            if self.dialog.entries_tableWidget.selectedItems()[0].column() != 0:
                message = 'Must select a single from from the Case Entry column to delete a document.'
                return RequiredBox(message).exec()
            selected_entry_widget = self.dialog.entries_tableWidget.selectedItems()[0]
            entry_name = selected_entry_widget.text()
            entries_table = self.dialog.entries_tableWidget
            document = f'{self.dialog.entry_path}/{entry_name}'
            row = entries_table.row(selected_entry_widget)
            entries_table.removeRow(row)
            try:
                os.remove(document)
                logger.info(f'{document} deleted in workflow.')
            except PermissionError as error:
                message = 'The document is currently in use by another user and cannot be deleted until' \
                          ' they close the document.'
                InfoBox(message).exec()
                logger.warning(error)
        else:
            message = 'Must select only a single row from the Case Entry column to delete a document.'
            return RequiredBox(message).exec()

    def load_new_entries(self):
        """Need to fix as message shows no cases loaded if one loads cases and other list doesnt."""
        pending_entries = os.listdir(f'{self.dialog.entry_path}')
        if len(pending_entries) == self.dialog.entries_tableWidget.rowCount():
            message = 'There were no new entries availalbe to load.'
            return InfoBox(message, 'No Entries to Load').exec()
        if len(pending_entries) != self.dialog.entries_tableWidget.rowCount():
            entry_count = self.dialog.entries_tableWidget.rowCount()
            while entry_count >= 0:
                self.dialog.entries_tableWidget.removeRow(0)
                entry_count -= 1
            self.load_pending_entries_list()


class ProbationWorkflowDialog(base.BaseDialogBuilder):
    """Based Dialog builder class for Probation Digital Workflows."""

    _signal_connector = ProbationWorkflowDialogSignalConnector
    _slots = ProbationWorkflowDialogSlotFunctions
    _view_modifier = ProbationWorkflowDialogViewModifier

    def __init__(self, parent=None):
        super().__init__(parent)
        self.functions.create_table_on_dialog_load()


class ComControlWorkflowDialog(ProbationWorkflowDialog, Ui_ComControlWorkflowDialog):
    """Dialog builder class for Community Control Digital Workflow."""

    entry_path = COM_CONTROL_PATH
    dialog_name = 'Community Control Digital Workflow'


class PretrialWorkflowDialog(ProbationWorkflowDialog, Ui_PretrialWorkflowDialog):
    """Dialog builder class for Pretrial Digital Workflow."""

    entry_path = SCRAM_PATH
    dialog_name = 'Pretrial Digital Workflow'
