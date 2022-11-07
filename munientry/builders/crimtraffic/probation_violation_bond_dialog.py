"""Builder module for the Probation Violation Bond Dialog."""
from loguru import logger

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.bond_checkers import ProbationViolationBondDialogInfoChecker
from munientry.loaders.cms_case_loaders import CmsNoChargeLoader
from munientry.models.case_information.plea_entries import (
    CommunityControlViolationEntryCaseInformation,
)
from munientry.models.conditions_models import CommunityControlViolationBondConditions
from munientry.updaters.no_grid_case_updaters import ProbationViolationBondDialogUpdater
from munientry.views.probation_violation_bond_dialog_ui import (
    Ui_ProbationViolationBondDialog,
)


class ProbationViolationBondDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Probation Violation Bond Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()


class ProbationViolationBondDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Probation Violation Bond Dialog."""

    def hide_bond_conditions(self):
        if self.dialog.bond_type_box.currentText() == 'No Bond':
            self.dialog.bond_conditions_frame.setHidden(True)
        else:
            self.dialog.bond_conditions_frame.setHidden(False)

    def set_if_no_bond(self):
        if self.dialog.bond_type_box.currentText() == 'No Bond':
            self.dialog.bond_amount_box.setCurrentText('None')


class ProbationViolationBondDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal connector for Probation Violation Bond Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.dialog.bond_type_box.currentTextChanged.connect(
            self.dialog.functions.hide_bond_conditions,
        )
        self.dialog.bond_type_box.currentTextChanged.connect(self.dialog.functions.set_if_no_bond)


class ProbationViolationBondDialog(crim.CrimTrafficDialogBuilder, Ui_ProbationViolationBondDialog):
    """Dialog builder class for 'Prelim. Probation Violation / Bond' Entry."""

    build_dict = {
        'dialog_name': 'Probation Violation Bond Dialog',
        'view': ProbationViolationBondDialogViewModifier,
        'slots': ProbationViolationBondDialogSlotFunctions,
        'signals': ProbationViolationBondDialogSignalConnector,
        'case_information_model': CommunityControlViolationEntryCaseInformation,
        'loader': CmsNoChargeLoader,
        'updater': ProbationViolationBondDialogUpdater,
        'info_checker': ProbationViolationBondDialogInfoChecker,
    }

    def additional_setup(self):
        self.entry_case_information.bond_conditions = CommunityControlViolationBondConditions()


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
