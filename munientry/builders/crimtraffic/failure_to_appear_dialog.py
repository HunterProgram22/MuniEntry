"""Builder module for the Failure To Appear Dialog."""
import munientry.builders.base_dialogs
from loguru import logger

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.base_checks import FailureToAppearDialogInfoChecker
from munientry.data.cms_case_loaders import CmsNoChargeLoader
from munientry.models.case_information.plea_entries import (
    FailureToAppearEntryCaseInformation,
)
from munientry.models.conditions_models import FailureToAppearConditions
from munientry.updaters.no_grid_case_updaters import FailureToAppearDialogUpdater
from munientry.views.failure_to_appear_dialog_ui import Ui_FailureToAppearDialog


class FailureToAppearDialogViewModifier(crim.BaseDialogViewModifier):
    """View builder for Failure To Appear Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()


class FailureToAppearDialogSlotFunctions(crim.BaseDialogSlotFunctions):
    """Additional functions for Failure To Appear Dialog."""

    def hide_warrant_radius(self):
        if self.dialog.arrest_warrant_checkBox.isChecked():
            self.dialog.arrest_warrant_radius_label.setHidden(False)
            self.dialog.arrest_warrant_radius_box.setHidden(False)
        else:
            self.dialog.arrest_warrant_radius_label.setHidden(True)
            self.dialog.arrest_warrant_radius_box.setHidden(True)

    def hide_bond_boxes(self):
        if self.dialog.set_bond_checkBox.isChecked():
            self.dialog.bond_type_box.setHidden(False)
            self.dialog.bond_amount_box.setHidden(False)
            self.dialog.bond_type_label.setHidden(False)
            self.dialog.bond_amount_label.setHidden(False)
        else:
            self.dialog.bond_type_box.setHidden(True)
            self.dialog.bond_amount_box.setHidden(True)
            self.dialog.bond_type_label.setHidden(True)
            self.dialog.bond_amount_label.setHidden(True)

    def set_bond_amount_box(self):
        if self.dialog.bond_type_box.currentText() == 'No Bond':
            self.dialog.bond_amount_box.setHidden(True)
            self.dialog.bond_amount_label.setHidden(True)
        elif self.dialog.bond_type_box.currentText() == 'Recognizance (OR) Bond':
            self.dialog.bond_amount_box.setHidden(True)
            self.dialog.bond_amount_label.setHidden(True)
        else:
            self.dialog.bond_amount_box.setHidden(False)
            self.dialog.bond_amount_label.setHidden(False)


class FailureToAppearDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Failure To Appear Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.dialog.arrest_warrant_checkBox.toggled.connect(
            self.dialog.functions.hide_warrant_radius,
        )
        self.dialog.set_bond_checkBox.toggled.connect(self.dialog.functions.hide_bond_boxes)
        self.dialog.bond_type_box.currentTextChanged.connect(
            self.dialog.functions.set_bond_amount_box,
        )


class FailureToAppearDialog(crim.CriminalDialogBuilder, Ui_FailureToAppearDialog):
    """Dialog builder class for 'Failure To Appear / Issue Warrant' Entry."""

    build_dict = {
        'dialog_name': 'Failure To Appear Dialog',
        'view': FailureToAppearDialogViewModifier,
        'slots': FailureToAppearDialogSlotFunctions,
        'signals': FailureToAppearDialogSignalConnector,
        'case_information_model': FailureToAppearEntryCaseInformation,
        'loader': CmsNoChargeLoader,
        'updater': FailureToAppearDialogUpdater,
        'info_checker': FailureToAppearDialogInfoChecker,
    }

    def additional_setup(self):
        self.entry_case_information.fta_conditions = FailureToAppearConditions()
        self.functions.hide_warrant_radius()
        self.functions.hide_bond_boxes()


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
