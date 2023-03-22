"""Builder for Admin Judge Digital Workflow Dialog."""
# pylint: disable = E1101
import datetime
import os
import io
import shutil

from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage
from loguru import logger
from PyQt6.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

from munientry.settings.paths import APPROVED_STAMP_PATH, DW_ADMIN_JUDGE, DW_APPROVED_DIR, DW_REJECTED_DIR
from munientry.builders import base_builders as base
from munientry.views.admin_entries_workflow_dialog_ui import Ui_AdminEntriesWorkflowDialog
from munientry.views.magistrate_adoption_workflow_dialog_ui import Ui_MagistrateAdoptionWorkflowDialog
from munientry.widgets.custom_widgets import WorkflowRadioButtonWidget
from munientry.widgets.message_boxes import InfoBox

from munientry.dialogs.workflows.document_reviewer import open_word_document

ADMIN_ENTRY_PATH = f'{DW_ADMIN_JUDGE}/Admin//'
MAGISTRATE_ADOPT_ENTRY_PATH = f'{DW_ADMIN_JUDGE}/MDAdopt//'
COL_FILENAME = 0
COL_DECISION = 1
COL_DATE = 2
COL_TIME = 3
ROW_HEIGHT = 50
DATE_FORMAT = '%B %d, %Y'  # noqa: WPS323
TIME_FORMAT = '%I:%M %p'


def get_entry_date_and_time(entry_path: str, entry_name: str) -> tuple[str, str]:
    """Returns a tuple of the date and time a file was created."""
    entry_path = os.path.join(entry_path, entry_name)
    entry_creation_time = os.path.getctime(entry_path)
    date_time_conversion = datetime.datetime.fromtimestamp(entry_creation_time)
    date = date_time_conversion.strftime(DATE_FORMAT)
    time = date_time_conversion.strftime(TIME_FORMAT)
    return date, time


def get_selected_entry_name(selected_widget: QTableWidgetItem) -> str:
    """Returns the text of widget.

    Raises:
        AttributeError: If no widget is selected.
    """
    if selected_widget is None:
        raise AttributeError
    return selected_widget.text()


def resize_columns(table: QTableWidget) -> None:
    """Sets first column in a table to stretch and remaing to size to contents."""
    header = table.horizontalHeader()
    header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
    for col in range(1, header.count()):
        header.setSectionResizeMode(col, QHeaderView.ResizeMode.ResizeToContents)


class AdminJudgeWorkflowDialogViewModifier(base.BaseDialogViewModifier):
    """View builder for Admin Judge Workflow Dialog."""


class AdminJudgeWorkflowDialogSignalConnector(base.BaseDialogSignalConnector):
    """Signal connector for Admin Judge Workflow Dialog."""

    def __init__(self, dialog) -> None:
        self.dialog = dialog
        self.connect_workflow_buttons()

    def connect_workflow_buttons(self) -> None:
        self.dialog.close_dialog_Button.released.connect(self.dialog.close)
        self.dialog.open_entry_Button.released.connect(self.dialog.functions.open_entry)
        self.dialog.complete_workflow_Button.released.connect(
            self.dialog.functions.complete_workflow,
        )


class AdminJudgeWorkflowDialogSlotFunctions(base.BaseDialogSlotFunctions):
    """Additional Functions for Admin Judge Workflow Dialog."""

    def create_table_on_dialog_load(self) -> None:
        num_columns = 4
        for col in range(num_columns):
            self.dialog.entries_tableWidget.insertColumn(col)

        header_labels = ['Case Entry', 'Decision', 'Date Created', 'Time Created']
        self.dialog.entries_tableWidget.setHorizontalHeaderLabels(header_labels)

        resize_columns(self.dialog.entries_tableWidget)

        self.load_pending_entries_list()
        for row in range(self.dialog.entries_tableWidget.rowCount()):
            self.dialog.entries_tableWidget.setRowHeight(row, ROW_HEIGHT)

    def load_pending_entries_list(self) -> None:
        entries = [
            doc for doc in os.listdir(self.dialog.entry_path) if not doc.startswith('.')
        ]
        table = self.dialog.entries_tableWidget
        for row, entry in enumerate(entries):
            self.create_entry_row(table, row, entry)
        table.setSortingEnabled(True)

    def create_entry_row(self, table_widget: QTableWidget, row: int, entry_name: str) -> None:
        table_widget.insertRow(row)
        table_widget.setItem(row, COL_FILENAME, QTableWidgetItem(entry_name))
        radio_button = WorkflowRadioButtonWidget()
        radio_button.buttonGroup.addButton((radio_button.approved))
        radio_button.buttonGroup.addButton((radio_button.rejected))
        table_widget.setCellWidget(row, COL_DECISION, radio_button)
        date, time = get_entry_date_and_time(self.dialog.entry_path, entry_name)
        table_widget.setItem(row, COL_DATE, QTableWidgetItem(date))
        table_widget.setItem(row, COL_TIME, QTableWidgetItem(time))

    def open_entry(self) -> None:
        selected_entry_widget = self.dialog.entries_tableWidget.selectedItems()[0]
        entry_name = get_selected_entry_name(selected_entry_widget)
        document_path = os.path.join(self.dialog.entry_path, entry_name)
        open_word_document(document_path)
        # try:
        #     selected_entry_widget = self.dialog.entries_tableWidget.selectedItems()[0]
        # except (IndexError) as index:
        #     logger.warning(index)
        #     return InfoBox('No entry was selected to open.', 'No Entry Selected').exec()
        # try:
        #     entry_name = get_selected_entry_name(selected_entry_widget)
        # except (AttributeError) as att:
        #     logger.warning(att)
        #     return InfoBox('No entry was selected to open.', 'No Entry Selected').exec()
        # try:
        #     document = os.path.join(self.dialog.entry_path, entry_name)
        # except (UnboundLocalError) as unbound:
        #     logger.warning(unbound)
        #     return InfoBox('No entry was selected to open.', 'No Entry Selected').exec()
        # logger.info(f'{document} opened in workflow.')
        # return os.startfile(document)

    def complete_workflow(self) -> None:
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
            if table.cellWidget(row, COL_DECISION).approved.isChecked():
                logger.info(f'{current_file} approved')
                approved_entry = self.approve_entry(current_file_path, current_file)
                # os.remove(current_file_path)

            elif table.cellWidget(row, COL_DECISION).rejected.isChecked():
                logger.info(f'{current_file} rejected')
                rejected_entry = self.reject_entry(current_file_path, current_file)
                # os.remove(current_file_path)
        self.update_table()

    def approve_entry(self, current_file_path, filename) -> None:
        doc = DocxTemplate(current_file_path)
        today = datetime.datetime.now()
        date_string = today.strftime(f'{DATE_FORMAT} - {TIME_FORMAT}')
        data_dict = {
            'time_stamp': f'FILED {date_string}',
            'admin_judge_signature': 'Judge Hemmeter',
        }
        doc.render(data_dict)
        doc.save(f'{DW_APPROVED_DIR}{filename}')
        logger.info(f'Entry Created: {filename}')

    def reject_entry(self, current_file_path, filename) -> None:
        doc = DocxTemplate(current_file_path)
        data_dict = {
            'time_stamp': f'REJECTED',
        }
        doc.render(data_dict)
        doc.save(f'{DW_REJECTED_DIR}{filename}')
        logger.info(f'Entry Rejected: {filename}')

    def update_table(self) -> None:
        """Removes rows where a row was approved or rejected.

        Loops in reverse so that removing a row does not affect the row for later
        loops checking rows above it the current row in the table.
        """
        table = self.dialog.entries_tableWidget
        for row in reversed(range(table.rowCount())):
            if table.cellWidget(row, COL_DECISION) is None:
                continue
            if table.cellWidget(row, COL_DECISION).approved.isChecked():
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

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.functions.create_table_on_dialog_load()


class MagistrateAdoptionWorkflowDialog(base.BaseDialogBuilder, Ui_MagistrateAdoptionWorkflowDialog):
    """Dialog builder class for Magistrate Adoption Digital Workflow."""

    entry_path = MAGISTRATE_ADOPT_ENTRY_PATH
    _signal_connector = AdminJudgeWorkflowDialogSignalConnector
    _slots = AdminJudgeWorkflowDialogSlotFunctions
    _view_modifier = AdminJudgeWorkflowDialogViewModifier
    dialog_name = 'Magistrate Adoption Digital Workflow'

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.functions.create_table_on_dialog_load()
