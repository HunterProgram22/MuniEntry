import pathlib

PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\resources\\templates\\"

class Template(object):
    """Template objects contain all the relevant data for each type of template.
    Changes to content of template should be made on the template directly."""
    def __init__ (self, template_name, template_path):
        self.template_name = template_name
        self.template_path = TEMPLATE_PATH + template_path


Magistrate_And_Judge_Final_Judgment_Template = Template(
    "Traffic Judgment Entry",
    "Magistrate_And_Judge_Final_Judgment_Template.docx",
)

Judge_Final_Judgment_Template = Template(
    "Traffic Judgment Entry",
    "Judge_Final_Judgment_Template.docx",
)


TEMPLATE_DICT = {
    "Bunner" : Magistrate_And_Judge_Final_Judgment_Template,
    "Pelanda" : Magistrate_And_Judge_Final_Judgment_Template,
    "Rohrer" : Judge_Final_Judgment_Template,
    "Hemmeter" : Judge_Final_Judgment_Template,
}
