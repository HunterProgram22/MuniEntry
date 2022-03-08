"""Module that contains ViewModifier classes. ViewModifier classes are called for a dialog
after the setupUI is called. This class makes changes to the view that are outside the the specific
view file. Modifications to the view are placed in the ViewModifier class so that they don't need to
be updated each time a view file is recompiled through the pyuic5 command."""
from loguru import logger
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QDate
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QCheckBox, QLineEdit, QTextEdit, QDateEdit, QTimeEdit

from package.controllers.helper_functions import set_future_date


TODAY = QtCore.QDate.currentDate()


class BaseDialogViewModifier(object):
    def __init__(self, dialog):
        dialog.setWindowIcon(QtGui.QIcon('./icons/gavel.ico'))
        dialog.setWindowFlags(dialog.windowFlags() |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowMaximizeButtonHint |
                            QtCore.Qt.WindowCloseButtonHint)
        dialog.setupUi(dialog)

    ###Main Dialog Setup Methods###
    def set_plea_trial_date(self, dialog):
        dialog.plea_trial_date.setDate(TODAY)

    def set_appearance_reason(self, dialog):
        if dialog.case_table == "final_pretrials":
            dialog.appearance_reason_box.setCurrentText("change of plea")
        elif dialog.case_table == "pleas":
            dialog.appearance_reason_box.setCurrentText("change of plea")
        elif dialog.case_table == "trials_to_court":
            dialog.appearance_reason_box.setCurrentText("trial to court")

    def set_balance_due_date(self, dialog):
        dialog.balance_due_date.setDate(TODAY)

    ###Additional Condition/Jail Dialog Setup Methods###
    def set_conditions_case_information_banner(self, dialog):
        column = dialog.charges_gridLayout.columnCount() + 1
        for _index, charge in enumerate(dialog.charges_list):
            charge = vars(charge)
            if charge is not None:
                dialog.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                dialog.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                dialog.charges_gridLayout.addWidget(QLabel(charge.get("finding")), 2, column)
                column += 1

    def set_license_suspension_default_date(self, dialog):
        dialog.license_suspension_date_box.setDate(TODAY)

    def set_community_service_default_date(self, dialog):
        dialog.community_service_date_to_complete_box.setDate(TODAY)

    def set_jail_report_default_date(self, dialog):
        dialog.report_date_box.setDate(TODAY)

    def set_report_days_notes_box(self, dialog):
        if dialog.jail_sentence_execution_type_box.currentText() == "consecutive days":
            dialog.jail_report_days_notes_box.setDisabled(True)
            dialog.jail_report_days_notes_box.setHidden(True)
        else:
            dialog.jail_report_days_notes_box.setDisabled(False)
            dialog.jail_report_days_notes_box.setHidden(False)

    @classmethod
    def hide_boxes(cls, dialog):
        for item in cls.condition_checkbox_list:
            (condition_checkbox, condition_field) = item
            if hasattr(dialog, condition_checkbox):
                getattr(dialog, condition_field).setEnabled(False)
                getattr(dialog, condition_field).setHidden(True)


class AddChargeDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_case_information_banner(dialog)

    def set_case_information_banner(self, dialog):
        dialog.defendant_name_label.setText(
            "State of Ohio v. {defendant_first_name} {defendant_last_name}".format(
                defendant_first_name=dialog.main_dialog.entry_case_information.defendant.first_name,
                defendant_last_name=dialog.main_dialog.entry_case_information.defendant.last_name
            )
        )
        dialog.case_number_label.setText(dialog.main_dialog.entry_case_information.case_number)


class AmendChargeDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_case_information_banner(dialog)

    def set_case_information_banner(self, dialog):
        dialog.defendant_name_label.setText(
            "State of Ohio v. {defendant_first_name} {defendant_last_name}".format(
                defendant_first_name=dialog.main_dialog.entry_case_information.defendant.first_name,
                defendant_last_name=dialog.main_dialog.entry_case_information.defendant.last_name
            )
        )
        dialog.case_number_label.setText(dialog.main_dialog.entry_case_information.case_number)


class FineOnlyDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_plea_trial_date(dialog)
        self.set_appearance_reason(dialog)
        self.set_balance_due_date(dialog)


class JailCCDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_plea_trial_date(dialog)
        self.set_appearance_reason(dialog)
        self.set_balance_due_date(dialog)


class DiversionDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_plea_trial_date(dialog)
        self.set_appearance_reason(dialog)
        diversion_pay_days_to_add = set_future_date(97, None, 1)
        dialog.diversion_fine_pay_date_box.setDate(QDate.currentDate().addDays(diversion_pay_days_to_add))
        jail_report_days_to_add = set_future_date(97, None, 4)
        dialog.diversion_jail_report_date_box.setDate(QDate.currentDate().addDays(jail_report_days_to_add))
        dialog.show_jail_report_date_box()
        dialog.show_other_conditions_box()


class NotGuiltyBondDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_plea_trial_date(dialog)
        self.set_appearance_reason(dialog)


class AddConditionsDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_conditions_case_information_banner(dialog)
        self.set_license_suspension_default_date(dialog)
        self.set_community_service_default_date(dialog)
        dialog.update_community_service_due_date()


class AddJailOnlyDialogViewModifier(BaseDialogViewModifier):
    condition_checkbox_list = [
        ("companion_cases_checkBox", "companion_cases_box"),
        ("companion_cases_checkBox", "jail_term_type_box"),
        ("companion_cases_checkBox", "consecutive_jail_days_label"),
    ]

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_conditions_case_information_banner(dialog)
        self.set_jail_report_default_date(dialog)
        self.hide_boxes(dialog)
        self.set_report_days_notes_box(dialog)


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
        self.set_conditions_case_information_banner(dialog)
        self.set_license_suspension_default_date(dialog)
        self.set_community_service_default_date(dialog)
        dialog.update_community_service_due_date()
        self.hide_boxes(dialog)
        self.set_jail_report_default_date(dialog)
        self.set_report_days_notes_box(dialog)


class AddSpecialBondConditionsDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_special_bond_conditions_case_information_banner(dialog)
        self.set_domestic_violence_surrender_weapons_default_date(dialog)

    def set_special_bond_conditions_case_information_banner(self, dialog):
        column = dialog.charges_gridLayout.columnCount() + 1
        for _index, charge in enumerate(dialog.charges_list):
            charge = vars(charge)
            if charge is not None:
                dialog.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                dialog.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                column += 1

    def set_domestic_violence_surrender_weapons_default_date(self, dialog):
        dialog.domestic_violence_surrender_weapons_dateBox.setDate(TODAY)