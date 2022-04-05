"""The condtions dialogs module contains 'secondary' dialogs that are opened from a
main entry dialog."""
from package.controllers.base_dialogs import BaseDialog
from package.views.add_community_control_dialog_ui import Ui_AddCommunityControlDialog
from package.views.add_conditions_dialog_ui import Ui_AddConditionsDialog
from package.views.add_jail_only_dialog_ui import Ui_AddJailOnly
from package.views.add_special_bond_conditions_dialog_ui import (
    Ui_AddSpecialBondConditionsDialog,
)
from package.controllers.view_modifiers import (
    AddConditionsDialogViewModifier,
    AddJailOnlyDialogViewModifier,
    AddCommunityControlDialogViewModifier,
    AddSpecialBondConditionsDialogViewModifier,
)
from package.controllers.signal_connectors import (
    AddConditionsDialogSignalConnector,
    AddJailOnlyDialogSignalConnector,
    AddCommunityControlDialogSignalConnector,
    AddSpecialBondConditionsDialogSignalConnector,
)
from package.controllers.slot_functions import (
    AddConditionsDialogSlotFunctions,
    AddCommunityControlDialogSlotFunctions,
    AddSpecialBondConditionsDialogSlotFunctions,
    AddJailOnlyDialogSlotFunctions,
)


def enable_condition_frames(conditions_dialog, main_dialog):
    """The function is called from some of the conditions dialogs on init to hide frames
    for conditions that have not been selected in the main dialog. This is necessary
    because the base view contains all frames."""
    for item in conditions_dialog.CONDITIONS_FRAMES:
        (frame_checkbox, frame) = item
        if getattr(main_dialog, frame_checkbox).isChecked():
            getattr(conditions_dialog, frame).setEnabled(True)
        else:
            frame = getattr(conditions_dialog, frame)
            frame.setParent(None)
            frame.deleteLater()


class AddConditionsDialog(BaseDialog, Ui_AddConditionsDialog):
    """The 'secondary' conditions dialog for the Fines Only Plea Dialog."""

    CONDITIONS_FRAMES = [
        ("other_conditions_checkBox", "other_conditions_frame"),
        ("license_suspension_checkBox", "license_suspension_frame"),
        ("community_service_checkBox", "community_service_frame"),
    ]

    def __init__(self, main_dialog, parent=None):
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)
        enable_condition_frames(self, main_dialog)

    def modify_view(self):
        return AddConditionsDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = AddConditionsDialogSlotFunctions(self)
        self.functions.update_community_service_due_date()

    def connect_signals_to_slots(self):
        return AddConditionsDialogSignalConnector(self)


class AddJailOnlyDialog(BaseDialog, Ui_AddJailOnly):
    """This 'secondary' dialog is called from a warning message if the
    user forgot to set jail time."""

    condition_checkbox_dict = {
        "companion_cases_checkBox": ["companion_cases_box",
                                     "jail_term_type_box",
                                     "consecutive_jail_days_label"],
    }

    def __init__(self, main_dialog, parent=None):
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)

    def modify_view(self):
        return AddJailOnlyDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = AddJailOnlyDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return AddJailOnlyDialogSignalConnector(self)


class AddCommunityControlDialog(BaseDialog, Ui_AddCommunityControlDialog):
    """The 'secondary' conditions dialog for the Jail CC Plea Dialog."""

    CONDITIONS_FRAMES = [
        ("other_conditions_checkBox", "other_conditions_frame"),
        ("license_suspension_checkBox", "license_suspension_frame"),
        ("community_service_checkBox", "community_service_frame"),
        ("community_control_checkBox", "community_control_frame"),
        ("jail_checkBox", "jail_commitment_frame"),
        ("impoundment_checkBox", "impoundment_frame"),
        ("victim_notification_checkBox", "victim_notification_frame"),
    ]

    condition_checkbox_dict = {
        "gps_exclusion_checkBox": ["gps_exclusion_radius_box", "gps_exclusion_location_box"],
        "community_control_not_within_500_feet_checkBox": ["community_control_not_within_500_feet_person_box"],
        "community_control_no_contact_checkBox": ["community_control_no_contact_with_box"],
        "house_arrest_checkBox": ["house_arrest_time_box"],
        "community_control_community_service_checkBox": ["community_control_community_service_hours_box"],
        "other_community_control_checkBox": ["other_community_control_conditions_box"],
        "alcohol_monitoring_checkBox": ["alcohol_monitoring_time_box"],
        "pay_restitution_checkBox": ["pay_restitution_amount_box", "pay_restitution_to_box"],
        "companion_cases_checkBox": ["companion_cases_box", "jail_term_type_box", "consecutive_jail_days_label"],
        "specialized_docket_checkBox": ["specialized_docket_box"],
    }


    def __init__(self, main_dialog, parent=None):
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)
        enable_condition_frames(self, main_dialog)

    def modify_view(self):
        return AddCommunityControlDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = AddCommunityControlDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return AddCommunityControlDialogSignalConnector(self)


class AddSpecialBondConditionsDialog(BaseDialog, Ui_AddSpecialBondConditionsDialog):
    """The 'secondary' dialog for the Not Guilty Bond Dialog."""

    CONDITIONS_FRAMES = [
        ("other_conditions_checkBox", "other_conditions_frame"),
        ("admin_license_suspension_checkBox", "admin_license_suspension_frame"),
        ("domestic_violence_checkBox", "domestic_violence_frame"),
        ("vehicle_seizure_checkBox", "vehicle_seizure_frame"),
        ("no_contact_checkBox", "no_contact_frame"),
        ("custodial_supervision_checkBox", "custodial_supervision_frame"),
    ]

    def __init__(self, main_dialog, parent=None):
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)
        enable_condition_frames(self, main_dialog)

    def modify_view(self):
        return AddSpecialBondConditionsDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = AddSpecialBondConditionsDialogSlotFunctions(self)

    def connect_signals_to_slots(self):
        return AddSpecialBondConditionsDialogSignalConnector(self)
