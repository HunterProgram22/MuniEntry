from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QLabel
from controllers.base_dialogs import BaseDialog
from loguru import logger
from models.case_information import CommunityService, LicenseSuspension, OtherConditions, \
    DomesticViolenceBondConditions, AdminLicenseSuspensionConditions, NoContact, CustodialSupervision, VehicleSeizure
from views.add_conditions_dialog_ui import Ui_AddConditionsDialog
from views.add_special_bond_conditions_dialog_ui import Ui_AddSpecialBondConditionsDialog


class AddConditionsDialog(BaseDialog, Ui_AddConditionsDialog):
    """The AddConditionsDialog is created when the addConditionsButton is clicked on
    the NoJailPleaDialog. The conditions that are available to enter information
    for are based on the checkboxes that are checked on the NJPD screen."""
    @logger.catch
    def __init__(self, main_dialog, parent=None):
        self.charges_list = main_dialog.case_information.charges_list  # Show charges on banner
        super().__init__(self, parent)
        self.case_information = main_dialog.case_information
        self.community_service = main_dialog.community_service_checkBox.isChecked()
        self.license_suspension = main_dialog.license_suspension_checkBox.isChecked()
        self.other_conditions = main_dialog.other_conditions_checkBox.isChecked()
        self.other_conditions = main_dialog.other_conditions_checkBox.isChecked()
        self.enable_condition_frames()

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
    def modify_view(self):
        """Modifies the view of AddConditionsDialog that is created by the UI
        file. Gets the total number of charges from the charges in charges_list then
        loops through the charges_list and adds parts of each charge to the
        view."""
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowMaximizeButtonHint)
        column = self.charges_gridLayout.columnCount() + 1
        for _index, charge in enumerate(self.charges_list):
            charge = vars(charge)
            if charge is not None:
                self.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                self.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                self.charges_gridLayout.addWidget(QLabel(charge.get("finding")), 2, column)
                column += 1

    @logger.catch
    def enable_condition_frames(self):
        """Enables the frames on the AddConditionsDialog dialog if the condition is checked
        on the NoJailPleaDialog screen."""
        if self.other_conditions is True:
            self.other_conditions_frame.setEnabled(True)
        if self.license_suspension is True:
            self.license_suspension_frame.setEnabled(True)
            self.license_suspension_date_box.setDate(QtCore.QDate.currentDate())
        if self.community_service is True:
            self.community_service_frame.setEnabled(True)
            self.community_service_date_to_complete_box.setDate(QtCore.QDate.currentDate())

    @logger.catch
    def add_conditions(self):
        """The method is connected to the pressed() signal of add_conditions_Button on the
        Add Conditions screen.

        TODO: Creating a new instance of the special conditions here to avoid data being persistent
        and carrying over to a future case. This requires resetting ordered to true even though it
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
    def add_community_service_terms(self):
        """The method adds the data entered to the CommunityService object
        that is created when the dialog is initialized.
        SEE COMMENT in add_conditions about need to rest value to true."""
        self.case_information.community_service.hours_of_service = \
            self.community_service_hours_ordered_box.value()
        self.case_information.community_service.days_to_complete_service = \
            self.community_service_days_to_complete_box.currentText()
        self.case_information.community_service.due_date_for_service = \
            self.community_service_date_to_complete_box.date().toString("MMMM dd, yyyy")
        self.case_information.community_service.ordered = True

    @logger.catch
    def add_license_suspension_details(self):
        """The method adds the data entered to the LicenseSuspension object
        that is created when the dialog is initialized."""
        self.case_information.license_suspension.license_type = \
            self.license_type_box.currentText()
        self.case_information.license_suspension.suspended_date = \
            self.license_suspension_date_box.date().toString("MMMM dd, yyyy")
        self.case_information.license_suspension.suspension_term = \
            self.term_of_suspension_box.currentText()
        if self.remedial_driving_class_checkBox.isChecked():
            self.case_information.license_suspension.remedial_driving_class_required = True
        else:
            self.case_information.license_suspension.remedial_driving_class_required = False
        self.case_information.license_suspension.ordered = True

    @logger.catch
    def add_other_condition_details(self):
        """The method allows for adding other conditions based on free form text
        entry."""
        self.case_information.other_conditions.terms = (
            self.other_conditions_plainTextEdit.toPlainText()
        )
        self.case_information.other_conditions.ordered = True

    @logger.catch
    def set_community_service_date(self, _index):
        """Sets the community_service_date_to_complete_box based on the number
        of days chosen in the community_service_date_to_complete_box. The _index is passed from the
        signal but not used."""
        days_to_complete = int(self.community_service_days_to_complete_box.currentText())
        self.community_service_date_to_complete_box.setDate(
            QDate.currentDate().addDays(days_to_complete)
        )


class AddSpecialBondConditionsDialog(BaseDialog, Ui_AddSpecialBondConditionsDialog):
    """The AddSpecialBondConditionsDialog is for Bond Conditions for NGBond and FTABond Dialogs."""
    @logger.catch
    def __init__(self, main_dialog, parent=None):
        self.charges_list = main_dialog.case_information.charges_list  # Show charges on banner
        super().__init__(self, parent)
        self.case_information = main_dialog.case_information
        self.domestic_violence = main_dialog.domestic_violence_checkBox.isChecked()
        self.admin_license_suspension = main_dialog.admin_license_suspension_checkBox.isChecked()
        self.vehicle_seizure = main_dialog.vehicle_seizure_checkBox.isChecked()
        self.no_contact = main_dialog.no_contact_checkBox.isChecked()
        self.custodial_supervision = main_dialog.custodial_supervision_checkBox.isChecked()
        self.other_conditions = main_dialog.other_conditions_checkBox.isChecked()
        self.enable_condition_frames()

    @logger.catch
    def connect_signals_to_slots(self):
        """This method overrides the base_dialog method because there are no
        fields to clear or create_entry button to press."""
        self.cancel_Button.pressed.connect(self.close_event)
        self.add_special_conditions_Button.pressed.connect(self.add_special_conditions)
        self.add_special_conditions_Button.released.connect(self.close_window)

    @logger.catch
    def enable_condition_frames(self):
        if self.domestic_violence is True:
            self.domestic_violence_frame.setEnabled(True)
        if self.admin_license_suspension is True:
            self.admin_license_suspension_frame.setEnabled(True)
        if self.vehicle_seizure is True:
            self.vehicle_seizure_frame.setEnabled(True)
        if self.no_contact is True:
            self.no_contact_frame.setEnabled(True)
        if self.custodial_supervision is True:
            self.custodial_supervision_frame.setEnabled(True)
        if self.other_conditions is True:
            self.other_conditions_frame.setEnabled(True)

    @logger.catch
    def add_special_conditions(self):
        """The method is connected to the pressed() signal of add_special_conditions_Button on the
        Add Special Conditions screen.

        TODO: Creating a new instance of the special conditions here to avoid data being persistent
        and carrying over to a future case. This requires resetting ordered to true even though it
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
        self.case_information.vehicle_seizure.ordered = self.vehicle_seizure
        self.case_information.vehicle_seizure.vehicle_make_model = \
            self.vehicle_make_model_box.text()
        self.case_information.vehicle_seizure.vehicle_license_plate = \
            self.vehicle_license_plate_box.text()
        self.case_information.vehicle_seizure.tow_to_residence = \
            self.tow_to_residence_checkBox.isChecked()
        self.case_information.vehicle_seizure.motion_to_return_vehicle = \
            self.motion_to_return_vehicle_checkBox.isChecked()
        self.case_information.vehicle_seizure.state_opposes = \
            self.state_opposes_box.currentText()
        self.case_information.vehicle_seizure.disposition_motion_to_return = \
            self.disposition_motion_to_return_box.currentText()

    @logger.catch
    def add_other_condition_terms(self):
        """The method allows for adding other conditions based on free form text
        entry.
        TODO: Refactor into one conditions dialog and rename to match add_conditions version."""
        self.case_information.other_conditions.ordered = self.other_conditions
        self.case_information.other_conditions.terms = \
            self.other_conditions_plainTextEdit.toPlainText()

    @logger.catch
    def add_custodial_supervision_terms(self):
        self.case_information.custodial_supervision.ordered = self.custodial_supervision
        self.case_information.custodial_supervision.supervisor = \
            self.custodial_supervision_supervisor_box.text()

    @logger.catch
    def add_domestic_violence_terms(self):
        self.case_information.domestic_violence_conditions.ordered = self.domestic_violence
        self.case_information.domestic_violence_conditions.vacate_residence = \
            self.domestic_violence_vacate_checkBox.isChecked()
        self.case_information.domestic_violence_conditions.residence_address = \
            self.domestic_violence_residence_box.text()
        self.case_information.domestic_violence_conditions.exclusive_possession_to = \
            self.domestic_violence_exclusive_possession_to_box.text()
        self.case_information.domestic_violence_conditions.surrender_weapons = \
            self.domestic_violence_surrender_weapons_checkBox.isChecked()
        self.case_information.domestic_violence_conditions.surrender_weapons_date = \
            self.domestic_violence_surrender_weapons_dateBox.date().toString("MMMM dd, yyyy")

    @logger.catch
    def add_no_contact_terms(self):
        self.case_information.no_contact.ordered = self.no_contact
        self.case_information.no_contact.name = self.no_contact_name_box.text()

    @logger.catch
    def add_admin_license_suspension_terms(self):
        self.case_information.admin_license_suspension.ordered = \
            self.admin_license_suspension
        self.case_information.admin_license_suspension.objection = \
            self.admin_license_suspension_objection_box.currentText()
        self.case_information.admin_license_suspension.disposition = \
            self.admin_license_suspension_disposition_box.currentText()
        self.case_information.admin_license_suspension.explanation = \
            self.admin_license_suspension_explanation_box.text()

    @logger.catch
    def modify_view(self):
        """Modifies the view that is created by the UI file. Gets the total number of charges
        from the charges in charges_list then loops through the charges_list and adds parts of
        each charge to the view."""
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowMaximizeButtonHint)
        column = self.charges_gridLayout.columnCount() + 1
        for _index, charge in enumerate(self.charges_list):
            charge = vars(charge)
            if charge is not None:
                self.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                self.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                column += 1
