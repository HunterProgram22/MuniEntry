"""Helper functions that are used throughout the application."""
import os
from datetime import date, timedelta

from docxtpl import DocxTemplate
from loguru import logger

from settings import SAVE_PATH

@logger.catch
def create_entry(dialog):
    """The dialog is the controller dialog that is the source of case information."""
    dialog.doc = DocxTemplate(dialog.template.template_path)
    dialog.doc.render(dialog.case_information.get_case_information())
    docname = set_document_name(dialog)
    dialog.doc.save(SAVE_PATH + docname)
    os.startfile(SAVE_PATH + docname)


def set_document_name(dialog):
    """Sets document name based on the case number and name of the template
    must include '.docx' to make it a Word document."""
    return dialog.case_information.case_number + "_" + dialog.template.template_name + ".docx"


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
