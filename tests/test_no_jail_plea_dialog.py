import pytest
import os
import sys
import inspect
from time import sleep
from datetime import date, timedelta

from pytestqt.plugin import QtBot
from PyQt5 import QtCore

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import MuniEntry_app
from models.case_information import CaseLoadData
from controllers.no_jail_plea_dialogs import (
    NoJailPleaDialog,
    AmendOffenseDialog,
)
from controllers.conditions_dialogs import AddConditionsDialog
from settings import create_arraignments_database_connection

TODAY = date.today()
arraignments_database = create_arraignments_database_connection()


"""Functions for Testing"""
def add_case_information(dialog):
    QtBot.keyClicks(dialog.case_number_lineEdit, "21TRC1234")
    QtBot.keyClicks(dialog.defendant_first_name_lineEdit, "John")
    QtBot.keyClicks(dialog.defendant_last_name_lineEdit, "Smith")


def start_no_jail_plea_dialog(qtbot, judicial_officer, case):
    dialog = NoJailPleaDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    add_case_information(dialog)
    return dialog


def start_amendment_dialog(qtbot, case_information):
    dialog = AmendOffenseDialog(case_information)
    qtbot.addWidget(dialog)
    return dialog


def start_add_conditions_dialog(qtbot, case_information):
    dialog = AddConditionsDialog(case_information)
    qtbot.addWidget(dialog)
    return dialog


def add_offense_speeding_25(dialog):
    """The numbers in itemAtPosition need to be changed when ui is updated."""
    dialog.offense_choice_box.setCurrentText("Speeding > 25 mph")
    QtBot.mouseClick(dialog.add_charge_Button, QtCore.Qt.LeftButton)
    dialog.charges_gridLayout.itemAtPosition(4, 2).widget().setCurrentText("Not Guilty")
    dialog.charges_gridLayout.itemAtPosition(5, 2).widget().setCurrentText("Guilty")
    dialog.charges_gridLayout.itemAtPosition(6, 2).widget().setText("50")
    dialog.charges_gridLayout.itemAtPosition(7, 2).widget().setText("25")

def add_offense_speeding_25_after_delete(dialog):
    dialog.offense_choice_box.setCurrentText("Speeding > 25 mph")
    QtBot.mouseClick(dialog.add_charge_Button, QtCore.Qt.LeftButton)
    dialog.charges_gridLayout.itemAtPosition(4, 6).widget().setCurrentText("Not Guilty")
    dialog.charges_gridLayout.itemAtPosition(5, 6).widget().setCurrentText("Guilty")
    dialog.charges_gridLayout.itemAtPosition(6, 6).widget().setText("50")
    dialog.charges_gridLayout.itemAtPosition(7, 6).widget().setText("25")


@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window(arraignments_database)
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app


@pytest.fixture
def dialog(app, qtbot):
    QtBot.mouseClick(app.bunner_radioButton, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.NoJailPleaButton, QtCore.Qt.LeftButton)
    dialog = start_no_jail_plea_dialog(qtbot, app.judicial_officer, app.case_to_load)
    return dialog


"""TESTING"""
"""Two columns are added every time a charge is added with add offense to view.
The columns with content are evens (0, 2, 4, etc)."""

def test_open_no_jail_plea_dialog(app, dialog):
    assert dialog.windowTitle() == "No Jail Plea Case Information"


def test_case_information_dialog(app, dialog):
    assert dialog.case_number_lineEdit.text() == "21TRC1234"
    assert dialog.defendant_first_name_lineEdit.text() == "John"
    assert dialog.defendant_last_name_lineEdit.text() == "Smith"


def test_offense_to_statute(app, dialog):
    """This test is failing but actual functionality in app works -
    issue is with tab and autocomplete"""
    dialog.offense_choice_box.setCurrentText("Driving Under Suspension")
    assert dialog.statute_choice_box.currentText() == "4510.11"
    assert dialog.degree_choice_box.currentText() == "M1"
    dialog.offense_choice_box.setCurrentText("Speeding > 25 mph")
    assert dialog.statute_choice_box.currentText() == "4511.21(B)(2)"
    assert dialog.degree_choice_box.currentText() == "Minor Misdemeanor"


def test_statute_to_offense(app, dialog):
    dialog.statute_choice_box.setCurrentText("4511.21(B)(3)")
    assert dialog.offense_choice_box.currentText() == "Speeding > 35 mph"
    assert dialog.degree_choice_box.currentText() == "Minor Misdemeanor"
    dialog.statute_choice_box.setCurrentText("4511.33")
    assert dialog.offense_choice_box.currentText() == "Driving in Marked Lanes"
    assert dialog.degree_choice_box.currentText() == "Minor Misdemeanor"


def test_add_offense(app, dialog):
    add_offense_speeding_25(dialog)
    assert (
        dialog.charges_gridLayout.itemAtPosition(0, 2).widget().text()
        == "Speeding > 25 mph"
    )
    assert (
        dialog.charges_gridLayout.itemAtPosition(4, 2).widget().currentText() == "Not Guilty"
    )
    assert dialog.charges_gridLayout.itemAtPosition(5, 2).widget().currentText() == "Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(6, 2).widget().text() == "50"
    assert dialog.charges_gridLayout.itemAtPosition(7, 2).widget().text() == "25"


def test_add_multiple_offenses(app, dialog):
    add_offense_speeding_25(dialog)
    assert (
        dialog.charges_gridLayout.itemAtPosition(0, 2).widget().text()
        == "Speeding > 25 mph"
    )
    assert (
        dialog.charges_gridLayout.itemAtPosition(4, 2).widget().currentText() == "Not Guilty"
    )
    assert dialog.charges_gridLayout.itemAtPosition(5, 2).widget().currentText() == "Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(6, 2).widget().text() == "50"
    assert dialog.charges_gridLayout.itemAtPosition(7, 2).widget().text() == "25"
    # Second Charge
    dialog.offense_choice_box.setCurrentText("Driving in Marked Lanes")
    QtBot.mouseClick(dialog.add_charge_Button, QtCore.Qt.LeftButton)
    dialog.charges_gridLayout.itemAtPosition(4, 4).widget().setCurrentText("Guilty")
    dialog.charges_gridLayout.itemAtPosition(5, 4).widget().setCurrentText("Guilty")
    dialog.charges_gridLayout.itemAtPosition(6, 4).widget().setText("75")
    dialog.charges_gridLayout.itemAtPosition(7, 4).widget().setText("0")
    assert (
        dialog.charges_gridLayout.itemAtPosition(0, 4).widget().text()
        == "Driving in Marked Lanes"
    )
    assert dialog.charges_gridLayout.itemAtPosition(4, 4).widget().currentText() == "Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(5, 4).widget().currentText() == "Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(6, 4).widget().text() == "75"
    assert dialog.charges_gridLayout.itemAtPosition(7, 4).widget().text() == "0"


def test_add_offense_and_delete_offense(app, dialog):
    add_offense_speeding_25(dialog)
    QtBot.mouseClick(
        dialog.charges_gridLayout.itemAtPosition(9, 2).widget(), QtCore.Qt.LeftButton
    )
    assert dialog.charges_gridLayout.itemAtPosition(0, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(4, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(5, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(6, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(7, 2) == None


def test_add_two_delete_one_add_one_offense(app, dialog):
    add_offense_speeding_25(dialog)
    add_offense_speeding_25(dialog)
    assert (
        dialog.charges_gridLayout.itemAtPosition(0, 2).widget().text()
        == "Speeding > 25 mph"
    )
    assert (
        dialog.charges_gridLayout.itemAtPosition(4, 2).widget().currentText() == "Not Guilty"
    )
    assert dialog.charges_gridLayout.itemAtPosition(5, 2).widget().currentText() == "Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(6, 2).widget().text() == "50"
    assert dialog.charges_gridLayout.itemAtPosition(7, 2).widget().text() == "25"
    # Delete first offense and check
    QtBot.mouseClick(
        dialog.charges_gridLayout.itemAtPosition(9, 2).widget(), QtCore.Qt.LeftButton
    )
    assert dialog.charges_gridLayout.itemAtPosition(0, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(4, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(5, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(6, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(7, 2) == None
    # Add third offense, but two total since one deleted.
    add_offense_speeding_25_after_delete(dialog)
    # Third added check
    assert (
        dialog.charges_gridLayout.itemAtPosition(0, 6).widget().text()
        == "Speeding > 25 mph"
    )
    assert (
        dialog.charges_gridLayout.itemAtPosition(4, 6).widget().currentText() == "Not Guilty"
    )
    assert dialog.charges_gridLayout.itemAtPosition(5, 6).widget().currentText() == "Guilty"
    assert dialog.charges_gridLayout.itemAtPosition(6, 6).widget().text() == "50"
    assert dialog.charges_gridLayout.itemAtPosition(7, 6).widget().text() == "25"


# def test_fines_due_date(app, dialog):
#     """This test will fail right now because it doesn't account for the
#     next_tuesday function that is being used."""
#     dialog.ability_to_pay_box.setCurrentText("forthwith")
#     assert dialog.balance_due_date.date() == TODAY
#     dialog.ability_to_pay_box.setCurrentText("within 30 days")
#     assert dialog.balance_due_date.date() == TODAY + timedelta(days=30)
#     dialog.ability_to_pay_box.setCurrentText("within 60 days")
#     assert dialog.balance_due_date.date() == TODAY + timedelta(days=60)
#     dialog.ability_to_pay_box.setCurrentText("within 90 days")
#     assert dialog.balance_due_date.date() == TODAY + timedelta(days=90)


def test_fra_in_file_and_court(app, dialog):
    dialog.fra_in_file_box.setCurrentText("Yes")
    assert dialog.entry_case_information.fra_in_file == True
    dialog.fra_in_file_box.setCurrentText("No")
    assert dialog.entry_case_information.fra_in_file == False
    dialog.fra_in_file_box.setCurrentText("N/A")
    assert dialog.entry_case_information.fra_in_file == None
    dialog.fra_in_court_box.setCurrentText("Yes")
    assert dialog.entry_case_information.fra_in_court == True
    dialog.fra_in_court_box.setCurrentText("No")
    assert dialog.entry_case_information.fra_in_court == False
    dialog.fra_in_court_box.setCurrentText("N/A")
    assert dialog.entry_case_information.fra_in_court == None


# def test_amend_offense(dialog, qtbot):
#     QtBot.mouseClick(dialog.amend_offense_Button, QtCore.Qt.LeftButton)
#     dialog = start_amendment_dialog(qtbot, dialog.entry_case_information)
#     assert dialog.windowTitle() == "Amend Charge"


# def test_add_conditions(dialog, qtbot):
#     QtBot.mouseClick(dialog.add_conditions_Button, QtCore.Qt.LeftButton)
#     dialog = start_add_conditions_dialog(qtbot, dialog)
#     assert dialog.windowTitle() == "Additional Conditions"


def test_create_entry(app, dialog):
    add_offense_speeding_25(dialog)
    QtBot.mouseClick(dialog.create_entry_Button, QtCore.Qt.LeftButton)
