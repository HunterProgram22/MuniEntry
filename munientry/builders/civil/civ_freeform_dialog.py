"""Builder module for the Civil Freeform Entry Dialog."""
from loguru import logger

from munientry.builders import base_builders as base
from munientry.loaders.cms_case_loaders import CivCmsLoader
from munientry.models.case_information.civil_case_information import CivFreeformEntryCaseInformation
from munientry.updaters.civil_updaters import CivFreeformDialogUpdater
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

    _case_information_model = CivFreeformEntryCaseInformation
    _case_loader = CivCmsLoader
    _model_updater = CivFreeformDialogUpdater
    _signal_connector = CivFreeformDialogSignalConnector
    _slots = CivFreeformDialogSlotFunctions
    _view_modifier = CivFreeformDialogViewModifier
    dialog_name = 'Civil Freeform Entry Dialog'

    def __init__(self, judicial_officer, cms_case=None, parent=None) -> None:
        super().__init__(parent)
        # self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        loaded_case = cms_case.case_number
        logger.info(f'Loaded Case {loaded_case}')
        self.load_entry_case_information_model()
        self.entry_case_information.judicial_officer = self.judicial_officer
        self.load_cms_data_to_view()
        try:
            self.defense_counsel_name_box.load_attorneys()
        except AttributeError as error:
            logger.warning(error)
        # self.popup_dialog = None
        self.additional_setup()

    def additional_setup(self):
        """Abstract base method used in subclasses for additional setup after init."""



if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
