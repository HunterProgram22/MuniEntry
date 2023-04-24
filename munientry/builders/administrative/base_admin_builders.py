"""Common base classes for Admin Dialogs."""
from loguru import logger

from munientry.builders import base_builders as base


class AdminDialogBuilder(base.BaseDialogBuilder):
    """The base class for all Admin Dialogs."""

    def __init__(self, judicial_officer=None, cms_case=None, case_table=None, parent=None):
        self.case_table = case_table
        super().__init__(parent)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        self.load_entry_case_information_model()
        self.load_cms_data_to_view()
        case_number = cms_case.case_number
        logger.info(f'Loading {case_number} from {self.case_table}')
        self.additional_setup()

    def additional_setup(self):
        """Abstract base method used in subclasses for additional setup after init."""


class AdminViewModifier(base.BaseDialogViewModifier):
    """Base View Builder for Admin Dialogs."""


class AdminSignalConnector(base.BaseDialogSignalConnector):
    """Base Signal Connector for Admin Dialogs."""


class AdminSlotFunctions(base.BaseDialogSlotFunctions):
    """Additional functions for Admin Dialogs."""
