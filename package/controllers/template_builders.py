"""Module contains classes for building templates and entries"""
from os import startfile

from docxtpl import DocxTemplate
from package.views.custom_widgets import RequiredBox
from settings import SAVE_PATH, TEMPLATE_PATH, SUBDOC_PATH


class TemplateBuilder(object):
    def __init__(self, dialog: object) -> None:
        self.dialog = dialog.dialog
        self.dialog.update_entry_case_information()
        self.case_data = self.dialog.entry_case_information.get_case_information()
        self.base_template_name = 'Base_No_Conditions_Template.docx'
        self.base_template = self.build_base_template()
        self.create_case_entry()
        self.save_case_entry()
        self.open_case_entry()

    def build_base_template(self) -> str:
        """Returns the string template path of the base template after it renders and saves
        the template."""
        template = DocxTemplate(f'{TEMPLATE_PATH}{self.base_template_name}')
        subdoc_dict = self.set_subdoc_templates(template)
        doc_name = self.set_document_name()
        template.render(subdoc_dict)
        template_path = f'{SAVE_PATH}{doc_name}'
        template.save(template_path)
        return template_path

    def create_case_entry(self) -> None:
        self.case_entry = DocxTemplate(self.base_template)
        self.case_entry.render(self.case_data)

    def save_case_entry(self):
        self.case_entry_docname = self.set_document_name()
        self.case_entry.save(f'{SAVE_PATH}{self.case_entry_docname}')

    def open_case_entry(self):
        try:
            startfile(SAVE_PATH + self.case_entry_docname)
        except PermissionError:
            self.dialog.message_box = RequiredBox(
                "An entry for this case is already open in Word."
                " You must close the Word document first."
            )
            self.dialog.message_box.exec()

    def set_document_name(self) -> str:
        """Returns a name for the document in the format CaseNumber_TemplateName.docx"""
        return f"{self.dialog.entry_case_information.case_number}_{self.dialog.template.template_name}.docx"


    def set_subdoc_templates(self, doc):
        judicial_officer = self.dialog.entry_case_information.judicial_officer
        court_costs_subdoc = doc.new_subdoc(f'{SUBDOC_PATH}Court_Costs_Template.docx')
        financial_responsibilty_subdoc = doc.new_subdoc(f'{SUBDOC_PATH}Financial_Responsibility_Template.docx')
        service_subdoc = doc.new_subdoc(f'{SUBDOC_PATH}Service_Template.docx')
        charge_grid_subdoc = doc.new_subdoc(f'{SUBDOC_PATH}Charge_Grid_Template.docx')
        caption_subdoc = doc.new_subdoc(f'{SUBDOC_PATH}Criminal_Caption_Template.docx')
        document_title_subdoc = doc.new_subdoc(f'{SUBDOC_PATH}Document_Title_Template.docx')
        signature_subdoc = doc.new_subdoc(f'{SUBDOC_PATH}Signature_Template.docx')
        magistrate_notice_subdoc = doc.new_subdoc(f'{SUBDOC_PATH}Magistrate_Notice_Template.docx')
        appearance_reason_template = self.get_appearance_reason_template()
        appearance_reason_subdoc = doc.new_subdoc(f'{SUBDOC_PATH}{appearance_reason_template}')
        additional_conditions_subdoc = doc.new_subdoc(f'{SUBDOC_PATH}Additional_Conditions_Template.docx')
        subdoc_dict = {
            'judicial_officer': self.dialog.entry_case_information.judicial_officer,
            'additional_conditions_subdoc': additional_conditions_subdoc,
            'appearance_reason_subdoc': appearance_reason_subdoc,
            'financial_responsibility_subdoc': financial_responsibilty_subdoc,
            'court_costs_subdoc': court_costs_subdoc,
            'service_subdoc': service_subdoc,
            'charge_grid_subdoc': charge_grid_subdoc,
            'caption_subdoc': caption_subdoc,
            'document_title_subdoc': document_title_subdoc,
            'signature_subdoc': signature_subdoc,
            'magistrate_notice_subdoc': magistrate_notice_subdoc,
        }
        return subdoc_dict

    def get_appearance_reason_template(self):
        appearance_reason = self.dialog.entry_case_information.appearance_reason
        if appearance_reason == 'LEAP Sentencing':
            return 'Leap_Sentencing_Appearance_Template.docx'
        if appearance_reason == 'arraignment':
            return 'Arraignment_Appearance_Template.docx'
