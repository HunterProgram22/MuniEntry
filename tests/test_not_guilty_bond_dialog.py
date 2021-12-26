import pytest
import os
import sys
import pytest
from conftest import mouse_click, enter_data
from controllers.conditions_dialogs import AddConditionsDialog
from controllers.base_dialogs import AmendOffenseDialog
from datetime import date, timedelta


TODAY = date.today()


def add_offense_speeding_25(ngb_dialog_nocase):
    """The numbers in itemAtPosition need to be changed when ui is updated."""
    ngb_dialog_nocase.offense_choice_box.setCurrentText("Speeding > 25 mph")
    mouse_click(ngb_dialog_nocase.add_charge_Button)
    ngb_dialog_nocase.charges_gridLayout.itemAtPosition(3, 2).widget().setCurrentText("Not Guilty")


def add_offense_speeding_25_after_delete(ngb_dialog_nocase):
    ngb_dialog_nocase.offense_choice_box.setCurrentText("Speeding > 25 mph")
    mouse_click(ngb_dialog_nocase.add_charge_Button)
    ngb_dialog_nocase.charges_gridLayout.itemAtPosition(3, 6).widget().setCurrentText("Not Guilty")


#TESTS

def test_case_information_dialog(ngb_dialog, add_case_information):
    assert ngb_dialog.case_number_lineEdit.text() == "21TRC1234"
    assert ngb_dialog.defendant_first_name_lineEdit.text() == "John"
    assert ngb_dialog.defendant_last_name_lineEdit.text() == "Smith"


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


def test_create_entry(app, dialog):
    add_offense_speeding_25(dialog)
    QtBot.mouseClick(dialog.create_entry_Button, QtCore.Qt.LeftButton)
