"""Signal connector module for the MainWindow."""
from munientry.mainwindow.dialog_starter import start_dialog


class MainWindowSignalConnector(object):
    """Class for connecting signals to slots of the Main Window."""

    def __init__(self, main_window: object) -> None:
        self.main_window = main_window
        self.connect_general_buttons()
        self.connect_judicial_officers_to_set_officer()
        self.connect_dialog_buttons_to_start_dialog()
        # self.connect_crim_traffic_buttons_to_start_dialog()
        # self.connect_scheduling_buttons_to_start_dialog()
        # self.connect_admin_buttons_to_start_dialog()
        # self.connect_admin_no_case_buttons_to_start_dialog()
        # self.connect_digital_workflow_buttons_to_start_dialog()
        # self.connect_probation_workflow_buttons_to_start_dialog()

    def connect_general_buttons(self):
        self.main_window.reload_cases_Button.released.connect(self.main_window.reload_case_lists)
        self.main_window.random_judge_Button.released.connect(self.main_window.assign_judge)
        self.main_window.visiting_judge_radioButton.toggled.connect(
            self.main_window.set_visiting_judge,
        )
        self.main_window.tabWidget.currentChanged.connect(self.main_window.set_person_stack_widget)
        self.main_window.get_case_Button.pressed.connect(self.main_window.query_case_info)
        self.main_window.show_docket_Button.pressed.connect(self.main_window.show_case_docket)
        self.main_window.show_docket_case_list_Button.pressed.connect(
            self.main_window.show_case_docket_case_list,
        )

    def connect_judicial_officers_to_set_officer(self) -> None:
        for key in self.main_window.judicial_officer_buttons_dict:
            key.clicked.connect(self.main_window.update_judicial_officer)

    def connect_dialog_buttons_to_start_dialog(self) -> None:
        for key, value in self.main_window.dialog_buttons_dict.items():
            key.released.connect(
                lambda value=value, mainwindow=self.main_window: start_dialog(value, mainwindow)
            )


    # def connect_crim_traffic_buttons_to_start_dialog(self) -> None:
    #     for key, value in self.main_window.crim_traffic_dialog_buttons_dict.items():
    #         key.released.connect(
    #             lambda value=value, mainwindow=self.main_window: start_dialog(value, mainwindow)
    #         )
    #
    # def connect_scheduling_buttons_to_start_dialog(self) -> None:
    #     for key, value in self.main_window.scheduling_dialog_buttons_dict.items():
    #         key.released.connect(
    #             lambda value=value, mainwindow=self.main_window: start_dialog(value, mainwindow)
    #         )
    #
    # def connect_admin_buttons_to_start_dialog(self) -> None:
    #     for key, value in self.main_window.admin_dialog_buttons_dict.items():
    #         key.released.connect(
    #             lambda value=value, mainwindow=self.main_window: start_dialog(value, mainwindow)
    #         )
    #
    # def connect_admin_no_case_buttons_to_start_dialog(self) -> None:
    #     for key, value in self.main_window.admin_dialog_no_case_buttons_dict.items():
    #         key.released.connect(
    #             lambda value=value, mainwindow=self.main_window: start_dialog(value, mainwindow)
    #         )
    #
    # def connect_digital_workflow_buttons_to_start_dialog(self) -> None:
    #     for key, value in self.main_window.digital_workflow_buttons_dict.items():
    #         key.released.connect(
    #             lambda value=value, mainwindow=self.main_window: start_dialog(value, mainwindow)
    #         )
    #
    # def connect_probation_workflow_buttons_to_start_dialog(self) -> None:
    #     for key, value in self.main_window.probation_workflow_buttons_dict.items():
    #         key.released.connect(
    #             lambda value=value, mainwindow=self.main_window: start_dialog(value, mainwindow)
    #         )
