"""Module for creating entries."""
from __future__ import annotations

from os import startfile

from docxtpl import DocxTemplate
from loguru import logger

from munientry.data.scheduling_data_loader import save_scheduling_data
from munientry.digitalworkflow.workflow_checker import WorkflowCheck
from munientry.paths import DEFAULT_SAVE_PATH, CRIMTRAFFIC_SAVE_PATH, FISCAL_SAVE_PATH, \
    DRIVE_SAVE_PATH, SCHEDULING_SAVE_PATH, JURY_PAY_SAVE_PATH
from munientry.widgets.message_boxes import RequiredBox

WORD_PDF_FORMAT_NUMBER = 17


class BaseEntryCreator(object):
    """Base class for creating entries."""

    save_path = DEFAULT_SAVE_PATH

    def __init__(self, dialog):
        self.dialog = dialog

    def create_entry_process(self):
        if self.update_info_and_perform_checks() == 'Pass':
            self.case_data = self.dialog.entry_case_information.get_case_information()
            self.docname = self._set_document_name()
            self.create_entry()

    def create_entry(self) -> None:
        """Loads the proper template and creates the entry.

        Uses the default SAVE_PATH from settings.py.

        This is overridden in the create_entry method in subpackages (Administrative, CrimTraffic,
        etc.) with the specific path for saving those entry types.
        """
        doc = DocxTemplate(self.dialog.template.template_path)
        doc.render(self.case_data)
        try:
            doc.save(f'{self.save_path}{self.docname}')
        except PermissionError as error:
            logger.warning(error)
            self.dialog.message_box = RequiredBox(
                'An entry for this case is already open in Word.\n'
                + 'You must close the Word document first.',
            )
            self.dialog.message_box.exec()
        logger.info(f'Entry Created: {self.docname}')
        startfile(f'{self.save_path}{self.docname}')

    def update_info_and_perform_checks(self):
        """This method performs an update then calls to the main_entry_dialog's InfoChecker class.

        The InfoChecker check_status will return as 'Fail' if any of the checks are hard stops -
        meaning the warning message doesn't allow immediate correction.

        The dialog.update_entry_case_information is called a second time to update the model
        with any changes to information that was made by the InfoChecker checks.
        """
        self.dialog.update_entry_case_information()
        self.dialog.perform_info_checks()
        if self.dialog.dialog_checks.check_status == 'Fail':
            return 'Fail'
        self.dialog.update_entry_case_information()
        return 'Pass'

    def _set_document_name(self) -> str:
        """Returns a name for the document in the format CaseNumber_TemplateName.docx.

        Example: 21CRB1234_Crim_Traffic Judgment Entry.docx
        """
        case_number = self.dialog.entry_case_information.case_number
        template_name = self.dialog.template.template_name
        return f'{case_number}_{template_name}.docx'


class CrimTrafficEntryCreator(BaseEntryCreator):
    """Entry Creator for CrimTraffic entries.

    Contains a check to see if a workflow entry needs to be created.

    TODO: Add setting to turn off workflow.
    """

    save_path = CRIMTRAFFIC_SAVE_PATH

    def __init__(self, dialog):
        super().__init__(dialog)
        self.workflow_doc = None
        self.workflow_path = None

    def create_entry_process(self):
        if self.update_info_and_perform_checks() == 'Pass':
            self.case_data = self.dialog.entry_case_information.get_case_information()
            self.docname = self._set_document_name()
            self.create_entry()

    def create_entry(self) -> None:
        """Overrides BaseEntryCreator and Loads the proper template and creates the entry."""
        if self.dialog.workflow_status == 'ON':
            self.check_if_workflow_entry_needed()
        doc = DocxTemplate(self.dialog.template.template_path)
        doc.render(self.case_data)
        try:
            doc.save(f'{self.save_path}{self.docname}')
        except PermissionError as error:
            logger.warning(error)
            self.dialog.message_box = RequiredBox(
                'An entry for this case is already open in Word.\n'
                + 'You must close the Word document first.',
            )
            self.dialog.message_box.exec()
        logger.info(f'Entry Created: {self.docname}')
        if self.workflow_doc is not None:
            self.create_workflow_entry_process()
        startfile(f'{self.save_path}{self.docname}')

    def check_if_workflow_entry_needed(self) -> tuple(object, str):
        """Checks the case information of the Dialog.

        If the case information meets workflow dialog requirements a worklow copy of the entry
        is created.
        """
        case_information = self.dialog.entry_case_information
        if WorkflowCheck(case_information).check_for_probation_workflow()[0] is True:
            self.workflow_doc = DocxTemplate(self.dialog.template.template_path)
            self.workflow_path = WorkflowCheck(case_information).check_for_probation_workflow()[1]

    def create_workflow_entry_process(self):
        """Creates a copy of the main entry that is created.

        Labels the entry as a Draft entry and modfies case number to indicate draft entry.
        """
        local_case_data = self.case_data
        case_number = local_case_data.get('case_number')
        local_case_data['case_number'] = f'{case_number}_DRAFT_ENTRY'
        self.workflow_doc.render(local_case_data)
        self.workflow_docname = f'DRAFT_{self.docname}'
        self.workflow_doc.save(f'{self.workflow_path}{self.workflow_docname}')
        logger.info(f'Created Draft entry for {self.workflow_docname}')


class SchedulingEntryCreator(BaseEntryCreator):
    """Entry Creator for Scheduling entries."""

    save_path = SCHEDULING_SAVE_PATH

    def create_entry(self) -> None:
        """Overrides BaseEntryCreator and Loads the proper template and creates the entry.

        Saves the scheduling data to the MuniEntry_db.sqlite.
        """
        doc = DocxTemplate(self.dialog.template.template_path)
        doc.render(self.case_data)
        save_scheduling_data(self.case_data)
        try:
            doc.save(f'{self.save_path}{self.docname}')
        except PermissionError as error:
            logger.warning(error)
            self.dialog.message_box = RequiredBox(
                'An entry for this case is already open in Word.\n'
                + 'You must close the Word document first.',
            )
            self.dialog.message_box.exec()
        logger.info(f'Entry Created: {self.docname}')
        startfile(f'{self.save_path}{self.docname}')


class DrivingPrivilegesEntryCreator(BaseEntryCreator):
    """Entry Creator for Driving Privilege entries."""

    save_path = DRIVE_SAVE_PATH

    def _set_document_name(self) -> str:
        """Overrides BaseEntryCreator _set_document_name.

        Sets the document name based on driver name instead of case number.
        """
        first_name = self.dialog.entry_case_information.defendant.first_name
        last_name = self.dialog.entry_case_information.defendant.last_name
        template_name = self.dialog.template.template_name
        return f'{first_name}_{last_name}_{template_name}.docx'


class AdminFiscalEntryCreator(BaseEntryCreator):
    """Entry Creator for Admin Fiscal entries."""

    save_path = FISCAL_SAVE_PATH

    def _set_document_name(self) -> str:
        """Overrides BaseEntryCreator set_document_name.

        Sets the document name based on driver name instead of case number.
        """
        account_number = self.dialog.entry_case_information.account_number
        vendor_name = self.dialog.entry_case_information.disbursement_vendor
        invoice = self.dialog.entry_case_information.invoice_number
        return f'{account_number}_{vendor_name}_{invoice}.docx'


class JuryPaymentEntryCreator(BaseEntryCreator):

    save_path = JURY_PAY_SAVE_PATH

    def _set_document_name(self) -> str:
        """Overrides BaseEntryCreator set_document_name.

        Sets the document name based on defendant name and case number.
        """
        case_number = self.dialog.entry_case_information.case_number
        last_name = self.dialog.entry_case_information.defendant.last_name
        template_name = self.dialog.template.template_name
        return f'{case_number}_{last_name}_{template_name}.docx'
