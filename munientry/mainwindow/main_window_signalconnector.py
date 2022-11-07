"""Signal connector module for the MainWindow."""
from functools import partial

from munientry.mainwindow.dialog_starter import start_dialog


class MainWindowSignalConnector(object):
    """Class for connecting signals to slots of the Main Window."""

    def __init__(self, main_window: object) -> None:
        self.main_window = main_window
        self.connect_general_buttons()
        self.connect_judicial_officers_to_set_officer()
        self.connect_dialog_buttons_to_start_dialog()

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
        """Updates the judicial officer whenever a judicial officer radio button is selected."""
        for key in self.main_window.judicial_officer_buttons_dict:
            key.clicked.connect(self.main_window.update_judicial_officer)

    def connect_dialog_buttons_to_start_dialog(self) -> None:
        """Connects all dialog buttons to the appropriate dialog.

        Each dialog button is binded to the start_dialog function with the dialog itself. When
        pressed the start_dialog function starts the dialog load process.
        """
        for button, dialog in self.main_window.dialog_buttons_dict.items():
            button.released.connect(partial(start_dialog, dialog, self.main_window))
