"""Module containing all classes for building and using the Scheduling Entry Dialogs.

**munientry.builders.scheduling.sched_entry_dialogs**
"""
from typing import TYPE_CHECKING

from loguru import logger
from PyQt6.QtCore import QDate

from munientry.settings.business_constants import (
    DAY_DICT,
    EVENT_DICT,
    PRETRIAL_TIME_DICT,
    SPEEDY_TRIAL_TIME_DICT,
)
from munientry.builders.scheduling import base_scheduling_builders as sched
from munientry.checkers.scheduling_checks import SchedulingChecks
from munientry.loaders.cms_case_loaders import SchedulingCrimCmsLoader
from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.updaters.scheduling_updaters import (
    SchedulingModelUpdater,
)
from munientry.views.scheduling_entry_dialog_ui import Ui_SchedulingEntryDialog

if TYPE_CHECKING:
    from PyQt6.QtCore import QDate

ROHRER_SCHEDULING_ENTRY = 'Rohrer Scheduling Entry'
ROHRER_TRIAL_DAY = 'Tuesday'
ROHRER_FINAL_PRETRIAL_DAY = 'Thursday'
ROHRER_PRETRIAL_DAY = 'Monday'
HEMMETER_SCHEDULING_ENTRY = 'Hemmeter Scheduling Entry'
HEMMETER_TRIAL_DAY = 'Thursday'
HEMMETER_FINAL_PRETRIAL_DAY = 'Tuesday'
HEMMETER_PRETRIAL_DAY = 'Wednesday'
TRIAL = 'Trial'
PRETRIAL = 'Pretrial'
FINAL_PRETRIAL = 'Final Pretrial'
ENTRY_DATE_FORMAT = 'MMMM dd, yyyy'


def set_scheduling_dialog_name(sender) -> str:
    """Returns a string of the dialog name based on the button that is pressed."""
    if sender.objectName() == 'rohrer_schedulingEntryButton':
        return ROHRER_SCHEDULING_ENTRY
    if sender.objectName() == 'hemmeter_schedulingEntryButton':
        return HEMMETER_SCHEDULING_ENTRY
    return 'None'


class SchedulingEntryDialogViewModifier(sched.SchedulingViewModifier):
    """Class that sets and modifies the view for the Scheduling Entry Dialogs."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_view_dates()
        self.dialog.final_pretrial_time.setCurrentText('1:00 PM')

    def set_view_dates(self):
        today = QDate.currentDate()
        self.dialog.arrest_summons_date.setDate(today)
        self.dialog.trial_date.setDate(today)
        self.dialog.entry_date.setDate(today)


class SchedulingEntryDialogSignalConnector(sched.SchedulingSignalConnector):
    """Class that connects all signals for the Scheduling Entry Dialogs."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_speedy_trial_items()
        self.connect_pretrial_radio_buttons()
        self.connect_scheduling_date_fields()

    def connect_speedy_trial_items(self):
        arrest = self.dialog.arrest_summons_date
        charge = self.dialog.highest_charge_box
        jail_days = self.dialog.days_in_jail_line
        continuance_days = self.dialog.continuance_days_line

        arrest.dateChanged.connect(self.dialog.functions.set_speedy_trial_date_label)
        arrest.dateChanged.connect(self.dialog.functions.update_all_scheduled_dates)
        charge.currentIndexChanged.connect(self.dialog.functions.set_speedy_trial_date_label)
        charge.currentIndexChanged.connect(self.dialog.functions.update_all_scheduled_dates)
        continuance_days.textChanged.connect(self.dialog.functions.set_speedy_trial_date_label)
        continuance_days.textChanged.connect(self.dialog.functions.update_all_scheduled_dates)
        jail_days.textChanged.connect(self.dialog.functions.set_speedy_trial_date_label)
        jail_days.textChanged.connect(self.dialog.functions.update_all_scheduled_dates)

    def connect_scheduling_date_fields(self):
        self.dialog.final_pretrial_date.dateChanged.connect(
            self.dialog.functions.update_trial_and_pretrial_only,
        )

    def connect_pretrial_radio_buttons(self):
        final_and_pretrial_update = self.dialog.functions.update_final_pretrial_and_pretrial_only
        set_pretrial = self.dialog.functions.set_pretrial_scheduled
        pretrial_radio_btns = [
            self.dialog.four_week_pretrial_radio_btn,
            self.dialog.three_week_pretrial_radio_btn,
            self.dialog.two_week_pretrial_radio_btn,
            self.dialog.no_pretrial_radio_btn,
        ]
        for button in pretrial_radio_btns:
            button.clicked.connect(final_and_pretrial_update)
            button.clicked.connect(set_pretrial)


class SchedulingEntryDialogSlotFunctions(sched.SchedulingSlotFunctions):
    """Class that contains all signals for the Scheduling Entry Dialogs."""

    def set_pretrial_scheduled(self):
        if self.dialog.no_pretrial_radio_btn.isChecked():
            self.dialog.entry_case_information.pretrial_scheduled = False
            self.dialog.pretrial_date.hide()
            self.dialog.pretrial_date_label.hide()
        else:
            self.dialog.entry_case_information.pretrial_scheduled = True
            self.dialog.pretrial_date.show()
            self.dialog.pretrial_date_label.show()

    def update_all_scheduled_dates(self):
        if self.dialog.dialog_name == ROHRER_SCHEDULING_ENTRY:
            trial_date = self.set_trial_date(ROHRER_TRIAL_DAY)
            self.dialog.trial_date.setDate(trial_date)
            self.update_final_pretrial_and_pretrial_only()
        elif self.dialog.dialog_name == HEMMETER_SCHEDULING_ENTRY:
            trial_date = self.set_trial_date(HEMMETER_TRIAL_DAY)
            self.dialog.trial_date.setDate(trial_date)
            self.update_final_pretrial_and_pretrial_only()

    def update_trial_and_pretrial_only(self):
        if self.dialog.dialog_name == ROHRER_SCHEDULING_ENTRY:
            trial_date = self.set_trial_date(ROHRER_TRIAL_DAY)
            self.dialog.trial_date.setDate(trial_date)
            pretrial_date = self.set_event_date(ROHRER_PRETRIAL_DAY, PRETRIAL)
            self.dialog.pretrial_date.setDate(pretrial_date)
        elif self.dialog.dialog_name == HEMMETER_SCHEDULING_ENTRY:
            trial_date = self.set_trial_date(HEMMETER_TRIAL_DAY)
            self.dialog.trial_date.setDate(trial_date)
            pretrial_date = self.set_event_date(HEMMETER_PRETRIAL_DAY, PRETRIAL)
            self.dialog.pretrial_date.setDate(pretrial_date)

    def update_final_pretrial_and_pretrial_only(self):
        if self.dialog.dialog_name == ROHRER_SCHEDULING_ENTRY:
            final_pretrial_date = self.set_event_date(ROHRER_FINAL_PRETRIAL_DAY, FINAL_PRETRIAL)
            pretrial_date = self.set_event_date(ROHRER_PRETRIAL_DAY, PRETRIAL)
        elif self.dialog.dialog_name == HEMMETER_SCHEDULING_ENTRY:
            final_pretrial_date = self.set_event_date(HEMMETER_FINAL_PRETRIAL_DAY, FINAL_PRETRIAL)
            pretrial_date = self.set_event_date(HEMMETER_PRETRIAL_DAY, PRETRIAL)
        self.dialog.final_pretrial_date.setDate(final_pretrial_date)
        self.dialog.pretrial_date.setDate(pretrial_date)

    def set_trial_date(self, day_to_set: str) -> 'QDate':
        """Returns a date for trial based on specific Judge.

        The trial date is set 2 days (via TRIAL constant) after the final pretrial.
        Then if the day 2 days later is not the specific trial date for the Judge,
        which is Tuesday for Judge Rohrer and Thursday for Judge Hemmeter, it will
        return a date that is the next Tuesday or Thursday.
        """
        days_to_event = EVENT_DICT.get(TRIAL)
        event_date = self.dialog.final_pretrial_date.date().addDays(days_to_event)
        while event_date.dayOfWeek() != DAY_DICT.get(day_to_set):
            event_date = event_date.addDays(1)
        return event_date

    def set_event_date(self, day_to_set: str, event_to_set: str) -> 'QDate':
        if event_to_set == PRETRIAL:
            pretrial_time = self.get_pretrial_time()
            event_date = self.dialog.trial_date.date().addDays(-pretrial_time)
        else:
            days_to_event = EVENT_DICT.get(event_to_set)
            event_date = self.dialog.trial_date.date().addDays(-days_to_event)
        while event_date.dayOfWeek() != DAY_DICT.get(day_to_set):
            event_date = event_date.addDays(-1)
        return event_date

    def get_pretrial_time(self) -> int:
        """Returns the number of days the pretrial is to be set before final pretrial."""
        pretrial_radio_btns = [
            self.dialog.four_week_pretrial_radio_btn,
            self.dialog.three_week_pretrial_radio_btn,
            self.dialog.two_week_pretrial_radio_btn,
            self.dialog.no_pretrial_radio_btn,
        ]
        for button in pretrial_radio_btns:
            if button.isChecked():
                return PRETRIAL_TIME_DICT.get(button.text())
        return 0

    def get_speedy_trial_date(self) -> 'QDate':
        speedy_trial_days = self.get_speedy_trial_days()
        days_in_jail = self.get_days_in_jail()
        continuance_days = self.get_continuance_days()
        speedy_trial_days = (speedy_trial_days + continuance_days) - days_in_jail
        return self.dialog.arrest_summons_date.date().addDays(speedy_trial_days)

    def set_speedy_trial_date_label(self):
        speedy_trial_date = self.get_speedy_trial_date()
        speedy_trial_date = speedy_trial_date.toString(ENTRY_DATE_FORMAT)
        self.dialog.speedy_trial_date_label.setText(speedy_trial_date)

    def get_speedy_trial_days(self) -> int:
        key = self.dialog.highest_charge_box.currentText()
        return SPEEDY_TRIAL_TIME_DICT.get(key)

    def get_days_in_jail(self) -> int:
        """Multiply days in jail times 3 for speedy trial calculations."""
        if self.dialog.days_in_jail_line.text() == '':
            days_in_jail = 0
        else:
            days_in_jail = int(self.dialog.days_in_jail_line.text())
        return 3 * days_in_jail

    def get_continuance_days(self) -> int:
        if self.dialog.continuance_days_line.text() == '':
            continuance_days = 0
        else:
            continuance_days = int(self.dialog.continuance_days_line.text())
        return continuance_days


class SchedulingEntryModelUpdater(SchedulingModelUpdater):
    """Class for updating Case Information for the Scheduling Entry Dialog."""

    def set_scheduling_dates(self):
        self.model.jury_trial.date = self.dialog.trial_date.date().toString(ENTRY_DATE_FORMAT)
        self.model.final_pretrial.date = self.dialog.final_pretrial_date.date().toString(
            ENTRY_DATE_FORMAT,
        )
        if self.dialog.no_pretrial_radio_btn.isChecked():
            self.model.pretrial.date = None
        else:
            self.model.pretrial.date = self.dialog.pretrial_date.date().toString(ENTRY_DATE_FORMAT)
            self.model.pretrial.location = self.set_courtroom()
        self.model.final_pretrial.time = self.dialog.final_pretrial_time.currentText()
        self.model.jury_trial.location = self.set_courtroom()
        self.model.final_pretrial.location = self.set_courtroom()

    def set_courtroom(self) -> str:
        """Sets the hearing location for the case data.

        This is used to set the hearing location even though it is not populated in an
        entry because it is used in saving the scheduling data to the database.
        """
        if self.dialog.dialog_name == 'Rohrer Scheduling Entry':
            return 'Courtroom A'
        if self.dialog.dialog_name == 'Hemmeter Scheduling Entry':
            return 'Courtroom B'
        return 'Unknown'


class SchedulingEntryCheckList(SchedulingChecks):
    """Class with checks for the Scheduling Entry Dialogs."""

    check_list = [
        'check_final_pretrial_date',
        'check_trial_date',
    ]


class SchedulingEntryDialog(sched.SchedulingDialogBuilder, Ui_SchedulingEntryDialog):
    """The builder class for the Scheduling Entry."""

    _case_information_model = SchedulingCaseInformation
    _case_loader = SchedulingCrimCmsLoader
    _info_checker = SchedulingEntryCheckList
    _model_updater = SchedulingEntryModelUpdater
    _signal_connector = SchedulingEntryDialogSignalConnector
    _slots = SchedulingEntryDialogSlotFunctions
    _view_modifier = SchedulingEntryDialogViewModifier
    dialog_name = None

    def additional_setup(self):
        """The additional setup sets the dialog name after init because the Hemmeter and Rohrer
        scheduling entries use a common base.
        """
        self.dialog_name = set_scheduling_dialog_name(self.sender())
        self.setWindowTitle(f'{self.dialog_name} Case Information')
        self.functions.set_speedy_trial_date_label()
        self.functions.update_all_scheduled_dates()
        self.functions.set_pretrial_scheduled()
