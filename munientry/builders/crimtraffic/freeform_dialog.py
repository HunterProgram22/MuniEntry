"""Builder module for the Freeform Entry Dialog."""
from loguru import logger

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.base_checks import FreeformDialogInfoChecker
from munientry.data.cms_case_loaders import CmsNoChargeLoader
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


class FreeformDialog(crim.CrimTrafficDialogBuilder, Ui_FreeformEntryDialog):
    """Dialog builder class for 'Freeform Entry'."""

    build_dict = {
        'dialog_name': 'Freeform Entry Dialog',
        'view': FreeformDialogViewModifier,
        'slots': FreeformDialogSlotFunctions,
        'signals': FreeformDialogSignalConnector,
        'case_information_model': FreeformEntryCaseInformation,
        'loader': CmsNoChargeLoader,
        'updater': FreeformDialogUpdater,
        'info_checker': FreeformDialogInfoChecker,
    }


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
