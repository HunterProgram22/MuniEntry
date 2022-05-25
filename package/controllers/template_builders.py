"""Module contains classes for building templates and entries"""
from os import startfile

from docxtpl import DocxTemplate
from package.views.custom_widgets import RequiredBox
from settings import SAVE_PATH, TEMPLATE_PATH


class TemplateBuilder(object):
    def __init__(self, dialog):
        self.dialog = dialog.dialog
        self.create_entry()

    def set_document_name(self):
        """Returns a name for the document in the format CaseNumber_TemplateName.docx
        (i.e. 21CRB1234_Crim_Traffic Judgment Entry.docx"""
        return (
            f"{self.dialog.entry_case_information.case_number}"
                f"_{self.dialog.template.template_name}.docx"
        )

    def create_entry(self):
        """Loads the proper template and creates the entry."""
        self.dialog.update_entry_case_information()
        # base_template = DocxTemplate(self.dialog.template.template_path)
        base_template = DocxTemplate(TEMPLATE_PATH + 'Base_Template.docx')

        case_data = self.get_subdoc_templates(base_template)

        base_templatename = self.build_base_template(base_template, case_data)

        # Render main base_template with the subbase_template parts already loaded
        doc_two = DocxTemplate(SAVE_PATH + base_templatename)
        doc_two.render(case_data)
        docname = self.set_document_name()
        try:
            doc_two.save(SAVE_PATH + docname)

            startfile(SAVE_PATH + docname)
        except PermissionError:
            self.dialog.message_box = RequiredBox(
                "An entry for this case is already open in Word."
                " You must close the Word document first."
            )
            self.dialog.message_box.exec()

    def build_base_template(self, base_template, case_data):
        # Load first base_template by pulling necessary subbase_templates to create main base_template
        base_template.render(case_data)
        base_templatename = self.set_document_name()
        base_template.save(SAVE_PATH + base_templatename)
        return base_templatename

    def get_subdoc_templates(self, doc):
        court_costs_subdoc = doc.new_subdoc(TEMPLATE_PATH + 'Court_Costs_Template.docx')
        service_subdoc = doc.new_subdoc(TEMPLATE_PATH + 'Service_Template.docx')
        charge_grid_subdoc = doc.new_subdoc(TEMPLATE_PATH + 'Charge_Grid_Template.docx')
        caption_subdoc = doc.new_subdoc(TEMPLATE_PATH + 'Criminal_Caption_Template.docx')
        document_title_subdoc = doc.new_subdoc(TEMPLATE_PATH + 'Document_Title_Template.docx')
        case_data = self.dialog.entry_case_information.get_case_information()
        case_data['court_costs_subdoc'] = court_costs_subdoc
        case_data['service_subdoc'] = service_subdoc
        case_data['charge_grid_subdoc'] = charge_grid_subdoc
        case_data['caption_subdoc'] = caption_subdoc
        case_data['document_title_subdoc'] = document_title_subdoc
        return case_data
