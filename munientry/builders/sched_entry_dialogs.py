"""Module containing all classes for building and using the Scheduling Entry Dialogs."""
from loguru import logger

from munientry.builders.base_dialogs import SchedulingBaseDialog
from munientry.controllers.signal_connectors import BaseDialogSignalConnector
from munientry.controllers.slot_functions import BaseDialogSlotFunctions
from munientry.controllers.view_modifiers import BaseDialogViewModifier
from munientry.data.cms_case_loaders import CmsNoChargeLoader
from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.models.template_types import TEMPLATE_DICT
from munientry.settings import (
    DAY_DICT,
    EVENT_DICT,
    PRETRIAL_TIME_DICT,
    SPEEDY_TRIAL_TIME_DICT,
    TODAY,
    TYPE_CHECKING,
)
from munientry.updaters.general_updaters import CaseInformationUpdater
from munientry.views.scheduling_entry_dialog_ui import Ui_SchedulingEntryDialog

if TYPE_CHECKING:
    from PyQt5.QtCore import QDate

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


class SchedulingEntryDialog(SchedulingBaseDialog, Ui_SchedulingEntryDialog):
    """The builder class for the Scheduling Entry Dialog."""

    def __init__(
        self, judicial_officer=None, cms_case=None, case_table=None, parent=None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = set_scheduling_dialog_name(self.sender())
        logger.info(f'Loaded Dialog: {self.dialog_name}')
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.setWindowTitle(f'{self.dialog_name} Case Information')
        self.entry_case_information = SchedulingCaseInformation()
        self.load_cms_data_to_view()
        self.functions.set_speedy_trial_date_label()
        self.functions.update_all_scheduled_dates()

    def load_cms_data_to_view(self):
        return CmsNoChargeLoader(self)

    def modify_view(self):
        return SchedulingEntryDialogViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = SchedulingEntryDialogSlotFunctions(self)
        SchedulingEntryDialogSignalConnector(self)

    def update_entry_case_information(self):
        return SchedulingEntryDialogCaseInformationUpdater(self)


class SchedulingEntryDialogViewModifier(BaseDialogViewModifier):
    """Class that sets and modifies the view for the Scheduling Entry Dialogs."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.arrest_summons_date_box.setDate(TODAY)
        self.dialog.trial_dateEdit.setDate(TODAY)
        self.dialog.plea_trial_date.setDate(TODAY)


class SchedulingEntryDialogSignalConnector(BaseDialogSignalConnector):
    """Class that connects all signals for the Scheduling Entry Dialogs."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.functions = dialog.functions
        self.connect_speedy_trial_items()
        self.connect_pretrial_radio_buttons()
        self.dialog.clear_fields_case_Button.released.connect(
            self.functions.clear_case_information_fields,
        )
        self.dialog.create_entry_Button.released.connect(self.functions.create_entry)
        self.dialog.close_dialog_Button.released.connect(self.dialog.functions.close_window)

    def connect_speedy_trial_items(self):
        self.dialog.arrest_summons_date_box.dateChanged.connect(
            self.functions.set_speedy_trial_date_label,
        )
        self.dialog.arrest_summons_date_box.dateChanged.connect(
            self.functions.update_all_scheduled_dates,
        )
        self.dialog.highest_charge_box.currentIndexChanged.connect(
            self.functions.set_speedy_trial_date_label,
        )
        self.dialog.days_in_jail_lineEdit.textChanged.connect(
            self.functions.set_speedy_trial_date_label,
        )
        self.dialog.continuance_days_lineEdit.textChanged.connect(
            self.functions.set_speedy_trial_date_label,
        )
        self.dialog.highest_charge_box.currentIndexChanged.connect(
            self.functions.update_all_scheduled_dates,
        )
        self.dialog.days_in_jail_lineEdit.textChanged.connect(
            self.functions.update_all_scheduled_dates,
        )
        self.dialog.continuance_days_lineEdit.textChanged.connect(
            self.functions.update_all_scheduled_dates,
        )

    def connect_scheduling_date_fields(self):
        """Only the final_pretrial_dateEdit field is connected.

        In order to update other date fields on data entry another solution is required because
        adding other connections creates a loop due to the signal sent when a date is changed.
        """
        self.dialog.final_pretrial_dateEdit.dateChanged.connect(
            self.functions.update_trial_and_pretrial_only,
        )

    def connect_pretrial_radio_buttons(self):
        """Local functions are only used to shorten line length to < 100 characters."""
        final_and_pretrial_update = self.functions.update_final_pretrial_and_pretrial_only
        set_pretrial = self.functions.set_pretrial_scheduled
        self.dialog.four_week_pretrial_radioButton.clicked.connect(final_and_pretrial_update)
        self.dialog.three_week_pretrial_radioButton.clicked.connect(final_and_pretrial_update)
        self.dialog.two_week_pretrial_radioButton.clicked.connect(final_and_pretrial_update)
        self.dialog.no_pretrial_radioButton.clicked.connect(final_and_pretrial_update)
        self.dialog.four_week_pretrial_radioButton.clicked.connect(set_pretrial)
        self.dialog.three_week_pretrial_radioButton.clicked.connect(set_pretrial)
        self.dialog.two_week_pretrial_radioButton.clicked.connect(set_pretrial)
        self.dialog.no_pretrial_radioButton.clicked.connect(set_pretrial)


class SchedulingEntryDialogSlotFunctions(BaseDialogSlotFunctions):
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
        if self.dialog.dialog_name == ROHRER_SCHEDULING_ENTRY:
            trial_date = self.set_trial_date('Tuesday', TRIAL)
            self.dialog.trial_dateEdit.setDate(trial_date)
            pretrial_date = self.set_event_date('Monday', PRETRIAL)
            self.dialog.pretrial_dateEdit.setDate(pretrial_date)
        elif self.dialog.dialog_name == HEMMETER_SCHEDULING_ENTRY:
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
            pretrial_date =  self.set_event_date('Wednesday', PRETRIAL)
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
        for button in [self.dialog.four_week_pretrial_radioButton, self.dialog.three_week_pretrial_radioButton,
                       self.dialog.two_week_pretrial_radioButton, self.dialog.no_pretrial_radioButton, ]:
            if button.isChecked():
                return PRETRIAL_TIME_DICT.get(button.text())

    def get_speedy_trial_date(self) -> 'QDate':
        speedy_trial_days = self.get_speedy_trial_days()
        days_in_jail = self.get_days_in_jail()
        continuance_days = self.get_continuance_days()
        speedy_trial_days = (speedy_trial_days + continuance_days) - days_in_jail
        speedy_trial_date = self.dialog.arrest_summons_date_box.date().addDays(speedy_trial_days)
        return speedy_trial_date

    def set_speedy_trial_date_label(self):
        speedy_trial_date = self.get_speedy_trial_date()
        speedy_trial_date = speedy_trial_date.toString(ENTRY_DATE_FORMAT)
        self.dialog.speedy_trial_date_label.setText(speedy_trial_date)

    def get_speedy_trial_days(self) -> int:
        key = self.dialog.highest_charge_box.currentText()
        speedy_trial_days = SPEEDY_TRIAL_TIME_DICT.get(key)
        return speedy_trial_days

    def get_days_in_jail(self) -> int:
        """Multiply days in jail times 3 for speedy trial calculations."""
        if self.dialog.days_in_jail_lineEdit.text() == "":
            days_in_jail = 0
        else:
            days_in_jail = int(self.dialog.days_in_jail_lineEdit.text())
        return 3 * days_in_jail

    def get_continuance_days(self) -> int:
        if self.dialog.continuance_days_lineEdit.text() == "":
            continuance_days = 0
        else:
            continuance_days = int(self.dialog.continuance_days_lineEdit.text())
        return continuance_days


class SchedulingEntryDialogCaseInformationUpdater(CaseInformationUpdater):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.view = dialog
        self.update_model_with_case_information_frame_data()

    def update_model_with_case_information_frame_data(self):
        """Calls the methods that update all model with all fields in the case information (top
        frame) in all main entry dialogs."""
        self.set_case_number_and_date()
        self.set_party_information()
        self.set_defense_counsel_information()
        self.set_scheduling_dates()

    def set_case_number_and_date(self):
        self.model.case_number = self.view.case_number_lineEdit.text()
        self.model.plea_trial_date = self.view.plea_trial_date.date().toString(ENTRY_DATE_FORMAT)

    def set_party_information(self):
        self.model.defendant.first_name = self.view.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.view.defendant_last_name_lineEdit.text()

    def set_defense_counsel_information(self):
        self.model.defense_counsel = self.view.defense_counsel_name_box.currentText()

    def set_scheduling_dates(self):
        self.model.trial_date = self.view.trial_dateEdit.date().toString(ENTRY_DATE_FORMAT)
        self.model.final_pretrial_date = self.view.final_pretrial_dateEdit.date().toString(
            ENTRY_DATE_FORMAT
        )
        self.model.pretrial_date = self.view.pretrial_dateEdit.date().toString(ENTRY_DATE_FORMAT)
        self.model.final_pretrial_time = self.view.final_pretrial_time_box.currentText()


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
