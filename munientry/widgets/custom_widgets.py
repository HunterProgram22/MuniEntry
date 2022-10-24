"""Module containing custom widgets.

If using QtDesigner for creation of the Ui file you must promote the widget to one of the custom
widgets that is used. The header file for this module must then be added in QtDesigner so that
when the file is converted using 'pyuic6 -o {python_view_file.py} {qt_ui_file.ui}' this
module will be imported as part of the python_view_file.py.
"""
import re

from loguru import logger
from PyQt6.QtCore import QDate, QSize, QTime
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import (
    QCheckBox,
    QDateEdit,
    QLabel,
    QLineEdit,
    QPushButton,
    QTimeEdit,
)

from munientry.widgets.widget_settings import (
    EVENT_WHEEL_EVENT,
    NO_FOCUS,
    STRONG_FOCUS,
    WHITE_BACKGROUND_STYLE_SHEET,
)

DATE_FORMAT = 'MMMM dd, yyyy'
TIME_FORMAT = 'hh:mm A'
TODAY = QDate.currentDate()
TODAY_STRING = TODAY.toString(DATE_FORMAT)
DEFAULT_TIME_STRING = '08:30 AM'
LABEL_WIDTH = 200
LABEL_HEIGHT_MAX = 50
LABEL_HEIGH_MIN = 0
LABEL_MIN_SIZE = QSize(LABEL_WIDTH, LABEL_HEIGH_MIN)
LABEL_MAX_SIZE = QSize(LABEL_WIDTH, LABEL_HEIGHT_MAX)

OAC_CODE_STRING = 'https://codes.ohio.gov/ohio-administrative-code/rule-'
ORC_CODE_STRING = 'https://codes.ohio.gov/ohio-revised-code/section-'
MUNI_CODE_STRING = r'https://library.municode.com/oh\\'
GOOGLE_STRING = 'https://www.google.com/'


def set_url_link(statute: str) -> str:
    """Matches pattern of statute and sets appropriate URL for hyperlink.

    Returns a hyperlink to www.google.com if no match found.
    """
    admin_code = r'\d\d\d\d.\d\d-\d-\d\d'
    url_statute = re.search(admin_code, statute)
    if url_statute is not None:
        url_statute = url_statute.group()
        url_statute = url_statute.replace('.', ':')
        return f'<a href="{OAC_CODE_STRING}{url_statute}">{statute}</a>'
    admin_code_two = r'\d\d\d\d.\d\d-\d\d-\d\d'
    url_statute = re.search(admin_code_two, statute)
    if url_statute is not None:
        url_statute = url_statute.group()
        url_statute = url_statute.replace('.', ':')
        return f'<a href="{OAC_CODE_STRING}{url_statute}">{statute}</a>'

    seven_digit_stat = r'\d\d\d\d.\d\d\d'
    url_statute = re.search(seven_digit_stat, statute)
    if url_statute is not None:
        url_statute = url_statute.group()
        return f'<a href="{ORC_CODE_STRING}{url_statute}">{statute}</a>'
    six_digit_stat = r'\d\d\d\d.\d\d'
    url_statute = re.search(six_digit_stat, statute)
    if url_statute is not None:
        url_statute = url_statute.group()
        return f'<a href="{ORC_CODE_STRING}{url_statute}">{statute}</a>'

    five_digit_stat = r'\d\d\d.\d\d'
    url_statute = re.search(five_digit_stat, statute)
    if url_statute is not None:
        url_statute = url_statute.group()
        return f'<a href="{MUNI_CODE_STRING}">{statute}</a>'

    return f'<a href="{GOOGLE_STRING}">{statute}</a>'


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


class StatuteLineEdit(QLabel):
    """Custom QLabel widget to allow for setting hyperlinks for statutes."""

    def __init__(self, statute: str = None, parent=None):
        super().__init__(parent)
        self.setStyleSheet(
            'font: bold "Palatino Linotype"; font-size: 10pt',
        )
        self.set_up_widget(statute)
        self.statute = statute

    def get_text(self) -> str:
        """Returns the string of the statute that is used in the entry.

        This is used to provide the text as a string in lieu of the displayed hyperlink.
        """
        return self.statute

    def set_up_widget(self, statute: str):
        self.statute = statute
        self.setMinimumSize(LABEL_MIN_SIZE)
        self.setMaximumSize(LABEL_MAX_SIZE)
        self.setObjectName('statute_lineEdit')
        url_link = set_url_link(self.statute)
        self.setText(url_link)
        self.setOpenExternalLinks(True)


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
class IntegerValidator(QLineEdit):
    """Custom LineEdit class for adding a integer validator."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.validator = QIntValidator(0, 1000, self)
        self.setValidator(self.validator)


class ChargeGridIntegerWidget(IntegerValidator):
    """Base Custom Class for common Charge Grid Line Edit fields."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.setMinimumSize(LABEL_MIN_SIZE)
        self.setMaximumSize(LABEL_MAX_SIZE)
        self.setStyleSheet(WHITE_BACKGROUND_STYLE_SHEET)


class FineLineEdit(ChargeGridIntegerWidget):
    """Custom LineEdit for Fines."""

    def __init__(self, offense=None, parent=None):
        super().__init__(parent)
        self.setObjectName('fines_amount')
        self.set_fine_amount(offense)

    def set_fine_amount(self, offense):
        if offense == 'Seatbelt - Driver':
            self.setText('30')
        elif offense == 'Seatbelt - Passenger':
            self.setText('20')
        elif offense == 'Failure to Stop for School Bus':
            self.setText('500')
        else:
            self.setText('')


class FineSuspendedLineEdit(ChargeGridIntegerWidget):
    """Custom LineEdit for Fines Suspended."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('fines_suspended')


class JailLineEdit(ChargeGridIntegerWidget):
    """Custom LineEdit for Jail Days."""

    def __init__(self, offense=None, parent=None):
        super().__init__(parent)
        self.setObjectName('jail_days')


class JailSuspendedLineEdit(ChargeGridIntegerWidget):
    """Custom LineEdit for Jail Days Suspended."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('jail_days_suspended')


class JailTimeCreditLineEdit(ChargeGridIntegerWidget):
    """Custom LineEdit for Jail Credit."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName('jail_time_credit_box')


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
