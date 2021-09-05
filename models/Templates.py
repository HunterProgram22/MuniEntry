import pathlib

PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\resources\\templates\\"

class Template(object):
    """Template objects contain all the relevant data for each type of template.
    Changes to content of template should be made on the template directly."""
    def __init__ (self, template_name, template_path, judicial_officer):
        self.template_name = template_name
        self.template_path = TEMPLATE_PATH + template_path
        self.template_judicial_officer = judicial_officer


Bunner_Template = Template(
    "Traffic Judgment Entry",
    "Bunner_No_Jail_Traffic_Template.docx",
    "Bunner"
    )

Pelanda_Template = Template(
    "Traffic Judgment Entry",
    "Pelanda_No_Jail_Traffic_Template.docx",
    "Pelanda"
    )

Rohrer_Template = Template(
    "Traffic Judgment Entry",
    "Rohrer_No_Jail_Traffic_Template.docx",
    "Rohrer"
    )

Hemmeter_Template = Template(
    "Traffic Judgment Entry",
    "Hemmeter_No_Jail_Traffic_Template.docx",
    "Hemmeter"
    )

TEMPLATE_DICT = {
    "Bunner" : Bunner_Template,
    "Pelanda" : Pelanda_Template,
    "Rohrer" : Rohrer_Template,
    "Hemmeter" : Hemmeter_Template
}
