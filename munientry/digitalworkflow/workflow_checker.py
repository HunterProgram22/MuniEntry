"""Module for checking entries and moving into workflow."""
import win32com.client
from loguru import logger
from munientry.settings import DW_MATTOX

SCRAM_PATH = f'{DW_MATTOX}/Scram_Gps//'
COMM_CONTROL_PATH = f'{DW_MATTOX}/Comm_Control//'


class WorkflowCheck(object):

    scram_gps_entries = [
        'NotGuiltyBondEntryCaseInformation',
        'NoPleaBondEntryCaseInformation',
        'BondHearingEntryCaseInformation'
    ]

    comm_control_entries = [
        'JailCCEntryCaseInformation',
        'SentencingOnlyEntryCaseInformation',
        'TrialSentencingEntryCaseInformation',
    ]

    def __init__(self, case_information):
        self.case_information = case_information
        # self.saved_entry = saved_entry
        # logger.debug(self.saved_entry)
        # self.docname = docname
        # self.check_for_probation_workflow()

    def check_for_probation_workflow(self) -> (bool, str):
        if self.case_information.__class__.__name__ in self.scram_gps_entries:
            if self.case_information.bond_conditions.monitoring is True:
                return (True, SCRAM_PATH)
                # self.move_to_probation_workflow(SCRAM_PATH)
        if self.case_information.__class__.__name__ in self.comm_control_entries:
            if self.case_information.community_control.ordered is True:
                return (True, COMM_CONTROL_PATH)
                # self.move_to_probation_workflow(COMM_CONTROL_PATH)

    def move_to_probation_workflow(self, path):
        """The conversion from Word to PDF is done using win32com.

        The enum for wdFormatPDF for FileFormat is 17 to convert to PDF.

        https://learn.microsoft.com/en-us/office/vba/api/word.wdsaveformat?source=recommendations

        TODO: There is an issue of a document locking because the Word Doc is not closed.
        TODO: NOT PRODUCTION READY!
        """
        no_type_docname = self.docname[:-5]
        pdf_docname = f'{path}{no_type_docname}.pdf'
        self.word_app = win32com.client.Dispatch('Word.Application')
        self.word_doc = self.word_app.Documents.Open(self.saved_entry)
        self.word_doc.SaveAs(pdf_docname, FileFormat=17)
        logger.info(f'Moved {no_type_docname} to workflow')
