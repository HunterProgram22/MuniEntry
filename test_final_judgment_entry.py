import pytest
from time import sleep
from pytestqt.plugin import QtBot
from PyQt5 import QtCore

import MuniEntry_app
from Dialogs.CriminalDialogs import CaseInformationDialog, SentencingDialog

"""Functions for Testing"""


def add_case_information(screen):
    QtBot.keyClicks(screen.case_number, "21TRC1234")
    QtBot.keyClicks(screen.defendant_name, "John Smith")
    QtBot.keyClicks(screen.defendant_attorney_name, "Robert Shapiro")


def press_continue_button(screen, nextDialog):
    QtBot.mouseClick(screen.pushButton, QtCore.Qt.LeftButton)
    next_screen = nextDialog(screen.case_information)
    return next_screen


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
    screen = CaseInformationDialog()
    qtbot.addWidget(screen)
    add_case_information(screen)
    assert screen.case_number.text() == "21TRC1234"
    assert screen.defendant_name.text() == "John Smith"
    assert screen.defendant_attorney_name.text() == "Robert Shapiro"
    screen.close()
    next_screen = press_continue_button(screen, SentencingDialog)
    assert next_screen.case_number_label.text() == "21TRC1234"
    assert next_screen.defendant_name_label.text() == "John Smith"
    assert (
        next_screen.defendant_attorney_name_label.text() == "Attorney: Robert Shapiro"
    )


# def test_main_window(qtbot):
#   widget = MainWindow()
#   qtbot.addWidget(widget)
#   qtbot.mouseClick(widget.about_button, QtCore.Qt.LeftButton)
#   qtbot.waitUntil(widget.about_box.isVisible)
#   assert widget.about_box.text() == 'This is a GUI App'
