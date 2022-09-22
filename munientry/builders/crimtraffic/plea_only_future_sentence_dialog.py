"""Builder module for the Plea Only - Future Sentencing Dialog."""
from loguru import logger

from munientry.builders.base_dialogs import (
    BaseDialogSlotFunctions,
    BaseDialogViewModifier,
    CriminalDialogBuilder,
)
from munientry.checkers.plea_only_checkers import PleaOnlyDialogInfoChecker
from munientry.controllers import charges_grids as cg
from munientry.controllers.signal_connectors import BaseDialogSignalConnector
from munientry.data.cms_case_loaders import CmsChargeLoader
from munientry.models.case_information.plea_entries import PleaOnlyEntryCaseInformation
from munientry.updaters.grid_case_updaters import PleaOnlyDialogUpdater
from munientry.views.plea_only_dialog_ui import Ui_PleaOnlyDialog


class PleaOnlyDialogViewModifier(BaseDialogViewModifier):
    """View builder for Plea Only - Future Sentence Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.charges_gridLayout.__class__ = cg.PleaOnlyGrid
        self.set_appearance_reason()


class PleaOnlyDialogSignalConnector(BaseDialogSignalConnector):
    """Signal Connector for Plea Only - Future Sentence Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_plea_all_button_signals(dialog)


class PleaOnlyDialogSlotFunctions(BaseDialogSlotFunctions):
    """Additional functions for Plea Only - Future Sentence Dialog."""


class PleaOnlyDialog(CriminalDialogBuilder, Ui_PleaOnlyDialog):
    """Dialog builder class for 'Plea Only - Future Sentencing' dialog."""

    build_dict = {
        'dialog_name': 'Plea Only Dialog',
        'view': PleaOnlyDialogViewModifier,
        'slots': PleaOnlyDialogSlotFunctions,
        'signals': PleaOnlyDialogSignalConnector,
        'case_information_model': PleaOnlyEntryCaseInformation,
        'loader': CmsChargeLoader,
        'updater': PleaOnlyDialogUpdater,
        'info_checker': PleaOnlyDialogInfoChecker,
    }


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
