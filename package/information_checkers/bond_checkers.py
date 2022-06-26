"""Module that contains data checks that are ran when a user creates an entry."""
from loguru import logger
from PyQt5.QtWidgets import QDialog

from package.information_checkers.base_checks import BondInfoChecker


class NoPleaBondDialogInfoChecker(BondInfoChecker):
    """Class with checks for the No Plea Bond Dialog."""

    conditions_list = [
        ('admin_license_suspension', 'disposition', 'Admin License Suspension'),
        ('vehicle_seizure', 'vehicle_make_model', 'Vehicle Seizure'),
        ('no_contact', 'name', 'No Contact'),
        ('custodial_supervision', 'supervisor', 'Custodial Supervision'),
        ('other_conditions', 'terms', 'Other Conditions'),
    ]

    def __init__(self, dialog: QDialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
            'check_defense_counsel',
            'check_if_no_bond_amount',
            'check_if_improper_bond_type',
            'check_additional_conditions_ordered',
            'check_domestic_violence_bond_condition',
        ]
        self.check_status = self.perform_check_list()


class BondHearingDialogInfoChecker(BondInfoChecker):
    """Class with checks for the Bond Hearing Dialog."""

    conditions_list = [
        ('admin_license_suspension', 'disposition', 'Admin License Suspension'),
        ('vehicle_seizure', 'vehicle_make_model', 'Vehicle Seizure'),
        ('no_contact', 'name', 'No Contact'),
        ('custodial_supervision', 'supervisor', 'Custodial Supervision'),
        ('other_conditions', 'terms', 'Other Conditions'),
    ]

    def __init__(self, dialog: QDialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
            'check_defense_counsel',
            'check_if_no_bond_modification_decision',
            'check_if_no_bond_amount',
            'check_if_improper_bond_type',
            'check_additional_conditions_ordered',
            'check_domestic_violence_bond_condition',
        ]
        self.check_status = self.perform_check_list()


class ProbationViolationBondDialogInfoChecker(BondInfoChecker):
    """Class with checks for the Probation Violation Bond Dialog."""

    def __init__(self, dialog: QDialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
            'check_defense_counsel',
            'check_if_no_bond_amount',
            'check_if_improper_bond_type',
        ]
        self.check_status = self.perform_check_list()


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
