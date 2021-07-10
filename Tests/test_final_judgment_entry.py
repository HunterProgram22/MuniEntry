import pytest

import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import MuniEntry_app

from time import sleep
from pytestqt.plugin import QtBot
from PyQt5 import QtCore

from Dialogs.CriminalDialogs import (
    CaseInformationDialog,
    SentencingDialog,
    OviDialog,
    AbilityToPayDialog,
    CommunityControlDialog,
)

"""Functions for Testing"""


def add_case_information(screen):
    QtBot.keyClicks(screen.case_number, "21TRC1234")
    QtBot.keyClicks(screen.defendant_name, "John Smith")
    QtBot.keyClicks(screen.defendant_attorney_name, "Robert Shapiro")

def add_offense(screen):
    QtBot.keyClicks(screen.offense_choice_box, "Failure to Control - R.C. 4511.202")
    QtBot.keyClicks(screen.degree_choice_box, "MM")
    QtBot.keyClicks(screen.plea_choice_box, "No Contest")
    QtBot.keyClicks(screen.finding_choice_box, "Guilty")
    QtBot.keyClicks(screen.fines_amount, "250.00")
    QtBot.keyClicks(screen.fines_suspended, "125.00")
    QtBot.keyClicks(screen.jail_days, "180")
    QtBot.keyClicks(screen.jail_days_suspended, "175")
    QtBot.mouseClick(screen.addOffenseButton, QtCore.Qt.LeftButton)

def add_ovi_details(screen):
    QtBot.keyClicks(screen.ovi_offenses_within_ten_years_box, "2")
    QtBot.mouseClick(screen.high_bac_test_checkbox, QtCore.Qt.LeftButton)
    QtBot.mouseClick(screen.refused_breathylizer_checkbox, QtCore.Qt.LeftButton)
    QtBot.keyClicks(screen.ovi_offenses_within_twenty_years_box, "5")

def check_banner(screen):
    assert screen.case_number_label.text() == "21TRC1234"
    assert screen.defendant_name_label.text() == "John Smith"
    assert screen.defendant_attorney_name_label.text() == "Attorney: Robert Shapiro"

def press_continue_button(screen, nextDialog):
    QtBot.mouseClick(screen.continueButton, QtCore.Qt.LeftButton)
    next_screen = nextDialog(screen.case_information)
    return next_screen

def start_dialog(qtbot):
    screen = CaseInformationDialog()
    qtbot.addWidget(screen)
    add_case_information(screen)
    return screen

@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window()
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app


"""TESTING"""
def test_title(app):
    assert app.windowTitle() == "MuniEntry"


def test_final_judgment_buton(app):
    QtBot.mouseClick(app.FinalJudgmentEntryButton, QtCore.Qt.LeftButton)


def test_case_information_dialog(qtbot):
    screen = start_dialog(qtbot)
    assert screen.case_number.text() == "21TRC1234"
    assert screen.defendant_name.text() == "John Smith"
    assert screen.defendant_attorney_name.text() == "Robert Shapiro"


def test_ovi_dialog(qtbot):
    screen = start_dialog(qtbot)
    QtBot.mouseClick(screen.ovi_checkbox, QtCore.Qt.LeftButton)
    next_screen = press_continue_button(screen, OviDialog)
    assert next_screen.windowTitle() == "Operating a Vehicle Impaired"
    check_banner(next_screen)
    third_screen = press_continue_button(next_screen, SentencingDialog)
    assert third_screen.windowTitle() == "Sentencing"
    check_banner(third_screen)


def test_ovi_details(qtbot):
    """This test also passes but is again throwing a windows fatal exception code
    0xe0000002. Need to see what is causing this code. Same code as for test_add_offense."""
    screen = start_dialog(qtbot)
    QtBot.mouseClick(screen.ovi_checkbox, QtCore.Qt.LeftButton)
    next_screen = press_continue_button(screen, OviDialog)
    add_ovi_details(next_screen)
    third_screen = press_continue_button(next_screen, SentencingDialog)
    fourth_screen = press_continue_button(third_screen, AbilityToPayDialog)
    fifth_screen = press_continue_button(fourth_screen, CommunityControlDialog)
    QtBot.mouseClick(fifth_screen.createEntryButton, QtCore.Qt.LeftButton)


def test_sentencing_dialog(qtbot):
    screen = start_dialog(qtbot)
    next_screen = press_continue_button(screen, SentencingDialog)
    check_banner(next_screen)


def test_ability_to_pay_dialog(qtbot):
    screen = start_dialog(qtbot)
    next_screen = press_continue_button(screen, SentencingDialog)
    third_screen = press_continue_button(next_screen, AbilityToPayDialog)
    assert third_screen.windowTitle() == "Ability To Pay"
    check_banner(third_screen)


def test_community_control_dialog(qtbot):
    screen = start_dialog(qtbot)
    next_screen = press_continue_button(screen, SentencingDialog)
    third_screen = press_continue_button(next_screen, AbilityToPayDialog)
    fourth_screen = press_continue_button(third_screen, CommunityControlDialog)
    assert fourth_screen.windowTitle() == "Community Control"
    check_banner(fourth_screen)


def test_add_offense(qtbot):
    """This test passes but is throwing a windows fatal exception code
    0xe0000002. Need to see what is causing this code."""
    screen = start_dialog(qtbot)
    next_screen = press_continue_button(screen, SentencingDialog)
    add_offense(next_screen)
    assert next_screen.windowTitle() =="Sentencing"
    assert next_screen.offense_choice_box.currentText() == ""
    third_screen = press_continue_button(next_screen, AbilityToPayDialog)
    QtBot.mouseClick(third_screen.createEntryButton, QtCore.Qt.LeftButton)
