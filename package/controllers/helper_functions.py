"""Helper functions that are used throughout the application."""
from datetime import date, timedelta

from PyQt5.QtWidgets import QMessageBox
from loguru import logger

from MuniEntry.package.views.custom_widgets import WarningBox


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
    """Class that checks dialog to make sure the appropriate information is entered."""
    def __init__(self, dialog):
        self.dialog = dialog

    @classmethod
    def check_defense_counsel(cls, dialog):
        if (dialog.defense_counsel_name_box.text() == ""
            and not dialog.defense_counsel_waived_checkBox.isChecked()
        ):
            message = WarningBox("There is no attorney listed. Did "
                                 "the Defendant waive his right to counsel?"
                                 "\n\nIf you select 'No' you must enter a name "
                                 "for Def. Counsel.")
            return_value = message.exec()
            if return_value == QMessageBox.Yes:
                dialog.defense_counsel_waived_checkBox.setChecked(True)
            elif return_value == QMessageBox.No:
                return None
        else:
            return "Pass"

    @classmethod
    def check_plea_and_findings(cls, dialog):
        if dialog.charges_gridLayout.check_plea_and_findings() is None:
            return None
        else:
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
