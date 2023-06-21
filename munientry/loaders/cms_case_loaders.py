"""Module for loading the CMS case data into the main_entry_dialog view."""
from typing import TYPE_CHECKING

from loguru import logger

from munientry.models.criminal_charge_models import CriminalCharge

if TYPE_CHECKING:
    from munientry.builders.base_builders import BaseDialogBuilder


class BaseCmsLoader(object):
    """Base Case Management System Loader from which all others inherit."""

    def __init__(self, dialog: 'BaseDialogBuilder') -> None:
        self.dialog = dialog
        self.cms_case = dialog.cms_case
        if self.cms_case.case_number is not None:
            self.load_cms_data()

    def set_case_number(self) -> None:
        self.dialog.case_number_lineEdit.setText(self.cms_case.case_number)

    def load_cms_data(self) -> None:
        self.set_case_number()


class CivCmsLoader(BaseCmsLoader):
    """Base loader class for civil cases."""

    def set_plaintiff_name(self) -> None:
        self.dialog.plaintiff_lineEdit.setText(self.cms_case.primary_plaintiff.party_name)

    def set_defendant_name(self) -> None:
        self.dialog.defendant_lineEdit.setText(self.cms_case.primary_defendant.party_name)

    def load_cms_data(self) -> None:
        super().load_cms_data()
        self.set_plaintiff_name()
        self.set_defendant_name()


class CrimCmsLoader(BaseCmsLoader):
    """Base loader class for loading data from an external case management system."""

    def set_defendant_name(self) -> None:
        self.dialog.defendant_first_name_lineEdit.setText(self.cms_case.defendant.first_name)
        self.dialog.defendant_last_name_lineEdit.setText(self.cms_case.defendant.last_name)

    def set_defense_counsel_name(self) -> None:
        if self.cms_case.defense_counsel is not None:
            self.dialog.defense_counsel_name_box.addItem(self.cms_case.defense_counsel)
            self.dialog.defense_counsel_name_box.setCurrentText(self.cms_case.defense_counsel)

    def set_defense_counsel_type(self) -> None:
        """Sets the type for defense counsel to public defender or private counsel.

        If the case has a public defender, set the defense counsel type to 'Public Defender'. If
        the case has a private attorney or no attorney, set the defense counsel type to
        'Private Counsel'.
        """
        if self.cms_case.defense_counsel is not None and (
            self.cms_case.defense_counsel_type == 1 or not self.cms_case.defense_counsel.strip()
        ):
            defense_counsel_type = 'Public Defender'
        else:
            defense_counsel_type = 'Private Counsel'
        self.dialog.defense_counsel_type_box.setCurrentText(defense_counsel_type)

    def load_cms_data(self) -> None:
        super().load_cms_data()
        self.set_defendant_name()


class SchedulingCrimCmsLoader(CrimCmsLoader):
    """Loader for Scheduling dialogs."""

    def load_cms_data(self) -> None:
        super().load_cms_data()
        self.set_defense_counsel_name()


class ProbationCrimCmsLoader(CrimCmsLoader):
    """Loader for Probation dialogs."""


class CrimCmsNoChargeLoader(CrimCmsLoader):
    """Class for Loading CMS data when the charges do not need to be loaded.

    This is for dialogs with no ChargeGrid.
    """

    def load_cms_data(self) -> None:
        super().load_cms_data()
        self.set_defense_counsel_name()
        self.set_defense_counsel_type()


class CrimSealingLoader(CrimCmsNoChargeLoader):
    """Loader for the Criminal Sealing Dialog."""

    def load_cms_data(self) -> None:
        super().load_cms_data()
        self.dialog.offense_date.set_date_from_string(self.cms_case.violation_date, 'yyyy-MM-dd')
        offense_list = ', '.join(str(charge[0]) for charge in self.cms_case.charges_list)
        self.dialog.offense_line_edit.setText(offense_list)


class CmsDrivingInfoLoader(CrimCmsLoader):
    """Loader for CMS data for Driving Privileges."""

    def set_defendant_driving_info(self) -> None:
        defendant = self.cms_case.defendant
        self.dialog.defendant_address_lineEdit.setText(defendant.address)
        self.dialog.defendant_city_lineEdit.setText(defendant.city)
        self.dialog.defendant_state_lineEdit.setText(defendant.state)
        self.dialog.defendant_zipcode_lineEdit.setText(defendant.zipcode)
        self.dialog.defendant_driver_license_lineEdit.setText(defendant.license_number)
        self.dialog.defendant_dob_lineEdit.setText(defendant.birth_date)

    def load_cms_data(self) -> None:
        super().load_cms_data()
        try:
            self.set_defendant_driving_info()
        except AttributeError as error:
            logger.warning(error)


class CmsChargeLoader(CrimCmsNoChargeLoader):
    """Class for Loading CMS data when the charges in a case need to be loaded for the dialog.

    This is for dialogs with a Charge Grid, but no FRA (insurance) information.
    """

    def __init__(self, dialog: 'BaseDialogBuilder') -> None:
        self.criminal_charge: CriminalCharge = None
        super().__init__(dialog)

    def add_cms_charges_to_entry_case_information(self) -> None:
        """Loads charges from the sql database objec (self.cms_case) into the data model.

        The charge from self.cms_case.charges_list is a tuple in the format:
        (Offense, Statute, Degree, Offense Type [Moving/Non-Moving/Criminal], Violation Date).
        """
        for charge in self.cms_case.charges_list:
            self.criminal_charge = CriminalCharge()
            self.criminal_charge.offense = charge[0]
            self.criminal_charge.statute = charge[1]
            self.criminal_charge.degree = charge[2]
            self.criminal_charge.type = self.set_offense_type(charge[3])
            self.criminal_charge.violation_date = charge[4]
            self.dialog.entry_case_information.add_charge_to_list(self.criminal_charge)
            self.add_charge_to_grid()
        self.dialog.setFocus()

    def add_charge_to_grid(self) -> None:
        self.dialog.charges_gridLayout.add_fields_to_charges_grid(self.dialog)

    def set_offense_type(self, cms_type: str) -> str:
        """Sets the offense type for each charge to either Moving, Non-moving, or Criminal.

        The offense type is used in calculating court costs.

        In a criminal case the charge is always criminal. If there is 'No Data' provided by the
        case management system, then it is set to 'Moving.'

        The rationale that if the user uses the show costs and fines it would provide the highest
        possible costs if there is no data. Then defendant will get actual costs that
        could actually be less when they go to clerk's office.
        """
        case_number = self.cms_case.case_number
        if case_number and case_number[2:5] == 'CRB':
            return 'Criminal'
        if cms_type == '0':
            return 'Non-moving'
        return 'Moving'

    def load_cms_data(self) -> None:
        super().load_cms_data()
        self.add_cms_charges_to_entry_case_information()


class CmsFraLoader(CmsChargeLoader):
    """Loader for sentencing dialogs when there is FRA (insurance) data for the case."""

    fra_value = {'Y': 'Yes', 'N': 'No', 'U': 'N/A'}

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.load_fra_data()
        self.hide_fra_if_criminal_case()

    def load_fra_data(self) -> None:
        fra_value = self.fra_value.get(self.cms_case.fra_in_file, None)
        if self.cms_case.case_number is None or fra_value is None:
            self.dialog.fra_in_file_box.setCurrentText('N/A')
        else:
            self.dialog.fra_in_file_box.setCurrentText(fra_value)

    def hide_fra_if_criminal_case(self) -> None:
        """The Insurance (FRA) data is not used in criminal cases so it is hidden."""
        if self.cms_case.case_number is None:
            self.dialog.fra_frame.setHidden(False)
        else:
            is_criminal_case = self.cms_case.case_number[2:5] == 'CRB'
            self.dialog.fra_frame.setHidden(is_criminal_case)
