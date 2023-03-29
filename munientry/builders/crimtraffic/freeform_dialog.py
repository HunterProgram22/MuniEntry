"""Builder module for the Freeform Entry Dialog."""
from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.base_checks import DefenseCounselChecker
from munientry.loaders.cms_case_loaders import CrimCmsNoChargeLoader
from munientry.models.case_information.plea_entries import FreeformEntryCaseInformation
from munientry.updaters.no_grid_case_updaters import FreeformDialogUpdater
from munientry.views.freeform_dialog_ui import Ui_FreeformEntryDialog


class FreeformDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Freeform Entry Dialog."""


class FreeformDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Freeform Entry Dialog."""


class FreeformDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Freeform Entry Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()


class FreeformDialogInfoChecker(DefenseCounselChecker):
    """Class with all checks for Freeform Entry Dialog."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.check_list = [
            'check_defense_counsel',
        ]
        self.check_status = self.perform_check_list()


class FreeformDialog(crim.CrimTrafficDialogBuilder, Ui_FreeformEntryDialog):
    """Dialog builder class for Freeform Entry."""

    _case_information_model = FreeformEntryCaseInformation
    _case_loader = CrimCmsNoChargeLoader
    _info_checker = FreeformDialogInfoChecker
    _model_updater = FreeformDialogUpdater
    _signal_connector = FreeformDialogSignalConnector
    _slots = FreeformDialogSlotFunctions
    _view_modifier = FreeformDialogViewModifier
    dialog_name = 'Freeform Entry'
