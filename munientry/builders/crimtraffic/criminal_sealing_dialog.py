"""Builder module for the Criminal Sealing Entry Dialog."""
from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.base_checks import DefenseCounselChecks
from munientry.loaders.cms_case_loaders import CrimSealingLoader
from munientry.models.case_information.criminal_case_information import CrimSealingModel
from munientry.updaters.no_grid_case_updaters import CriminalSealingDialogUpdater
from munientry.views.criminal_sealing_dialog_ui import Ui_CriminalSealingEntryDialog


class CriminalSealingDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Criminal Sealing Entry Dialog."""


class CriminalSealingDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Criminal Sealing Entry Dialog."""

    def toggle_denial_reasons_box(self):
        if self.dialog.seal_decision_box.currentText() == 'Denied - with reason':
            self.dialog.denial_reasons_text_box.show()
            self.dialog.denial_reasons_label.show()
        else:
            self.dialog.denial_reasons_text_box.hide()
            self.dialog.denial_reasons_label.hide()


class CriminalSealingDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Criminal Sealing Entry Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_toggle_fields()

    def connect_toggle_fields(self):
        self.dialog.seal_decision_box.currentTextChanged.connect(
            self.dialog.functions.toggle_denial_reasons_box
        )


class CriminalSealingDialogInfoChecker(DefenseCounselChecks):
    """Class with all checks for Criminal Sealing Entry Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.check_list = [
            'check_defense_counsel',
        ]
        self.check_status = self.perform_check_list()


class CriminalSealingDialog(crim.CrimTrafficDialogBuilder, Ui_CriminalSealingEntryDialog):
    """Dialog builder class for Criminal Sealing Entry."""
    _case_information_model = CrimSealingModel
    _case_loader = CrimSealingLoader
    _info_checker = CriminalSealingDialogInfoChecker
    _model_updater = CriminalSealingDialogUpdater
    _signal_connector = CriminalSealingDialogSignalConnector
    _slots = CriminalSealingDialogSlotFunctions
    _view_modifier = CriminalSealingDialogViewModifier
    dialog_name = 'Criminal Sealing Entry'

    def additional_setup(self):
        self.functions.toggle_denial_reasons_box()
        self.bci_number_line_edit.setFocus()
