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


Magistrate_And_Judge_Final_Judgment_Template = Template(
    "Traffic Judgment Entry",
    "Magistrate_And_Judge_Final_Judgment_Template.docx",
)

Leap_Plea_And_Admission_Template = Template(
    "LEAP Plea Admission Entry",
    "Leap_Plea_Admission_Template.docx",
)

Leap_Plea_Precourt_Completion_Template = Template(
    "LEAP Plea Precourt Completion Entry",
    "Leap_Plea_Precourt_Completion_Template.docx",
)

FTA_Bond_Template = Template(
    "FTA Bond Dialog",
    "FTA_Bond_Template.docx",
)

Not_Guilty_Bond_Template = Template(
    "Not Guilty Bond Dialog",
    "Not_Guilty_Bond_Template.docx",
)



TEMPLATE_DICT = {
    "No Jail Plea Dialog": Magistrate_And_Judge_Final_Judgment_Template,
    "Leap Plea Dialog": Leap_Plea_And_Admission_Template,
    "Leap Precourt Completion Dialog": Leap_Plea_Precourt_Completion_Template,
    "FTA Bond Dialog": FTA_Bond_Template,
    "Not Guilty Bond Dialog": Not_Guilty_Bond_Template,
}
