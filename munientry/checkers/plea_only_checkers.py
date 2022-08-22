"""Module that contains information checks for plea only dialogs."""
from loguru import logger

from munientry.checkers.base_checks import BondInfoChecker, ChargeGridInfoChecker
from munientry.settings import TYPE_CHECKING

# if TYPE_CHECKING:
from PyQt5.QtWidgets import QDialog


class LeapAdmissionPleaDialogInfoChecker(ChargeGridInfoChecker):
    """Class with all checks for LEAP Admission Plea Dialog."""

    def __init__(self, dialog: QDialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
            'check_defense_counsel',
            'check_if_no_plea_entered',
        ]
        self.check_status = self.perform_check_list()


class PleaOnlyDialogInfoChecker(ChargeGridInfoChecker):
    """Class with all checks for Plea Only Dialog.

    The Plea Only Dialog includes the finding. Sentencing is set out in the future.
    """

    def __init__(self, dialog: QDialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
            'check_defense_counsel',
            'check_if_no_plea_entered',
            'check_if_no_finding_entered',
        ]
        self.check_status = self.perform_check_list()


class NotGuiltyBondDialogInfoChecker(ChargeGridInfoChecker, BondInfoChecker):
    """Class with all checks for Not Guilty Bond Dialog."""

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
            'check_if_no_plea_entered',
            'check_if_no_bond_amount',
            'check_if_improper_bond_type',
            'check_additional_conditions_ordered',
            'check_domestic_violence_bond_condition',
        ]
        self.check_status = self.perform_check_list()


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
