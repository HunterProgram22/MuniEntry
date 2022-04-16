"""Helper functions that are used throughout the application."""
from datetime import date, timedelta


def set_future_date(days_to_add: int, weekday_due_date: str) -> int:
    """Accepts the number of days to add and a day of the week that will be added on to the
    number of days for the future court date that is to be set."""
    today = date.today()
    future_date = today + timedelta(days_to_add)
    future_date = next_court_day(future_date, weekday_due_date)
    return (future_date - today).days


def next_court_day(future_date: date, weekday_due_date: str) -> date:
    """Returns a date object that is the total number of days plus the days required to be
    added to get to the next specified court date"""
    weekday_convert_dict = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
    }
    weekday = weekday_convert_dict.get(weekday_due_date, 0)
    days_ahead = weekday - future_date.weekday()
    if days_ahead <= 0:  # Target day already happened this week
        days_ahead += 7
    return future_date + timedelta(days_ahead)
