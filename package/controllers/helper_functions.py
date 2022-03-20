"""Helper functions that are used throughout the application."""
from datetime import date, timedelta


def set_future_date(days_to_add, weekday_due_date):
    """This is a general helper function that will accept the numbers of days to
    add to the current date and set a new date.
    :days_to_add: A string from the view.
    :next_day: The next day of the week to set the date after the days to add.
    For example 0 days sets it to the next Monday after the added days, 1 sets
    it to the next Tuesday after the added days, etc."""
    future_date = date.today() + timedelta(days_to_add)
    today = date.today()
    future_date = next_court_day(future_date, weekday_due_date)
    total_days_to_add = (future_date - today).days
    return total_days_to_add


def next_court_day(future_date, weekday_due_date):
    """This function returns the number of days to add to today to set
    the actual date needed. If it is 1 it would be Tuesday, 3 would
    be Wednesday, etc."""
    weekday_convert_dict = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
    }
    weekday = weekday_convert_dict.get(weekday_due_date)
    days_ahead = weekday - future_date.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return future_date + timedelta(days_ahead)
