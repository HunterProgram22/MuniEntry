"""Module containing custom widgets.

If using QtDesigner for creation of the Ui file you must promote the widget to one of the custom
widgets that is used. The header file for this module must then be added in QtDesigner so that
when the file is converted using 'pyuic6 -o {python_view_file.py} {qt_ui_file.ui}' this
module will be imported as part of the python_view_file.py.
"""
from loguru import logger
from PyQt6.QtCore import QDate, QTime
from PyQt6.QtWidgets import QCheckBox, QDateEdit, QPushButton, QTimeEdit, QWidget, QRadioButton, \
    QButtonGroup, QHBoxLayout

from munientry.widgets.widget_settings import (
    DATE_FORMAT,
    DEFAULT_TIME_STRING,
    EVENT_WHEEL_EVENT,
    NO_FOCUS,
    STRONG_FOCUS,
    TIME_FORMAT,
    TODAY,
    TODAY_STRING,
)


class NoScrollDateEdit(QDateEdit):
    """Custom DateEdit used to ignore wheel scroll from the mouse."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(STRONG_FOCUS)
        self.setDate(TODAY)

    def get_date_as_string(self) -> str:
        return self.date().toString(DATE_FORMAT)

    def set_date_from_string(self, date_str: str) -> QDate:
        if date_str is None:
            date_str = TODAY_STRING
        date_str = QDate.fromString(date_str, DATE_FORMAT)
        return self.setDate(date_str)

    def wheelEvent(self, event):
        if event == EVENT_WHEEL_EVENT:
            event.ignore()


class NoScrollTimeEdit(QTimeEdit):
    """Custom TimeEdit used to ignore wheel scroll from the mouse."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(STRONG_FOCUS)

    def get_time_as_string(self) -> str:
        return self.time().toString(TIME_FORMAT)

    def set_time_from_string(self, time_str: str) -> QTime:
        if time_str is None:
            time_str = DEFAULT_TIME_STRING
        time_str = QTime.fromString(time_str, TIME_FORMAT)
        return self.setTime(time_str)

    def wheelEvent(self, event):
        if event == EVENT_WHEEL_EVENT:
            event.ignore()


class ChargeGridDeleteButton(QPushButton):
    """Custom PushButton used for deleting charges from the charge grids."""

    def __init__(self, column, charge, dialog, parent=None):
        super().__init__(parent)
        self.column_index = column
        self.charge = charge
        self.dialog = dialog
        self.set_up_widget()

    def set_up_widget(self):
        self.setStyleSheet('background-color: rgb(170, 58, 63);')
        self.setText('Delete')
        self.setObjectName('charge_grid_delete_Button')
        self.setFocusPolicy(NO_FOCUS)
        self.pressed.connect(self.delete_charge_from_grid_and_charges_list)

    def delete_charge_from_grid_and_charges_list(self):
        """Uses the delete_button indexed to the column to delete the QLabels for the charge."""
        logger.info(f'Deleted Charge: {self.charge}, col={self.column_index}')
        self.dialog.entry_case_information.charges_list.remove(self.charge)
        for row in range(self.dialog.charges_gridLayout.rowCount()):
            layout_item = self.dialog.charges_gridLayout.itemAtPosition(row, self.column_index)
            if layout_item is not None:
                layout_item.widget().deleteLater()
                self.dialog.charges_gridLayout.removeItem(layout_item)


class ChargeGridAmendButton(QPushButton):
    """Custom PushButton used to amend a charge in the charge grid."""

    def __init__(self, column, charge, dialog, parent=None):
        super().__init__(parent)
        self.column_index = column
        self.charge = charge
        self.dialog = dialog
        self.set_up_widget()

    def set_up_widget(self):
        self.setStyleSheet('background-color: rgb(62, 146, 255);')
        self.setText('Amend')
        self.setObjectName('charge_grid_amend_Button')
        self.setFocusPolicy(NO_FOCUS)
        self.released.connect(self.dialog.functions.start_amend_offense_dialog)


class ConditionCheckbox(QCheckBox):
    """Custom CheckBox used for logging."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.toggled.connect(self.log_toggle)

    def log_toggle(self):
        checkbox_text = self.sender().text()
        checkbox_bool = self.sender().isChecked()
        logger.button(f'{checkbox_text} Checkbox Set: {checkbox_bool}')


class AlliedCheckbox(QCheckBox):
    """Custom CheckBox used for auto-setting Finding box in charge grid when allied offense."""

    def __init__(self, column_index, dialog, parent=None):
        super().__init__(parent)
        self.column_index = column_index
        self.dialog = dialog
        self.set_up_widget()

    def set_up_widget(self):
        self.setText('Allied Offense')
        self.setObjectName('allied_checkBox')
        self.setFocusPolicy(STRONG_FOCUS)
        self.toggled.connect(self.set_to_allied)

    def set_to_allied(self):
        logger.button(f'Allied Checkbox Set: {self.isChecked()}')
        grid = self.dialog.charges_gridLayout
        finding_box = grid.itemAtPosition(grid.row_finding, self.column_index).widget()
        if self.isChecked():
            try:
                if finding_box.currentText() == 'Guilty':
                    finding_box.setCurrentText('Guilty - Allied Offense')
                elif finding_box.currentText() == 'Not Guilty':
                    finding_box.setCurrentText('Not Guilty - Allied Offense')
            except AttributeError as error:
                logger.warning(error)
        else:
            try:
                if finding_box.currentText() == 'Guilty - Allied Offense':
                    finding_box.setCurrentText('Guilty')
                elif finding_box.currentText() == 'Not Guilty - Allied Offense':
                    finding_box.setCurrentText('Not Guilty')
            except AttributeError as error_two:
                logger.warning(error_two)


class DismissedCheckbox(QCheckBox):
    """Custom CheckBox used for disabling unneeded charge grid fields when charge is dismissed."""

    def __init__(self, column_index, dialog, parent=None):
        super().__init__(parent)
        self.dialog = dialog
        self.column_index = column_index
        self.set_up_widget()

    def set_up_widget(self):
        self.setText('Offense Dismissed')
        self.setObjectName('dismissed_checkBox')
        self.setFocusPolicy(STRONG_FOCUS)
        self.toggled.connect(self.set_to_dismissed)

    def set_to_dismissed(self):
        """TODO: the try except block is bc Leap Dialogs and NoJail not having same # rows. Fix."""
        logger.button(f'Dismissed Checkbox Set: {self.isChecked()}')
        grid = self.dialog.charges_gridLayout
        col = self.column_index
        if self.isChecked():
            try:
                grid.itemAtPosition(grid.row_plea, col).widget().setCurrentText('Dismissed')
            except AttributeError as error:
                logger.warning(error)
            try:
                grid.itemAtPosition(grid.row_finding, col).widget().setHidden(True)
                grid.itemAtPosition(grid.row_fine, col).widget().setHidden(True)
                grid.itemAtPosition(grid.row_fine_suspended, col).widget().setHidden(True)
                grid.itemAtPosition(grid.row_jail_days, col).widget().setHidden(True)
                grid.itemAtPosition(grid.row_jail_days_suspended, col).widget().setHidden(True)
                grid.itemAtPosition(grid.row_amend_button, col).widget().setHidden(True)
                grid.itemAtPosition(grid.row_delete_button, col).widget().setHidden(True)
            except AttributeError as error_one:
                logger.warning(error_one)
        else:
            try:
                grid.itemAtPosition(grid.row_plea, col).widget().setCurrentText('')
            except AttributeError as error_two:
                logger.warning(error_two)
            try:
                grid.itemAtPosition(grid.row_finding, col).widget().setHidden(False)
                grid.itemAtPosition(grid.row_fine, col).widget().setHidden(False)
                grid.itemAtPosition(grid.row_fine_suspended, col).widget().setHidden(False)
                grid.itemAtPosition(grid.row_jail_days, col).widget().setHidden(False)
                grid.itemAtPosition(grid.row_jail_days_suspended, col).widget().setHidden(False)
                grid.itemAtPosition(grid.row_amend_button, col).widget().setHidden(False)
                grid.itemAtPosition(grid.row_delete_button, col).widget().setHidden(False)
            except AttributeError as error_three:
                logger.warning(error_three)


# DataValidator Widgets


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')


class WorkflowRadioButtonWidget(QWidget):
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
