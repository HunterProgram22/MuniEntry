"""Module containing all classes for building and using the Scheduling Entry Dialogs."""
from loguru import logger

from munientry.builders.scheduling import base_scheduling_builders as sched
from munientry.checkers.base_checks import BaseChecker
from munientry.helper_functions import set_courtroom
from munientry.loaders.cms_case_loaders import SchedulingCmsLoader
from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.models.template_types import TEMPLATE_DICT
from munientry.settings import (
    DAY_DICT,
    EVENT_DICT,
    PRETRIAL_TIME_DICT,
    SPEEDY_TRIAL_TIME_DICT,
    TYPE_CHECKING,
)
from munientry.appsettings.pyqt_constants import TODAY
from munientry.updaters.scheduling_updaters import (
    SchedulingDialogCaseInformationUpdater,
)
from munientry.views.scheduling_entry_dialog_ui import Ui_SchedulingEntryDialog

if TYPE_CHECKING:
    from PyQt6.QtCore import QDate

ROHRER_SCHEDULING_ENTRY = 'Rohrer Scheduling Entry'
HEMMETER_SCHEDULING_ENTRY = 'Hemmeter Scheduling Entry'
TRIAL = 'Trial'
PRETRIAL = 'Pretrial'
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

    def set_view_dates(self):
        self.dialog.arrest_summons_date_box.setDate(TODAY)
        self.dialog.trial_dateEdit.setDate(TODAY)
        self.dialog.entry_date.setDate(TODAY)


class SchedulingEntryDialogSignalConnector(sched.SchedulingSignalConnector):
    """Class that connects all signals for the Scheduling Entry Dialogs."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_speedy_trial_items()
        self.connect_pretrial_radio_buttons()
        self.connect_scheduling_date_fields()

    def connect_speedy_trial_items(self):
        self.dialog.arrest_summons_date_box.dateChanged.connect(
            self.dialog.functions.set_speedy_trial_date_label,
        )
        self.dialog.arrest_summons_date_box.dateChanged.connect(
            self.dialog.functions.update_all_scheduled_dates,
        )
        self.dialog.highest_charge_box.currentIndexChanged.connect(
            self.dialog.functions.set_speedy_trial_date_label,
        )
        self.dialog.days_in_jail_lineEdit.textChanged.connect(
            self.dialog.functions.set_speedy_trial_date_label,
        )
        self.dialog.continuance_days_lineEdit.textChanged.connect(
            self.dialog.functions.set_speedy_trial_date_label,
        )
        self.dialog.highest_charge_box.currentIndexChanged.connect(
            self.dialog.functions.update_all_scheduled_dates,
        )
        self.dialog.days_in_jail_lineEdit.textChanged.connect(
            self.dialog.functions.update_all_scheduled_dates,
        )
        self.dialog.continuance_days_lineEdit.textChanged.connect(
            self.dialog.functions.update_all_scheduled_dates,
        )

    def connect_scheduling_date_fields(self):
        """Only the final_pretrial_dateEdit field is connected.

        NOTE: This may be working as needed so TODO may not be needed.

        TODO: In order to update other date fields on data entry another solution is required because
        adding other connections creates a loop due to the signal sent when a date is changed.
        """
        self.dialog.final_pretrial_dateEdit.dateChanged.connect(
            self.dialog.functions.update_trial_and_pretrial_only,
        )

    def connect_pretrial_radio_buttons(self):
        """Local functions are only used to shorten line length to < 100 characters."""
        final_and_pretrial_update = self.dialog.functions.update_final_pretrial_and_pretrial_only
        set_pretrial = self.dialog.functions.set_pretrial_scheduled
        self.dialog.four_week_pretrial_radioButton.clicked.connect(final_and_pretrial_update)
        self.dialog.three_week_pretrial_radioButton.clicked.connect(final_and_pretrial_update)
        self.dialog.two_week_pretrial_radioButton.clicked.connect(final_and_pretrial_update)
        self.dialog.no_pretrial_radioButton.clicked.connect(final_and_pretrial_update)
        self.dialog.four_week_pretrial_radioButton.clicked.connect(set_pretrial)
        self.dialog.three_week_pretrial_radioButton.clicked.connect(set_pretrial)
        self.dialog.two_week_pretrial_radioButton.clicked.connect(set_pretrial)
        self.dialog.no_pretrial_radioButton.clicked.connect(set_pretrial)


class SchedulingEntryDialogSlotFunctions(sched.SchedulingSlotFunctions):
    """Class that contains all signals for the Scheduling Entry Dialogs."""

    def set_pretrial_scheduled(self):
        if self.dialog.no_pretrial_radioButton.isChecked():
            self.dialog.entry_case_information.pretrial_scheduled = False
            self.dialog.pretrial_dateEdit.setHidden(True)
            self.dialog.pretrial_date_label.setHidden(True)
        else:
            self.dialog.entry_case_information.pretrial_scheduled = True
            self.dialog.pretrial_dateEdit.setHidden(False)
            self.dialog.pretrial_date_label.setHidden(False)

    def update_all_scheduled_dates(self):
        if self.dialog.dialog_name == ROHRER_SCHEDULING_ENTRY:
            trial_date = self.set_event_date('Tuesday', TRIAL)
            self.dialog.trial_dateEdit.setDate(trial_date)
            self.update_final_pretrial_and_pretrial_only()
        elif self.dialog.dialog_name == HEMMETER_SCHEDULING_ENTRY:
            trial_date = self.set_event_date('Thursday', TRIAL)
            self.dialog.trial_dateEdit.setDate(trial_date)
            self.update_final_pretrial_and_pretrial_only()

    def update_trial_and_pretrial_only(self):
        logger.debug('Update trial and pretrial')
        if self.dialog.dialog_name == ROHRER_SCHEDULING_ENTRY:
            logger.debug('Update Rohrer')
            trial_date = self.set_trial_date('Tuesday', TRIAL)
            self.dialog.trial_dateEdit.setDate(trial_date)
            pretrial_date = self.set_event_date('Monday', PRETRIAL)
            self.dialog.pretrial_dateEdit.setDate(pretrial_date)
        elif self.dialog.dialog_name == HEMMETER_SCHEDULING_ENTRY:
            logger.debug('Update Hemmeter')
            trial_date = self.set_trial_date('Thursday', TRIAL)
            self.dialog.trial_dateEdit.setDate(trial_date)
            pretrial_date = self.set_event_date('Wednesday', PRETRIAL)
            self.dialog.pretrial_dateEdit.setDate(pretrial_date)

    def update_final_pretrial_and_pretrial_only(self):
        if self.dialog.dialog_name == ROHRER_SCHEDULING_ENTRY:
            final_pretrial_date = self.set_event_date('Thursday', 'Final Pretrial')
            pretrial_date = self.set_event_date('Monday', PRETRIAL)
        elif self.dialog.dialog_name == HEMMETER_SCHEDULING_ENTRY:
            final_pretrial_date = self.set_event_date('Tuesday', 'Final Pretrial')
            pretrial_date = self.set_event_date('Wednesday', PRETRIAL)
        self.dialog.final_pretrial_dateEdit.setDate(final_pretrial_date)
        self.dialog.pretrial_dateEdit.setDate(pretrial_date)

    def set_trial_date(self, day_to_set: str, event_to_set: str) -> 'QDate':
        if event_to_set == TRIAL:
            days_to_event = EVENT_DICT.get(event_to_set)
            event_date = self.dialog.final_pretrial_dateEdit.date().addDays(days_to_event)
            while event_date.dayOfWeek() != DAY_DICT.get(day_to_set):
                event_date = event_date.addDays(1)
            return event_date

    def set_event_date(self, day_to_set: str, event_to_set: str) -> 'QDate':
        if event_to_set == TRIAL:
            days_until_speedy_trial_date = TODAY.daysTo(self.get_speedy_trial_date())
            event_date = TODAY.addDays(days_until_speedy_trial_date)
        elif event_to_set == PRETRIAL:
            pretrial_time = self.get_pretrial_time()
            event_date = self.dialog.trial_dateEdit.date().addDays(-pretrial_time)
        else:
            days_to_event = EVENT_DICT.get(event_to_set)
            event_date = self.dialog.trial_dateEdit.date().addDays(-days_to_event)
        while event_date.dayOfWeek() != DAY_DICT.get(day_to_set):
            event_date = event_date.addDays(-1)
        return event_date

    def get_pretrial_time(self) -> int:
        pretrial_buttons = [
            self.dialog.four_week_pretrial_radioButton,
            self.dialog.three_week_pretrial_radioButton,
            self.dialog.two_week_pretrial_radioButton,
            self.dialog.no_pretrial_radioButton,
        ]
        for button in pretrial_buttons:
            if button.isChecked():
                return PRETRIAL_TIME_DICT.get(button.text())

    def get_speedy_trial_date(self) -> 'QDate':
        speedy_trial_days = self.get_speedy_trial_days()
        days_in_jail = self.get_days_in_jail()
        continuance_days = self.get_continuance_days()
        speedy_trial_days = (speedy_trial_days + continuance_days) - days_in_jail
        return self.dialog.arrest_summons_date_box.date().addDays(speedy_trial_days)

    def set_speedy_trial_date_label(self):
        speedy_trial_date = self.get_speedy_trial_date()
        speedy_trial_date = speedy_trial_date.toString(ENTRY_DATE_FORMAT)
        self.dialog.speedy_trial_date_label.setText(speedy_trial_date)

    def get_speedy_trial_days(self) -> int:
        key = self.dialog.highest_charge_box.currentText()
        return SPEEDY_TRIAL_TIME_DICT.get(key)

    def get_days_in_jail(self) -> int:
        """Multiply days in jail times 3 for speedy trial calculations."""
        if self.dialog.days_in_jail_lineEdit.text() == '':
            days_in_jail = 0
        else:
            days_in_jail = int(self.dialog.days_in_jail_lineEdit.text())
        return 3 * days_in_jail

    def get_continuance_days(self) -> int:
        if self.dialog.continuance_days_lineEdit.text() == '':
            continuance_days = 0
        else:
            continuance_days = int(self.dialog.continuance_days_lineEdit.text())
        return continuance_days


class SchedulingEntryDialogCaseInformationUpdater(SchedulingDialogCaseInformationUpdater):
    """Class for updating Case Information for the Scheduling Entry Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.update_model_with_case_information_frame_data()

    def set_scheduling_dates(self):
        self.model.jury_trial_date = self.dialog.trial_dateEdit.date().toString(ENTRY_DATE_FORMAT)
        self.model.final_pretrial_date = self.dialog.final_pretrial_dateEdit.date().toString(
            ENTRY_DATE_FORMAT,
        )
        if self.dialog.no_pretrial_radioButton.isChecked():
            self.model.pretrial_date = None
        else:
            self.model.pretrial_date = self.dialog.pretrial_dateEdit.date().toString(ENTRY_DATE_FORMAT)
        self.model.final_pretrial_time = self.dialog.final_pretrial_time_box.currentText()
        self.model.hearing_location = self.set_courtroom()

    def set_courtroom(self) -> str:
        """Sets the hearing location for the case data.

        This is used to set the hearing location even though it is not populated in an
        entry because it is used in saving the scheduling data to the database.
        """
        if self.dialog.dialog_name == 'Rohrer Scheduling Entry':
            return 'Courtroom A'
        if self.dialog.dialog_name == 'Hemmeter Scheduling Entry':
            return 'Courtroom B'


class SchedulingEntryDialogInfoChecker(BaseChecker):
    """Class with checks for the General Notice Hearing Info Checker."""

    def __init__(self, dialog) -> None:
        super().__init__(dialog)
        self.dialog_check_list = [
            'check_if_trial_date_is_today',
        ]
        self.check_status = self.perform_check_list()


class SchedulingEntryDialog(sched.SchedulingDialogBuilder, Ui_SchedulingEntryDialog):
    """The builder class for the Scheduling Entry Dialog."""

    build_dict = {
        'dialog_name': None,
        'view': SchedulingEntryDialogViewModifier,
        'slots': SchedulingEntryDialogSlotFunctions,
        'signals': SchedulingEntryDialogSignalConnector,
        'case_information_model': SchedulingCaseInformation,
        'loader': SchedulingCmsLoader,
        'updater': SchedulingEntryDialogCaseInformationUpdater,
        'info_checker': SchedulingEntryDialogInfoChecker,
    }

    def additional_setup(self):
        """The additional setup sets the template here after init.

        The template is set after init because the dialog name is not set initially from the build
        dict because there are two dialogs and templates built (Rohrer and Hemmeter) in this module.

        TODO: For clarity these should probably just be separated out to separate dialog modules.
        """
        self.dialog_name = set_scheduling_dialog_name(self.sender())
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.setWindowTitle(f'{self.dialog_name} Case Information')
        self.functions.set_speedy_trial_date_label()
        self.functions.update_all_scheduled_dates()


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
