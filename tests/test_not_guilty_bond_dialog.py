from conftest import mouse_click
from datetime import date


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


# TESTS

def test_case_information_dialog(ngb_dialog_nocase, ngb_add_case_information):
    assert ngb_dialog_nocase.case_number_lineEdit.text() == "21TRC1234"
    assert ngb_dialog_nocase.defendant_first_name_lineEdit.text() == "John"
    assert ngb_dialog_nocase.defendant_last_name_lineEdit.text() == "Smith"


def test_offense_to_statute(ngb_dialog):
    ngb_dialog.offense_choice_box.setCurrentText("Driving Under Suspension")
    assert ngb_dialog.statute_choice_box.currentText() == "4510.11"
    assert ngb_dialog.degree_choice_box.currentText() == "M1"
    ngb_dialog.offense_choice_box.setCurrentText("Speeding > 25 mph")
    assert ngb_dialog.statute_choice_box.currentText() == "4511.21(B)(2)"
    assert ngb_dialog.degree_choice_box.currentText() == "Minor Misdemeanor"


def test_statute_to_offense(ngb_dialog_nocase):
    ngb_dialog_nocase.statute_choice_box.setCurrentText("4511.21(B)(3)")
    assert ngb_dialog_nocase.offense_choice_box.currentText() == "Speeding > 35 mph"
    assert ngb_dialog_nocase.degree_choice_box.currentText() == "Minor Misdemeanor"
    ngb_dialog_nocase.statute_choice_box.setCurrentText("4511.33")
    assert ngb_dialog_nocase.offense_choice_box.currentText() == "Driving in Marked Lanes"
    assert ngb_dialog_nocase.degree_choice_box.currentText() == "Minor Misdemeanor"


def test_add_offense(ngb_dialog_nocase, qtbot):
    add_offense_speeding_25(ngb_dialog_nocase)
    assert (
        ngb_dialog_nocase.charges_gridLayout.itemAtPosition(0, 2).widget().text()
        == "Speeding > 25 mph"
    )
    assert (
        ngb_dialog_nocase.charges_gridLayout.itemAtPosition(3, 2).widget().currentText() == "Not Guilty"
    )


def test_add_multiple_offenses(ngb_dialog_nocase):
    add_offense_speeding_25(ngb_dialog_nocase)
    assert (
        ngb_dialog_nocase.charges_gridLayout.itemAtPosition(0, 2).widget().text()
        == "Speeding > 25 mph"
    )
    assert (
        ngb_dialog_nocase.charges_gridLayout.itemAtPosition(3, 2).widget().currentText() == "Not Guilty"
    )
    # Second Charge
    ngb_dialog_nocase.offense_choice_box.setCurrentText("Driving in Marked Lanes")
    mouse_click(ngb_dialog_nocase.add_charge_Button)
    ngb_dialog_nocase.charges_gridLayout.itemAtPosition(3, 4).widget().setCurrentText("Guilty")
    assert (
        ngb_dialog_nocase.charges_gridLayout.itemAtPosition(0, 4).widget().text()
        == "Driving in Marked Lanes"
    )
    assert ngb_dialog_nocase.charges_gridLayout.itemAtPosition(3, 4).widget().currentText() == "Guilty"


def test_add_offense_and_delete_offense(ngb_dialog_nocase):
    add_offense_speeding_25(ngb_dialog_nocase)
    mouse_click(ngb_dialog_nocase.charges_gridLayout.itemAtPosition(4, 2).widget())
    assert ngb_dialog_nocase.charges_gridLayout.itemAtPosition(0, 2) == None
    assert ngb_dialog_nocase.charges_gridLayout.itemAtPosition(3, 2) == None


def test_add_two_delete_one_add_one_offense(ngb_dialog_nocase):
    add_offense_speeding_25(ngb_dialog_nocase)
    add_offense_speeding_25(ngb_dialog_nocase)
    assert (
        ngb_dialog_nocase.charges_gridLayout.itemAtPosition(0, 2).widget().text()
        == "Speeding > 25 mph"
    )
    assert (
        ngb_dialog_nocase.charges_gridLayout.itemAtPosition(3, 2).widget().currentText() == "Not Guilty"
    )
    # Delete first offense and check
    mouse_click(ngb_dialog_nocase.charges_gridLayout.itemAtPosition(4, 2).widget())
    assert ngb_dialog_nocase.charges_gridLayout.itemAtPosition(0, 2) == None
    assert ngb_dialog_nocase.charges_gridLayout.itemAtPosition(3, 2) == None
    # Add third offense, but two total since one deleted.
    add_offense_speeding_25_after_delete(ngb_dialog_nocase)
    # Third added check
    assert (
        ngb_dialog_nocase.charges_gridLayout.itemAtPosition(0, 6).widget().text()
        == "Speeding > 25 mph"
    )
    assert (
        ngb_dialog_nocase.charges_gridLayout.itemAtPosition(3, 6).widget().currentText() == "Not Guilty"
    )


def test_create_entry(ngb_dialog_nocase):
    add_offense_speeding_25(ngb_dialog_nocase)
    mouse_click(ngb_dialog_nocase.create_entry_Button)
