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
)

"""Functions for Testing"""


def add_case_information(screen):
    QtBot.keyClicks(screen.case_number, "21TRC1234")
    QtBot.keyClicks(screen.defendant_name, "John Smith")
    QtBot.keyClicks(screen.defendant_attorney_name, "Robert Shapiro")


def check_banner(screen):
    assert screen.case_number_label.text() == "21TRC1234"
    assert screen.defendant_name_label.text() == "John Smith"
    assert screen.defendant_attorney_name_label.text() == "Attorney: Robert Shapiro"


def press_continue_button(screen, nextDialog):
    QtBot.mouseClick(screen.continueButton, QtCore.Qt.LeftButton)
    return nextDialog(screen.case_information)


def start_dialog(qtbot):
    screen = CaseInformationDialog()
    qtbot.addWidget(screen)
    add_case_information(screen)
    return screen


"""TESTING"""


@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window()
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app


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


# def test_sentencing_dialog_add_offense(qtbot):
# screen = start_dialog(qtbot)
# next_screen = press_continue_button(screen, SentencingDialog)
# QtBot.keyClicks()


# def test_main_window(qtbot):
#   widget = MainWindow()
#   qtbot.addWidget(widget)
#   qtbot.mouseClick(widget.about_button, QtCore.Qt.LeftButton)
#   qtbot.waitUntil(widget.about_box.isVisible)
#   assert widget.about_box.text() == 'This is a GUI App'
