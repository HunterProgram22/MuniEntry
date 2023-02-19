"""Builder module for the Plea Only - Future Sentencing Dialog."""
from loguru import logger

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.plea_only_checkers import PleaOnlyDialogInfoChecker
from munientry.loaders.cms_case_loaders import CmsChargeLoader
from munientry.models.case_information.plea_entries import PleaOnlyEntryCaseInformation
from munientry.updaters.grid_case_updaters import PleaOnlyDialogUpdater
from munientry.views.plea_only_dialog_ui import Ui_PleaOnlyDialog


class PleaOnlyDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Plea Only - Future Sentence Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()


class PleaOnlyDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Plea Only - Future Sentence Dialog."""

    def show_hide_bond_amount(self):
        if self.dialog.plea_only_bond_type_box.currentText() == 'OR Bond':
            self.dialog.plea_only_bond_amount_box.setHidden(True)
            self.dialog.label_8.setHidden(True)
        elif self.dialog.plea_only_bond_type_box.currentText() == 'Continue Existing Bond':
            self.dialog.plea_only_bond_amount_box.setHidden(True)
            self.dialog.label_8.setHidden(True)
        else:
            self.dialog.plea_only_bond_amount_box.setVisible(True)
            self.dialog.label_8.setVisible(True)


class PleaOnlyDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Plea Only - Future Sentence Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_plea_all_button_signals()
        self.connect_bond_signals()

    def connect_bond_signals(self):
        self.dialog.plea_only_bond_type_box.currentTextChanged.connect(
            self.dialog.functions.show_hide_bond_amount,
        )


class PleaOnlyDialog(crim.CrimTrafficDialogBuilder, Ui_PleaOnlyDialog):
    """Dialog builder class for 'Plea Only - Future Sentencing' dialog."""

    _case_information_model = PleaOnlyEntryCaseInformation
    _case_loader = CmsChargeLoader
    _info_checker = PleaOnlyDialogInfoChecker
    _model_updater = PleaOnlyDialogUpdater
    _signal_connector = PleaOnlyDialogSignalConnector
    _slots = PleaOnlyDialogSlotFunctions
    _view_modifier = PleaOnlyDialogViewModifier
    dialog_name = 'Plea Only Dialog'


    def additional_setup(self):
        self.functions.show_hide_bond_amount()


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
