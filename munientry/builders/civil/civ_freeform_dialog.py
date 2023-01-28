"""Builder module for the Civil Freeform Entry Dialog."""
from loguru import logger

from munientry.builders import base_builders as base
# from munientry.checkers.base_checks import FreeformDialogInfoChecker
# from munientry.loaders.cms_case_loaders import CmsNoChargeLoader
# from munientry.models.case_information.plea_entries import FreeformEntryCaseInformation
# from munientry.updaters.no_grid_case_updaters import FreeformDialogUpdater
from munientry.views.civ_freeform_dialog_ui import Ui_CivFreeformDialog


class CivFreeformDialogViewModifier(base.BaseDialogViewModifier):
    """View builder for Civil Freeform Entry Dialog."""


class CivFreeformDialogSlotFunctions(base.BaseDialogSlotFunctions):
    """Additional functions for Civil Freeform Entry Dialog."""

    def clear_case_information_fields(self):
        """Overrides base method because different label names used.

        TODO: Refactor base method to criminal base.
        """
        self.dialog.plaintiff_lineEdit.clear()
        self.dialog.defendant_lineEdit.clear()
        self.dialog.case_number_lineEdit.clear()
        self.dialog.plaintiff_lineEdit.setFocus()


class CivFreeformDialogSignalConnector(base.BaseDialogSignalConnector):
    """Signal Connector for Civil Freeform Entry Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()


class CivFreeformDialog(base.BaseDialogBuilder, Ui_CivFreeformDialog):
    """Dialog builder class for Civil Freeform Entry."""

    # _case_information_model = FreeformEntryCaseInformation
    # _case_loader = CmsNoChargeLoader
    # _info_checker = FreeformDialogInfoChecker
    # _model_updater = FreeformDialogUpdater
    _signal_connector = CivFreeformDialogSignalConnector
    _slots = CivFreeformDialogSlotFunctions
    _view_modifier = CivFreeformDialogViewModifier
    dialog_name = 'Civil Freeform Entry Dialog'


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
