"""
The main application entry point. The main window contains options for
selecting the judicial officer on the case and also different templates.
"""
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from loguru import logger

from models.party_types import JudicialOfficer
from views.main_window_ui import Ui_MainWindow
from controllers.minor_misdemeanor_dialogs import MinorMisdemeanorDialog
from controllers.leap_plea_dialogs import LeapPleaLongDialog, LeapPleaShortDialog
from controllers.fta_bond_dialogs import FTABondDialog
from settings import CASES_DATABASE
from resources.db.DatabaseCreation import create_cases_list

logger.add("./resources/logs/Error_log_{time}.log")



@logger.catch
def create_database_connections():
    """The databases for the application are created upon import of the module, which is done
    on application startup. The connections to the databases are created, but the opening and
    closing of the databases is handled by the appropriate class dialog."""
    arraignments_database_connection = QSqlDatabase.addDatabase("QSQLITE", "cases")
    arraignments_database_connection.setDatabaseName(CASES_DATABASE)
    return arraignments_database_connection


class Window(QMainWindow, Ui_MainWindow):
    """The MainWindow of the application.  If changes to the view
    (Ui_MainWindow) are made in QtDesigner then the command
    'pyuic5 -o views/main_window_ui.py resources/ui/MainWindow.ui' must be run
    to update changes to the view file.

    All slots and signals are connected after the view is created. Slots and
    signals can be linked in the view (using QtDesigner or directly in the view
    file after pyuic5 is run), however, connecting in MainWindow (class Window)
    is generally cleaner and allows ease of scalabilty.

    :judicial_officer_dict: - If a new judicial officer is added then
    they only need a radio button added to the view (key:
    self.lastname_radioButton, value: "Lastname").The button will be connected
    to the slot for self.judicial_officer by the function
    connect_judicial_officer_buttons.

    :dialog_dict: - If a new entry button is added to the view then a new
    key:value pair needs to be added to dialog_dict (key: buttonName, value:
    dialogObject).
    """

    def __init__(self, arraignment_list, parent=None):
        super().__init__(parent)
        self.setupUi(self)  # The self argument that is called is MainWindow
        self.connect_menu_signal_slots()
        self.judicial_officer = None
        self.judicial_officer_type = None
        self.judicial_officer_dict = {
            self.bunner_radioButton: JudicialOfficer("Amanda", "Bunner", "Magistrate"),
            self.pelanda_radioButton: JudicialOfficer("Kevin", "Pelanda", "Magistrate"),
            self.kudela_radioButton: JudicialOfficer("Justin", "Kudela", "Magistrate"),
            self.rohrer_radioButton: JudicialOfficer("Kyle", "Rohrer", "Judge"),
            self.hemmeter_radioButton: JudicialOfficer("Marianne", "Hemmeter", "Judge"),
        }
        self.dialog_dict = {
            self.MinorMisdemeanorTrafficButton: MinorMisdemeanorDialog,
            self.LeapPleaLongButton: LeapPleaLongDialog,
            self.LeapPleaShortButton: LeapPleaShortDialog,
            self.FTABondButton: FTABondDialog,
        }
        self.connect_judicial_officer_buttons()
        self.connect_entry_buttons()
        self.arraignment_list = create_cases_list()
        self.load_arraignment_case_list()


    def load_arraignment_case_list(self):
        self.arraignment_cases_box.addItems(self.arraignment_list)

    def connect_judicial_officer_buttons(self):
        """Connects the radio buttons for each judicial officer to their
        JudicialOfficer object.

        'Clicked' is used instead of 'pressed' for connecting the
        judicial_officer buttons because 'pressed' was causing an
        inconsistent bug."""
        for key in self.judicial_officer_dict:
            key.clicked.connect(self.set_judicial_officer)

    def set_judicial_officer(self):
        """Sets the judicial officer for the main application that will be
        transferred to the entry that is selected."""
        for key, value in self.judicial_officer_dict.items():
            print("SJO Ran")
            if key.isChecked():
                print("Checked")
                self.judicial_officer = value
                print(self.judicial_officer)

    def connect_entry_buttons(self):
        """Cycles through all buttons that are listed in the dialog_dict and
        connects them to the slot for each button. Connects the starting dialog
        that will be launched upon button press."""
        for key in self.dialog_dict:
            key.pressed.connect(self.start_dialog_from_entry_button)

    def connect_menu_signal_slots(self):
        """Self explanatory."""
        self.menu_file_exit.triggered.connect(self.close)

    @logger.catch
    def start_dialog_from_entry_button(self):
        """
        Launches the dialog that is connected to each button.
        The judicial_officer argument must be passed to insure the creation
        of the proper template features.

        TODO: "Issue is in the self.arraignment list is pulling the string case number from the create_cases_list
        in the databasecreation module. Need to load the case object. Use get case to load function  "
        """
        #try:
        print(self.judicial_officer)
        if self.judicial_officer is None:
            print(self.judicial_officer)
            #raise AttributeError
        case_to_load = next((case for case in self.arraignment_list if case.case_number == self.arraignment_cases_box.currentText()), None)
        dialog = self.dialog_dict[self.sender()](self.judicial_officer, case_to_load)
        dialog.exec()
        # except AttributeError:
        #     print(AttributeError)
        #     message = QMessageBox()
        #     message.setIcon(QMessageBox.Warning)
        #     message.setWindowTitle("Required")
        #     message.setText("You must select a judicial officer.")
        #     message.setStandardButtons(QMessageBox.Ok)
        #     message.exec()

    @logger.catch
    def get_case_to_load(self):
        """This calls the database_statutes and behind the scenes sets the appropriate case type
        for each charge. It does not show up in the view, but is used for calculating costs."""
        key = self.statute_choice_box.currentText()
        if self.freeform_entry_checkBox.isChecked():
            return None
        query = QSqlQuery(database_statutes)
        query.prepare("SELECT * FROM charges WHERE " "statute LIKE '%' || :key || '%'")
        query.bindValue(":key", key)
        query.exec()
        while query.next():
            statute = query.value(2)
            offense_type = query.value(4)
            if statute == key:
                return offense_type


@logger.catch
def main():
    """The main loop of the application. A logger is wrapped on the function
    but needs to be set up to properly log error files. It won't catch all
    errors from the application, only those causing a main loop error."""
    app = QApplication(sys.argv)
    arraignment_list = create_database_connections()
    #arraignment_list.open()
    win = Window(arraignment_list)
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
