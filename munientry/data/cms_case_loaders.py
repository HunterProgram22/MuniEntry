"""Module for loading the CMS case data into the main_entry_dialog view."""
from __future__ import annotations

from loguru import logger

from munientry.models.criminal_charge_models import CriminalCharge
from munientry.settings import TYPE_CHECKING

if TYPE_CHECKING:
    from PyQt5.QtWidgets import QDialog


class CmsNoChargeLoader(object):
    """Class for Loading CMS data when the charges do not need to be loaded.

    This is for dialogs with no ChargeGrid.
    """

    def __init__(self, dialog: QDialog) -> None:
        self.dialog = dialog
        self.cms_case = dialog.cms_case
        if self.cms_case.case_number is not None:
            self.load_cms_data()

    def load_cms_data(self) -> None:
        """Loads the case management system data to the dialog."""
        self.set_case_number()
        self.set_defendant_name()
        try:
            self.set_defense_counsel_name()
        except AttributeError as err:
            logger.warning(err)
        try:
            self.set_defense_counsel_type()
        except AttributeError as error:
            logger.warning(error)

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
        """Sets the type for defense counsel to public defender or private counsel.

        Data from CMS will indicate PD if the attorney is a public defender. If there is no
        attorney then the field is set to Public Defender. If there is an attorney, and CMS does
        not indicate it PD, then it is set to Private Counsel.
        """
        if self.cms_case.defense_counsel_type == '1':
            self.dialog.defense_counsel_type_box.setCurrentText('Public Defender')
        elif self.cms_case.defense_counsel.strip() == '':
            self.dialog.defense_counsel_type_box.setCurrentText('Public Defender')
        else:
            self.dialog.defense_counsel_type_box.setCurrentText('Private Counsel')


class CmsDrivingInfoLoader(CmsNoChargeLoader):
    """Loader for CMS data for Driving Privileges."""

    def __init__(self, dialog: QDialog) -> None:
        super().__init__(dialog)

    def load_cms_data(self) -> None:
        self.set_case_number()
        self.set_defendant_name()
        try:
            self.set_defendant_driving_info()
        except AttributeError as error:
            logger.warning(error)

    def set_defendant_driving_info(self):
        self.dialog.defendant_address_lineEdit.setText(self.cms_case.defendant.address)
        self.dialog.defendant_city_lineEdit.setText(self.cms_case.defendant.city)
        self.dialog.defendant_state_lineEdit.setText(self.cms_case.defendant.state)
        self.dialog.defendant_zipcode_lineEdit.setText(self.cms_case.defendant.zipcode)
        self.dialog.defendant_driver_license_lineEdit.setText(self.cms_case.defendant.license_number)
        self.dialog.defendant_dob_lineEdit.setText(self.cms_case.defendant.birth_date)


class CmsChargeLoader(CmsNoChargeLoader):
    """Class for Loading CMS data when the charges in a case need to be loaded for the dialog.

    This is for dialogs with a Charge Grid, but no FRA (insurance) information.
    """

    def __init__(self, dialog: QDialog) -> None:
        self.criminal_charge = None
        super().__init__(dialog)

    def load_cms_data(self):
        super().load_cms_data()
        self.add_cms_charges_to_entry_case_information()

    def add_cms_charges_to_entry_case_information(self):
        """Loads charges from the sql database objec (self.cms_case) into the data model.

        The charge from self.cms_case.charges_list is a tuple in the format:
        (Offense, Statute, Degree, Offense Type [Moving/Non-Moving/Criminal]).
        """
        for charge in self.cms_case.charges_list:
            self.criminal_charge = CriminalCharge()
            self.criminal_charge.offense = charge[0]
            self.criminal_charge.statute = charge[1]
            self.criminal_charge.degree = charge[2]
            self.criminal_charge.type = self.set_offense_type(charge[3])
            self.dialog.entry_case_information.add_charge_to_list(self.criminal_charge)
            self.dialog.add_charge_to_grid()
            self.dialog.setFocus()

    def set_offense_type(self, cms_type):
        """Sets the offense type for each charge to either Moving, Non-moving, or Criminal.

        The offense type is used in calculating court costs.

        In a criminal case the charge is always criminal. If there is 'No Data' provided by the
        case management system, then it is set to 'Moving.'

        The rationale that if the user uses the show costs and fines it would provide the highest
        possible costs if there is no data. Then defendant will get actual costs that
        could actually be less when they go to clerk's office.
        """
        if self.cms_case.case_number[2:5] == 'CRB':
            return 'Criminal'
        if cms_type == '0':
            return 'Non-moving'
        if cms_type == '1':
            return 'Moving'
        return 'Moving'


class CmsFraLoader(CmsChargeLoader):
    """Loader for sentencing dialogs when there is FRA (insurance) data for the case."""

    fra_value = {'Y': 'Yes', 'N': 'No', 'U': 'N/A'}

    def __init__(self, dialog: QDialog) -> None:
        super().__init__(dialog)
        self.load_fra_data()
        self.hide_fra_if_criminal_case()

    def load_fra_data(self) -> None:
        if self.cms_case.case_number is None:
            self.dialog.fra_in_file_box.setCurrentText('N/A')
        elif self.cms_case.fra_in_file in self.fra_value:
            self.dialog.fra_in_file_box.setCurrentText(
                self.fra_value.get(self.cms_case.fra_in_file),
            )
        else:
            self.dialog.fra_in_file_box.setCurrentText('N/A')

    def hide_fra_if_criminal_case(self) -> None:
        """The Insurance (FRA) data is not used in criminal cases so it is hidden."""
        if self.cms_case.case_number is None:
            return self.dialog.fra_frame.setHidden(False)
        if 'TRC' in self.cms_case.case_number:
            return self.dialog.fra_frame.setHidden(False)
        if 'TRD' in self.cms_case.case_number:
            return self.dialog.fra_frame.setHidden(False)
        if self.cms_case.case_number[2:5] == 'CRB':
            return self.dialog.fra_frame.setHidden(True)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
