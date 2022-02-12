from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel
from package.controllers.base_dialogs import BaseDialog
from loguru import logger
from package.models.case_information import OtherConditions, DomesticViolenceBondConditions, \
    AdminLicenseSuspensionConditions, NoContact, CustodialSupervision, VehicleSeizure
from package.views.add_community_control_dialog_ui import Ui_AddCommunityControlDialog
from package.views.add_conditions_dialog_ui import Ui_AddConditionsDialog
from package.views.add_special_bond_conditions_dialog_ui import Ui_AddSpecialBondConditionsDialog
from package.controllers.helper_functions import set_future_date


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
        if hasattr(main_dialog, item[0]):
            if getattr(main_dialog, item[0]).isChecked():
                getattr(conditions_dialog, item[1]).setEnabled(True)
            else:
                frame = getattr(conditions_dialog, item[1])
                frame.setParent(None)
                frame.deleteLater()


class ConditionsDialog(BaseDialog):
    def __init__(self, main_dialog, parent=None):
        self.charges_list = main_dialog.entry_case_information.charges_list  # Show charges on banner
        super().__init__(parent)
        self.case_information = main_dialog.entry_case_information
        self.main_dialog = main_dialog

    @logger.catch
    def modify_view(self):
        """Modifies the view of AddConditionsDialog that is created by the UI
        file. Gets the total number of charges from the charges in charges_list then
        loops through the charges_list and adds parts of each charge to the
        view."""
        column = self.charges_gridLayout.columnCount() + 1
        for _index, charge in enumerate(self.charges_list):
            charge = vars(charge)
            if charge is not None:
                self.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                self.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                self.charges_gridLayout.addWidget(QLabel(charge.get("finding")), 2, column)
                column += 1
        self.license_suspension_date_box.setDate(QtCore.QDate.currentDate())
        self.community_service_date_to_complete_box.setDate(QtCore.QDate.currentDate())

    @logger.catch
    def connect_signals_to_slots(self):
        """This method overrides the base_dialog connect_signals_to_slots entirely because
        there are no fields to clear or create_entry_button to press."""
        self.cancel_Button.pressed.connect(self.close_event)
        self.add_conditions_Button.pressed.connect(self.add_conditions)
        self.add_conditions_Button.released.connect(self.close_window)
        self.community_service_days_to_complete_box.currentIndexChanged.connect(
            self.set_community_service_date
        )

    @logger.catch
    def add_conditions(self):
        """The conditions in this method in the case class are in both the No Jail and the JaillCC dialogs."""
        if self.main_dialog.community_service_checkBox.isChecked():
            self.add_conditions_factory(self.case_information.community_service, self.case_information.community_service.terms_list)
        if self.main_dialog.license_suspension_checkBox.isChecked():
            self.add_conditions_factory(self.case_information.license_suspension, self.case_information.license_suspension.terms_list)
        if self.main_dialog.other_conditions_checkBox.isChecked():
            self.add_conditions_factory(self.case_information.other_conditions, self.case_information.other_conditions.terms_list)

    @logger.catch
    def add_conditions_factory(self, conditions, terms_list):
        """Using the terms_list for the specific condition, which is an attribute in the model, this method cycles
        through all the fields in the UI and transfers the data from the field in the view to the model."""
        self.widget_type_check_set(conditions, terms_list)

    @logger.catch
    def set_community_service_date(self, _index):
        """Sets the community_service_date_to_complete_box based on the number of days chosen in the
        community_service_date_to_complete_box. The _index is passed from the signal but not used."""
        days_to_complete = int(self.community_service_days_to_complete_box.currentText())
        self.community_service_date_to_complete_box.setDate(QDate.currentDate().addDays(days_to_complete))


class AddConditionsDialog(ConditionsDialog, Ui_AddConditionsDialog):
    """The AddConditionsDialog is created when the addConditionsButton is clicked on
    the NoJailPleaDialog. The conditions that are available to enter information
    for are based on the checkboxes that are checked on the NJPD screen."""
    @logger.catch
    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)
        enable_condition_frames(self, main_dialog)


class AddCommunityControlDialog(ConditionsDialog, Ui_AddCommunityControlDialog):
    """The AddCommunityControlDialog is created when the addConditionsButton is clicked on
    the JailCCPleaDialog. The conditions that are available to enter information
    for are based on the checkboxes that are checked on the JCPD screen."""
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
        ("diversion_jail_imposed_checkBox", "diversion_jail_report_date_box"),
    ]

    @logger.catch
    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)
        self.community_control = True if main_dialog.community_control_checkBox.isChecked() else False
        self.jail_terms = True if main_dialog.jail_checkBox.isChecked() else False
        self.diversion = True if main_dialog.diversion_checkBox.isChecked() else False
        self.impoundment = True if main_dialog.impoundment_checkBox.isChecked() else False
        self.victim_notification = True if main_dialog.victim_notification_checkBox.isChecked() else False
        enable_condition_frames(self, main_dialog)

    @logger.catch
    def modify_view(self):
        super().modify_view()
        self.report_date_box.setDate(QDate.currentDate())
        diversion_pay_days_to_add = set_future_date(90, None, 1)
        self.diversion_fine_pay_date_box.setDate(QDate.currentDate().addDays(diversion_pay_days_to_add))
        jail_report_days_to_add = set_future_date(90, None, 4)
        self.diversion_jail_report_date_box.setDate(QDate.currentDate().addDays(jail_report_days_to_add))
        self.hide_boxes()

    @logger.catch
    def add_conditions(self):
        """The method calls the base method and then adds community control specific conditions to add."""
        super().add_conditions()
        if self.main_dialog.community_control_checkBox.isChecked():
            self.add_conditions_factory(self.case_information.community_control, self.case_information.community_control.terms_list)
        if self.main_dialog.jail_checkBox.isChecked():
            self.add_conditions_factory(self.case_information.jail_terms, self.case_information.jail_terms.terms_list)
        if self.main_dialog.diversion_checkBox.isChecked():
            self.add_conditions_factory(self.case_information.diversion, self.case_information.diversion.terms_list)
        if self.main_dialog.impoundment_checkBox.isChecked():
            self.add_conditions_factory(self.case_information.impoundment, self.case_information.impoundment.terms_list)
        if self.main_dialog.victim_notification_checkBox.isChecked():
            self.add_conditions_factory(self.case_information.victim_notification, self.case_information.victim_notification.terms_list)

    @logger.catch
    def connect_signals_to_slots(self):
        """This method overrides the base_dialog connect_signals_to_slots entirely because
        there are no fields to clear or create_entry_button to press."""
        self.cancel_Button.pressed.connect(self.close_event)
        self.add_conditions_Button.pressed.connect(self.add_conditions)
        self.add_conditions_Button.released.connect(self.close_window)
        self.community_service_days_to_complete_box.currentIndexChanged.connect(
            self.set_community_service_date
        )
        self.gps_exclusion_checkBox.toggled.connect(self.set_field_enabled)
        self.community_control_not_within_500_feet_checkBox.toggled.connect(self.set_field_enabled)
        self.community_control_no_contact_checkBox.toggled.connect(self.set_field_enabled)
        self.house_arrest_checkBox.toggled.connect(self.set_field_enabled)
        self.community_control_community_service_checkBox.toggled.connect(self.set_field_enabled)
        self.other_community_control_checkBox.toggled.connect(self.set_field_enabled)
        self.alcohol_monitoring_checkBox.toggled.connect(self.set_field_enabled)
        self.pay_restitution_checkBox.toggled.connect(self.set_field_enabled)
        self.report_type_box.currentTextChanged.connect(self.set_report_date)
        self.diversion_jail_imposed_checkBox.toggled.connect(self.set_field_enabled)

    def set_report_date(self):
        if self.report_type_box.currentText() == "date set by Office of Community Control":
            self.report_date_box.setDisabled(True)
            self.report_date_box.setHidden(True)
            self.report_time_box.setDisabled(True)
            self.report_time_box.setHidden(True)
            self.report_date_label.setHidden(True)
            self.report_time_label.setHidden(True)
        elif self.report_type_box.currentText() == "forthwith":
            self.report_date_box.setDisabled(True)
            self.report_date_box.setHidden(True)
            self.report_time_box.setDisabled(True)
            self.report_time_box.setHidden(True)
            self.report_date_label.setHidden(True)
            self.report_time_label.setHidden(True)
        else:
            self.report_date_box.setEnabled(True)
            self.report_date_box.setHidden(False)
            self.report_time_box.setEnabled(True)
            self.report_time_box.setHidden(False)
            self.report_date_label.setHidden(False)
            self.report_time_label.setHidden(False)

    def set_field_enabled(self):
        """Loops through the conditions_checkbox_list and if the box is checked for the condition it will show
        any additional fields that are required for that condition."""
        for index, item in enumerate(AddCommunityControlDialog.condition_checkbox_list):
            if hasattr(self, item[0]):
                if getattr(self, item[0]).isChecked():
                    getattr(self, item[1]).setEnabled(True)
                    getattr(self, item[1]).setHidden(False)
                    getattr(self, item[1]).setFocus(True)
                else:
                    getattr(self, item[1]).setEnabled(False)
                    getattr(self, item[1]).setHidden(True)

    def hide_boxes(self):
        for index, item in enumerate(AddCommunityControlDialog.condition_checkbox_list):
            if hasattr(self, item[0]):
                getattr(self, item[1]).setEnabled(False)
                getattr(self, item[1]).setHidden(True)


class AddSpecialBondConditionsDialog(BaseDialog, Ui_AddSpecialBondConditionsDialog):
    """The AddSpecialBondConditionsDialog is for Bond Conditions for NGBond and FTABond Dialogs."""
    @logger.catch
    def __init__(self, main_dialog, parent=None):
        self.charges_list = main_dialog.entry_case_information.charges_list  # Show charges on banner
        super().__init__(parent)
        self.case_information = main_dialog.entry_case_information
        self.main_dialog = main_dialog
        self.domestic_violence_surrender_weapons_dateBox.setDate(QtCore.QDate.currentDate())
        enable_condition_frames(self, main_dialog)

    @logger.catch
    def connect_signals_to_slots(self):
        """This method overrides the base_dialog method because there are no
        fields to clear or create_entry button to press."""
        self.cancel_Button.pressed.connect(self.close_event)
        self.add_special_conditions_Button.pressed.connect(self.add_special_conditions)
        self.add_special_conditions_Button.released.connect(self.close_window)

    @logger.catch
    def add_special_conditions(self):
        """The method is connected to the pressed() signal of add_special_conditions_Button on the
        Add Special Conditions screen."""
        if self.main_dialog.domestic_violence_checkBox.isChecked():
            self.add_domestic_violence_terms()
        if self.main_dialog.admin_license_suspension_checkBox.isChecked():
            self.add_admin_license_suspension_terms()
        if self.main_dialog.no_contact_checkBox.isChecked():
            self.add_no_contact_terms()
        if self.main_dialog.custodial_supervision_checkBox.isChecked():
            self.add_custodial_supervision_terms()
        if self.main_dialog.other_conditions_checkBox.isChecked():
            self.add_other_condition_terms()
        if self.main_dialog.vehicle_seizure_checkBox.isChecked():
            self.add_vehicle_seizure_terms()

    @logger.catch
    def add_vehicle_seizure_terms(self):
        vehicle_seizure_terms_list = [
            ("vehicle_make_model", "vehicle_make_model_box"),
            ("vehicle_license_plate", "vehicle_license_plate_box"),
            ("tow_to_residence", "tow_to_residence_checkBox"),
            ("motion_to_return_vehicle", "motion_to_return_vehicle_checkBox"),
            ("state_opposes", "state_opposes_box"),
            ("disposition_motion_to_return", "disposition_motion_to_return_box"),
        ]
        self.widget_type_check_set(self.case_information.vehicle_seizure, vehicle_seizure_terms_list)
        self.case_information.vehicle_seizure.ordered = True

    @logger.catch
    def add_other_condition_terms(self):
        """TODO: Refactor into one conditions dialog and rename to match add_conditions version."""
        other_conditions_terms_list = [
            ("terms", "other_conditions_textEdit"),
        ]
        self.widget_type_check_set(self.case_information.other_conditions, other_conditions_terms_list)
        self.case_information.other_conditions.ordered = True

    @logger.catch
    def add_custodial_supervision_terms(self):
        custodial_supervision_terms_list = [
            ("supervisor", "custodial_supervision_supervisor_box"),
        ]
        self.widget_type_check_set(self.case_information.custodial_supervision, custodial_supervision_terms_list)
        self.case_information.custodial_supervision.ordered = True

    @logger.catch
    def add_domestic_violence_terms(self):
        domestic_violence_terms_list = [
            ("vacate_residence", "domestic_violence_vacate_checkBox"),
            ("residence_address", "domestic_violence_residence_box"),
            ("exclusive_possession_to", "domestic_violence_exclusive_possession_to_box"),
            ("surrender_weapons", "domestic_violence_surrender_weapons_checkBox"),
            ("surrender_weapons_date", "domestic_violence_surrender_weapons_dateBox"),
        ]
        self.widget_type_check_set(self.case_information.domestic_violence_conditions, domestic_violence_terms_list)
        self.case_information.domestic_violence_conditions.ordered = True

    @logger.catch
    def add_no_contact_terms(self):
        no_contact_terms_list = [
            ("name", "no_contact_name_box"),
        ]
        self.widget_type_check_set(self.case_information.no_contact, no_contact_terms_list)
        self.case_information.no_contact.ordered = True

    @logger.catch
    def add_admin_license_suspension_terms(self):
        admin_license_terms_list = [
            ("objection", "admin_license_suspension_objection_box"),
            ("disposition", "admin_license_suspension_disposition_box"),
            ("explanation", "admin_license_suspension_explanation_box"),
        ]
        self.widget_type_check_set(self.case_information.admin_license_suspension, admin_license_terms_list)
        self.case_information.admin_license_suspension.ordered = True

    @logger.catch
    def modify_view(self):
        """Modifies the view that is created by the UI file. Gets the total number of charges
        from the charges in charges_list then loops through the charges_list and adds parts of
        each charge to the view."""
        column = self.charges_gridLayout.columnCount() + 1
        for _index, charge in enumerate(self.charges_list):
            charge = vars(charge)
            if charge is not None:
                self.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                self.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                column += 1
