from loguru import logger
from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel

from package.controllers.base_dialogs import BaseDialog
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
        super().__init__(parent)
        self.case_information = main_dialog.entry_case_information
        self.main_dialog = main_dialog

    @logger.catch
    def modify_view(self):
        """Overrides the BaseDialog modify_view and modifies the view of AddConditionsDialog
        that is created by the UI file. Gets the total number of charges from the charges in
        charges_list then loops through the charges_list and adds parts of each charge to the
        view. Also sets date fields to 'today.'"""
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
        self.set_community_service_date()

    @logger.catch
    def connect_signals_to_slots(self):
        """Overrides the BaseDialog connect_signals_to_slots entirely because
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
            self.transfer_field_data_to_model(self.case_information.community_service)
        if self.main_dialog.license_suspension_checkBox.isChecked():
            self.transfer_field_data_to_model(self.case_information.license_suspension)
        if self.main_dialog.other_conditions_checkBox.isChecked():
            self.transfer_field_data_to_model(self.case_information.other_conditions)

    @logger.catch
    def set_community_service_date(self, _index=None):
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
    for are based on the checkboxes that are checked on the JCPD screen.

    :conditions_checkbox_list: list of tuples that show or hide fields only when they are
    necessary for additional data input because the checkbox is checked."""
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
        ("companion_cases_checkBox", "companion_cases_box"),
        ("companion_cases_checkBox", "jail_term_type_box"),
        ("companion_cases_checkBox", "consecutive_jail_days_label"),

    ]

    @logger.catch
    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)
        enable_condition_frames(self, main_dialog)

    @logger.catch
    def modify_view(self):
        super().modify_view()
        self.report_date_box.setDate(QDate.currentDate())
        diversion_pay_days_to_add = set_future_date(97, None, 1)
        self.diversion_fine_pay_date_box.setDate(QDate.currentDate().addDays(diversion_pay_days_to_add))
        jail_report_days_to_add = set_future_date(97, None, 4)
        self.diversion_jail_report_date_box.setDate(QDate.currentDate().addDays(jail_report_days_to_add))
        self.hide_boxes()
        self.show_report_days_notes_box()

    @logger.catch
    def add_conditions(self):
        """The method calls the base method add_conditions and then adds community control specific conditions."""
        super().add_conditions()
        if self.main_dialog.community_control_checkBox.isChecked():
            self.transfer_field_data_to_model(self.case_information.community_control)
        if self.main_dialog.jail_checkBox.isChecked():
            self.transfer_field_data_to_model(self.case_information.jail_terms)
        if self.main_dialog.diversion_checkBox.isChecked():
            self.transfer_field_data_to_model(self.case_information.diversion)
            self.case_information.diversion.program_name = self.case_information.diversion.get_program_name()
        if self.main_dialog.impoundment_checkBox.isChecked():
            self.transfer_field_data_to_model(self.case_information.impoundment)
        if self.main_dialog.victim_notification_checkBox.isChecked():
            self.transfer_field_data_to_model(self.case_information.victim_notification)

    @logger.catch
    def connect_signals_to_slots(self):
        """This method overrides the base_dialog connect_signals_to_slots entirely because
        there are no fields to clear or create_entry_button to press."""
        self.cancel_Button.pressed.connect(self.close_event)
        self.add_conditions_Button.pressed.connect(self.add_conditions)
        self.add_conditions_Button.released.connect(self.close_window)
        self.community_service_days_to_complete_box.currentIndexChanged.connect(self.set_community_service_date)
        self.gps_exclusion_checkBox.toggled.connect(self.set_field_enabled)
        self.community_control_not_within_500_feet_checkBox.toggled.connect(self.set_field_enabled)
        self.community_control_no_contact_checkBox.toggled.connect(self.set_field_enabled)
        self.house_arrest_checkBox.toggled.connect(self.set_field_enabled)
        self.community_control_community_service_checkBox.toggled.connect(self.set_field_enabled)
        self.other_community_control_checkBox.toggled.connect(self.set_field_enabled)
        self.alcohol_monitoring_checkBox.toggled.connect(self.set_field_enabled)
        self.pay_restitution_checkBox.toggled.connect(self.set_field_enabled)
        self.report_type_box.currentTextChanged.connect(self.set_report_date)
        self.jail_sentence_execution_type_box.currentTextChanged.connect(self.show_report_days_notes_box)
        self.diversion_jail_imposed_checkBox.toggled.connect(self.set_field_enabled)
        self.companion_cases_checkBox.toggled.connect(self.set_field_enabled)

    def show_report_days_notes_box(self):
        if self.jail_sentence_execution_type_box.currentText() == "consecutive days":
            self.jail_report_days_notes_box.setDisabled(True)
            self.jail_report_days_notes_box.setHidden(True)
        else:
            self.jail_report_days_notes_box.setDisabled(False)
            self.jail_report_days_notes_box.setHidden(False)

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
        for item in AddCommunityControlDialog.condition_checkbox_list:
            (condition_checkbox, condition_field) = item
            if hasattr(self, condition_checkbox):
                if getattr(self, condition_checkbox).isChecked():
                    getattr(self, condition_field).setEnabled(True)
                    getattr(self, condition_field).setHidden(False)
                    getattr(self, condition_field).setFocus(True)
                else:
                    getattr(self, condition_field).setEnabled(False)
                    getattr(self, condition_field).setHidden(True)

    def hide_boxes(self):
        """This method is called from modify_view as part of the init to hide all optional boxes on load."""
        for item in AddCommunityControlDialog.condition_checkbox_list:
            (condition_checkbox, condition_field) = item
            if hasattr(self, condition_checkbox):
                getattr(self, condition_field).setEnabled(False)
                getattr(self, condition_field).setHidden(True)


class AddSpecialBondConditionsDialog(BaseDialog, Ui_AddSpecialBondConditionsDialog):
    """The AddSpecialBondConditionsDialog is for Bond Conditions for NGBond and FTABond Dialogs."""
    @logger.catch
    def __init__(self, main_dialog, parent=None):
        self.charges_list = main_dialog.entry_case_information.charges_list  # Show charges on banner
        super().__init__(parent)
        self.case_information = main_dialog.entry_case_information
        self.main_dialog = main_dialog
        enable_condition_frames(self, main_dialog)

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
        self.domestic_violence_surrender_weapons_dateBox.setDate(QtCore.QDate.currentDate())

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
            self.transfer_field_data_to_model(self.case_information.domestic_violence_conditions)
        if self.main_dialog.admin_license_suspension_checkBox.isChecked():
            self.transfer_field_data_to_model(self.case_information.admin_license_suspension)
        if self.main_dialog.no_contact_checkBox.isChecked():
            self.transfer_field_data_to_model(self.case_information.no_contact)
        if self.main_dialog.custodial_supervision_checkBox.isChecked():
            self.transfer_field_data_to_model(self.case_information.custodial_supervision)
        if self.main_dialog.other_conditions_checkBox.isChecked():
            self.transfer_field_data_to_model(self.case_information.other_conditions)
        if self.main_dialog.vehicle_seizure_checkBox.isChecked():
            self.transfer_field_data_to_model(self.case_information.vehicle_seizure)
