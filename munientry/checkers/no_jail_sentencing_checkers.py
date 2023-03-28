"""Module containing information checks for plea and sentencing dialogs with no jail time."""
from loguru import logger

from munientry.checkers.base_checks import (
    FAIL,
    PASS,
    ChargeGridInfoChecker,
    InsuranceInfoChecker,
)
from munientry.widgets.message_boxes import RequiredBox


class FineOnlyDialogInfoChecker(ChargeGridInfoChecker, InsuranceInfoChecker):
    """Class with checks for the Fine Only Dialog."""

    conditions_list = [
        ('license_suspension', 'license_type', 'License Suspension'),
        ('community_service', 'hours_of_service', 'Community Service'),
        ('other_conditions', 'terms', 'Other Conditions'),
    ]

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.check_list = [
            'check_defense_counsel',
            'check_if_no_plea_entered',
            'check_if_no_finding_entered',
            'check_insurance',
            'check_additional_conditions_ordered',
        ]
        self.check_status = self.perform_check_list()


class LeapSentencingDialogInfoChecker(ChargeGridInfoChecker, InsuranceInfoChecker):
    """Class with checks for LEAP Sentencing Dialog."""

    conditions_list = [
        ('license_suspension', 'license_type', 'License Suspension'),
        ('community_service', 'hours_of_service', 'Community Service'),
        ('other_conditions', 'terms', 'Other Conditions'),
    ]

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.check_list = [
            'check_defense_counsel',
            'check_if_leap_plea_date_is_today',
            'check_if_no_plea_entered',
            'check_if_no_finding_entered',
            'check_insurance',
            'check_additional_conditions_ordered',
        ]
        self.check_status = self.perform_check_list()


class DiversionDialogInfoChecker(ChargeGridInfoChecker, InsuranceInfoChecker):
    """Class with checks for Diversion Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.check_list = [
            'check_defense_counsel',
            'check_if_no_plea_entered',
            'check_if_no_finding_entered',
            'check_if_diversion_program_selected',
            'check_insurance',
        ]
        self.check_status = self.perform_check_list()

    def check_if_diversion_program_selected(self) -> str:
        diversion_program_list = [
            'marijuana_diversion',
            'theft_diversion',
            'other_diversion',
        ]
        for program in diversion_program_list:
            if getattr(self.dialog.entry_case_information.diversion, program) is True:
                return PASS
        message = 'No Diversion Program was selected.\n\nPlease choose a Diversion Program.'
        RequiredBox(message, 'Diversion Program Required').exec()
        return FAIL
