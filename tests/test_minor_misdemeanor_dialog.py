import pytest
import os, sys, inspect
from time import sleep
from datetime import date, timedelta

from pytestqt.plugin import QtBot
from PyQt5 import QtCore

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import MuniEntry_app
from controllers.CriminalDialogs import (
    CaseInformationDialog,
    AmendOffenseDialog,
)
from controllers.MinorMisdemeanorDialogs import (
    MinorMisdemeanorDialog,
)

TODAY = date.today()

"""Functions for Testing"""
def add_case_information(dialog):
    QtBot.keyClicks(dialog.case_number_lineEdit, "21TRC1234")
    QtBot.keyClicks(dialog.defendant_first_name_lineEdit, "John")
    QtBot.keyClicks(dialog.defendant_last_name_lineEdit, "Smith")

def start_minor_misdemeanor_dialog(qtbot, judicial_officer):
    dialog = MinorMisdemeanorDialog(judicial_officer)
    qtbot.addWidget(dialog)
    add_case_information(dialog)
    return dialog

def start_amendment_dialog(qtbot):
    dialog = AmendOffenseDialog()
    qtbot.addWidget(dialog)
    return dialog

def add_offense_speeding_25(dialog):
    dialog.offense_choice_box.setCurrentText("Speeding > 25 mph")
    dialog.plea_choice_box.setCurrentText("Not Guilty")
    dialog.finding_choice_box.setCurrentText("Guilty")
    dialog.fines_amount.setText("50")
    dialog.fines_suspended.setText("25")
    QtBot.mouseClick(dialog.addChargeButton, QtCore.Qt.LeftButton)

@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window()
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app

@pytest.fixture
def dialog(app, qtbot):
    QtBot.mouseClick(app.MinorMisdemeanorTrafficButton, QtCore.Qt.LeftButton)
    dialog = start_minor_misdemeanor_dialog(qtbot, app.judicial_officer)
    return dialog

"""TESTING"""
"""Two columns are added every time a charge is added with add offense to view.
The columns with content are evens (0, 2, 4, etc)."""

def test_open_minor_misdemeanor_dialog(app, dialog):
    assert dialog.windowTitle() == "Minor Misdemeanor Case Information"

def test_case_information_dialog(app, dialog):
    assert dialog.case_number_lineEdit.text() == "21TRC1234"
    assert dialog.defendant_first_name_lineEdit.text() == "John"
    assert dialog.defendant_last_name_lineEdit.text() == "Smith"

def test_offense_to_statute(app, dialog):
    dialog.offense_choice_box.setCurrentText("Speeding > 25 mph")
    assert dialog.statute_choice_box.currentText() == "R.C. 4511.21(B)(2)"
    assert dialog.degree_choice_box.currentText() == "MM"
    dialog.offense_choice_box.setCurrentText("Driving Under Suspension")
    assert dialog.statute_choice_box.currentText() == "R.C. 4510.11"
    assert dialog.degree_choice_box.currentText() == "M1"

def test_statute_to_offense(app, dialog):
    dialog.statute_choice_box.setCurrentText("R.C. 4511.21(B)(3)")
    assert dialog.offense_choice_box.currentText() == "Speeding > 35 mph"
    assert dialog.degree_choice_box.currentText() == "MM"
    dialog.statute_choice_box.setCurrentText("R.C. 4511.33")
    assert dialog.offense_choice_box.currentText() == "Driving in Marked Lanes"
    assert dialog.degree_choice_box.currentText() == "MM"

def test_add_offense(app, dialog):
    add_offense_speeding_25(dialog)
    assert dialog.charges_gridLayout.itemAtPosition(0, 2).widget().text() == "Speeding > 25 mph"
    assert dialog.charges_gridLayout.itemAtPosition(3, 2).widget().text() == "Not Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(4, 2).widget().text() == "Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(5, 2).widget().text() == "50"
    assert dialog.charges_gridLayout.itemAtPosition(6, 2).widget().text() == "25"

def test_add_multiple_offenses(app, dialog):
    add_offense_speeding_25(dialog)
    assert dialog.charges_gridLayout.itemAtPosition(0, 2).widget().text() == "Speeding > 25 mph"
    assert dialog.charges_gridLayout.itemAtPosition(3, 2).widget().text() == "Not Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(4, 2).widget().text() == "Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(5, 2).widget().text() == "50"
    assert dialog.charges_gridLayout.itemAtPosition(6, 2).widget().text() == "25"
    # Second Charge
    dialog.offense_choice_box.setCurrentText("Driving in Marked Lanes")
    dialog.plea_choice_box.setCurrentText("Guilty")
    dialog.finding_choice_box.setCurrentText("Guilty")
    dialog.fines_amount.setText("75")
    dialog.fines_suspended.setText("0")
    QtBot.mouseClick(dialog.addChargeButton, QtCore.Qt.LeftButton)
    assert dialog.charges_gridLayout.itemAtPosition(0, 4).widget().text() == "Driving in Marked Lanes"
    assert dialog.charges_gridLayout.itemAtPosition(3, 4).widget().text() == "Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(4, 4).widget().text() == "Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(5, 4).widget().text() == "75"
    assert dialog.charges_gridLayout.itemAtPosition(6, 4).widget().text() == "0"

def test_add_offense_and_delete_offense(app, dialog):
    add_offense_speeding_25(dialog)
    QtBot.mouseClick(dialog.addChargeButton, QtCore.Qt.LeftButton)
    QtBot.mouseClick(
        dialog.charges_gridLayout.itemAtPosition(8, 2).widget(),
        QtCore.Qt.LeftButton
        )
    assert dialog.charges_gridLayout.itemAtPosition(0, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(3, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(4, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(5, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(6, 2) == None

def test_add_two_delete_one_add_one_offense(app, dialog):
    add_offense_speeding_25(dialog)
    add_offense_speeding_25(dialog)
    assert dialog.charges_gridLayout.itemAtPosition(0, 2).widget().text() == "Speeding > 25 mph"
    assert dialog.charges_gridLayout.itemAtPosition(3, 2).widget().text() == "Not Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(4, 2).widget().text() == "Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(5, 2).widget().text() == "50"
    assert dialog.charges_gridLayout.itemAtPosition(6, 2).widget().text() == "25"
    # Delete first offense and check
    QtBot.mouseClick(
        dialog.charges_gridLayout.itemAtPosition(8, 2).widget(),
        QtCore.Qt.LeftButton
        )
    assert dialog.charges_gridLayout.itemAtPosition(0, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(3, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(4, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(5, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(6, 2) == None
    # Add third offense, but two total since one deleted.
    add_offense_speeding_25(dialog)
    # Second Added check
    assert dialog.charges_gridLayout.itemAtPosition(0, 4).widget().text() == "Speeding > 25 mph"
    assert dialog.charges_gridLayout.itemAtPosition(3, 4).widget().text() == "Not Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(4, 4).widget().text() == "Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(5, 4).widget().text() == "50"
    assert dialog.charges_gridLayout.itemAtPosition(6, 4).widget().text() == "25"
    # Third added check
    assert dialog.charges_gridLayout.itemAtPosition(0, 6).widget().text() == "Speeding > 25 mph"
    assert dialog.charges_gridLayout.itemAtPosition(3, 6).widget().text() == "Not Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(4, 6).widget().text() == "Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(5, 6).widget().text() == "50"
    assert dialog.charges_gridLayout.itemAtPosition(6, 6).widget().text() == "25"

def test_fines_due_date(app, dialog):
    dialog.ability_to_pay_box.setCurrentText("forthwith")
    assert dialog.balance_due_date.date() == TODAY
    dialog.ability_to_pay_box.setCurrentText("within 30 days")
    assert dialog.balance_due_date.date() == TODAY + timedelta(days=30)
    dialog.ability_to_pay_box.setCurrentText("within 60 days")
    assert dialog.balance_due_date.date() == TODAY + timedelta(days=60)
    dialog.ability_to_pay_box.setCurrentText("within 90 days")
    assert dialog.balance_due_date.date() == TODAY + timedelta(days=90)

def test_amend_offense(dialog, qtbot):
    QtBot.mouseClick(dialog.amendOffenseButton, QtCore.Qt.LeftButton)
    dialog = start_amendment_dialog(qtbot)
    dialog.windowTitle() == "Amendment"

def test_create_entry(app, dialog):
    """TODO: Add offenses to populate entry."""
    QtBot.mouseClick(dialog.createEntryButton, QtCore.Qt.LeftButton)
