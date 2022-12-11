"""Builder module for the Arraignment Continuance Dialog."""
from loguru import logger

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.base_checks import ArraignmentContinueDialogInfoChecker
from munientry.loaders.cms_case_loaders import CmsNoChargeLoader
from munientry.models.case_information.plea_entries import (
    ArraignmentContinueEntryCaseInformation,
)

from munientry.updaters.no_grid_case_updaters import ArraignmentContinueDialogUpdater

from munientry.views.arraignment_continue_dialog_ui import Ui_ArraignmentContinueDialog


class ArraignmentContinueDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Arraignment Continuance Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()


class ArraignmentContinueDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Arraignment Continuance Dialog."""



class ArraignmentContinueDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Arraignment Continuance Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()


class ArraignmentContinueDialog(crim.CrimTrafficDialogBuilder, Ui_ArraignmentContinueDialog):
    """Dialog builder class for Arraignment Continuance Entry."""

    _case_information_model = ArraignmentContinueEntryCaseInformation
    _case_loader = CmsNoChargeLoader
    _info_checker = ArraignmentContinueDialogInfoChecker
    _model_updater = ArraignmentContinueDialogUpdater
    _signal_connector = ArraignmentContinueDialogSignalConnector
    _slots = ArraignmentContinueDialogSlotFunctions
    _view_modifier = ArraignmentContinueDialogViewModifier
    dialog_name = 'Arraignment Continuance Dialog'

    def additional_setup(self):
        pass
        # self.entry_case_information.arraignment_continue_conditions = ArraignmentContinueConditions()


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
