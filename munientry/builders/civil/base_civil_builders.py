"""Base Classes for Civil Entries."""
from loguru import logger

from munientry.builders import base_builders as base
from munientry.models.template_types import TEMPLATE_DICT
from munientry.widgets.message_boxes import InfoBox


class CivilDialogBuilder(base.BaseDialogBuilder):

    def __init__(self, judicial_officer, cms_case=None, parent=None) -> None:
        super().__init__(parent)
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        loaded_case = cms_case.case_number
        logger.info(f'Loaded Case {loaded_case}')
        self.load_entry_case_information_model()
        self.entry_case_information.judicial_officer = self.judicial_officer
        self.load_cms_data_to_view()
        self.popup_dialog = None
        self.additional_setup()

    def additional_setup(self):
        """Abstract base method used in subclasses for additional setup after init."""


class CivilViewModifier(base.BaseDialogViewModifier):
    """Base Civil View Modifier."""


class CivilSlotFunctions(base.BaseDialogSlotFunctions):

    def clear_case_information_fields(self):
        """Overrides base method because different label names used.

        TODO: Refactor base method to criminal base.
        """
        self.dialog.plaintiff_lineEdit.clear()
        self.dialog.defendant_lineEdit.clear()
        self.dialog.case_number_lineEdit.clear()
        self.dialog.plaintiff_lineEdit.setFocus()


class CivilSignalConnector(base.BaseDialogSignalConnector):

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
