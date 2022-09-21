"""Builder module for the Plea Only - Future Sentencing Dialog."""
from loguru import logger

from munientry.builders.base_dialogs import CriminalDialogBuilder
from munientry.checkers.plea_only_checkers import PleaOnlyDialogInfoChecker
from munientry.controllers import charges_grids as cg
from munientry.controllers.signal_connectors import BaseDialogSignalConnector
from munientry.controllers.slot_functions import BaseDialogSlotFunctions
from munientry.controllers.view_modifiers import BaseDialogViewModifier
from munientry.data.cms_case_loaders import CmsChargeLoader
from munientry.models.case_information.plea_entries import PleaOnlyEntryCaseInformation
from munientry.updaters.grid_case_updaters import PleaOnlyDialogUpdater
from munientry.views.plea_only_dialog_ui import Ui_PleaOnlyDialog


class PleaOnlyDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.charges_gridLayout.__class__ = cg.PleaOnlyGrid
        self.set_appearance_reason()


class PleaOnlyDialogSignalConnector(BaseDialogSignalConnector):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals(dialog)
        self.connect_plea_all_button_signals(dialog)


class PleaOnlyDialogSlotFunctions(BaseDialogSlotFunctions):
    def __init__(self, dialog):
        self.dialog = dialog


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

    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.entry_case_information.judicial_officer = self.judicial_officer


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
