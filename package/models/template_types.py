"""Module that contains all the template objects for use in the
application."""
import pathlib


PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\resources\\templates\\"


class Template():
    """Template objects contain all the relevant data for each type of template.
    Changes to content of template should be made on the template directly."""
    def __init__(self, template_name, template_path):
        self.template_name = template_name
        self.template_path = TEMPLATE_PATH + template_path


No_Jail_Plea_Final_Judgment_Template = Template(
    "Crim_Traffic Judgment Entry",
    "No_Jail_Plea_Final_Judgment_Template.docx",
)

Jail_CC_Plea_Final_Judgment_Template = Template(
    "Crim_Traffic Judgment Entry",
    "Jail_Plea_Final_Judgment_Template.docx",
)

Diversion_Template = Template(
    "Diversion Judgment Entry",
    "Diversion_Template.docx",
)

Not_Guilty_Bond_Template = Template(
    "Not Guilty Bond Dialog",
    "Not_Guilty_Bond_Template.docx",
)


TEMPLATE_DICT = {
    "No Jail Plea Dialog": No_Jail_Plea_Final_Judgment_Template,
    "Jail CC Plea Dialog": Jail_CC_Plea_Final_Judgment_Template,
    "Diversion Plea Dialog": Diversion_Template,
    "Not Guilty Bond Dialog": Not_Guilty_Bond_Template,
}
