from __future__ import annotations

from loguru import logger
from munientry.builders.base_dialogs import BaseDialogBuilder
from munientry.models.template_types import TEMPLATE_DICT


class SchedulingBaseDialog(BaseDialogBuilder):
    """The base class for all scheduling entries."""

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
