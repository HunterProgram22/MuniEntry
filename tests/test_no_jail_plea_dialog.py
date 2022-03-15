import pytest
from conftest import mouse_click
from datetime import date, timedelta
from package.controllers.plea_finding_controllers import NoJailPleaFindingFines

TODAY = date.today()


def add_offense_speeding_25(njp_dialog_nocase):
    """The numbers in itemAtPosition need to be changed when ui is updated."""
    njp_dialog_nocase.offense_choice_box.setCurrentText("Speeding > 25 mph")
    mouse_click(njp_dialog_nocase.add_charge_Button)
    njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_plea, 2).widget().setCurrentText("Not Guilty")
    njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_finding, 2).widget().setCurrentText("Guilty")
    njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine, 2).widget().setText("50")
    njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine_suspended, 2).widget().setText("25")


def add_offense_speeding_25_after_delete(njp_dialog_nocase):
    njp_dialog_nocase.offense_choice_box.setCurrentText("Speeding > 25 mph")
    mouse_click(njp_dialog_nocase.add_charge_Button)
    njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_plea, 6).widget().setCurrentText("Not Guilty")
    njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_finding, 6).widget().setCurrentText("Guilty")
    njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine, 6).widget().setText("50")
    njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine_suspended, 6).widget().setText("25")


#TESTS

def test_case_information_dialog(njp_dialog_nocase, njp_add_case_information):
    assert njp_dialog_nocase.case_number_lineEdit.text() == "21TRC1234"
    assert njp_dialog_nocase.defendant_first_name_lineEdit.text() == "John"
    assert njp_dialog_nocase.defendant_last_name_lineEdit.text() == "Smith"


def test_offense_to_statute(njp_dialog):
    njp_dialog.offense_choice_box.setCurrentText("Driving Under Suspension")
    assert njp_dialog.statute_choice_box.currentText() == "4510.11"
    assert njp_dialog.degree_choice_box.currentText() == "M1"
    njp_dialog.offense_choice_box.setCurrentText("Speeding > 25 mph")
    assert njp_dialog.statute_choice_box.currentText() == "4511.21(B)(2)"
    assert njp_dialog.degree_choice_box.currentText() == "Minor Misdemeanor"


def test_statute_to_offense(njp_dialog_nocase):
    njp_dialog_nocase.statute_choice_box.setCurrentText("4511.21(B)(3)")
    assert njp_dialog_nocase.offense_choice_box.currentText() == "Speeding > 35 mph"
    assert njp_dialog_nocase.degree_choice_box.currentText() == "Minor Misdemeanor"
    njp_dialog_nocase.statute_choice_box.setCurrentText("4511.33")
    assert njp_dialog_nocase.offense_choice_box.currentText() == "Driving in Marked Lanes"
    assert njp_dialog_nocase.degree_choice_box.currentText() == "Minor Misdemeanor"


# Add Charge: Two columns are added every time a charge is added with add offense to view.
# The columns with content are evens (0, 2, 4, etc).
def test_add_offense(njp_dialog_nocase, qtbot):
    add_offense_speeding_25(njp_dialog_nocase)
    # dialog = NoJailPleaDialog()
    # qtbot.addWidget(dialog)
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_offense, 2).widget().text() == "Speeding > 25 mph"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_plea, 2).widget().currentText() == "Not Guilty"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_finding, 2).widget().currentText() == "Guilty"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine, 2).widget().text() == "50"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine_suspended, 2).widget().text() == "25"


def test_add_multiple_offenses(njp_dialog_nocase):
    add_offense_speeding_25(njp_dialog_nocase)
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_offense, 2).widget().text() == "Speeding > 25 mph"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_plea, 2).widget().currentText() == "Not Guilty"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_finding, 2).widget().currentText() == "Guilty"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine, 2).widget().text() == "50"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine_suspended, 2).widget().text() == "25"
    # Second Charge
    njp_dialog_nocase.offense_choice_box.setCurrentText("Driving in Marked Lanes")
    mouse_click(njp_dialog_nocase.add_charge_Button)
    njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_plea, 4).widget().setCurrentText("Guilty")
    njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_finding, 4).widget().setCurrentText("Guilty")
    njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine, 4).widget().setText("75")
    njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine_suspended, 4).widget().setText("0")
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_offense, 4).widget().text() == "Driving in Marked Lanes"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_plea, 4).widget().currentText() == "Guilty"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_finding, 4).widget().currentText() == "Guilty"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine, 4).widget().text() == "75"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine_suspended, 4).widget().text() == "0"


def test_add_offense_and_delete_offense(njp_dialog_nocase):
    add_offense_speeding_25(njp_dialog_nocase)
    mouse_click(njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_delete_button, 2).widget())
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_offense, 2) == None
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_plea, 2) == None
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_finding, 2) == None
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine, 2) == None
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine_suspended, 2) == None


def test_add_two_delete_one_add_one_offense(njp_dialog_nocase):
    add_offense_speeding_25(njp_dialog_nocase)
    add_offense_speeding_25(njp_dialog_nocase)
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_offense, 2).widget().text() == "Speeding > 25 mph"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_plea, 2).widget().currentText() == "Not Guilty"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_finding, 2).widget().currentText() == "Guilty"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine, 2).widget().text() == "50"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine_suspended, 2).widget().text() == "25"
    # Delete first offense and check
    mouse_click(njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_delete_button, 2).widget())
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_offense, 2) == None
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_plea, 2) == None
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_finding, 2) == None
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine, 2) == None
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine_suspended, 2) == None
    # Add third offense, but two total since one deleted.
    add_offense_speeding_25_after_delete(njp_dialog_nocase)
    # Third added check
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_offense, 6).widget().text() == "Speeding > 25 mph"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_plea, 6).widget().currentText() == "Not Guilty"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_finding, 6).widget().currentText() == "Guilty"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine, 6).widget().text() == "50"
    assert njp_dialog_nocase.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine_suspended, 6).widget().text() == "25"


@pytest.mark.xfail
def test_fines_due_date(njp_dialog):
    """Failing because next_tuesday function not accounted for yet."""
    njp_dialog.ability_to_pay_box.setCurrentText("forthwith")
    assert njp_dialog.balance_due_date.date() == TODAY
    njp_dialog.ability_to_pay_box.setCurrentText("within 30 days")
    assert njp_dialog.balance_due_date.date() == TODAY + timedelta(days=30)
    njp_dialog.ability_to_pay_box.setCurrentText("within 60 days")
    assert njp_dialog.balance_due_date.date() == TODAY + timedelta(days=60)
    njp_dialog.ability_to_pay_box.setCurrentText("within 90 days")
    assert njp_dialog.balance_due_date.date() == TODAY + timedelta(days=90)


def test_fra_in_file_and_court(njp_dialog):
    njp_dialog.fra_in_file_box.setCurrentText("Yes")
    assert njp_dialog.entry_case_information.fra_in_file == True
    njp_dialog.fra_in_file_box.setCurrentText("No")
    assert njp_dialog.entry_case_information.fra_in_file == False
    njp_dialog.fra_in_file_box.setCurrentText("N/A")
    assert njp_dialog.entry_case_information.fra_in_file == None
    njp_dialog.fra_in_court_box.setCurrentText("Yes")
    assert njp_dialog.entry_case_information.fra_in_court == True
    njp_dialog.fra_in_court_box.setCurrentText("No")
    assert njp_dialog.entry_case_information.fra_in_court == False
    njp_dialog.fra_in_court_box.setCurrentText("N/A")
    assert njp_dialog.entry_case_information.fra_in_court == None


def test_create_entry(njp_dialog):
    add_offense_speeding_25(njp_dialog)
    mouse_click(njp_dialog.defense_counsel_waived_checkBox)
    mouse_click(njp_dialog.no_contest_all_Button)
    mouse_click(njp_dialog.create_entry_Button)
    assert njp_dialog.entry_case_information is not None
