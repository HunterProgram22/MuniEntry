"""Builder module for the Criminal Sealing Entry Dialog."""
from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.base_checks import CriminalSealingDialogInfoChecker
from munientry.loaders.cms_case_loaders import CrimCmsNoChargeLoader
from munientry.models.case_information.plea_entries import CriminalSealingEntryCaseInformation
from munientry.updaters.no_grid_case_updaters import CriminalSealingDialogUpdater
from munientry.views.criminal_sealing_dialog_ui import Ui_CriminalSealingEntryDialog


class CriminalSealingDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Criminal Sealing Entry Dialog."""


class CriminalSealingDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Criminal Sealing Entry Dialog."""


class CriminalSealingDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Criminal Sealing Entry Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()


class CriminalSealingDialog(crim.CrimTrafficDialogBuilder, Ui_CriminalSealingEntryDialog):
    """Dialog builder class for Criminal Sealing Entry."""
    _case_information_model = CriminalSealingEntryCaseInformation
    _case_loader = CrimCmsNoChargeLoader
    _info_checker = CriminalSealingDialogInfoChecker
    _model_updater = CriminalSealingDialogUpdater
    _signal_connector = CriminalSealingDialogSignalConnector
    _slots = CriminalSealingDialogSlotFunctions
    _view_modifier = CriminalSealingDialogViewModifier
    dialog_name = 'Criminal Sealing Entry'
