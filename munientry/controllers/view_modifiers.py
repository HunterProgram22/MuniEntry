"""Module that contains ViewModifier classes. ViewModifier classes are called for a dialog
after the setupUI is called. This class makes changes to the view that are outside the the specific
view file. Modifications to the view are placed in the ViewModifier class so that they don't need to
be updated each time a view file is recompiled through the pyuic5 command."""
from loguru import logger
from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel
from munientry.builders.crimtraffic.base_crimtraffic_builders import BaseDialogViewModifier

from munientry.controllers import charges_grids as cg

TODAY = QtCore.QDate.currentDate()


class AddChargeDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_case_information_banner()


class AmendChargeDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_case_information_banner()


class LeapSentencingDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.charges_gridLayout.__class__ = cg.FineOnlyChargeGrid


class SentencingOnlyDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.charges_gridLayout.__class__ = cg.JailChargesGrid


class TrialSentencingDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.charges_gridLayout.__class__ = cg.JailChargesGrid


class FailureToAppearDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()


class FreeformDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)


class AddConditionsDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_conditions_case_information_banner()
        self.load_existing_data_to_dialog()

    def load_existing_data_to_dialog(self):
        CONDITIONS_CLASSES = [
            ("other_conditions_checkBox", "other_conditions"),
            ("license_suspension_checkBox", "license_suspension"),
            ("community_service_checkBox", "community_service"),
        ]
        for item in CONDITIONS_CLASSES:
            (condition_checkbox, model_class) = item
            if getattr(self.dialog.main_dialog, condition_checkbox).isChecked():
                model_class = getattr(self.dialog.main_dialog.entry_case_information, model_class)
                self.transfer_model_data_to_view(model_class)
            else:
                continue


class AddJailOnlyDialogViewModifier(BaseDialogViewModifier):
    condition_checkbox_list = [
        ("companion_cases_checkBox", "companion_cases_box"),
        ("companion_cases_checkBox", "jail_term_type_box"),
        ("companion_cases_checkBox", "consecutive_jail_days_label"),
    ]

    def __init__(self, dialog):
        """This does not include a load_existing_data_to_dialog method because it is only called
        from a warning message if user forgot to add jail reporting terms and chooses to add them
        after getting the warning."""
        super().__init__(dialog)
        self.set_conditions_case_information_banner()
        self.load_existing_data_to_dialog()
        self.hide_boxes(dialog)  # Class method needs dialog ? TODO: Fix
        self.set_report_date_view()
        self.set_report_days_notes_box()

    def load_existing_data_to_dialog(self):
        CONDITIONS_CLASSES = [
            ("jail_checkBox", "jail_terms"),
        ]
        for item in CONDITIONS_CLASSES:
            (condition_checkbox, model_class) = item
            if getattr(self.dialog.main_dialog, condition_checkbox).isChecked():
                model_class = getattr(self.dialog.main_dialog.entry_case_information, model_class)
                self.transfer_model_data_to_view(model_class)
            else:
                continue

    def set_report_date_view(self):
        if self.dialog.report_type_box.currentText() == 'date set by Office of Community Control':
            self.dialog.report_date_box.setDisabled(True)
            self.dialog.report_date_box.setHidden(True)
            self.dialog.report_time_box.setDisabled(True)
            self.dialog.report_time_box.setHidden(True)
            self.dialog.report_date_label.setHidden(True)
            self.dialog.report_time_label.setHidden(True)
        elif self.dialog.report_type_box.currentText() == 'forthwith':
            self.dialog.report_date_box.setDisabled(True)
            self.dialog.report_date_box.setHidden(True)
            self.dialog.report_time_box.setDisabled(True)
            self.dialog.report_time_box.setHidden(True)
            self.dialog.report_date_label.setHidden(True)
            self.dialog.report_time_label.setHidden(True)
        else:
            self.dialog.report_date_box.setEnabled(True)
            self.dialog.report_date_box.setHidden(False)
            self.dialog.report_time_box.setEnabled(True)
            self.dialog.report_time_box.setHidden(False)
            self.dialog.report_date_label.setHidden(False)
            self.dialog.report_time_label.setHidden(False)

    def set_report_days_notes_box(self):
        if self.dialog.jail_sentence_execution_type_box.currentText() == 'consecutive days':
            self.dialog.jail_report_days_notes_box.setDisabled(True)
            self.dialog.jail_report_days_notes_box.setHidden(True)
        else:
            self.dialog.jail_report_days_notes_box.setDisabled(False)
            self.dialog.jail_report_days_notes_box.setHidden(False)


class AddCommunityControlDialogViewModifier(BaseDialogViewModifier):
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
        ("specialized_docket_checkBox", "specialized_docket_box"),
    ]

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_conditions_case_information_banner()
        self.load_existing_data_to_dialog()
        self.hide_boxes(dialog) # Class method needs dialog ? TODO: Fix

    def load_existing_data_to_dialog(self):
        CONDITIONS_CLASSES = [
            ("other_conditions_checkBox", "other_conditions"),
            ("license_suspension_checkBox", "license_suspension"),
            ("community_service_checkBox", "community_service"),
            ("community_control_checkBox", "community_control"),
            ("impoundment_checkBox", "impoundment"),
            ("victim_notification_checkBox", "victim_notification"),
        ]
        for item in CONDITIONS_CLASSES:
            (condition_checkbox, model_class) = item
            if getattr(self.dialog.main_dialog, condition_checkbox).isChecked():
                model_class = getattr(self.dialog.main_dialog.entry_case_information, model_class)
                self.transfer_model_data_to_view(model_class)
            else:
                continue


class AddSpecialBondConditionsDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_special_bond_conditions_case_information_banner()
        self.load_existing_data_to_dialog()

    def set_special_bond_conditions_case_information_banner(self):
        column = self.dialog.charges_gridLayout.columnCount() + 1
        for charge in self.dialog.charges_list:
            logger.debug(charge)
            charge = vars(charge)
            if charge is not None:
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                column += 1

    def load_existing_data_to_dialog(self):
        CONDITIONS_CLASSES = [
            ("other_conditions_checkBox", "other_conditions"),
            ("admin_license_suspension_checkBox", "admin_license_suspension"),
            ("domestic_violence_checkBox", "domestic_violence_conditions"),
            ("vehicle_seizure_checkBox", "vehicle_seizure"),
            ("no_contact_checkBox", "no_contact"),
            ("custodial_supervision_checkBox", "custodial_supervision"),
        ]
        for item in CONDITIONS_CLASSES:
            (condition_checkbox, model_class) = item
            if getattr(self.dialog.main_dialog, condition_checkbox).isChecked():
                model_class = getattr(self.dialog.main_dialog.entry_case_information, model_class)
                self.transfer_model_data_to_view(model_class)
            else:
                continue


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
