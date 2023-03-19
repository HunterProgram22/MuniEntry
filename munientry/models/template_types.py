"""Contains all the template objects used in the application."""
import os

from dataclasses import dataclass
from types import MappingProxyType

from munientry.appsettings.paths import TEMPLATE_PATH


def get_template_dict() -> MappingProxyType:
    """Generate a dictionary of templates and sets the template paths.

    Returns:
        MappingProxyType: An immutable dictionary of templates.
    """
    template_dict = {}
    for template in TEMPLATE_LIST:
        template_dict[template.template_name] = template
    return MappingProxyType(template_dict)


@dataclass
class Template(object):
    """Container for a template name and template path.

    TODO: In the Builder Class the attribute of template name becomes dialog_name, need to update.
    """

    template_name: str
    template_path: str

    def __post_init__(self):
        """Set the full path for the template file."""
        self.template_path = os.path.join(TEMPLATE_PATH, self.template_path)


TEMPLATE_LIST = (
    Template('Arraignment Continuance Entry', 'Arraignment_Continue_Template.docx'),
    Template('Fine Only Judgment Entry', 'Fine_Only_Plea_Final_Judgment_Template.docx'),
    Template('Jury Payment Entry', 'Jury_Payment_Template.docx'),
    Template('Admin Fiscal Entry', 'Admin_Fiscal_Template.docx'),
    Template('Driving Privileges Entry', 'Driving_Privileges_Template.docx'),
    Template('Leap Admission Plea Entry', 'Leap_Admission_Plea_Template.docx'),
    Template('Leap Admission Plea Valid Entry', 'Leap_Admission_Plea_Valid_Template.docx'),
    Template('Leap Sentencing Judgment Entry', 'Leap_Sentencing_Template.docx'),
    Template('Sentencing Judgment Entry', 'Sentencing_Only_Template.docx'),
    Template('Jail CC Judgment Entry', 'Jail_Plea_Final_Judgment_Template.docx'),
    Template('Trial Judgment Entry', 'Trial_Sentencing_Template.docx'),
    Template('Diversion Judgment Entry', 'Diversion_Template.docx'),
    Template('Not Guilty Bond Entry', 'Not_Guilty_Bond_Template.docx'),
    Template('No Plea Bond Entry', 'No_Plea_Bond_Template.docx'),
    Template('Probation Violation Bond Entry', 'Probation_Violation_Bond_Template.docx'),
    Template('Failure To Appear Entry', 'Failure_To_Appear_Template.docx'),
    Template('Freeform Entry', 'Freeform_Entry_Template.docx'),
    Template('Bond Hearing Entry', 'Bond_Hearing_Template.docx'),
    Template('Plea Only Entry', 'Plea_Only_Template.docx'),
    Template('Rohrer Scheduling Entry', 'Scheduling_Entry_Template_Rohrer.docx'),
    Template('Hemmeter Scheduling Entry', 'Scheduling_Entry_Template_Hemmeter.docx'),
    Template('Final And Jury Notice Hearing Entry', 'Final_Jury_Notice_Of_Hearing_Template.docx'),
    Template('General Notice Of Hearing Entry', 'General_Notice_Of_Hearing_Template.docx'),
    Template('Trial To Court Notice Hearing Entry', 'Trial_To_Court_Hearing_Notice_Template.docx'),
    Template('Civil Freeform Entry', 'Civil_Freeform_Entry_Template.docx'),
    Template('Criminal Sealing Entry', 'Criminal_Sealing_Entry_Template.docx'),
    Template('Terms Of Community Control Entry', 'Terms_Of_Community_Control_Template.docx'),
    Template('Notice Of Community Control Violation Entry', 'Notice_CC_Violation_Template.docx'),
)

TEMPLATE_DICT = get_template_dict()
