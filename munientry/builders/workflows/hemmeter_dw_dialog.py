"""Builder for Admin Judge Digital Workflow Dialog."""
import datetime
import os
import shutil

from loguru import logger
from PyQt6.QtWidgets import QButtonGroup, QHeaderView, QTableWidgetItem, QWidget, QRadioButton, QHBoxLayout
from PyQt6 import QtCore

from munientry.builders import base_builders as base
from munientry.views.admin_entries_workflow_dialog_ui import Ui_AdminEntriesWorkflowDialog
from munientry.appsettings.paths import DW_HEMMETER, DW_APPROVED_DIR, DW_REJECTED_DIR
from munientry.widgets.message_boxes import InfoBox, RequiredBox

ADMIN_ENTRY_PATH = f'{DW_HEMMETER}/Admin//'
COL_FILENAME = 0
COL_DECISION = 1
COL_DATE = 2
COL_TIME = 3
ROW_HEIGHT = 50
DATE_FORMAT = '%b %d, %Y'
TIME_FORMAT = '%I:%M %p'

class DigitalWorkflowRadioButtonWidget(QWidget):
    """A Widget with two radio buttons for approving or rejecting a decision."""

    def __init__(self):
        super().__init__()
        self.approved = QRadioButton()
        self.approved.setText('Approved')
        self.rejected = QRadioButton()
        self.rejected.setText('Rejected')
        self.buttonGroup = QButtonGroup()
        self.buttonGroup.addButton(self.approved)
        self.buttonGroup.addButton(self.rejected)
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.horizontalLayout.addWidget(self.approved)
        self.horizontalLayout.addWidget(self.rejected)


class AdminJudgeWorkflowDialogViewModifier(base.BaseDialogViewModifier):
    """View builder for Admin Judge Workflow Dialog."""


class AdminJudgeWorkflowDialogSignalConnector(base.BaseDialogSignalConnector):
    """Signal connector for Admin Judge Workflow Dialog."""

    def __init__(self, dialog):
        self.dialog = dialog
        self.connect_workflow_buttons()

    def connect_workflow_buttons(self):
        self.dialog.close_dialog_Button.released.connect(self.dialog.close)
        self.dialog.open_entry_Button.released.connect(self.dialog.functions.open_entry)
        self.dialog.complete_workflow_Button.released.connect(
            self.dialog.functions.complete_workflow
        )


class AdminJudgeWorkflowDialogSlotFunctions(base.BaseDialogSlotFunctions):
    """Additional Functions for Admin Judge Workflow Dialog."""

    def create_table_on_dialog_load(self):
        num_columns = 4
        for i in range(num_columns):
            self.dialog.entries_tableWidget.insertColumn(i)

        header_labels = ['Case Entry', 'Decision', 'Date Created', 'Time Created']
        self.dialog.entries_tableWidget.setHorizontalHeaderLabels(header_labels)

        self._resize_columns(self.dialog.entries_tableWidget)

        self.load_pending_entries_list()
        for i in range(self.dialog.entries_tableWidget.rowCount()):
            self.dialog.entries_tableWidget.setRowHeight(i, ROW_HEIGHT)

    def _resize_columns(self, table):
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)

    def load_pending_entries_list(self):
        entries = [
            entry for entry in os.listdir(self.dialog.entry_path) if not entry.startswith('.')
        ]
        table = self.dialog.entries_tableWidget
        for row, entry in enumerate(entries):
            entry_path = os.path.join(self.dialog.entry_path, entry)
            entry_creation_time = os.path.getctime(entry_path)
            date_time_conversion = datetime.datetime.fromtimestamp(entry_creation_time)
            date = date_time_conversion.strftime(DATE_FORMAT)
            time = date_time_conversion.strftime(TIME_FORMAT)
            self.create_entry_row(table, row, entry, date, time)
        table.setSortingEnabled(True)

    def create_entry_row(self, table_widget, row, entry_name, date, time):
        table_widget.insertRow(row)
        table_widget.setItem(row, COL_FILENAME, QTableWidgetItem(entry_name))
        radio_button = DigitalWorkflowRadioButtonWidget()
        radio_button.buttonGroup.addButton((radio_button.approved))
        radio_button.buttonGroup.addButton((radio_button.rejected))
        table_widget.setCellWidget(row, COL_DECISION, radio_button)
        table_widget.setItem(row, COL_DATE, QTableWidgetItem(date))
        table_widget.setItem(row, COL_TIME, QTableWidgetItem(time))

    def open_entry(self):
        try:
            selected_entry_widget = self.dialog.entries_tableWidget.selectedItems()[0]
            entry_name = self.get_selected_entry_name(selected_entry_widget)
            document = os.path.join(self.dialog.entry_path, entry_name)
            os.startfile(document)
            logger.info(f'{document} opened in workflow.')
        except (IndexError, AttributeError):
            InfoBox('No entry was selected to open.', 'No Entry Selected').exec()
            logger.warning('No entry selected.')

    def get_selected_entry_name(self, selected_entry_widget):
        if selected_entry_widget is None:
            raise AttributeError
        return selected_entry_widget.text()

    def complete_workflow(self):
        """Loops through table rows and moves files if approved or rejected.

        The table rows are not removed until after all files are moved so that the
        rows of the table will not change during the loop.
        """
        table = self.dialog.entries_tableWidget
        for row in range(table.rowCount()):
            current_file = table.item(row, COL_FILENAME).text()
            current_file_path = os.path.join(ADMIN_ENTRY_PATH, current_file)
            if table.cellWidget(row, COL_DECISION) is None:
                continue
            elif table.cellWidget(row, COL_DECISION).approved.isChecked():
                logger.info(f'{current_file} approved')
                destination_directory = DW_APPROVED_DIR
                shutil.move(current_file_path, destination_directory)
            elif table.cellWidget(row, COL_DECISION).rejected.isChecked():
                logger.info(f'{current_file} rejected')
                destination_directory = DW_REJECTED_DIR
                shutil.move(current_file_path, destination_directory)
        self.update_table()

    def update_table(self):
        """Removes rows where a row was approved or rejected.

        Loops in reverse so that removing a row does not affect the row for later
        loops checking rows above it the current row in the table.
        """
        table = self.dialog.entries_tableWidget
        for row in reversed(range(table.rowCount())):
            if table.cellWidget(row, COL_DECISION) is None:
                continue
            elif table.cellWidget(row, COL_DECISION).approved.isChecked():
                table.removeRow(row)
            elif table.cellWidget(row, COL_DECISION).rejected.isChecked():
                table.removeRow(row)


class AdminWorkflowDialog(base.BaseDialogBuilder, Ui_AdminEntriesWorkflowDialog):
    """Dialog builder class for Admin Entries Digital Workflow."""

    entry_path = ADMIN_ENTRY_PATH
    _signal_connector = AdminJudgeWorkflowDialogSignalConnector
    _slots = AdminJudgeWorkflowDialogSlotFunctions
    _view_modifier = AdminJudgeWorkflowDialogViewModifier
    dialog_name = 'Admin Entries Digital Workflow'

    def __init__(self, parent=None):
        super().__init__(parent)
        self.functions.create_table_on_dialog_load()
