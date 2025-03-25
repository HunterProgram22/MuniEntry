"""Module for initiating and grouping court staff for the application."""
from loguru import logger
from PyQt6.QtWidgets import QInputDialog

from munientry.models.party_types import JudicialOfficer

ADMIN = 'Admin Staff Person'
ASSN_COMM = 'Assignment Commissioner'
BOND_CCO = 'Bond Intake Officer'
CCO = 'Community Control Officer'
CHIEF_CCO = 'Chief Community Control Officer'
CT_ADMIN = 'Court Administrator'
DEP_CCCO = 'Deputy Chief Community Control Officer'
JUDGE = 'Judge'
JURY = 'Jury Commissioner'
MAGISTRATE = 'Magistrate'


class CourtStaffManager(object):
    """Container for the court_staff_widget on the MainWindow of the application.

    The CourtStaffManager is instantiated into the MainWindow attribute court_staff to provide
    all necessary functions for manipulating the court_staff_widget (QStackedWidget) on the
    MainWindow.
    """

    def __init__(self, mainwindow):
        self.mw = mainwindow
        self.judicial_officer_buttons: list = [
            self.mw.judge_1_radio_btn,
            self.mw.judge_2_radio_btn,
            self.mw.visiting_judge_radio_btn,
            self.mw.mag_1_radio_btn,
            self.mw.mag_2_radio_btn,
            self.mw.mag_3_radio_btn,
        ]
        self.assignment_commissioner_buttons: list = [
            self.mw.assn_comm_1_radio_btn,
            self.mw.assn_comm_2_radio_btn,
            self.mw.no_assn_comm_radio_btn,
        ]
        self.administrative_staff_buttons: list = [
            self.mw.assn_comm_1_admin_radio_btn,
            self.mw.assn_comm_2_admin_radio_btn,
            self.mw.court_admin_admin_radio_btn,
            self.mw.jury_comm_1_admin_radio_btn,
            self.mw.mag_1_admin_radio_btn,
            self.mw.mag_2_admin_radio_btn,
            self.mw.mag_3_admin_radio_btn,
            self.mw.none_admin_radio_btn,
        ]
        self.probation_staff_buttons: list = [
            self.mw.chief_prob_officer_radio_btn,
            self.mw.dep_chief_prob_officer_radio_btn,
            self.mw.prob_officer_1_radio_btn,
            self.mw.prob_officer_2_radio_btn,
            self.mw.prob_officer_3_radio_btn,
            self.mw.prob_officer_4_radio_btn,
            self.mw.prob_officer_5_radio_btn,
            self.mw.bond_intake_officer_radio_btn,
        ]
        self.court_staff_buttons_dict: dict = self.create_court_staff_buttons_dict()

    def set_person_stack_widget(self) -> None:
        stack_mapping = {
            'crim_traffic_tab': self.mw.judicial_officers_stack,
            'scheduling_tab': self.mw.assignment_commissioners_stack,
            'administrative_tab': self.mw.admin_staff_stack,
            'civil_tab': self.mw.judicial_officers_stack,
            'probation_tab': self.mw.comm_control_officers_stack,
        }
        current_tab_name = self.mw.entries_tab_widget.currentWidget().objectName()
        current_stack = stack_mapping.get(current_tab_name)
        if current_stack is not None:
            self.mw.court_staff_widget.setCurrentWidget(current_stack)
            logger.info(f'Current Staff Stack is {current_stack.objectName()}')
        logger.info(f'Current Entry Tab is {current_tab_name}')

    def update_court_staff(self) -> None:
        self.mw.judicial_officer = self.court_staff_buttons_dict.get(self.mw.sender())
        judicial_officer = self.mw.judicial_officer.last_name
        logger.info(f'Court Staff set to: {judicial_officer}')

    def set_visiting_judge(self) -> None:
        title = 'Set Visiting Judge'
        if self.mw.visiting_judge_radio_btn.isChecked():
            first_name, ok_input = QInputDialog.getText(self.mw, title, 'Enter Judge First Name:')
            last_name, ok_input = QInputDialog.getText(self.mw, title, 'Enter Judge Last Name:')
            if ok_input:
                visiting_judge = JudicialOfficer(f'{first_name}', f'{last_name}', JUDGE)
                updated_data = {self.mw.visiting_judge_radio_btn: visiting_judge}
                self.court_staff_buttons_dict.update(updated_data)
                self.mw.visiting_judge_radio_btn.setText(f'Judge {last_name}')

    def create_court_staff_buttons_dict(self) -> dict:
        return {
            self.mw.judge_1_radio_btn: JudicialOfficer('Mark', 'Fowler', JUDGE),
            self.mw.judge_2_radio_btn: JudicialOfficer('Kyle', 'Rohrer', JUDGE),
            self.mw.visiting_judge_radio_btn: JudicialOfficer('None', 'Assigned', JUDGE),
            self.mw.mag_1_radio_btn: JudicialOfficer('Amanda', 'Bunner', MAGISTRATE),
            self.mw.mag_2_radio_btn: JudicialOfficer('Kevin', 'Pelanda', MAGISTRATE),
            self.mw.mag_3_radio_btn: JudicialOfficer('Justin', 'Kudela', MAGISTRATE),

            self.mw.assn_comm_1_radio_btn: JudicialOfficer('Pat', 'Dattilo', ASSN_COMM),
            self.mw.assn_comm_2_radio_btn: JudicialOfficer('Tina', 'Spiers', ASSN_COMM),
            self.mw.no_assn_comm_radio_btn: JudicialOfficer('None', 'Assigned', ASSN_COMM),

            self.mw.assn_comm_1_admin_radio_btn: JudicialOfficer('Pat', 'Dattilo', ASSN_COMM),
            self.mw.assn_comm_2_admin_radio_btn: JudicialOfficer('Tina', 'Spiers', ASSN_COMM),
            self.mw.court_admin_admin_radio_btn: JudicialOfficer('Justin', 'Kudela', CT_ADMIN),
            self.mw.jury_comm_1_admin_radio_btn: JudicialOfficer('Tina', 'Spiers', JURY),
            self.mw.none_admin_radio_btn: JudicialOfficer('None', 'Assigned', ADMIN),
            self.mw.mag_1_admin_radio_btn: JudicialOfficer('Amanda', 'Bunner', MAGISTRATE),
            self.mw.mag_2_admin_radio_btn: JudicialOfficer('Kevin', 'Pelanda', MAGISTRATE),
            self.mw.mag_3_admin_radio_btn: JudicialOfficer('Justin', 'Kudela', MAGISTRATE),

            self.mw.chief_prob_officer_radio_btn: JudicialOfficer('Lindsey', 'Blue', CHIEF_CCO),
            self.mw.dep_chief_prob_officer_radio_btn: JudicialOfficer('Kurt', 'Olson', DEP_CCCO),
            self.mw.prob_officer_1_radio_btn: JudicialOfficer('Andrew', 'Conway', CCO),
            self.mw.prob_officer_2_radio_btn: JudicialOfficer('Elliot', 'Lagendyk', CCO),
            self.mw.prob_officer_3_radio_btn: JudicialOfficer('Jessica', 'Scholz', CCO),
            self.mw.prob_officer_4_radio_btn: JudicialOfficer('Adam', 'Garloch', CCO),
            self.mw.prob_officer_5_radio_btn: JudicialOfficer('Kara', 'Moore', CCO),
            self.mw.bond_intake_officer_radio_btn: JudicialOfficer('Sheryl', 'Titus', BOND_CCO),
        }
