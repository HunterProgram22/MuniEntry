"""Contains all the template objects used in the application."""
import types
from dataclasses import dataclass

from munientry.appsettings.paths import TEMPLATE_PATH


@dataclass(frozen=True)
class Template(object):
    """Container for a template name and template path.

    Changes to content of template must be made on the template directly.
    """
    template_name: str
    template_path: str

    def __post_init__(self):
        object.__setattr__(self, 'template_path', f'{TEMPLATE_PATH}{self.template_path}')


def get_template_dict():
    template_dict = {}
    for template in TEMPLATE_LIST:
        template_dict[template.template_name] = template
    return types.MappingProxyType(template_dict)


TEMPLATE_LIST = [
    Template('Arraignment Continuance Entry', 'Arraignment_Continue_Template.docx'),
    Template('Fine Only Judgment Entry', 'Fine_Only_Plea_Final_Judgment_Template.docx'),
    Template('Jury Payment Entry', 'Jury_Payment_Template.docx'),
    Template('Admin Fiscal Entry', 'Admin_Fiscal_Template.docx'),
    Template('Driving Privileges Entry', 'Driving_Privileges_Template.docx'),
    Template('Leap Admission Plea Entry', 'Leap_Admission_Plea_Template.docx'),
    Template('Leap Admission Plea Already Valid Entry', 'Leap_Admission_Plea_Already_valid_Template.docx'),
    Template('Leap Sentencing Judgment Entry', 'Leap_Sentencing_Template.docx'),
    Template('Sentencing Judgment Entry', 'Sentencing_Only_Template.docx'),
    Template('Jail CC Judgment Entry', 'Jail_Plea_Final_Judgment_Template.docx'),
    Template('Trial Judgment Entry', 'Trial_Sentencing_Template.docx'),
    Template('Diversion Judgment Entry', 'Diversion_Template.docx'),
    Template('Not Guilty Bond Entry', 'Not_Guilty_Bond_Template'),
    Template('No Plea Bond Entry', 'No_Plea_Bond_Template'),
    Template('Probation Violation Bond Entry', 'Probation_Violation_Bond_Template.docx'),
    Template('Failure To Appear Entry', 'Failure_To_Appear_Template.docx'),
    Template('Freeform Entry', 'Freeform_Entry_Template.docx'),
    Template('Bond Hearing Entry', 'Bond_Hearing_Template.docx'),
    Template('Plea Only Entry', 'Plea_Only_Template.docx'),

]

TEMPLATE_DICT = get_template_dict()
# Scheduling_Entry_Template_Rohrer = Template(
#     'Rohrer Scheduling Entry',
#     'Scheduling_Entry_Template_Rohrer.docx',
# )
#
# Scheduling_Entry_Template_Hemmeter = Template(
#     'Hemmeter Scheduling Entry',
#     'Scheduling_Entry_Template_Hemmeter.docx',
# )
#
# Final_Jury_Notice_Of_Hearing_Template = Template(
#     'Final and Jury Notice Of Hearing Entry',
#     'Final_Jury_Notice_Of_Hearing_Template.docx',
# )
#
# General_Notice_Of_Hearing_Template = Template(
#     'General Notice Of Hearing Entry',
#     'General_Notice_Of_Hearing_Template.docx',
# )
#
# Trial_To_Court_Hearing_Notice_Template = Template(
#     'Trial To Court Notice Of Hearing Entry',
#     'Trial_To_Court_Hearing_Notice_Template.docx',
# )
#
# Civil_Freeform_Entry_Template = Template(
#     'Civil Freeform Entry',
#     'Civil_Freeform_Entry_Template.docx',
# )
#
# Criminal_Sealing_Entry_Template = Template(
#     'Criminal Sealing Entry',
#     'Criminal_Sealing_Entry_Template.docx',
# )