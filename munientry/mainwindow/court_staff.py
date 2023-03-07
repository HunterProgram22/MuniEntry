"""Module for initiating and grouping court staff for the application."""

class CourtStaff(object):

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow


    def set_judicial_officer_buttons(self):
        return [
            self.judge_1_radio_btn,
            self.judge_2_radio_btn,
            self.visiting_judge_radio_btn,
            self.mag_1_radio_btn,
            self.mag_2_radio_btn,
            self.mag_3_radio_btn
        ]


    def set_assignment_commissioner_buttons(self):
        return [
            self.assn_comm_1_radio_btn,
            self.assn_comm_2_radio_btn,
            self.no_assn_comm_radio_btn,
    ]
