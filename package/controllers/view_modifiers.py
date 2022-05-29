"""Module that contains ViewModifier classes. ViewModifier classes are called for a dialog
after the setupUI is called. This class makes changes to the view that are outside the the specific
view file. Modifications to the view are placed in the ViewModifier class so that they don't need to
be updated each time a view file is recompiled through the pyuic5 command."""
import datetime, time

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel, QComboBox, QCheckBox, QLineEdit, QTextEdit, QDateEdit, \
    QTimeEdit, QRadioButton

from settings import WIDGET_TYPE_SET_DICT
from package.controllers.helper_functions import set_future_date


TODAY = QtCore.QDate.currentDate()


class BaseDialogViewModifier:
    def __init__(self, dialog):
        self.dialog = dialog
        self.dialog.setWindowIcon(QtGui.QIcon('./icons/gavel.ico'))
        self.dialog.setWindowFlags(self.dialog.windowFlags() |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowMaximizeButtonHint |
                            QtCore.Qt.WindowCloseButtonHint)
        self.dialog.setupUi(self.dialog)

    def set_appearance_reason(self):
        if self.dialog.case_table == "final_pretrials":
            self.dialog.appearance_reason_box.setCurrentText("a change of plea")
        elif self.dialog.case_table == "pleas":
            self.dialog.appearance_reason_box.setCurrentText("a change of plea")
        elif self.dialog.case_table == "trials_to_court":
            self.dialog.appearance_reason_box.setCurrentText("trial to court")

    def set_case_information_banner(self):
        self.dialog.defendant_name_label.setText(
            "State of Ohio v. {defendant_first_name} {defendant_last_name}".format(
                defendant_first_name=self.dialog.main_dialog.entry_case_information.defendant.first_name,
                defendant_last_name=self.dialog.main_dialog.entry_case_information.defendant.last_name
            )
        )
        self.dialog.case_number_label.setText(self.dialog.main_dialog.entry_case_information.case_number)

    ###Additional Condition/Jail Dialog Setup Methods###
    def set_conditions_case_information_banner(self):
        column = self.dialog.charges_gridLayout.columnCount() + 1
        for _index, charge in enumerate(self.dialog.charges_list):
            charge = vars(charge)
            if charge is not None:
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("finding")), 2, column)
                column += 1

    def set_report_date_view(self):
        if self.dialog.report_type_box.currentText() == "date set by Office of Community Control":
            self.dialog.report_date_box.setDisabled(True)
            self.dialog.report_date_box.setHidden(True)
            self.dialog.report_time_box.setDisabled(True)
            self.dialog.report_time_box.setHidden(True)
            self.dialog.report_date_label.setHidden(True)
            self.dialog.report_time_label.setHidden(True)
        elif self.dialog.report_type_box.currentText() == "forthwith":
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
        if self.dialog.jail_sentence_execution_type_box.currentText() == "consecutive days":
            self.dialog.jail_report_days_notes_box.setDisabled(True)
            self.dialog.jail_report_days_notes_box.setHidden(True)
        else:
            self.dialog.jail_report_days_notes_box.setDisabled(False)
            self.dialog.jail_report_days_notes_box.setHidden(False)

    @classmethod
    def hide_boxes(cls, dialog):
        for item in cls.condition_checkbox_list:
            (condition_checkbox, condition_field) = item
            if hasattr(dialog, condition_checkbox):
                if getattr(dialog, condition_checkbox).isChecked():
                    getattr(dialog, condition_field).setEnabled(True)
                    getattr(dialog, condition_field).setHidden(False)
                else:
                    getattr(dialog, condition_field).setEnabled(False)
                    getattr(dialog, condition_field).setHidden(True)

    def transfer_model_data_to_view(self, model_class):
        """Loops through the terms_list for a model and loads data into the view of the dialog on
        load. This is to allow for previously entered data to be shown if a user comes back to
        the dialog after having previously entered data."""
        for (model_attribute, view_field) in model_class.terms_list:
            key = getattr(self.dialog, view_field).__class__.__name__
            view = getattr(self.dialog, view_field)
            getattr(view, WIDGET_TYPE_SET_DICT.get(key))(getattr(model_class, model_attribute))


class AddChargeDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_case_information_banner()


class AmendChargeDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_case_information_banner()


class FineOnlyDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()


class LeapSentencingDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)


class LeapAdmissionPleaDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()


class PleaOnlyDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()


class JailCCDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()


class TrialSentencingDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)


class DiversionDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()
        self.set_diversion_fine_pay_date_box()
        self.set_diversion_jail_report_date_box()

    def set_diversion_fine_pay_date_box(self):
        """Diversion pay date is set to the first Tuesday after 97 days - 90 days to comply, plus 7 days
        to process paperwork (per Judge Hemmeter). The 1 in the set_future_date is for Tuesday."""
        diversion_pay_days_to_add = set_future_date(97, "Tuesday")
        self.dialog.diversion_fine_pay_date_box.setDate(QDate.currentDate().addDays(diversion_pay_days_to_add))

    def set_diversion_jail_report_date_box(self):
        """Diversion jail report date is set to the first Friday after 97 days - 90 days to comply, plus 7 days
        to process paperwork (per Judge Hemmeter). The 4 in the set_future_date is for Friday."""
        jail_report_days_to_add = set_future_date(97, "Friday")
        self.dialog.diversion_jail_report_date_box.setDate(QDate.currentDate().addDays(jail_report_days_to_add))


class NotGuiltyBondDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()
        self.dialog.monitoring_type_box.setHidden(True)
        self.dialog.specialized_docket_type_box.setHidden(True)


class NoPleaBondDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()
        self.dialog.monitoring_type_box.setHidden(True)
        self.dialog.specialized_docket_type_box.setHidden(True)


class BondHearingDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.monitoring_type_box.setHidden(True)
        self.dialog.specialized_docket_type_box.setHidden(True)


class ProbationViolationBondDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()


class FailureToAppearDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()


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
