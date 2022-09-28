"""Contains classes for building the Driving Privileges Dialog."""
from loguru import logger
from PyQt5.QtCore import QDate

from munientry.builders.base_dialogs import BaseDialogSignalConnector
from munientry.builders.crimtraffic.base_crimtraffic_builders import (
    BaseDialogSlotFunctions,
    BaseDialogViewModifier,
)
from munientry.builders.scheduling.base_scheduling_builders import SchedulingBaseDialog
from munientry.checkers.base_checks import BaseChecker
from munientry.data.cms_case_loaders import CmsDrivingInfoLoader
from munientry.models.privileges_models import (
    DrivingPrivilegesInformation,
    EmployerSchoolInformation,
)
from munientry.updaters.general_updaters import CaseInformationUpdater
from munientry.views.driving_privileges_dialog_ui import Ui_DrivingPrivilegesDialog

TODAY = QDate.currentDate()


class DrivingPrivilegesViewModifier(BaseDialogViewModifier):
    """View class that creates and modifies the view for the General Notice of Hearing Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.plea_trial_date.setDate(TODAY)


class DrivingPrivilegesSignalConnector(BaseDialogSignalConnector):
    """Connects signals to slots for Driving Privileges Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_other_dialog_signals()

    def connect_other_dialog_signals(self):
        self.dialog.other_conditions_checkBox.toggled.connect(
            self.dialog.functions.enable_other_conditions,
        )
        self.dialog.add_employer_school_Button.released.connect(
            self.dialog.functions.add_employer_school,
        )
        self.dialog.suspension_term_box.currentTextChanged.connect(
            self.dialog.functions.update_end_suspension_date,
        )


class DrivingPrivilegesSlotFunctions(BaseDialogSlotFunctions):
    """Slot functions used only by Driving Privileges Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self._driving_days_list = [
            self.dialog.sunday_checkBox,
            self.dialog.monday_checkBox,
            self.dialog.tuesday_checkBox,
            self.dialog.wednesday_checkBox,
            self.dialog.thursday_checkBox,
            self.dialog.friday_checkBox,
            self.dialog.saturday_checkBox,
        ]
        self._privileges_type_list = [
            self.dialog.occupational_checkBox,
            self.dialog.educational_checkBox,
            self.dialog.vocational_checkBox,
        ]
        self._driving_hours_list = [
            self.dialog.from_hours_lineEdit,
            self.dialog.to_hours_lineEdit,
        ]
        self._condition_boxes_list = [
            self.dialog.varied_hours_checkBox,
            self.dialog.other_conditions_checkBox,
        ]

    def update_end_suspension_date(self) -> None:
        suspension_days_dict = {
            '90 Days': 90,
            '1 Year': 365,
            '2 Years': 730,
            '3 Years': 1095,
            '4 Years': 1460,
            '5 Years': 1825,
            '6 Years': 2190,
            '7 Years': 2555,
        }
        term = self.dialog.suspension_term_box.currentText()
        suspension_start_date = self.dialog.suspension_start_date.date()
        term_days = suspension_days_dict.get(term, 0)
        end_date = suspension_start_date.addDays(term_days)
        self.dialog.suspension_end_date.setDate(end_date)

    def enable_other_conditions(self):
        if self.dialog.other_conditions_checkBox.isChecked():
            self.dialog.other_conditions_lineEdit.setEnabled(True)
            self.dialog.other_conditions_lineEdit.setHidden(False)
            self.dialog.other_conditions_lineEdit.setFocus()
        else:
            self.dialog.other_conditions_lineEdit.setEnabled(False)
            self.dialog.other_conditions_lineEdit.setHidden(True)

    def add_employer_school(self):
        employer_school = EmployerSchoolInformation()
        employer_school.name = self.dialog.employer_name_lineEdit.text()
        employer_school.address = self.dialog.employer_address_lineEdit.text()
        employer_school.city = self.dialog.employer_city_lineEdit.text()
        employer_school.state = self.dialog.employer_state_lineEdit.text()
        employer_school.zipcode = self.dialog.employer_zipcode_lineEdit.text()
        employer_school.privileges_type = self._get_privileges_type()
        employer_school.driving_days = self._get_driving_days()
        employer_school.driving_hours = self._get_driving_hours()
        employer_school.other_conditions = self._get_other_conditions()
        logger.info(employer_school)
        self.dialog.entry_case_information.add_employer_school_to_list(employer_school)
        self._set_employer_school_label()
        self._clear_employer_school_fields()
        self.dialog.occupational_checkBox.setFocus()

    def _set_employer_school_label(self):
        employer_school_names = [
            employer.name for employer in self.dialog.entry_case_information.employer_school_list
        ]
        employer_school_string = ', '.join(employer_school_names)
        self.dialog.employer_school_label.setText(employer_school_string)

    def _clear_employer_school_fields(self):
        self.dialog.employer_name_lineEdit.clear()
        self.dialog.employer_address_lineEdit.clear()
        self.dialog.employer_city_lineEdit.clear()
        self.dialog.employer_state_lineEdit.clear()
        self.dialog.employer_zipcode_lineEdit.clear()
        self._clear_driving_days()
        self._clear_privileges_types()
        self._clear_conditions_boxes()
        self._clear_hours_fields()

    def _get_other_conditions(self) -> str:
        if self.dialog.varied_hours_checkBox.isChecked():
            if self.dialog.other_conditions_checkBox.isChecked():
                other_conditions_text = self.dialog.other_conditions_lineEdit.text()
                return f'Days and hours may vary. {other_conditions_text}'
        if self.dialog.other_conditions_checkBox.isChecked():
            other_conditions_text = self.dialog.other_conditions_lineEdit.text()
            return f'{other_conditions_text}'
        if self.dialog.varied_hours_checkBox.isChecked():
            return 'Days and hours may vary.'
        return ''

    def _get_driving_hours(self) -> str:
        driving_hours = [hours.text() for hours in self._driving_hours_list]
        return ' to '.join(driving_hours)

    def _get_driving_days(self) -> str:
        driving_days = [day.text() for day in self._driving_days_list if day.isChecked()]
        return ', '.join(driving_days)

    def _get_privileges_type(self) -> str:
        privileges_type = [priv.text() for priv in self._privileges_type_list if priv.isChecked()]
        if len(privileges_type) == 1:
            return privileges_type[0]
        return ', '.join(privileges_type)

    def _clear_driving_days(self) -> list:
        return [day.setChecked(False) for day in self._driving_days_list]

    def _clear_privileges_types(self) -> list:
        return [priv.setChecked(False) for priv in self._privileges_type_list]

    def _clear_conditions_boxes(self) -> list:
        return [condition.setChecked(False) for condition in self._condition_boxes_list]

    def _clear_hours_fields(self) -> list:
        return [hours.clear() for hours in self._driving_hours_list]


class DrivingPrivilegesCaseInformationUpdater(CaseInformationUpdater):
    """Updates case information for Driving Privileges Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_case_number_and_date()
        self.set_defendant_driving_info()
        self.set_privileges_info()

    def set_case_number_and_date(self):
        self.model.judicial_officer = self.dialog.judicial_officer
        self.model.case_number = self.dialog.case_number_lineEdit.text()
        self.model.plea_trial_date = self.dialog.plea_trial_date.date().toString('MMMM dd, yyyy')

    def set_defendant_driving_info(self):
        self.model.defendant.first_name = self.dialog.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.dialog.defendant_last_name_lineEdit.text()
        self.model.defendant.address = self.dialog.defendant_address_lineEdit.text()
        self.model.defendant.city = self.dialog.defendant_city_lineEdit.text()
        self.model.defendant.state = self.dialog.defendant_state_lineEdit.text()
        self.model.defendant.zipcode = self.dialog.defendant_zipcode_lineEdit.text()
        self.model.defendant.license_number = self.dialog.defendant_driver_license_lineEdit.text()
        self.model.defendant.birth_date = self.dialog.defendant_dob_lineEdit.text()

    def set_privileges_info(self):
        radio_buttons = [
            self.dialog.court_suspension_radioButton, self.dialog.als_suspension_radioButton,
        ]
        suspension_type = [button for button in radio_buttons if button.isChecked()]
        self.model.suspension_type = suspension_type[0].text()
        self.model.suspension_start_date = self.dialog.suspension_start_date.get_date()
        self.model.suspension_end_date = self.dialog.suspension_end_date.get_date()
        self.model.ignition_interlock = self.dialog.ignition_interlock_checkBox.isChecked()
        self.model.restricted_tags = self.dialog.restricted_tags_checkBox.isChecked()


class DrivingPrivilegesDialogInfoChecker(BaseChecker):
    """Class with checks for the Driving Privileges Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = []
        self.check_status = self.perform_check_list()


class DrivingPrivilegesDialog(SchedulingBaseDialog, Ui_DrivingPrivilegesDialog):
    """Builder for the Driving Privileges Dialog.

    The judicial_officer for this entry is the selected Assignment Commissioner.
    """

    build_dict = {
        'dialog_name': 'Driving Privileges Entry',
        'view': DrivingPrivilegesViewModifier,
        'slots': DrivingPrivilegesSlotFunctions,
        'signals': DrivingPrivilegesSignalConnector,
        'case_information_model': DrivingPrivilegesInformation,
        'loader': CmsDrivingInfoLoader,
        'updater': DrivingPrivilegesCaseInformationUpdater,
        'info_checker': DrivingPrivilegesDialogInfoChecker,
    }

    def additional_setup(self):
        self.setWindowTitle(f'{self.dialog_name} Case Information')
        self.functions.enable_other_conditions()


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
