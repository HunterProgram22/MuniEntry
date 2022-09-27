from __future__ import annotations

from loguru import logger
from munientry.builders.base_dialogs import BaseDialog
from munientry.models.scheduling_information import SchedulingCaseInformation


class SchedulingBaseDialog(BaseDialog):
    """The base class for all scheduling entries."""

    def __init__(self, judicial_officer=None, cms_case=None, case_table=None, parent=None):
        super().__init__(parent)
        self.case_table = case_table
        self.judicial_officer = judicial_officer
        self.entry_case_information = SchedulingCaseInformation()
        self.cms_case = cms_case
        case_number = cms_case.case_number
        logger.info(f'Loading {case_number} from {self.case_table}')
        self.load_cms_data_to_view()