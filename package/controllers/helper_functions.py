"""Helper functions that are used throughout the application."""
from datetime import date, timedelta

from PyQt5.QtWidgets import QMessageBox
from loguru import logger

from MuniEntry.package.views.custom_widgets import WarningBox, RequiredBox


def set_document_name(dialog):
    """Sets document name based on the cms_case number and name of the template
    must include '.docx' to make it a Word document."""
    return dialog.entry_case_information.case_number + "_" + dialog.template.template_name + ".docx"


@logger.catch
def set_future_date(days_to_add, days_to_add_dict, next_day):
    """This is a general helper function that will accept the numbers of days to
    add to the current date and set a new date.
    :days_to_add: A string from the view.
    :days_to_add_dict: A dict that has the different date options available in
    the view.
    :next_day: The next day of the week to set the date after the days to add.
    For example 0 days sets it to the next Monday after the added days, 1 sets
    it to the next Tuesday after the added days, etc."""
    if days_to_add_dict is None:
        days_to_add = days_to_add
    else:
        days_to_add = days_to_add_dict[days_to_add]
    future_date = date.today() + timedelta(days_to_add)
    today = date.today()

    def next_court_day(future_date, weekday):
        """This function returns the number of days to add to today to set
        the actual date needed. If it is 1 it would be Tuesday, 3 would
        be Wednesday, etc."""
        days_ahead = weekday - future_date.weekday()
        if days_ahead <= 0:  # Target day already happened this week
            days_ahead += 7
        return future_date + timedelta(days_ahead)

    future_date = next_court_day(future_date, next_day)
    total_days_to_add = (future_date - today).days
    return total_days_to_add


class InfoChecker(object):
    """Class that checks dialog to make sure the appropriate information is entered.
    Methods are class methods because this is a factory method to perform checks and
    no object is instantiated."""
    @classmethod
    def check_defense_counsel(cls, dialog):
        if (dialog.defense_counsel_name_box.currentText() == ""
                and not dialog.defense_counsel_waived_checkBox.isChecked()):
            message = WarningBox("There is no attorney listed. Did "
                                 "the Defendant waive his right to counsel?"
                                 "\n\nIf you select 'No' you must enter a name "
                                 "for Def. Counsel.")
            return_value = message.exec()
            if return_value == QMessageBox.Yes:
                dialog.defense_counsel_waived_checkBox.setChecked(True)
                return "Pass"
            elif return_value == QMessageBox.No:
                return "Fail"
        else:
            return "Pass"

    @classmethod
    def check_plea_and_findings(cls, dialog):
        """Shows warning if no plea or findings are entered. Checks one at a time so unless all
        fields have a plea and finding you will get the warning until they are filled in."""
        row_plea, row_finding = dialog.charges_gridLayout.set_plea_and_finding_rows()
        column = 2
        loop_counter = 0
        while loop_counter < dialog.charges_gridLayout.columnCount():
            try:
                offense = dialog.charges_gridLayout.itemAtPosition(0, column).widget().text()
                if dialog.charges_gridLayout.itemAtPosition(row_plea, column).widget().currentText() == "":
                    message = RequiredBox(f"You must enter a plea for {offense}.")
                    message.exec()
                    return "Fail"
                elif dialog.charges_gridLayout.itemAtPosition(row_plea, column).widget().currentText() == "Dismissed":
                    column += 2
                    loop_counter += 1
                    continue
                elif dialog.charges_gridLayout.itemAtPosition(row_finding, column).widget().currentText() == "":
                    message = RequiredBox(f"You must enter a finding for {offense}.")
                    message.exec()
                    return "Fail"
            except AttributeError:
                pass
            column += 2
            loop_counter += 1
        return "Pass"

    @classmethod
    def check_insurance(cls, dialog):
        if (
            hasattr(dialog, 'fra_in_file_box')
            and dialog.fra_in_file_box.currentText() == "No"
            and dialog.fra_in_court_box.currentText() == "N/A"
        ):
            message = WarningBox("The information provided currently "
                                 "indicates insurance was not shown in the file. "
                                 "\n\nDid the defendant show proof of insurance in court?")
            return_value = message.exec()
            if return_value == QMessageBox.No:
                dialog.fra_in_court_box.setCurrentText("No")
                return "Pass"
            elif return_value == QMessageBox.Yes:
                dialog.fra_in_court_box.setCurrentText("Yes")
                return "Pass"
        else:
            return "Pass"

    @classmethod
    def check_bond_amount(cls, dialog):
        if(
            hasattr(dialog, 'bond_type_box')
            and dialog.bond_type_box.currentText() != 'Recognizance (OR) Bond'
            and dialog.bond_amount_box.currentText() == 'None (OR Bond)'
        ):
            message = RequiredBox("A bond type requiring a bond amount was selected, but a bond amount was not selected. Please specify the bond amount.")
            message.exec()
            return "Fail"
        if (
                hasattr(dialog, 'bond_type_box')
                and dialog.bond_type_box.currentText() == 'Recognizance (OR) Bond'
                and dialog.bond_amount_box.currentText() != 'None (OR Bond)'
        ):
            message = RequiredBox(
                "A Recognizance (OR) Bond was selected but a bond amount other than None(OR Bond) "
                "was chosen. Please either change bond type to 10% or Cash or Surety, or set bond amount to None (OR Bond).")
            message.exec()
            return "Fail"

    @classmethod
    def check_license_suspension(cls, dialog):
        conditions_list = [
            (dialog.entry_case_information.license_suspension.ordered, dialog.entry_case_information.license_suspension.license_type),
            (dialog.entry_case_information.community_service.ordered, dialog.entry_case_information.community_service.hours_of_service),
        ]
        for condition in conditions_list:
            if (
                condition[0] is True
                and condition[1] is None
            ):
                message = RequiredBox("The Additional Condition License Suspension is checked, but "
                                      "the details of the license suspension have not been entered. "
                                      "Click the Add Conditions button to add details, or uncheck the "
                                      "License Suspension box if there is no License Suspension in this case.")
                message.exec()
                return "Fail"
        return "Pass"
