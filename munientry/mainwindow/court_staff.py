"""Module for initiating and grouping court staff for the application."""
from loguru import logger
from PyQt6.QtWidgets import QInputDialog

from munientry.models.party_types import JudicialOfficer
from munientry.settings.config_settings import load_config

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
        self.config = load_config()
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
        self.update_button_labels()

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

    def _get_staff_member(self, prefix: str, role: str) -> JudicialOfficer:
        """Helper method to retrieve staff member from config."""
        staff = self.config['staff']
        first_name = staff.get(f'{prefix}_first', 'Unknown')
        last_name = staff.get(f'{prefix}_last', 'Unknown')
        return JudicialOfficer(first_name, last_name, role)

    def update_button_labels(self) -> None:
        """Update all radio button labels with names from config."""
        # Judges
        judge_1 = self._get_staff_member('judge_1', JUDGE)
        judge_2 = self._get_staff_member('judge_2', JUDGE)
        self.mw.judge_1_radio_btn.setText(f'Judge {judge_1.last_name}')
        self.mw.judge_2_radio_btn.setText(f'Judge {judge_2.last_name}')

        # Magistrates
        mag_1 = self._get_staff_member('magistrate_1', MAGISTRATE)
        mag_2 = self._get_staff_member('magistrate_2', MAGISTRATE)
        mag_3 = self._get_staff_member('magistrate_3', MAGISTRATE)
        self.mw.mag_1_radio_btn.setText(f'Magistrate {mag_1.last_name}')
        self.mw.mag_2_radio_btn.setText(f'Magistrate {mag_2.last_name}')
        self.mw.mag_3_radio_btn.setText(f'Magistrate {mag_3.last_name}')

        # Assignment Commissioners
        assn_1 = self._get_staff_member('assignment_comm_1', ASSN_COMM)
        assn_2 = self._get_staff_member('assignment_comm_2', ASSN_COMM)
        self.mw.assn_comm_1_radio_btn.setText(f'{assn_1.first_name} {assn_1.last_name}')
        self.mw.assn_comm_2_radio_btn.setText(f'{assn_2.first_name} {assn_2.last_name}')

        # Admin Assignment Commissioners
        self.mw.assn_comm_1_admin_radio_btn.setText(f'Assignment Commissioner {assn_1.last_name}')
        self.mw.assn_comm_2_admin_radio_btn.setText(f'Assignment Commissioner {assn_2.last_name}')

        # Admin Court Administrator and Jury Commissioner
        court_admin = self._get_staff_member('court_admin', CT_ADMIN)
        jury_comm = self._get_staff_member('jury_comm', JURY)
        self.mw.court_admin_admin_radio_btn.setText(f'Court Administrator {court_admin.last_name}')
        self.mw.jury_comm_1_admin_radio_btn.setText(f'Jury Commissioner {jury_comm.last_name}')

        # Admin Magistrates
        self.mw.mag_1_admin_radio_btn.setText(f'Magistrate {mag_1.last_name}')
        self.mw.mag_2_admin_radio_btn.setText(f'Magistrate {mag_2.last_name}')
        self.mw.mag_3_admin_radio_btn.setText(f'Magistrate {mag_3.last_name}')

        # Probation Staff
        chief = self._get_staff_member('chief_cco', CHIEF_CCO)
        deputy_chief = self._get_staff_member('deputy_chief_cco', DEP_CCCO)
        cco_1 = self._get_staff_member('cco_1', CCO)
        cco_2 = self._get_staff_member('cco_2', CCO)
        cco_3 = self._get_staff_member('cco_3', CCO)
        cco_4 = self._get_staff_member('cco_4', CCO)
        cco_5 = self._get_staff_member('cco_5', CCO)
        bond_officer = self._get_staff_member('bond_intake_officer', BOND_CCO)

        self.mw.chief_prob_officer_radio_btn.setText(f'Chief {chief.first_name} {chief.last_name}')
        self.mw.dep_chief_prob_officer_radio_btn.setText(
            f'Deputy Chief {deputy_chief.first_name} {deputy_chief.last_name}')
        self.mw.prob_officer_1_radio_btn.setText(f'Officer {cco_1.first_name} {cco_1.last_name}')
        self.mw.prob_officer_2_radio_btn.setText(f'Officer {cco_2.first_name} {cco_2.last_name}')
        self.mw.prob_officer_3_radio_btn.setText(f'Officer {cco_3.first_name} {cco_3.last_name}')
        self.mw.prob_officer_4_radio_btn.setText(f'Officer {cco_4.first_name} {cco_4.last_name}')
        self.mw.prob_officer_5_radio_btn.setText(f'Officer {cco_5.first_name} {cco_5.last_name}')
        self.mw.bond_intake_officer_radio_btn.setText(
            f'Pretrial Officer {bond_officer.first_name} {bond_officer.last_name}')

    def create_court_staff_buttons_dict(self) -> dict:
        return {
            # Judges
            self.mw.judge_1_radio_btn: self._get_staff_member('judge_1', JUDGE),
            self.mw.judge_2_radio_btn: self._get_staff_member('judge_2', JUDGE),
            self.mw.visiting_judge_radio_btn: JudicialOfficer('None', 'Assigned', JUDGE),

            # Magistrates
            self.mw.mag_1_radio_btn: self._get_staff_member('magistrate_1', MAGISTRATE),
            self.mw.mag_2_radio_btn: self._get_staff_member('magistrate_2', MAGISTRATE),
            self.mw.mag_3_radio_btn: self._get_staff_member('magistrate_3', MAGISTRATE),

            # Assignment Commissioners
            self.mw.assn_comm_1_radio_btn: self._get_staff_member('assignment_comm_1', ASSN_COMM),
            self.mw.assn_comm_2_radio_btn: self._get_staff_member('assignment_comm_2', ASSN_COMM),
            self.mw.no_assn_comm_radio_btn: JudicialOfficer('None', 'Assigned', ASSN_COMM),

            # Administrative Staff (Assignment Commissioners)
            self.mw.assn_comm_1_admin_radio_btn: self._get_staff_member('assignment_comm_1',
                                                                        ASSN_COMM),
            self.mw.assn_comm_2_admin_radio_btn: self._get_staff_member('assignment_comm_2',
                                                                        ASSN_COMM),

            # Administrative Staff (Other)
            self.mw.court_admin_admin_radio_btn: self._get_staff_member('court_admin', CT_ADMIN),
            self.mw.jury_comm_1_admin_radio_btn: self._get_staff_member('jury_comm', JURY),
            self.mw.none_admin_radio_btn: JudicialOfficer('None', 'Assigned', ADMIN),

            # Administrative Staff (Magistrates)
            self.mw.mag_1_admin_radio_btn: self._get_staff_member('magistrate_1', MAGISTRATE),
            self.mw.mag_2_admin_radio_btn: self._get_staff_member('magistrate_2', MAGISTRATE),
            self.mw.mag_3_admin_radio_btn: self._get_staff_member('magistrate_3', MAGISTRATE),

            # Probation Staff
            self.mw.chief_prob_officer_radio_btn: self._get_staff_member('chief_cco', CHIEF_CCO),
            self.mw.dep_chief_prob_officer_radio_btn: self._get_staff_member('deputy_chief_cco',
                                                                             DEP_CCCO),
            self.mw.prob_officer_1_radio_btn: self._get_staff_member('cco_1', CCO),
            self.mw.prob_officer_2_radio_btn: self._get_staff_member('cco_2', CCO),
            self.mw.prob_officer_3_radio_btn: self._get_staff_member('cco_3', CCO),
            self.mw.prob_officer_4_radio_btn: self._get_staff_member('cco_4', CCO),
            self.mw.prob_officer_5_radio_btn: self._get_staff_member('cco_5', CCO),
            self.mw.bond_intake_officer_radio_btn: self._get_staff_member('bond_intake_officer',
                                                                          BOND_CCO),
        }
