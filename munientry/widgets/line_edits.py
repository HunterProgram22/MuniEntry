"""Module containing custom line edit widgets.

If using QtDesigner for creation of the Ui file you must promote the widget to one of the custom
widgets that is used. The header file for this module must then be added in QtDesigner so that
when the file is converted using 'pyuic6 -o {python_view_file.py} {qt_ui_file.ui}' this
module will be imported as part of the python_view_file.py.
"""
import re

from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import QLabel, QLineEdit

from munientry.widgets.widget_settings import (
    LABEL_MAX_SIZE,
    LABEL_MIN_SIZE,
    WHITE_BACKGROUND_STYLE_SHEET,
)

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
