"""Contains classes for building the Driving Privileges Dialog."""
from loguru import logger
from PyQt5.QtCore import QDate

from munientry.builders.base_dialogs import SchedulingBaseDialog
from munientry.controllers.helper_functions import set_assigned_judge, set_courtroom
from munientry.controllers.signal_connectors import BaseDialogSignalConnector
from munientry.controllers.slot_functions import BaseDialogSlotFunctions
from munientry.controllers.view_modifiers import BaseDialogViewModifier
from munientry.data.cms_case_loaders import CmsDrivingInfoLoader
from munientry.models.cms_models import DrivingPrivilegesInformation
from munientry.models.template_types import TEMPLATE_DICT
from munientry.updaters.general_updaters import CaseInformationUpdater
from munientry.views.driving_privileges_dialog_ui import (
    Ui_DrivingPrivilegesDialog,
)

TODAY = QDate.currentDate()


class DrivingPrivilegesDialog(SchedulingBaseDialog, Ui_DrivingPrivilegesDialog):
    """Builder for the Driving Privileges Dialog.

    The judicial_officer for this entry is the selected Assignment Commissioner.

    The assigned_judge and courtroom is set by the button pressed choosing the dialog and entry.
    """

    def __init__(
            self, judicial_officer=None, cms_case=None, case_table=None, parent=None,
    ):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Driving Privileges Entry'
        self.entry_case_information = DrivingPrivilegesInformation()
        logger.info(f'Loaded Dialog: {self.dialog_name}')
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.setWindowTitle(f'{self.dialog_name} Case Information')

    def load_cms_data_to_view(self):
        return CmsDrivingInfoLoader(self)

    def modify_view(self):
        return DrivingPrivilegesViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = DrivingPrivilegesSlotFunctions(self)
        DrivingPrivilegesSignalConnector(self)

    def update_entry_case_information(self):
        return DrivingPrivilegesCaseInformationUpdater(self)


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
        self.dialog = dialog
        self.functions = dialog.functions
        self.dialog.clear_fields_case_Button.released.connect(
            self.functions.clear_case_information_fields,
        )
        self.dialog.create_entry_Button.released.connect(self.functions.create_entry)
        self.dialog.close_dialog_Button.released.connect(self.dialog.functions.close_window)


class DrivingPrivilegesSlotFunctions(BaseDialogSlotFunctions):
    """Slot functions used only by Driving Privileges Dialog.

    Currently no additional functions are added so only accesses BaseDialogSlotFunctions.
    """


class DrivingPrivilegesCaseInformationUpdater(CaseInformationUpdater):
    """Updates case information for Driving Privileges Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_case_number_and_date()
        self.set_defendant_driving_info()
        self.set_privileges_info()
        self.set_employer_school_info()

    def set_case_number_and_date(self):
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
        radio_buttons = [self.dialog.court_suspension_radioButton, self.dialog.als_suspension_radioButton]
        suspension_type = [button for button in radio_buttons if button.isChecked()]
        self.model.suspension_type = suspension_type[0].text()
        self.model.suspension_start_date = self.dialog.suspension_start_date.get_date()
        self.model.suspension_end_date = self.dialog.suspension_end_date.get_date()
        driving_days = self.get_driving_days()
        self.model.driving_days = ', '.join(driving_days)
        driving_hours = self.get_driving_hours()
        self.model.driving_hours = ' to '.join(driving_hours)
        privileges_type = self.get_privileges_type()
        self.model.privileges_type = ', '.join(privileges_type) if len(privileges_type) > 1 else ''.join(privileges_type)
        self.model.ignition_interlock = self.dialog.ignition_interlock_checkBox.isChecked()
        self.model.restricted_tags = self.dialog.restricted_tags_checkBox.isChecked()
        self.model.other_conditions = self.get_other_conditions()

    def get_other_conditions(self) -> str:
        if self.dialog.varied_hours_checkBox.isChecked() and self.dialog.other_conditions_checkBox.isChecked():
            return ' Days and hours may vary. and only other conditions.'
        if self.dialog.other_conditions_checkBox.isChecked():
            return ' and only other conditions.'
        if self.dialog.varied_hours_checkBox.isChecked():
            return '. Days and hours may vary.'
        else:
            return '.'

    def set_employer_school_info(self):
        self.model.employer_school_name = self.dialog.employer_name_lineEdit.text()
        self.model.employer_school_address = self.dialog.employer_address_lineEdit.text()

    def get_driving_hours(self) -> list:
        driving_hours_list = [
            self.dialog.from_hours_lineEdit,
            self.dialog.to_hours_lineEdit,
        ]
        return [hours.text() for hours in driving_hours_list]

    def get_driving_days(self) -> list:
        driving_days_list = [
            self.dialog.sunday_checkBox,
            self.dialog.monday_checkBox,
            self.dialog.tuesday_checkBox,
            self.dialog.wednesday_checkBox,
            self.dialog.thursday_checkBox,
            self.dialog.friday_checkBox,
            self.dialog.saturday_checkBox,
        ]
        return [day.text() for day in driving_days_list if day.isChecked()]

    def get_privileges_type(self) -> list:
        privileges_type_list = [
            self.dialog.occupational_checkBox,
            self.dialog.educational_checkBox,
            self.dialog.vocational_checkBox,
        ]
        return [type.text() for type in privileges_type_list if type.isChecked()]


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
