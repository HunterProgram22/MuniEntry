"""Contains classes for building the Driving Privileges Dialog."""
from loguru import logger
from PyQt5.QtCore import QDate

from munientry.builders.base_dialogs import SchedulingBaseDialog
from munientry.controllers.helper_functions import set_assigned_judge, set_courtroom
from munientry.controllers.signal_connectors import BaseDialogSignalConnector
from munientry.controllers.slot_functions import BaseDialogSlotFunctions
from munientry.controllers.view_modifiers import BaseDialogViewModifier
from munientry.data.cms_case_loaders import CmsDrivingInfoLoader
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
        self.update_model_with_case_information_frame_data()

    def update_model_with_case_information_frame_data(self):
        self.set_case_number_and_date()
        self.set_defendant_driving_info()

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


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
