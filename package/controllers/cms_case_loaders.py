"""Module for loading the CMS case data into the main_entry_dialog view."""
from __future__ import annotations
from package.models.criminal_charge_models import CriminalCharge


class CmsNoChargeLoader:
    """Class for Loading CMS data when there are no charges that need to be loaded for the dialog.
    This is for dialogs with no ChargeGrid."""
    def __init__(self, dialog: QDialog) -> None:
        self.dialog = dialog
        self.cms_case = dialog.cms_case
        if self.cms_case.case_number is not None:
            self.load_cms_data()

    def load_cms_data(self) -> None:
        """Loads the case management system data to the dialog."""
        self.set_case_number()
        self.set_defendant_name()
        self.set_defense_counsel_name()
        try:
            self.set_defense_counsel_type()
        except AttributeError:
            pass

    def set_case_number(self) -> None:
        self.dialog.case_number_lineEdit.setText(self.cms_case.case_number)

    def set_defendant_name(self) -> None:
        self.dialog.defendant_first_name_lineEdit.setText(self.cms_case.defendant.first_name)
        self.dialog.defendant_last_name_lineEdit.setText(self.cms_case.defendant.last_name)

    def set_defense_counsel_name(self) -> None:
        if self.cms_case.defense_counsel is not None:
            self.dialog.defense_counsel_name_box.addItem(self.cms_case.defense_counsel)
            self.dialog.defense_counsel_name_box.setCurrentText(self.cms_case.defense_counsel)

    def set_defense_counsel_type(self) -> None:
        if self.cms_case.defense_counsel_type == "PD":
            self.dialog.defense_counsel_type_box.setCurrentText("Public Defender")
        elif self.cms_case.defense_counsel.strip() == "":
            self.dialog.defense_counsel_type_box.setCurrentText("Public Defender")
        else:
            self.dialog.defense_counsel_type_box.setCurrentText("Private Counsel")


class CmsChargeLoader(CmsNoChargeLoader):
    """Class for Loading CMS data when the charges in a case need to be loaded for the dialog.
    This is for dialogs with a Charge Grid, but no FRA (insurance) information."""
    def __init__(self, dialog: QDialog) -> None:
        self.criminal_charge = None
        super().__init__(dialog)

    def load_cms_data(self):
        """Calls the CmsNoChargeLoader load_cms_data method to load all case information, then
        loads the charge information for the case."""
        super().load_cms_data()
        self.add_cms_criminal_charges_to_entry_case_information()

    def add_cms_criminal_charges_to_entry_case_information(self):
        """Loads the data from the cms_case object that is created from the sql
        table."""
        for charge in self.cms_case.charges_list:
            self.criminal_charge = CriminalCharge()
            (
                self.criminal_charge.offense,
                self.criminal_charge.statute,
                self.criminal_charge.degree,
                self.criminal_charge.type,
            ) = charge
            self.criminal_charge.type = self.set_offense_type()
            self.dialog.entry_case_information.add_charge_to_list(self.criminal_charge)
            self.dialog.add_charge_to_grid()
            self.dialog.setFocus()

    def set_offense_type(self):
        """This sets the charge type to Moving if CMS provides "No Data" the rationale
        that if the user uses the show costs and fines it would provide the highest
        possible costs if there is no data. Then defendant will get actual costs that
        could actually be less when they go to clerk's office."""
        if self.cms_case.case_number[2:5] == "CRB":
            return "Criminal"
        if self.criminal_charge.type == "False":
            return "Non-moving"
        if self.criminal_charge.type == "True":
            return "Moving"
        return "Moving"


class CmsFraLoader(CmsChargeLoader):
    """This subclass is used for the Fine Only Plea and Jail CC Plea Dialogs to load the
    FRA (insurance) data for the case."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.load_fra_data()
        self.hide_fra_if_criminal_case()

    def load_fra_data(self):
        fra_value_dict = {"Y": "Yes", "N": "No", "U": "N/A"}
        if self.cms_case.case_number is None:
            self.dialog.fra_in_file_box.setCurrentText("N/A")
        elif self.cms_case.fra_in_file in fra_value_dict:
            self.dialog.fra_in_file_box.setCurrentText(fra_value_dict[self.cms_case.fra_in_file])
        else:
            self.dialog.fra_in_file_box.setCurrentText("N/A")

    def hide_fra_if_criminal_case(self):
        if self.cms_case.case_number == None:
            return None
        elif self.cms_case.case_number[2:5] == "CRB":
            self.dialog.fra_frame.setHidden(True)
