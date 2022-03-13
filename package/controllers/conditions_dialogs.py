from loguru import logger
from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel

from package.controllers.base_dialogs import BaseDialog
from package.views.add_community_control_dialog_ui import Ui_AddCommunityControlDialog
from package.views.add_conditions_dialog_ui import Ui_AddConditionsDialog
from package.views.add_jail_only_dialog_ui import Ui_AddJailOnly
from package.views.add_special_bond_conditions_dialog_ui import Ui_AddSpecialBondConditionsDialog
from package.controllers.helper_functions import set_future_date
from package.controllers.view_modifiers import AddConditionsDialogViewModifier, \
    AddJailOnlyDialogViewModifier, AddCommunityControlDialogViewModifier, AddSpecialBondConditionsDialogViewModifier
from package.controllers.signal_connectors import AddConditionsDialogSignalConnector, \
    AddJailOnlyDialogSignalConnector, AddCommunityControlDialogSignalConnector, \
    AddSpecialBondConditionsDialogSignalConnector
from package.controllers.slot_functions import AddConditionsDialogSlotFunctions, \
    AddCommunityControlDialogSlotFunctions, AddSpecialBondConditionsDialogSlotFunctions, AddJailOnlyDialogSlotFunctions


CONDITIONS_FRAMES = [
    ("other_conditions_checkBox", "other_conditions_frame"),
    ("license_suspension_checkBox", "license_suspension_frame"),
    ("community_service_checkBox", "community_service_frame"),
    ("admin_license_suspension_checkBox", "admin_license_suspension_frame"),
    ("domestic_violence_checkBox", "domestic_violence_frame"),
    ("vehicle_seizure_checkBox", "vehicle_seizure_frame"),
    ("no_contact_checkBox", "no_contact_frame"),
    ("custodial_supervision_checkBox", "custodial_supervision_frame"),
    ("community_control_checkBox", "community_control_frame"),
    ("jail_checkBox", "jail_commitment_frame"),
    ("diversion_checkBox", "diversion_frame"),
    ("impoundment_checkBox", "impoundment_frame"),
    ("victim_notification_checkBox", "victim_notification_frame"),
]


def enable_condition_frames(conditions_dialog, main_dialog):
    for index, item in enumerate(CONDITIONS_FRAMES):
        (frame_checkbox, frame) = item
        if hasattr(main_dialog, frame_checkbox):
            if getattr(main_dialog, frame_checkbox).isChecked():
                getattr(conditions_dialog, frame).setEnabled(True)
            else:
                frame = getattr(conditions_dialog, frame)
                frame.setParent(None)
                frame.deleteLater()


class ConditionsDialog(BaseDialog):
    def __init__(self, main_dialog, parent=None):
        self.charges_list = main_dialog.entry_case_information.charges_list  # Show charges on banner
        self.main_dialog = main_dialog
        super().__init__(parent)

    def update_community_service_due_date(self, _index=None):
        days_to_complete = int(self.community_service_days_to_complete_box.currentText())
        self.community_service_date_to_complete_box.setDate(QDate.currentDate().addDays(days_to_complete))


class AddConditionsDialog(ConditionsDialog, Ui_AddConditionsDialog):
    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)
        enable_condition_frames(self, main_dialog)

    def modify_view(self):
        return AddConditionsDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = AddConditionsDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return AddConditionsDialogSignalConnector(self)


class AddJailOnlyDialog(ConditionsDialog, Ui_AddJailOnly):
    jail_condition_checkbox_list = [
        ("companion_cases_checkBox", "companion_cases_box"),
        ("companion_cases_checkBox", "jail_term_type_box"),
        ("companion_cases_checkBox", "consecutive_jail_days_label"),
    ]
    @logger.catch
    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)

    @logger.catch
    def modify_view(self):
        return AddJailOnlyDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = AddJailOnlyDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return AddJailOnlyDialogSignalConnector(self)

    def set_field_enabled(self):
        """Loops through the conditions_checkbox_list and if the box is checked for the condition it will show
        any additional fields that are required for that condition."""
        for item in AddJailOnlyDialog.jail_condition_checkbox_list:
            (condition_checkbox, condition_field) = item
            if hasattr(self, condition_checkbox):
                if getattr(self, condition_checkbox).isChecked():
                    getattr(self, condition_field).setEnabled(True)
                    getattr(self, condition_field).setHidden(False)
                    getattr(self, condition_field).setFocus(True)
                else:
                    getattr(self, condition_field).setEnabled(False)
                    getattr(self, condition_field).setHidden(True)


class AddCommunityControlDialog(ConditionsDialog, Ui_AddCommunityControlDialog):
    """
    :conditions_checkbox_list: list of tuples that show or hide fields only when they are
    necessary for additional data input because the checkbox is checked.
    """
    condition_checkbox_list = [
        ("gps_exclusion_checkBox", "gps_exclusion_radius_box"),
        ("gps_exclusion_checkBox", "gps_exclusion_location_box"),
        ("community_control_not_within_500_feet_checkBox", "community_control_not_within_500_feet_person_box"),
        ("community_control_no_contact_checkBox", "community_control_no_contact_with_box"),
        ("house_arrest_checkBox", "house_arrest_time_box"),
        ("community_control_community_service_checkBox", "community_control_community_service_hours_box"),
        ("other_community_control_checkBox", "other_community_control_conditions_box"),
        ("alcohol_monitoring_checkBox", "alcohol_monitoring_time_box"),
        ("pay_restitution_checkBox", "pay_restitution_amount_box"),
        ("pay_restitution_checkBox", "pay_restitution_to_box"),
        ("companion_cases_checkBox", "companion_cases_box"),
        ("companion_cases_checkBox", "jail_term_type_box"),
        ("companion_cases_checkBox", "consecutive_jail_days_label"),
    ]

    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)
        enable_condition_frames(self, main_dialog)

    def modify_view(self):
        return AddCommunityControlDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = AddCommunityControlDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return AddCommunityControlDialogSignalConnector(self)


class AddSpecialBondConditionsDialog(BaseDialog, Ui_AddSpecialBondConditionsDialog):
    def __init__(self, main_dialog, parent=None):
        self.charges_list = main_dialog.entry_case_information.charges_list  # Show charges on banner
        self.main_dialog = main_dialog
        super().__init__(parent)
        enable_condition_frames(self, main_dialog)

    def modify_view(self):
        return AddSpecialBondConditionsDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = AddSpecialBondConditionsDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return AddSpecialBondConditionsDialogSignalConnector(self)
