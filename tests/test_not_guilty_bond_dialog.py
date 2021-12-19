import pytest
import os
import sys
import inspect
from datetime import date

from pytestqt.plugin import QtBot
from PyQt5 import QtCore

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import MuniEntry_app
from controllers.not_guilty_bond_dialogs import NotGuiltyBondDialog
from controllers.conditions_dialogs import AddConditionsDialog, AmendOffenseDialog
from settings import create_arraignments_database_connection

TODAY = date.today()
arraignments_database = create_arraignments_database_connection()


"""Functions for Testing"""
def add_case_information(dialog):
    QtBot.keyClicks(dialog.case_number_lineEdit, "21TRC1234")
    QtBot.keyClicks(dialog.defendant_first_name_lineEdit, "John")
    QtBot.keyClicks(dialog.defendant_last_name_lineEdit, "Smith")


def start_not_guily_bond_dialog(qtbot, judicial_officer, case):
    dialog = NotGuiltyBondDialog(judicial_officer, case)
    qtbot.addWidget(dialog)
    add_case_information(dialog)
    return dialog


def start_add_conditions_dialog(qtbot, case_information):
    dialog = AddConditionsDialog(case_information)
    qtbot.addWidget(dialog)
    return dialog


def add_offense_speeding_25(dialog):
    """The numbers in itemAtPosition need to be changed when ui is updated."""
    dialog.offense_choice_box.setCurrentText("Speeding > 25 mph")
    QtBot.mouseClick(dialog.add_charge_Button, QtCore.Qt.LeftButton)
    dialog.charges_gridLayout.itemAtPosition(3, 2).widget().setCurrentText("Not Guilty")


def add_offense_speeding_25_after_delete(dialog):
    dialog.offense_choice_box.setCurrentText("Speeding > 25 mph")
    QtBot.mouseClick(dialog.add_charge_Button, QtCore.Qt.LeftButton)
    dialog.charges_gridLayout.itemAtPosition(3, 6).widget().setCurrentText("Not Guilty")



@pytest.fixture
def app(qtbot):
    test_MuniEntry_app = MuniEntry_app.Window(arraignments_database)
    qtbot.addWidget(test_MuniEntry_app)
    return test_MuniEntry_app


@pytest.fixture
def dialog(app, qtbot):
    QtBot.mouseClick(app.pelanda_radioButton, QtCore.Qt.LeftButton)
    QtBot.mouseClick(app.NotGuiltyBondButton, QtCore.Qt.LeftButton)
    dialog = start_not_guily_bond_dialog(qtbot, app.judicial_officer, app.case_to_load)
    return dialog


"""TESTING"""
"""Two columns are added every time a charge is added with add offense to view.
The columns with content are evens (0, 2, 4, etc). Rows are different for the 
Not Guilty Bond Dialog then No Jail Plea - row 3 is plea and row 4 is delete button."""

def test_open_not_guilty_bond_dialog(app, dialog):
    assert dialog.windowTitle() == "Not Guilty Bond Case Information"


def test_case_information_dialog(app, dialog):
    assert dialog.case_number_lineEdit.text() == "21TRC1234"
    assert dialog.defendant_first_name_lineEdit.text() == "John"
    assert dialog.defendant_last_name_lineEdit.text() == "Smith"


def test_offense_to_statute(app, dialog):
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
        dialog.charges_gridLayout.itemAtPosition(3, 2).widget().currentText() == "Not Guilty"
    )


def test_add_multiple_offenses(app, dialog):
    add_offense_speeding_25(dialog)
    assert (
        dialog.charges_gridLayout.itemAtPosition(0, 2).widget().text()
        == "Speeding > 25 mph"
    )
    assert (
        dialog.charges_gridLayout.itemAtPosition(3, 2).widget().currentText() == "Not Guilty"
    )
    # Second Charge
    dialog.offense_choice_box.setCurrentText("Driving in Marked Lanes")
    QtBot.mouseClick(dialog.add_charge_Button, QtCore.Qt.LeftButton)
    dialog.charges_gridLayout.itemAtPosition(3, 4).widget().setCurrentText("Guilty")
    assert (
        dialog.charges_gridLayout.itemAtPosition(0, 4).widget().text()
        == "Driving in Marked Lanes"
    )
    assert dialog.charges_gridLayout.itemAtPosition(3, 4).widget().currentText() == "Guilty"


def test_add_offense_and_delete_offense(app, dialog):
    add_offense_speeding_25(dialog)
    QtBot.mouseClick(
        dialog.charges_gridLayout.itemAtPosition(4, 2).widget(), QtCore.Qt.LeftButton
    )
    assert dialog.charges_gridLayout.itemAtPosition(0, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(3, 2) == None


def test_add_two_delete_one_add_one_offense(app, dialog):
    add_offense_speeding_25(dialog)
    add_offense_speeding_25(dialog)
    assert (
        dialog.charges_gridLayout.itemAtPosition(0, 2).widget().text()
        == "Speeding > 25 mph"
    )
    assert (
        dialog.charges_gridLayout.itemAtPosition(3, 2).widget().currentText() == "Not Guilty"
    )
    # Delete first offense and check
    QtBot.mouseClick(
        dialog.charges_gridLayout.itemAtPosition(4, 2).widget(), QtCore.Qt.LeftButton
    )
    assert dialog.charges_gridLayout.itemAtPosition(0, 2) == None
    assert dialog.charges_gridLayout.itemAtPosition(3, 2) == None
    # Add third offense, but two total since one deleted.
    add_offense_speeding_25_after_delete(dialog)
    # Third added check
    assert (
        dialog.charges_gridLayout.itemAtPosition(0, 6).widget().text()
        == "Speeding > 25 mph"
    )
    assert (
        dialog.charges_gridLayout.itemAtPosition(3, 6).widget().currentText() == "Not Guilty"
    )


# def test_add_conditions(dialog, qtbot):
#     QtBot.mouseClick(dialog.add_conditions_Button, QtCore.Qt.LeftButton)
#     dialog = start_add_conditions_dialog(qtbot, dialog)
#     assert dialog.windowTitle() == "Additional Conditions"


def test_create_entry(app, dialog):
    add_offense_speeding_25(dialog)
    QtBot.mouseClick(dialog.create_entry_Button, QtCore.Qt.LeftButton)
