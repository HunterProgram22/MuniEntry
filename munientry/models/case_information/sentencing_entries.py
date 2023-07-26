"""Contains all dataclasses for entries that include FRA and Court Costs."""
import calendar
from loguru import logger
from dataclasses import dataclass, field

from munientry.checkers.base_checks import warning_check, min_charge_check
from munientry.checkers import check_messages as check_msg
from munientry.models import conditions_models as cm
from munientry.models.case_information.criminal_case_information import (
    CriminalCaseInformation,
)


@dataclass
class CriminalSentencingCaseInformation(CriminalCaseInformation):
    """Case information for insurance and court costs that is included in sentencing entries."""

    fra_in_file: bool = None
    fra_in_court: bool = None
    court_costs: object = field(default_factory=cm.CourtCosts)


@dataclass
class DiversionEntryCaseInformation(CriminalSentencingCaseInformation):
    """General case information data variables for diversion entry."""

    diversion: object = field(default_factory=cm.Diversion)
    other_conditions: object = field(default_factory=cm.OtherConditions)


@dataclass
class FineOnlyEntryCaseInformation(CriminalSentencingCaseInformation):
    """General case information data variables for fine only entry."""

    fines_and_costs_jail_credit: bool = False
    fine_jail_days: str = None
    total_fines: int = 0
    total_fines_suspended: int = 0
    community_service: object = field(default_factory=cm.CommunityService)
    license_suspension: object = field(default_factory=cm.LicenseSuspension)
    other_conditions: object = field(default_factory=cm.OtherConditions)


@dataclass
class LeapSentencingEntryCaseInformation(FineOnlyEntryCaseInformation):
    """General case information data variables and data for LEAP sentencing."""

    leap_plea_date: str = None


@dataclass
class JailCCEntryCaseInformation(FineOnlyEntryCaseInformation):
    """General case information data variables and data for jail and comm. control entry."""

    victim_statements: bool = False
    sentencing_date: str = None
    community_control: object = field(default_factory=cm.CommunityControl)
    jail_terms: object = field(default_factory=cm.JailTerms)
    victim_notification: object = field(default_factory=cm.VictimNotification)
    impoundment: object = field(default_factory=cm.Impoundment)

    @min_charge_check(check_msg.OVI_ONE_TITLE, check_msg.OVI_ONE_MSG)
    def ovi_one_mins(self, msg_response: int = None) -> bool:
        """Checks if the offense is a 1st OVI and Guilty and asks user if they want to set mins.

        Message box has three options - Yes set mins and dismiss other charges returns 0;
        Yes set mins and do not disimss other charges returns 1; and No returns 2.
        """
        if msg_response is None:
            violation_date = self.get_violation_date()
            return False, [violation_date]
        elif msg_response == 0:
            self.set_ovi_one_mins()
        elif msg_response == 1:
            self.set_ovi_one_mins()
        return True, msg_response

    def set_ovi_one_mins(self) -> None:
        self.community_control.type_of_control = 'basic'
        self.community_control.term_of_control = 'One Year'
        self.community_control.driver_intervention_program = True
        self.license_suspension.license_type = 'driving'
        self.license_suspension.suspended_date = self.get_violation_date()
        self.license_suspension.suspension_term = '12 months'
        self.license_suspension.als_terminated = True
        self.victim_notification.fingerprinting_ordered = True

    def get_violation_date(self) -> str:
        for charge in self.charges_list:
            if charge.offense == 'OVI Alcohol / Drugs 1st':
                try:
                    year = charge.violation_date[:4]
                    month_number = charge.violation_date[5:7]
                    day = charge.violation_date[8:]
                    month_name = calendar.month_name[int(month_number)]
                    date_formatted = f'{month_name} {day}, {year}'
                except TypeError as err:
                    logger.warning(err)
                    date_formatted = 'May 05, 2023'
                return date_formatted

@dataclass
class SentencingOnlyEntryCaseInformation(JailCCEntryCaseInformation):
    """General case information data variables for Sentencing Only entry."""

    plea_date: str = None


@dataclass
class TrialSentencingEntryCaseInformation(JailCCEntryCaseInformation):
    """General case information data variables and data for trial sentencing entry."""


if __name__ == "__main__":
    logger.info(f'{__name__} run directly.')
