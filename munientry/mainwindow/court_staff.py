"""Module for initiating and grouping court staff for the application."""
from loguru import logger
from PyQt6.QtWidgets import QInputDialog, QStackedWidget

from munientry.models.party_types import JudicialOfficer


class CourtStaffWidget(QStackedWidget):
    """Container for the court_staff_widget on the MainWindow of the application."""

    def __init__(self, mainwindow, parent=None):
        super().__init__(parent)
        self.mw = mainwindow
        self.judicial_officer_buttons: list = self.set_judicial_officer_buttons()
        self.assignment_commissioner_buttons: list = self.set_assignment_commissioner_buttons()
        self.administrative_staff_buttons: list = self.set_administrative_staff_buttons()
        self.court_staff_buttons_dict: dict = self.create_court_staff_buttons_dict()

    def set_person_stack_widget(self) -> None:
        stack_mapping = {
            'crim_traffic_Tab': self.mw.judicial_officers_Stack,
            'scheduling_Tab': self.mw.assignment_commissioners_Stack,
            'admin_Tab': self.mw.admin_staff_Stack,
            'civil_Tab': self.mw.judicial_officers_Stack,
            'probation_tab': self.mw.comm_control_officers_stack,
        }
        current_tab_name = self.mw.tabWidget.currentWidget().objectName()
        current_stack = stack_mapping.get(current_tab_name)
        if current_stack is not None:
            self.mw.court_staff_widget.setCurrentWidget(current_stack)
            logger.info(f'Current Staff Tab is {current_stack.objectName()}')
        logger.info(f'Current Entry Tab is {current_tab_name}')

    def update_court_staff(self) -> None:
        self.mw.judicial_officer = self.court_staff_buttons_dict.get(self.mw.sender())
        judicial_officer = self.mw.judicial_officer.last_name
        logger.action(f'Court Staff set to: {judicial_officer}')

    def set_visiting_judge(self):
        if self.mw.visiting_judge_radio_btn.isChecked():
            first_name, response_ok = QInputDialog.getText(
                self.mw, 'Set Visiting Judge', 'Enter Judge First Name:',
            )
            last_name, response_ok = QInputDialog.getText(
                self.mw, 'Set Visiting Judge', 'Enter Judge Last Name:',
            )
            if response_ok:
                update_dict = {
                    self.mw.visiting_judge_radio_btn: JudicialOfficer(
                        f'{first_name}', f'{last_name}', 'Judge',
                    ),
                }
                self.court_staff_buttons_dict.update(update_dict)
                self.mw.visiting_judge_radio_btn.setText(f'Judge {last_name}')

    def set_judicial_officer_buttons(self):
        return [
            self.mw.judge_1_radio_btn,
            self.mw.judge_2_radio_btn,
            self.mw.visiting_judge_radio_btn,
            self.mw.mag_1_radio_btn,
            self.mw.mag_2_radio_btn,
            self.mw.mag_3_radio_btn
        ]

    def set_assignment_commissioner_buttons(self):
        return [
            self.mw.assn_comm_1_radio_btn,
            self.mw.assn_comm_2_radio_btn,
            self.mw.no_assn_comm_radio_btn,
        ]

    def set_administrative_staff_buttons(self):
        return [
            self.mw.assn_comm_dattilo_radioButton,
            self.mw.assn_comm_patterson_radioButton,
            self.mw.court_admin_kudela_radioButton,
            self.mw.jury_comm_patterson_radioButton,
            self.mw.bunner_admin_radioButton,
            self.mw.none_admin_radioButton,
        ]

    def create_court_staff_buttons_dict(self) -> dict:
        return {
            self.mw.judge_1_radio_btn: JudicialOfficer('Marianne', 'Hemmeter', 'Judge'),
            self.mw.judge_2_radio_btn: JudicialOfficer('Kyle', 'Rohrer', 'Judge'),
            self.mw.visiting_judge_radio_btn: JudicialOfficer('None', 'Assigned', 'Judge'),
            self.mw.mag_1_radio_btn: JudicialOfficer('Amanda', 'Bunner', 'Magistrate'),
            self.mw.mag_2_radio_btn: JudicialOfficer('Kevin', 'Pelanda', 'Magistrate'),
            self.mw.mag_3_radio_btn: JudicialOfficer('Justin', 'Kudela', 'Magistrate'),
            self.mw.assn_comm_1_radio_btn: JudicialOfficer('Pat', 'Dattilo', 'Assignment Commissioner'),
            self.mw.assn_comm_2_radio_btn: JudicialOfficer('Kathryn', 'Patterson', 'Assignment Commissioner'),
            self.mw.no_assn_comm_radio_btn: JudicialOfficer('None', 'Assigned', 'Assignment Commissioner'),
            self.mw.assn_comm_dattilo_radioButton: JudicialOfficer('Pat', 'Dattilo', 'Assignment Commissioner'),
            self.mw.assn_comm_patterson_radioButton: JudicialOfficer('Kathryn', 'Patterson', 'Assignment Commissioner'),
            self.mw.court_admin_kudela_radioButton: JudicialOfficer('Justin', 'Kudela', 'Court Administrator'),
            self.mw.jury_comm_patterson_radioButton: JudicialOfficer('Kathryn', 'Patterson', 'Jury Commissioner'),
            self.mw.none_admin_radioButton: JudicialOfficer('None', 'Assigned', 'Admin Staff Person'),
            self.mw.bunner_admin_radioButton: JudicialOfficer('A', 'B', 'Admin Staff Person'),
        }
