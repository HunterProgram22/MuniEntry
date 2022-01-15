from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel
from controllers.base_dialogs import BaseDialog
from loguru import logger
from models.case_information import CommunityService, LicenseSuspension, OtherConditions, \
    DomesticViolenceBondConditions, AdminLicenseSuspensionConditions, NoContact, CustodialSupervision, \
    CommunityControl, VehicleSeizure, JailTerms
from views.add_community_control_dialog_ui import Ui_AddCommunityControlDialog
from views.add_conditions_dialog_ui import Ui_AddConditionsDialog
from views.add_special_bond_conditions_dialog_ui import Ui_AddSpecialBondConditionsDialog


CONDITIONS = [
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
]


def enable_condition_frames(conditions_dialog, main_dialog):
    for index, item in enumerate(CONDITIONS):
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
        self.community_service = True if main_dialog.community_service_checkBox.isChecked() else False
        self.license_suspension = True if main_dialog.license_suspension_checkBox.isChecked() else False
        self.other_conditions = True if main_dialog.other_conditions_checkBox.isChecked() else False

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
    def add_conditions(self):
        """The method is connected to the pressed() signal of add_conditions_Button on the
        Add Conditions screen.

        TODO: Creating a new instance of the special conditions here to avoid data being persistent
        and carrying over to a future cms_case. This requires resetting ordered to true even though it
        is set to true by the add_conditions_dict. Fix is probably to not set a default
        instance of the class in the dataclass.
        """
        if self.community_service is True:
            self.case_information.community_service = CommunityService()
            self.add_community_service_terms()
        if self.license_suspension is True:
            self.case_information.license_suspension = LicenseSuspension()
            self.add_license_suspension_details()
        if self.other_conditions is True:
            self.case_information.other_conditions = OtherConditions()
            self.add_other_condition_details()

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
    def add_community_service_terms(self):
        community_service_terms_list = [
            ("hours_of_service", "community_service_hours_ordered_box"),
            ("days_to_complete_service", "community_service_days_to_complete_box"),
            ("due_date_for_service", "community_service_date_to_complete_box"),
        ]
        self.widget_type_check_set(self.case_information.community_service, community_service_terms_list)
        self.case_information.community_service.ordered = True

    @logger.catch
    def add_jail_commitment_terms(self):
        jail_commitment_terms_list = [
            ("report_type", "report_type_box"),
            ("report_date", "report_date_box"),
            ("jail_time_credit", "jail_time_credit_box"),
            ("jail_term_type", "jail_term_type_box"),
            ("dip_ordered", "dip_checkBox"),
        ]
        self.widget_type_check_set(self.case_information.jail_terms, jail_commitment_terms_list)
        self.case_information.jail_terms.ordered = True

    @logger.catch
    def add_license_suspension_details(self):
        license_suspension_terms_list = [
            ("license_type", "license_type_box"),
            ("suspended_date", "license_suspension_date_box"),
            ("suspension_term", "term_of_suspension_box"),
            ("remedial_driving_class_required", "remedial_driving_class_checkBox"),
        ]
        self.widget_type_check_set(self.case_information.license_suspension, license_suspension_terms_list)
        self.case_information.license_suspension.ordered = True

    @logger.catch
    def add_other_condition_details(self):
        other_conditions_terms_list = [
            ("terms", "other_conditions_textEdit"),
        ]
        self.widget_type_check_set(self.case_information.other_conditions, other_conditions_terms_list)
        self.case_information.other_conditions.ordered = True

    @logger.catch
    def add_community_control_terms(self):
        community_control_terms_list = [
            ("type_of_control", "community_control_type_of_control_box"),
            ("term_of_control", "community_control_term_of_control_box"),
            ("not_within_500_feet_ordered", "community_control_not_within_500_feet_checkBox"),
            ("not_within_500_feet_person", "community_control_not_within_500_feet_person_box"),
            ("no_contact_with_ordered", "community_control_no_contact_checkBox"),
            ("no_contact_with_person", "community_control_no_contact_with_box"),
            ("alcohol_monitoring", "alcohol_monitoring_checkBox"),
            ("alcohol_monitoring_time", "alcohol_monitoring_time_box"),
            ("house_arrest", "house_arrest_checkBox"),
            ("house_arrest_time", "house_arrest_time_box"),
            ("interlock_vehicles_only", "interlock_vehicles_checkBox"),
            ("pay_restitution", "pay_restitution_checkBox"),
            ("pay_restitution_to", "pay_restitution_to_box"),
            ("pay_restitution_amount", "pay_restitution_amount_box"),
            ("antitheft_program", "antitheft_checkBox"),
            ("anger_management_program", "anger_management_checkBox"),
            ("alcohol_evaluation", "alcohol_evaluation_checkBox"),
            ("domestic_violence_program", "domestic_violence_program_checkBox"),
            ("driver_intervention_program", "driver_intervention_program_checkBox"),
            ("mental_health_evaluation", "mental_health_evaluation_checkBox"),
            ("other_community_control", "other_community_control_checkBox"),
            ("other_community_control_conditions", "other_community_control_conditions_box"),
            ("community_control_community_service", "community_control_community_service_checkBox"),
            ("community_control_community_service_hours", "community_control_community_service_hours_box"),
            ("gps_exclusion", "gps_exclusion_checkBox"),
            ("gps_exclusion_radius", "gps_exclusion_radius_box"),
            ("gps_exclusion_location", "gps_exclusion_location_box"),
            ("daily_reporting", "daily_reporting_checkBox"),
        ]
        self.widget_type_check_set(self.case_information.community_control, community_control_terms_list)
        self.case_information.community_control.ordered = True

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
    @logger.catch
    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)
        self.community_control = True if main_dialog.community_control_checkBox.isChecked() else False
        self.jail_terms = True if main_dialog.jail_checkBox.isChecked() else False
        enable_condition_frames(self, main_dialog)

    @logger.catch
    def modify_view(self):
        super().modify_view()
        self.report_date_box.setDate(QtCore.QDate.currentDate())

    @logger.catch
    def add_conditions(self):
        """The method calls the base method and then adds community control specific conditions to add."""
        super().add_conditions()
        if self.community_control is True:
            self.case_information.community_control = CommunityControl()
            self.add_community_control_terms()
        if self.jail_terms is True:
            self.case_information.jail_terms = JailTerms()
            self.add_jail_commitment_terms()

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
        self.community_control_not_within_500_feet_checkBox.toggled.connect(self.set_field_enabled_2)

    def set_field_enabled(self):
        if self.gps_exclusion_checkBox.isChecked():
            self.gps_exclusion_radius_box.setHidden(False)
            self.gps_exclusion_radius_box.setEnabled(True)
            self.gps_exclusion_location_box.setHidden(False)
            self.gps_exclusion_location_box.setEnabled(True)
            self.scrollAreaWidgetContents.adjustSize()
            return None
        else:
            self.gps_exclusion_radius_box.setHidden(True)
            self.gps_exclusion_radius_box.setDisabled(True)
            self.gps_exclusion_location_box.setHidden(True)
            self.gps_exclusion_location_box.setDisabled(True)
            self.scrollAreaWidgetContents.adjustSize()
            return None

    def set_field_enabled_2(self):
        if self.community_control_not_within_500_feet_checkBox.isChecked():
            self.community_control_not_within_500_feet_person_box.setHidden(False)
            self.scrollAreaWidgetContents.adjustSize()
            return None
        else:
            self.community_control_not_within_500_feet_person_box.setHidden(True)
            self.scrollAreaWidgetContents.adjustSize()
            return None


class AddSpecialBondConditionsDialog(BaseDialog, Ui_AddSpecialBondConditionsDialog):
    """The AddSpecialBondConditionsDialog is for Bond Conditions for NGBond and FTABond Dialogs."""
    @logger.catch
    def __init__(self, main_dialog, parent=None):
        self.charges_list = main_dialog.entry_case_information.charges_list  # Show charges on banner
        super().__init__(parent)
        self.case_information = main_dialog.entry_case_information
        self.domestic_violence_surrender_weapons_dateBox.setDate(QtCore.QDate.currentDate())
        self.domestic_violence = main_dialog.domestic_violence_checkBox.isChecked()
        self.admin_license_suspension = main_dialog.admin_license_suspension_checkBox.isChecked()
        self.vehicle_seizure = main_dialog.vehicle_seizure_checkBox.isChecked()
        self.no_contact = main_dialog.no_contact_checkBox.isChecked()
        self.custodial_supervision = main_dialog.custodial_supervision_checkBox.isChecked()
        self.other_conditions = main_dialog.other_conditions_checkBox.isChecked()
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
        Add Special Conditions screen.

        TODO: Creating a new instance of the special conditions here to avoid data being persistent
        and carrying over to a future cms_case. This requires resetting ordered to true even though it
        is set to true by the add_special_conditions_dict. Fix is probably to not set a default
        instance of the class in the dataclass."""
        if self.domestic_violence is True:
            self.case_information.domestic_violence_conditions = DomesticViolenceBondConditions()
            self.add_domestic_violence_terms()
        if self.admin_license_suspension is True:
            self.case_information.admin_license_suspension = AdminLicenseSuspensionConditions()
            self.add_admin_license_suspension_terms()
        if self.no_contact is True:
            self.case_information.no_contact = NoContact()
            self.add_no_contact_terms()
        if self.custodial_supervision is True:
            self.case_information.custodial_supervision = CustodialSupervision()
            self.add_custodial_supervision_terms()
        if self.other_conditions is True:
            self.case_information.other_conditions = OtherConditions()
            self.add_other_condition_terms()
        if self.vehicle_seizure is True:
            self.case_information.vehicle_seizure = VehicleSeizure()
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
