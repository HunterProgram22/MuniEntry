"""Common base classes for Scheduling Dialogs."""
from loguru import logger

from munientry.builders import base_builders as base
from munientry.creators.entry_creator import SchedulingEntryCreator
from munientry.models.template_types import TEMPLATE_DICT


class SchedulingDialogBuilder(base.BaseDialogBuilder):
    """The base class for all Scheduling Dialogs."""

    def __init__(self, judicial_officer=None, cms_case=None, case_table=None, parent=None):
        self.case_table = case_table
        super().__init__(parent)
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        self.load_entry_case_information_model()
        self.load_cms_data_to_view()
        case_number = cms_case.case_number
        logger.info(f'Loading {case_number} from {self.case_table}')
        self.additional_setup()

    def additional_setup(self):
        """Abstract base method used in subclasses for additional setup after init."""


class SchedulingViewModifier(base.BaseDialogViewModifier):
    """Base View Builder for Scheduling Dialogs."""


class SchedulingSignalConnector(base.BaseDialogSignalConnector):
    """Base Signal Connector for Scheduling Dialogs."""


class SchedulingSlotFunctions(base.BaseDialogSlotFunctions):
    """Additional functions for Scheduling Dialogs."""

    def create_entry_process(self) -> None:
        SchedulingEntryCreator(self.dialog)
