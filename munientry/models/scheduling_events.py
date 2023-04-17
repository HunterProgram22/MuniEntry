"""Event classes used for packaging events to load into the MuniEntryDB.

**munientry.data.scheduling_events**

Classes:

    Event(object)

    FinalPretrialEvent(Event)

    GeneralHearingEvent(Event)

    JuryTrialEvent(Event)

    TelephonePretrialEvent(Event)

    TrialToCourtEvent(Event)
"""
from loguru import logger

from munientry.helper_functions import format_date_string


class Event(object):
    """Object for storing and packaging case event data to be inserted into the MuniEntryDB."""

    event_name_field: str

    def __init__(self, case_data_dict: dict):
        self.case_data_dict = case_data_dict
        self.case_number = self.case_data_dict.get('case_number')
        defendant = self.case_data_dict.get('defendant')
        self.def_last_name = defendant.last_name
        self.def_first_name = defendant.first_name

        self.event = self.case_data_dict.get('event_data')
        self.event_location = self.event.get('location')
        self.event_name = self.load_event_name(self.event_name_field)
        self.event_date = format_date_string(self.event.get('date'))
        self.event_time = self.event.get('time')

    def load_event_name(self, event_name_field: str) -> str:
        if event_name_field == 'hearing_type':
            return self.event.get('type', 'None')
        return event_name_field


class FinalPretrialEvent(Event):
    """Event object for final pretrial court event."""

    event_name_field = 'Final Pretrial'


class GeneralHearingEvent(Event):
    """Event object for the General Notice of Hearing Entry.

    The General Notice of Hearing Entry schedules for multiple different types of hearings, but
    the dialog only schedules for a single date.
    """

    event_name_field = 'hearing_type'


class JuryTrialEvent(Event):
    """Event object for jury trial event."""

    event_name_field = 'Jury Trial'


class TelephonePretrialEvent(Event):
    """Event object for telephone pretrial court event."""

    event_name_field = 'Telephone Pretrial'


class TrialToCourtEvent(Event):
    """Event object for trial to court event."""

    event_name_field = 'Trial to Court'
