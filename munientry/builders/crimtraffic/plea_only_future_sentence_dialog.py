"""Builder module for the Plea Only - Future Sentencing Dialog."""
from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.crim_checks import ChargeGridChecks
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
        """
        Shows or hides the plea-only bond amount box and label based on the selected bond type.

        If the bond type is 'OR Bond' or 'Continue Existing Bond', the plea-only bond amount box
        and label are hidden. Otherwise, they are shown.
        """
        bond_type = self.dialog.plea_only_bond_type_box.currentText()
        hide_boxes = bond_type in {'OR Bond', 'Continue Existing Bond'}
        self.dialog.plea_only_bond_amount_box.setHidden(hide_boxes)
        self.dialog.bond_amount_label.setHidden(hide_boxes)


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


class PleaOnlyDialogInfoChecker(ChargeGridChecks):
    """Class with all checks for Plea Only Dialog.

    The Plea Only Dialog includes the finding. Sentencing is set out in the future.
    """

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.check_list = [
            'check_defense_counsel',
            'check_if_no_plea_entered',
            'check_if_no_finding_entered',
        ]
        self.check_status = self.perform_check_list()


class PleaOnlyDialog(crim.CrimTrafficDialogBuilder, Ui_PleaOnlyDialog):
    """Dialog builder class for 'Plea Only - Future Sentencing' dialog."""

    _case_information_model = PleaOnlyEntryCaseInformation
    _case_loader = CmsChargeLoader
    _info_checker = PleaOnlyDialogInfoChecker
    _model_updater = PleaOnlyDialogUpdater
    _signal_connector = PleaOnlyDialogSignalConnector
    _slots = PleaOnlyDialogSlotFunctions
    _view_modifier = PleaOnlyDialogViewModifier
    dialog_name = 'Plea Only Entry'

    def additional_setup(self):
        self.functions.show_hide_bond_amount()
