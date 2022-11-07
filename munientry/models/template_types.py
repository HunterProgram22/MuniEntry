"""Module that contains all the template objects for use in the
application."""
from loguru import logger
import pathlib


PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\resources\\templates\\"


class Template:
    """Template objects contain all the relevant data for each type of template.
    Changes to content of template should be made on the template directly."""

    def __init__(self, template_name, template_path):
        self.template_name = template_name
        self.template_path = TEMPLATE_PATH + template_path

Jury_Payment_Template = Template(
    'Jury Payment Entry',
    'Jury_Payment_Template.docx',
)

Admin_Fiscal_Template = Template(
    'Admin Fiscal Journal Entry',
    'Admin_Fiscal_Template.docx',
)

Driving_Privileges_Template = Template(
    'Driving Privileges Journal Entry',
    'Driving_Privileges_Template.docx',
)

Fine_Only_Plea_Final_Judgment_Template = Template(
    'Fine Only Judgment Entry',
    'Fine_Only_Plea_Final_Judgment_Template.docx',
)

Leap_Sentencing_Template = Template(
    'Leap Sentencing Judgment Entry',
    'Leap_Sentencing_Template.docx',
)

Sentencing_Only_Template = Template(
    'Sentencing Judgment Entry',
    'Sentencing_Only_Template.docx',
)

Jail_CC_Plea_Final_Judgment_Template = Template(
    'Jail CC Judgment Entry',
    'Jail_Plea_Final_Judgment_Template.docx',
)

Trial_Sentencing_Template = Template(
    'Trial Judgment Entry',
    'Trial_Sentencing_Template.docx',
)

Diversion_Template = Template(
    'Diversion Judgment Entry',
    'Diversion_Template.docx',
)

Not_Guilty_Bond_Template = Template(
    'Not Guilty Bond Entry',
    'Not_Guilty_Bond_Template.docx',
)

No_Plea_Bond_Template = Template(
    'No Plea Bond Entry',
    'No_Plea_Bond_Template.docx',
)

Probation_Violation_Bond_Template = Template(
    'Probation Violation Bond Entry',
    'Probation_Violation_Bond_Template.docx',
)

Failure_To_Appear_Template = Template(
    'Failure To Appear Entry',
    'Failure_To_Appear_Template.docx',
)

Freeform_Entry_Template = Template(
    'Freeform Entry',
    'Freeform_Entry_Template.docx',
)

Bond_Hearing_Template = Template(
    'Bond Hearing Entry',
    'Bond_Hearing_Template.docx',
)

Plea_Only_Template = Template(
    'Plea Only Entry',
    'Plea_Only_Template.docx',
)

Leap_Admission_Plea_Template = Template(
    'LEAP Admission Plea Entry',
    'Leap_Admission_Plea_Template.docx',
)

Leap_Admission_Plea_Already_Valid_Template = Template(
    'LEAP Admission Plea Already Valid Entry',
    'Leap_Admission_Plea_Already_Valid_Template.docx',
)

Scheduling_Entry_Template_Rohrer = Template(
    'Rohrer Scheduling Entry',
    'Scheduling_Entry_Template_Rohrer.docx',
)

Scheduling_Entry_Template_Hemmeter = Template(
    'Hemmeter Scheduling Entry',
    'Scheduling_Entry_Template_Hemmeter.docx',
)

Final_Jury_Notice_Of_Hearing_Template = Template(
    'Final and Jury Notice Of Hearing Entry',
    'Final_Jury_Notice_Of_Hearing_Template.docx',
)

General_Notice_Of_Hearing_Template = Template(
    'General Notice Of Hearing Entry',
    'General_Notice_Of_Hearing_Template.docx',
)

Trial_To_Court_Hearing_Notice_Template = Template(
    'Trial To Court Notice Of Hearing Entry',
    'Trial_To_Court_Hearing_Notice_Template.docx',
)


TEMPLATE_DICT = {
    'Fine Only Plea Dialog': Fine_Only_Plea_Final_Judgment_Template,
    'Jail CC Plea Dialog': Jail_CC_Plea_Final_Judgment_Template,
    'Trial Sentencing Dialog': Trial_Sentencing_Template,
    'Sentencing Only Dialog': Sentencing_Only_Template,
    'Diversion Plea Dialog': Diversion_Template,
    'Not Guilty Bond Dialog': Not_Guilty_Bond_Template,
    'No Plea Bond Dialog': No_Plea_Bond_Template,
    'Probation Violation Bond Dialog': Probation_Violation_Bond_Template,
    'Failure To Appear Dialog': Failure_To_Appear_Template,
    'Bond Hearing Dialog': Bond_Hearing_Template,
    'Plea Only Dialog': Plea_Only_Template,
    'Leap Admission Plea Dialog': Leap_Admission_Plea_Template,
    'Leap Admission Plea Already Valid Dialog': Leap_Admission_Plea_Already_Valid_Template,
    'Leap Sentencing Dialog': Leap_Sentencing_Template,


    'Rohrer Scheduling Entry': Scheduling_Entry_Template_Rohrer,
    'Hemmeter Scheduling Entry': Scheduling_Entry_Template_Hemmeter,
    'Freeform Entry Dialog': Freeform_Entry_Template,
    'Final And Jury Notice Of Hearing Entry': Final_Jury_Notice_Of_Hearing_Template,
    'General Notice Of Hearing Entry': General_Notice_Of_Hearing_Template,
    'Trial To Court Notice Of Hearing Entry': Trial_To_Court_Hearing_Notice_Template,

    'Driving Privileges Entry': Driving_Privileges_Template,

    'Admin Fiscal Entry': Admin_Fiscal_Template,
    'Jury Payment Entry': Jury_Payment_Template,
}


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
