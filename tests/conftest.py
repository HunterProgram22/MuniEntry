import os
import sys
import inspect

import pytest
from pytestqt.plugin import QtBot
from PyQt6.QtSql import QSqlDatabase
from PyQt6 import QtCore
from PyQt6.QtCore import QTimer

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from munientry import logging_module
from munientry.mainwindow.main_window import MainWindow
from munientry.entrycreators.entry_creator import CrimTrafficEntryCreator

CLOSE_TIMER = 50

"""
INSTRUCTIONS:

Use pytest -m 'not manual' to skip tests that require manual interaction
Use pytest -m 'not create_entry_test' to skip tests that open actual Word docx files

"""


@pytest.fixture
def mock_entry(monkeypatch):
    def mock_create_entry(self):
        return "Entry Created"
    monkeypatch.setattr(CrimTrafficEntryCreator, 'create_entry', mock_create_entry)


def open_daily_case_list_db_connection():
    return QSqlDatabase.database("con_daily_case_lists", open=True)

def enter_data(field, data: str):
    return QtBot.keyClicks(field, data)

def mouse_click(button):
    return QtBot.mouseClick(button, QtCore.Qt.MouseButton.LeftButton)

def key_click(field, key):
    return QtBot.keyClick(field, key)

def right_click(button):
    return QtBot.mouseClick(button, QtCore.Qt.MouseButton.RightButton)


@pytest.fixture
def main_window(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)

    def close_main_dialog():
        qtbot.addWidget(window.dialog)
        mouse_click(window.dialog.close_dialog_Button)

    QTimer.singleShot(50, close_main_dialog)
    return window


@pytest.fixture
def main_window_noclose(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    return window


@pytest.fixture
def driving_priv_dialog(qtbot, main_window):
    """Driving Privileges Dialog is driving_priv_dialog."""
    mouse_click(main_window.assn_comm_patterson_radioButton)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    enter_data(main_window.case_search_box, '22TRD01955')
    mouse_click(main_window.get_case_Button)
    mouse_click(main_window.limited_driving_privilegesButton)
    qtbot.addWidget(main_window.dialog)
    return main_window.dialog


@pytest.fixture
def hemmeter_gen_hearing_notice_dialog(qtbot, main_window):
    """Hemmeter General Notice of Hearing dialog."""
    mouse_click(main_window.patterson_radioButton)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    enter_data(main_window.case_search_box, '22TRD01955')
    mouse_click(main_window.get_case_Button)
    mouse_click(main_window.hemmeter_general_hearingButton)
    qtbot.addWidget(main_window.dialog)
    return main_window.dialog


@pytest.fixture
def rohrer_gen_hearing_notice_dialog(qtbot, main_window):
    """Rohrer General Notice of Hearing dialog."""
    mouse_click(main_window.dattilo_radioButton)
    main_window.search_tabWidget.setCurrentWidget(main_window.case_search_tab)
    enter_data(main_window.case_search_box, '22TRD01955')
    mouse_click(main_window.get_case_Button)
    mouse_click(main_window.rohrer_general_hearingButton)
    qtbot.addWidget(main_window.dialog)
    return main_window.dialog


@pytest.fixture
def diversion_dialog(qtbot, main_window):
    """Diversion Plea Dialog is diversion_dialog"""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.DiversionButton)
    qtbot.addWidget(main_window.dialog)
    return main_window.dialog


@pytest.fixture
def add_charge_dialog(qtbot, main_window):
    """Add Charge Dialog fixture."""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.JailCCPleaButton)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_charge_Button)

    QTimer.singleShot(50, close_popup_dialog)
    mouse_click(main_window.dialog.add_charge_Button)
    return main_window.dialog.popup_dialog


@pytest.fixture
def conditions_dialog(qtbot, main_window):
    """This is the fixture for the add conditions dialog on the the Fine Only main dialog."""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.FineOnlyPleaButton)
    mouse_click(main_window.dialog.license_suspension_checkBox)
    mouse_click(main_window.dialog.other_conditions_checkBox)
    mouse_click(main_window.dialog.community_service_checkBox)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(50, close_popup_dialog)
    mouse_click(main_window.dialog.add_conditions_Button)
    return main_window.dialog.popup_dialog


@pytest.fixture
def special_conditions_dialog(qtbot, main_window):
    """Fixture for the Add Special Bond Conditions dialog on the Not Guilty Bond main dialog."""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.arraignments_radioButton)
    mouse_click(main_window.NotGuiltyBondButton)
    mouse_click(main_window.dialog.domestic_violence_checkBox)
    mouse_click(main_window.dialog.admin_license_suspension_checkBox)
    mouse_click(main_window.dialog.custodial_supervision_checkBox)
    mouse_click(main_window.dialog.vehicle_seizure_checkBox)
    mouse_click(main_window.dialog.no_contact_checkBox)
    mouse_click(main_window.dialog.other_conditions_checkBox)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(50, close_popup_dialog)
    mouse_click(main_window.dialog.add_special_conditions_Button)
    return main_window.dialog.popup_dialog


@pytest.fixture
def ngb_dialog(qtbot, main_window):
    mouse_click(main_window.pelanda_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.NotGuiltyBondButton)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(50, close_popup_dialog)
    return main_window.dialog


@pytest.fixture
def fop_dialog(qtbot, main_window):
    mouse_click(main_window.pelanda_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.FineOnlyPleaButton)
    mouse_click(main_window.dialog.no_contest_all_Button)
    enter_data(main_window.dialog.fra_in_court_box, "Yes")

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(50, close_popup_dialog)
    return main_window.dialog


@pytest.fixture
def jcp_dialog(qtbot, main_window):
    mouse_click(main_window.bunner_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.JailCCPleaButton)
    mouse_click(main_window.dialog.no_contest_all_Button)
    enter_data(main_window.dialog.fra_in_court_box, "Yes")

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(50, close_popup_dialog)
    return main_window.dialog


@pytest.fixture
def sentencing_only_dialog(qtbot, main_window):
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.pleas_radioButton)
    enter_data(main_window.pleas_cases_box, "Barkschat - 21TRC05611")
    mouse_click(main_window.SentencingOnlyButton)
    mouse_click(main_window.dialog.guilty_all_Button)
    enter_data(main_window.dialog.fra_in_court_box, "Yes")

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(50, close_popup_dialog)
    return main_window.dialog


@pytest.fixture
def com_control_dialog(qtbot, main_window):
    """Add Community Control for Jail CC Plea Dialog."""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.final_pretrial_radioButton)
    mouse_click(main_window.JailCCPleaButton)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(50, close_popup_dialog)
    mouse_click(main_window.dialog.add_conditions_Button)
    return main_window.dialog.popup_dialog


@pytest.fixture
def com_control_dialog_com_control_conditions(qtbot, main_window):
    """Add Community Control is comcontrol_dialog. Uses the Jail Dialog
    as the main dialog because that is required."""
    mouse_click(main_window.hemmeter_radioButton)
    mouse_click(main_window.final_pretrial_radioButton)
    mouse_click(main_window.JailCCPleaButton)
    mouse_click(main_window.dialog.community_control_checkBox)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.add_conditions_Button)

    QTimer.singleShot(50, close_popup_dialog)
    mouse_click(main_window.dialog.add_conditions_Button)
    return main_window.dialog.popup_dialog


def check_barkschat(charges, plea):
    assert charges[0].offense == "OVI Alcohol / Drugs 3rd"
    assert charges[0].statute == "4511.19A1A"
    assert charges[0].degree == "UCM"
    assert charges[0].plea == plea
    assert charges[1].offense == "OVI Refusal 3rd/10yr Prior 20yr"
    assert charges[1].statute == "4511.19A2"
    assert charges[1].degree == "UCM"
    assert charges[1].plea == plea
    assert charges[2].offense == "Driving in Marked Lanes"
    assert charges[2].statute == "4511.33"
    assert charges[2].degree == "MM"
    assert charges[2].plea == plea


@pytest.fixture
def amend_charge_dialog(qtbot, main_window):
    """Amend Charge Dialog is amend_charge_dialog. Uses the Jail dialog as that
    is the most common."""
    mouse_click(main_window.rohrer_radioButton)
    mouse_click(main_window.final_pretrial_radioButton)
    enter_data(main_window.final_pretrial_cases_box, 'Barkschat - 21TRC05611')
    mouse_click(main_window.JailCCPleaButton)

    def close_popup_dialog():
        qtbot.addWidget(main_window.dialog.popup_dialog)
        mouse_click(main_window.dialog.popup_dialog.amend_charge_Button)

    QTimer.singleShot(100, close_popup_dialog)
    amend_button = main_window.dialog.charges_gridLayout.itemAtPosition(11, 2).widget()
    mouse_click(amend_button)
    return main_window.dialog.popup_dialog


CRIMTRAFFIC_ALL_DIALOG_BUTTONS = [
    ('JailCCPleaButton'),
    ('FineOnlyPleaButton'),
    ('DiversionButton'),
    ('NotGuiltyBondButton'),
    ('PleaOnlyButton'),
    ('NoPleaBondButton'),
    ('BondHearingButton'),
    ('ProbationViolationBondButton'),
    ('LeapAdmissionButton'),
    ('LeapAdmissionValidButton'),
    ('LeapSentencingButton'),
    ('TrialSentencingButton'),
    ('SentencingOnlyButton'),
    ('FailureToAppearButton'),
    ('FreeformEntryButton'),
    ('ArraignmentContinueButton'),
]

CRIMTRAFFIC_CHARGE_DIALOG_BUTTONS = [
    ('JailCCPleaButton'),
    ('FineOnlyPleaButton'),
    ('DiversionButton'),
    ('NotGuiltyBondButton'),
    ('PleaOnlyButton'),
    ('LeapAdmissionButton'),
    ('LeapAdmissionValidButton'),
    ('LeapSentencingButton'),
    ('TrialSentencingButton'),
    ('SentencingOnlyButton'),
]

CRIMTRAFFIC_FRA_DIALOG_BUTTONS = [
    ('JailCCPleaButton'),
    ('FineOnlyPleaButton'),
    ('DiversionButton'),
    ('LeapSentencingButton'),
    ('TrialSentencingButton'),
    ('SentencingOnlyButton'),
]

SCHEDULING_ALL_DIALOG_BUTTONS = [
    ('hemmeter_final_jury_hearingButton'),
    ('rohrer_final_jury_hearingButton'),
    ('hemmeter_general_hearingButton'),
    ('rohrer_general_hearingButton'),
    ('hemmeter_trial_court_hearingButton'),
    ('rohrer_trial_court_hearingButton'),
    ('rohrer_schedulingEntryButton'),
    ('hemmeter_schedulingEntryButton'),
]

