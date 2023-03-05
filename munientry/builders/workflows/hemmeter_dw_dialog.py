"""Builder for Hemmeter Digital Workflow Dialog."""
import datetime
import os
import shutil

from loguru import logger
from PyQt6.QtWidgets import QButtonGroup, QHeaderView, QTableWidgetItem, QWidget, QRadioButton, QHBoxLayout
from PyQt6 import QtCore

from munientry.builders import base_builders as base
from munientry.views.hemmeter_workflow_dialog_ui import Ui_HemmeterWorkflowDialog
from munientry.appsettings.paths import DW_HEMMETER, DW_APPROVED_DIR, DW_REJECTED_DIR
from munientry.widgets.message_boxes import InfoBox, RequiredBox

ADMIN_ENTRY_PATH = f'{DW_HEMMETER}/Admin//'


class HemmeterWorkflowDialogViewModifier(base.BaseDialogViewModifier):
    """View builder for Hemeter Workflow Dialog."""


class HemmeterWorkflowDialogSignalConnector(base.BaseDialogSignalConnector):
    """Signal connector for Hemmeter Workflow Dialog."""

    def __init__(self, dialog):
        self.dialog = dialog
        self.connect_workflow_buttons()

    def connect_workflow_buttons(self):
        self.dialog.close_dialog_Button.released.connect(self.dialog.close)
        self.dialog.open_entry_Button.released.connect(self.dialog.functions.open_entry)
        self.dialog.complete_workflow_Button.released.connect(
            self.dialog.functions.complete_workflow
        )


class RadioButtonWidget(QWidget):
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
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.addWidget(self.approved)
        self.horizontalLayout.addWidget(self.rejected)


class HemmeterWorkflowDialogSlotFunctions(base.BaseDialogSlotFunctions):
    """Additional Functions for Hemmeter Workflow Dialog."""

    def create_table_on_dialog_load(self):
        self.dialog.entries_tableWidget.insertColumn(0)
        self.dialog.entries_tableWidget.insertColumn(1)
        self.dialog.entries_tableWidget.insertColumn(2)
        self.dialog.entries_tableWidget.insertColumn(3)
        header = self.dialog.entries_tableWidget.horizontalHeader()
        self.dialog.entries_tableWidget.setHorizontalHeaderLabels(
            ['Case Entry', 'Decision', 'Date Created', 'Time Created'],
        )
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        self.load_pending_entries_list()
        for i in range(self.dialog.entries_tableWidget.rowCount()):
            self.dialog.entries_tableWidget.setRowHeight(i, 50)

    def load_pending_entries_list(self):
        pending_entries = os.listdir(self.dialog.entry_path)
        table = self.dialog.entries_tableWidget
        row = 0
        for entry_name in pending_entries:
            entry_creation_time = os.path.getctime(f'{self.dialog.entry_path}{entry_name}')
            date_time_conversion = datetime.datetime.fromtimestamp(entry_creation_time)
            date = date_time_conversion.strftime('%b %d, %Y')
            time = date_time_conversion.strftime('%I:%M %p')
            table.insertRow(row)
            table.setItem(row, 0, QTableWidgetItem(entry_name))
            radio_button = RadioButtonWidget()

            radio_button.buttonGroup.addButton((radio_button.approved))
            radio_button.buttonGroup.addButton((radio_button.rejected))
            table.setItem(row, 1, table.setCellWidget(row, 1, radio_button))
            table.setItem(row, 2, QTableWidgetItem(date))
            table.setItem(row, 3, QTableWidgetItem(time))
            row += 1
        table.setSortingEnabled(True)

    def open_entry(self):
        selected_entry_widget = self.dialog.entries_tableWidget.selectedItems()[0]
        entry_name = selected_entry_widget.text()
        document = f'{self.dialog.entry_path}/{entry_name}'
        os.startfile(document)
        logger.info(f'{document} opened in workflow.')

    def complete_workflow(self):
        logger.debug('complete workflow pressed')
        table = self.dialog.entries_tableWidget
        logger.debug('pre loop')
        logger.debug(table.rowCount())
        for row in range(table.rowCount()):
            logger.debug(table.rowCount())
            logger.debug(row)
            current_file = table.item(row, 0).text()
            logger.debug(current_file)
            current_file_path = os.path.join(ADMIN_ENTRY_PATH, current_file)
            if table.cellWidget(row, 1).approved.isChecked():
                logger.info(f'{current_file} approved')
                destination_directory = DW_APPROVED_DIR
                shutil.move(current_file_path, destination_directory)
            elif table.cellWidget(row, 1).rejected.isChecked():
                logger.info(f'{current_file} rejected')
                destination_directory = DW_REJECTED_DIR
                shutil.move(current_file_path, destination_directory)
        self.update_table()

    def update_table(self):
        table = self.dialog.entries_tableWidget
        for row in reversed(range(table.rowCount())):
            if table.cellWidget(row, 1).approved.isChecked():
                table.removeRow(row)
            if table.cellWidget(row, 1).rejected.isChecked():
                table.removeRow(row)



class HemmeterWorkflowDialog(base.BaseDialogBuilder, Ui_HemmeterWorkflowDialog):
    """Dialog builder class for Hemmeter Digital Workflow."""

    entry_path = ADMIN_ENTRY_PATH
    _signal_connector = HemmeterWorkflowDialogSignalConnector
    _slots = HemmeterWorkflowDialogSlotFunctions
    _view_modifier = HemmeterWorkflowDialogViewModifier
    dialog_name = 'Hemmeter Digital Workflow'

    def __init__(self, parent=None):
        super().__init__(parent)
        self.functions.create_table_on_dialog_load()
