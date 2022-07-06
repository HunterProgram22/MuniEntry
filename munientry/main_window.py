"""Module containing the Main Window of the application."""
from __future__ import annotations

import os
import random
from datetime import datetime
from typing import Type

from loguru import logger
from PyQt5 import QtGui
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QComboBox, QDialog, QMainWindow, QShortcut

from munientry.builders import bond_dialogs as bond
from munientry.builders import general_entry_dialogs as general_entry
from munientry.builders import plea_only_dialogs as plea_only
from munientry.builders import plea_sentence_dialogs as plea_sentence
from munientry.builders import sentencing_only_dialogs as sentencing_only
from munientry.builders.final_jury_hearing_notice_dialog import (
    FinalJuryNoticeOfHearingDialog,
)
from munientry.builders.general_hearing_notice_dialog import (
    GeneralNoticeOfHearingDialog,
)
from munientry.builders.sched_entry_dialogs import SchedulingEntryDialog
from munientry.builders.trial_to_court_hearing_notice_dialog import (
    TrialToCourtHearingDialog,
)
from munientry.data.databases import (
    CriminalCaseSQLRetriever,
    close_db_connection,
    create_daily_case_list_sql_tables,
    load_daily_case_list_data,
    open_db_connection,
    query_daily_case_list_data,
)
from munientry.models.cms_models import CmsCaseInformation
from munientry.models.party_types import JudicialOfficer
from munientry.settings import ICON_PATH, LOG_PATH, USER_LOG_NAME, VERSION_NUMBER
from munientry.views.custom_widgets import RequiredBox
from munientry.views.main_window_ui import Ui_MainWindow


# InfoChecker Wrappers
def check_judicial_officer(func):
    """Prohibits opening a dialog unless a judicial officer is selected."""
    def wrapper(self):
        if self.judicial_officer is None:
            RequiredBox('You must select a judicial officer.', 'Judicial Officer Required').exec()
        else:
            func(self)

    return wrapper


def check_case_list_selected(func):
    """Probhitis opening a dialog unless a daily case list is selected."""
    def wrapper(self):
        if any(key.isChecked() for key in self.daily_case_list_buttons_dict.keys()):
            func(self)
        else:
            RequiredBox(
                'You must select a case list. If not loading a case in the case list '
                'leave the case list field blank.', 'Daily Case List Required',
            ).exec()

    return wrapper


class MainWindow(QMainWindow, Ui_MainWindow):
    """The main window of the application that is the launching point for all dialogs."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.modify_view()
        self.create_dialog_slot_functions()
        self.connect_signals_to_slots()
        self.connect_menu_functions()
        self.functions.load_case_lists()
        self.functions.show_hide_daily_case_lists()
        self.judicial_officer: JudicialOfficer = None
        self.case_table: str = 'None'
        self.dialog: Type[QDialog] = QDialog


    def modify_view(self) -> MainWindowViewModifier:
        return MainWindowViewModifier(self)

    def connect_menu_functions(self) -> None:
        self.log_shortcut = QShortcut(QKeySequence('Ctrl+L'), self)
        self.log_shortcut.activated.connect(self.open_current_log)
        self.actionOpen_Current_Log.triggered.connect(self.open_current_log)

    def open_current_log(self, s=None) -> None:
        os.startfile(f'{LOG_PATH}{USER_LOG_NAME}')

    def create_dialog_slot_functions(self) -> None:
        self.functions = MainWindowSlotFunctions(self)

    def connect_signals_to_slots(self) -> MainWindowSignalConnector:
        return MainWindowSignalConnector(self)

    def set_selected_case_list_table(self) -> None:
        self.case_table = self.daily_case_list_buttons_dict.get(self.sender(), 'None')

    def update_judicial_officer(self) -> None:
        self.judicial_officer = self.judicial_officer_buttons_dict.get(self.sender())

    def set_case_to_load(self, selected_case_table: QComboBox) -> CmsCaseInformation:
        """Returns an empty CmsCaseInformation object if no case is selected.

        Otherwise returns a CmsCaseInformation object via CriminalCaseSQLRetriever().load_case()
        that contains all data from the Cms daily case list reports.
        """
        if selected_case_table.currentText() == '':
            return CmsCaseInformation()
        case_number = selected_case_table.currentText().split('- ')[1]
        return CriminalCaseSQLRetriever(case_number, self.case_table).load_case()

    @check_judicial_officer
    @check_case_list_selected
    def start_dialog_from_entry_button(self) -> None:
        """The decorator checks prevent the dialog execution unless compliant.

        :check_judicial_officer: Requires that a judicial officer is selected.

        'check_case_list_selected: Requires that a daily case list is selected, if no case
        is needed then must select a case list with the field blank.
        """
        selected_case_table = self.database_table_dict.get(self.case_table, QComboBox)
        cms_case_data = self.set_case_to_load(selected_case_table)
        self.dialog = self.dialog_buttons_dict[self.sender()](
            self.judicial_officer,
            cms_case=cms_case_data,
            case_table=self.case_table,
        )
        logger.log('DIALOG', f'{self.dialog.objectName()} Opened')
        self.dialog.exec()

    @check_case_list_selected
    def start_scheduling_entry(self) -> None:
        selected_case_table = self.database_table_dict.get(self.case_table, QComboBox)
        dialog_name = self.set_scheduling_dialog_name()
        cms_case_data = self.set_case_to_load(selected_case_table)
        self.dialog = SchedulingEntryDialog(
            dialog_name=dialog_name,
            cms_case=cms_case_data,
            case_table=self.case_table,
        )
        logger.log('DIALOG', f'{self.dialog.objectName()} Opened')
        self.dialog.exec()

    def set_scheduling_dialog_name(self) -> str:
        if self.sender().objectName() == 'rohrer_schedulingEntryButton':
            return 'Rohrer Scheduling Entry'
        if self.sender().objectName() == 'hemmeter_schedulingEntryButton':
            return 'Hemmeter Scheduling Entry'
        return 'None'

    def assign_judge(self):
        judge_list = ['Judge Hemmeter', 'Judge Rohrer']
        assigned_judge = random.choice(judge_list)
        now = datetime.now()
        now = now.strftime('%B %d, %Y at %H:%M:%S %p')
        self.assign_judge_label.setText(assigned_judge)
        self.last_judge_assigned_label.setText(f'The last judge assigned was {assigned_judge} at {now}')


class MainWindowViewModifier(object):
    """Class that modifies the view file."""

    def __init__(self, main_window: MainWindow) -> None:
        self.main_window = main_window
        self.main_window.setupUi(self.main_window)
        self.main_window.setWindowIcon(QtGui.QIcon(f'{ICON_PATH}gavel.ico'))
        self.main_window.setWindowTitle(f'MuniEntry - Version {VERSION_NUMBER}')
        self.create_main_window_dicts()

    def create_main_window_dicts(self) -> None:
        self.main_window.judicial_officer_buttons_dict = {
            self.main_window.bunner_radioButton: JudicialOfficer('Amanda', 'Bunner', 'Magistrate'),
            self.main_window.pelanda_radioButton: JudicialOfficer('Kevin', 'Pelanda', 'Magistrate'),
            self.main_window.kudela_radioButton: JudicialOfficer('Justin', 'Kudela', 'Magistrate'),
            self.main_window.rohrer_radioButton: JudicialOfficer('Kyle', 'Rohrer', 'Judge'),
            self.main_window.hemmeter_radioButton: JudicialOfficer('Marianne', 'Hemmeter', 'Judge'),
        }
        self.main_window.dialog_buttons_dict = {
            self.main_window.FineOnlyPleaButton: plea_sentence.FineOnlyPleaDialog,
            self.main_window.JailCCPleaButton: plea_sentence.JailCCPleaDialog,
            self.main_window.DiversionButton: plea_sentence.DiversionPleaDialog,
            self.main_window.NotGuiltyBondButton: plea_only.NotGuiltyBondDialog,
            self.main_window.FailureToAppearButton: general_entry.FailureToAppearDialog,
            self.main_window.ProbationViolationBondButton: bond.ProbationViolationBondDialog,
            self.main_window.BondHearingButton: bond.BondHearingDialog,
            self.main_window.PleaOnlyButton: plea_only.PleaOnlyDialog,
            self.main_window.NoPleaBondButton: bond.NoPleaBondDialog,
            self.main_window.LeapAdmissionButton: plea_only.LeapAdmissionPleaDialog,
            self.main_window.LeapAdmissionValidButton: plea_only.LeapPleaValidDialog,
            self.main_window.LeapSentencingButton: sentencing_only.LeapSentencingDialog,
            self.main_window.TrialSentencingButton: sentencing_only.TrialSentencingDialog,
            self.main_window.SentencingOnlyButton: sentencing_only.SentencingOnlyDialog,
            self.main_window.FreeformEntryButton: general_entry.FreeformDialog,
            self.main_window.final_jury_hearingEntryButton: FinalJuryNoticeOfHearingDialog,
            self.main_window.general_hearingEntryButton: GeneralNoticeOfHearingDialog,
            self.main_window.trial_to_court_hearingEntryButton: TrialToCourtHearingDialog,
        }
        self.main_window.daily_case_list_buttons_dict = {
            self.main_window.arraignments_radioButton: 'arraignments',
            self.main_window.slated_radioButton: 'slated',
            self.main_window.final_pretrial_radioButton: 'final_pretrials',
            self.main_window.pleas_radioButton: 'pleas',
            self.main_window.trials_to_court_radioButton: 'trials_to_court',
            self.main_window.pcvh_fcvh_radioButton: 'pcvh_fcvh',
        }
        self.main_window.database_table_dict = {
            'arraignments': self.main_window.arraignments_cases_box,
            'slated': self.main_window.slated_cases_box,
            'final_pretrials': self.main_window.final_pretrial_cases_box,
            'pleas': self.main_window.pleas_cases_box,
            'trials_to_court': self.main_window.trials_to_court_cases_box,
            'pcvh_fcvh': self.main_window.pcvh_fcvh_cases_box,
        }
        self.main_window.radio_buttons_case_lists_dict = {
            self.main_window.arraignments_radioButton: self.main_window.arraignments_cases_box,
            self.main_window.slated_radioButton: self.main_window.slated_cases_box,
            self.main_window.final_pretrial_radioButton: self.main_window.final_pretrial_cases_box,
            self.main_window.pleas_radioButton: self.main_window.pleas_cases_box,
            self.main_window.trials_to_court_radioButton:
                self.main_window.trials_to_court_cases_box,
            self.main_window.pcvh_fcvh_radioButton: self.main_window.pcvh_fcvh_cases_box,
        }


class MainWindowSignalConnector(object):
    """Class for connecting signals to slots of the Main Window."""

    def __init__(self, main_window: MainWindow) -> None:
        self.main_window = main_window
        self.main_window.reload_cases_Button.released.connect(
            self.main_window.functions.reload_case_lists,
        )
        self.main_window.rohrer_schedulingEntryButton.released.connect(
            self.main_window.start_scheduling_entry,
        )
        self.main_window.hemmeter_schedulingEntryButton.released.connect(
            self.main_window.start_scheduling_entry,
        )
        self.main_window.random_judge_Button.released.connect(self.main_window.assign_judge)
        self.connect_case_lists_to_show_hide()
        self.connect_case_lists_to_set_selected_case_list()
        self.connect_judicial_officers_to_set_officer()
        self.connect_dialog_buttons_to_start_dialog()

    def connect_case_lists_to_show_hide(self) -> None:
        for key in self.main_window.radio_buttons_case_lists_dict:
            key.toggled.connect(self.main_window.functions.show_hide_daily_case_lists)

    def connect_case_lists_to_set_selected_case_list(self) -> None:
        for key in self.main_window.daily_case_list_buttons_dict:
            key.clicked.connect(self.main_window.set_selected_case_list_table)

    def connect_judicial_officers_to_set_officer(self) -> None:
        for key in self.main_window.judicial_officer_buttons_dict:
            key.clicked.connect(self.main_window.update_judicial_officer)

    def connect_dialog_buttons_to_start_dialog(self) -> None:
        for key in self.main_window.dialog_buttons_dict:
            key.pressed.connect(self.main_window.start_dialog_from_entry_button)


class MainWindowSlotFunctions(object):
    """Class that contains common functions for the main window."""

    def __init__(self, main_window: MainWindow) -> None:
        self.main_window = main_window

    def load_case_lists(self, db_connection: QSqlDatabase = None) -> None:
        """Loads the cms_case numbers of all the cases that are in the daily_case_list databases.

        This does not load the cms_case data for each cms_case.

        The case count is one less than length of list because a blank line is inserted at the
        top of the case list. The case count becomes actual number of cases loaded.
        """
        if db_connection is None:
            db_connection = open_db_connection('con_daily_case_lists')
        for table_name, case_list in self.main_window.database_table_dict.items():
            old_case_count = 0 if len(case_list) == 0 else len(case_list)- 1
            case_list.clear()
            case_list.addItems(query_daily_case_list_data(table_name, db_connection))
            case_count = len(case_list) - 1
            logger.info(f'Table: {table_name} - Preload Cases: {old_case_count}; Postload Cases {case_count}')
        close_db_connection(db_connection)

    def reload_case_lists(self) -> None:
        """This method is connected to the reload cases button only.

        The databases are only recreated on reload since the initial load of the
        application already loads the databases.
        """
        logger.info('Reload cases button pressed.')
        conn = open_db_connection('con_daily_case_lists')
        create_daily_case_list_sql_tables(conn)
        load_daily_case_list_data(conn)
        self.main_window.functions.load_case_lists(conn)
        conn.close()

    def show_hide_daily_case_lists(self) -> None:
        selected_case_list = self.main_window.radio_buttons_case_lists_dict.get(
            self.main_window.sender(),
        )
        for case_list in self.main_window.radio_buttons_case_lists_dict.values():
            if case_list == selected_case_list:
                case_list.setEnabled(True)
                case_list.setHidden(False)
                case_list.setFocus()
            else:
                case_list.setCurrentText('')
                case_list.setHidden(True)
                case_list.setEnabled(False)
