"""Module that contains ViewModifier classes. ViewModifier classes are called for a dialog
after the setupUI is called. This class makes changes to the view that are outside the the specific
view file. Modifications to the view are placed in the ViewModifier class so that they don't need to
be updated each time a view file is recompiled through the pyuic5 command."""
import datetime

from loguru import logger
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QDate
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QCheckBox, QLineEdit, QTextEdit, QDateEdit, \
    QTimeEdit, QRadioButton

from package.views.custom_widgets import NoScrollComboBox, NoScrollDateEdit, NoScrollTimeEdit
from package.controllers.helper_functions import set_future_date


TODAY = QtCore.QDate.currentDate()


class BaseDialogViewModifier(object):
    def __init__(self, dialog):
        self.dialog = dialog
        self.dialog.setWindowIcon(QtGui.QIcon('./icons/gavel.ico'))
        self.dialog.setWindowFlags(self.dialog.windowFlags() |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowMaximizeButtonHint |
                            QtCore.Qt.WindowCloseButtonHint)
        self.dialog.setupUi(self.dialog)

    ###Main Dialog Setup Methods###
    def set_plea_trial_date(self):
        self.dialog.plea_trial_date.setDate(TODAY)
        self.dialog.plea_trial_date.__class__ = NoScrollDateEdit

    def set_appearance_reason(self):
        if self.dialog.case_table == "final_pretrials":
            self.dialog.appearance_reason_box.setCurrentText("change of plea")
        elif self.dialog.case_table == "pleas":
            self.dialog.appearance_reason_box.setCurrentText("change of plea")
        elif self.dialog.case_table == "trials_to_court":
            self.dialog.appearance_reason_box.setCurrentText("trial to court")

    def set_balance_due_date(self):
        self.dialog.balance_due_date.setDate(TODAY)

    def set_court_cost_and_fra_boxes_to_no_scroll(self):
        self.dialog.court_costs_box.__class__ = NoScrollComboBox
        self.dialog.ability_to_pay_box.__class__ = NoScrollComboBox
        self.dialog.fra_in_file_box.__class__ = NoScrollComboBox
        self.dialog.fra_in_court_box.__class__ = NoScrollComboBox
        self.dialog.balance_due_date.__class__ = NoScrollDateEdit

    def set_case_information_banner(self):
        self.dialog.defendant_name_label.setText(
            "State of Ohio v. {defendant_first_name} {defendant_last_name}".format(
                defendant_first_name=self.dialog.main_dialog.entry_case_information.defendant.first_name,
                defendant_last_name=self.dialog.main_dialog.entry_case_information.defendant.last_name
            )
        )
        self.dialog.case_number_label.setText(self.dialog.main_dialog.entry_case_information.case_number)

    ###Additional Condition/Jail Dialog Setup Methods###
    def set_jail_commitment_boxes_to_no_scroll(self):
        self.dialog.report_type_box.__class__ = NoScrollComboBox
        self.dialog.report_date_box.__class__ = NoScrollDateEdit
        self.dialog.report_time_box.__class__ = NoScrollTimeEdit
        self.dialog.jail_sentence_execution_type_box.__class__ = NoScrollComboBox
        self.dialog.jail_term_type_box.__class__ = NoScrollComboBox


    def set_conditions_case_information_banner(self):
        column = self.dialog.charges_gridLayout.columnCount() + 1
        for _index, charge in enumerate(self.dialog.charges_list):
            charge = vars(charge)
            if charge is not None:
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("finding")), 2, column)
                column += 1

    def set_license_suspension_default_view(self):
        self.dialog.license_suspension_date_box.setDate(TODAY)
        self.dialog.license_suspension_date_box.__class__ = NoScrollDateEdit
        self.dialog.license_type_box.__class__ = NoScrollComboBox
        self.dialog.term_of_suspension_box.__class__ = NoScrollComboBox

    def set_community_service_default_view(self):
        self.dialog.community_service_date_to_complete_box.setDate(TODAY)
        self.dialog.community_service_hours_ordered_box.__class__ = NoScrollComboBox
        self.dialog.community_service_days_to_complete_box.__class__ = NoScrollComboBox
        self.dialog.community_service_date_to_complete_box.__class__ = NoScrollDateEdit

    def set_jail_report_default_view(self):
        self.dialog.report_date_box.setDate(TODAY)

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

    def set_bond_condition_boxes_to_no_scroll(self):
        self.dialog.bond_type_box.__class__ = NoScrollComboBox
        self.dialog.bond_amount_box.__class__ = NoScrollComboBox
        self.dialog.monitoring_type_box.__class__ = NoScrollComboBox


    @classmethod
    def hide_boxes(cls, dialog):
        for item in cls.condition_checkbox_list:
            (condition_checkbox, condition_field) = item
            if hasattr(dialog, condition_checkbox):
                getattr(dialog, condition_field).setEnabled(False)
                getattr(dialog, condition_field).setHidden(True)

    def load_existing_data_to_dialog(self):
        CONDITIONS_CLASSES = [
            ("other_conditions_checkBox", "other_conditions"),
            ("license_suspension_checkBox", "license_suspension"),
            ("community_service_checkBox", "community_service"),
            ("admin_license_suspension_checkBox", "admin_license_suspension"),
            ("domestic_violence_checkBox", "domestic_violence_conditions"),
            ("vehicle_seizure_checkBox", "vehicle_seizure"),
            ("no_contact_checkBox", "no_contact"),
            ("custodial_supervision_checkBox", "custodial_supervision"),
            ("community_control_checkBox", "community_control"),
            ("jail_checkBox", "jail_terms"),
            ("impoundment_checkBox", "impoundment"),
            ("victim_notification_checkBox", "victim_notification"),
        ]
        for item in CONDITIONS_CLASSES:
            (condition_checkbox, model_class) = item
            if hasattr(self.dialog.main_dialog, condition_checkbox):
                if getattr(self.dialog.main_dialog, condition_checkbox).isChecked():
                    model_class = getattr(self.dialog.main_dialog.entry_case_information, model_class)
                    self.transfer_model_data_to_condition_dialog_fields(model_class)
                else:
                    continue

    def transfer_model_data_to_condition_dialog_fields(self, model_class):
        terms_list = getattr(model_class, "terms_list")
        for item in terms_list:
            (model_attribute, view_field) = item
            if view_field == "other_conditions_checkBox": # TODO: This exists to address OtherConditions using ordered in terms list
                continue
            elif isinstance(getattr(self.dialog, view_field), QComboBox):
                getattr(self.dialog, view_field).setCurrentText(getattr(model_class, model_attribute))
            elif isinstance(getattr(self.dialog, view_field), QCheckBox):
                getattr(self.dialog, view_field).setChecked(getattr(model_class, model_attribute))
            elif isinstance(getattr(self.dialog, view_field), QRadioButton):
                getattr(self.dialog, view_field).setChecked(getattr(model_class, model_attribute))
            elif isinstance(getattr(self.dialog, view_field), QLineEdit):
                getattr(self.dialog, view_field).setText(getattr(model_class, model_attribute))
            elif isinstance(getattr(self.dialog, view_field), QTextEdit):
                getattr(self.dialog, view_field).setPlainText(getattr(model_class, model_attribute))
            elif isinstance(getattr(self.dialog, view_field), QDateEdit):
                try:
                    format = "%B %d, %Y"
                    date = datetime.datetime.strptime(getattr(model_class, model_attribute), format)
                    getattr(self.dialog, view_field).setDate(date)
                except TypeError:
                    pass
            elif isinstance(getattr(self.dialog, view_field), QTimeEdit):
                try:
                    format = "%H:%M %p"
                    time = datetime.datetime.strptime(getattr(model_class, model_attribute), format)
                    getattr(self.dialog, view_field).setTime(time)
                except TypeError:
                    pass

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
        self.set_plea_trial_date()
        self.set_appearance_reason()
        self.set_balance_due_date()
        self.set_court_cost_and_fra_boxes_to_no_scroll()


class JailCCDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_plea_trial_date()
        self.set_appearance_reason()
        self.set_balance_due_date()
        self.set_court_cost_and_fra_boxes_to_no_scroll()
        self.dialog.in_jail_box.__class__ = NoScrollComboBox
        self.dialog.jail_time_credit_apply_box.__class__ = NoScrollComboBox


class DiversionDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_plea_trial_date()
        self.set_appearance_reason()
        self.set_diversion_fine_pay_date_box()
        self.set_diversion_jail_report_date_box()

    def set_diversion_fine_pay_date_box(self):
        """Diversion pay date is set to the first Tuesday after 97 days - 90 days to comply, plus 7 days
        to process paperwork (per Judge Hemmeter). The 1 in the set_future_date is for Tuesday."""
        diversion_pay_days_to_add = set_future_date(97, "Tuesday")
        self.dialog.diversion_fine_pay_date_box.setDate(QDate.currentDate().addDays(diversion_pay_days_to_add))
        self.dialog.diversion_fine_pay_date_box.__class__ = NoScrollDateEdit

    def set_diversion_jail_report_date_box(self):
        """Diversion jail report date is set to the first Friday after 97 days - 90 days to comply, plus 7 days
        to process paperwork (per Judge Hemmeter). The 4 in the set_future_date is for Friday."""
        jail_report_days_to_add = set_future_date(97, "Friday")
        self.dialog.diversion_jail_report_date_box.setDate(QDate.currentDate().addDays(jail_report_days_to_add))
        self.dialog.diversion_jail_report_date_box.__class__ = NoScrollDateEdit


class NotGuiltyBondDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_plea_trial_date()
        self.set_appearance_reason()
        self.set_bond_condition_boxes_to_no_scroll()
        self.dialog.specialized_docket_type_box.__class__ = NoScrollComboBox


class ProbationViolationBondDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_plea_trial_date()
        self.set_appearance_reason()
        self.set_bond_condition_boxes_to_no_scroll()


class FailureToAppearDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_plea_trial_date()
        self.set_appearance_reason()
        self.dialog.bond_type_box.__class__ = NoScrollComboBox
        self.dialog.bond_amount_box.__class__ = NoScrollComboBox


class AddConditionsDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_conditions_case_information_banner()
        self.set_license_suspension_default_view()
        self.set_community_service_default_view()
        self.load_existing_data_to_dialog()


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
        self.hide_boxes(dialog)  # Class method needs dialog ? TODO: Fix
        self.set_jail_report_default_view()
        self.set_report_date_view()
        self.set_report_days_notes_box()
        self.set_jail_commitment_boxes_to_no_scroll()


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
    ]

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_conditions_case_information_banner()
        self.set_license_suspension_default_view()
        self.set_community_service_default_view()
        self.load_existing_data_to_dialog()
        self.hide_boxes(dialog) # Class method needs dialog ? TODO: Fix
        self.set_jail_report_default_view()
        self.set_report_date_view()
        self.set_report_days_notes_box()
        self.set_jail_commitment_boxes_to_no_scroll()
        self.set_community_control_dialog_boxes_to_no_scroll()

    def set_community_control_dialog_boxes_to_no_scroll(self):
        self.dialog.community_control_type_of_control_box.__class__ = NoScrollComboBox
        self.dialog.community_control_term_of_control_box.__class__ = NoScrollComboBox
        self.dialog.house_arrest_time_box.__class__ = NoScrollComboBox
        self.dialog.gps_exclusion_radius_box.__class__ = NoScrollComboBox
        self.dialog.alcohol_monitoring_time_box.__class__ = NoScrollComboBox
        self.dialog.community_control_community_service_hours_box.__class__ = NoScrollComboBox
        self.dialog.vehicle_impound_time_box.__class__ = NoScrollComboBox
        self.dialog.vehicle_impound_action_box.__class__ = NoScrollComboBox


class AddSpecialBondConditionsDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_special_bond_conditions_case_information_banner()
        self.set_domestic_violence_surrender_weapons_default_date()
        self.load_existing_data_to_dialog()
        self.dialog.admin_license_suspension_objection_box.__class__ = NoScrollComboBox
        self.dialog.admin_license_suspension_disposition_box.__class__ = NoScrollComboBox
        self.dialog.domestic_violence_surrender_weapons_dateBox.__class__ = NoScrollDateEdit
        self.dialog.state_opposes_box.__class__ = NoScrollComboBox
        self.dialog.disposition_motion_to_return_box.__class__ = NoScrollComboBox

    def set_special_bond_conditions_case_information_banner(self):
        column = self.dialog.charges_gridLayout.columnCount() + 1
        for charge in self.dialog.charges_list:
            charge = vars(charge)
            if charge is not None:
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                column += 1

    def set_domestic_violence_surrender_weapons_default_date(self):
        self.dialog.domestic_violence_surrender_weapons_dateBox.setDate(TODAY)