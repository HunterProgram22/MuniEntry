"""Module containing classes for hearing notices."""
from loguru import logger

from munientry.builders.base_dialogs import SchedulingBaseDialog
from munientry.controllers.signal_connectors import BaseDialogSignalConnector
from munientry.controllers.slot_functions import BaseDialogSlotFunctions
from munientry.controllers.view_modifiers import BaseDialogViewModifier
from munientry.data.cms_case_loaders import CmsNoChargeLoader
from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.models.template_types import TEMPLATE_DICT
from munientry.settings import DAY_DICT, EVENT_DICT, TODAY, TYPE_CHECKING
from munientry.updaters.general_updaters import CaseInformationUpdater
from munientry.views.final_jury_notice_of_hearing_dialog_ui import (
    Ui_FinalJuryNoticeOfHearingDialog,
)

if TYPE_CHECKING:
    from PyQt5.QtCore import QDate

    from munientry.models.party_types import JudicialOfficer


class FinalJuryNoticeHearingDialog(SchedulingBaseDialog, Ui_FinalJuryNoticeOfHearingDialog):
    """Builder class for the Final and Jury Trial Notice of Hearing.

    The judicial_officer for this entry is the selected Assignment Commissioner.

    The assigned_judge is set by the button pressed choosing the dialog and entry.
    """

    def __init__(
        self, judicial_officer=None, cms_case=None, case_table=None, parent=None,
    ):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Final And Jury Notice Of Hearing Entry'
        logger.info(f'Loaded Dialog: {self.dialog_name}')

        self.assigned_judge = set_assigned_judge(self.sender())
        logger.debug(self.sender())

        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.setWindowTitle(f'{self.dialog_name} Case Information - {self.assigned_judge}')

    def load_cms_data_to_view(self):
        return CmsNoChargeLoader(self)

    def modify_view(self):
        return FinalJuryNoticeHearingViewModifier(self)

    def connect_signals_to_slots(self) -> None:
        self.functions = FinalJuryNoticeHearingSlotFunctions(self)
        FinalJuryNoticeHearingSignalConnector(self)

    def update_entry_case_information(self):
        return FinalJuryNoticeHearingCaseInformationUpdater(self)


class FinalJuryNoticeHearingViewModifier(BaseDialogViewModifier):
    """Class that sets and modifies the view for the Final Jury Notice of Hearing."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.set_view_dates()

    def set_view_dates(self):
        self.dialog.plea_trial_date.setDate(TODAY)
        self.dialog.trial_dateEdit.setDate(TODAY)
        self.dialog.final_pretrial_dateEdit.setDate(TODAY)


class FinalJuryNoticeHearingSignalConnector(BaseDialogSignalConnector):
    """Class that connects all signals for the Final Jury Notice of Hearing."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog = dialog
        self.functions = dialog.functions
        self.dialog.clear_fields_case_Button.released.connect(
            self.functions.clear_case_information_fields,
        )
        self.dialog.create_entry_Button.released.connect(self.functions.create_entry)
        self.dialog.close_dialog_Button.released.connect(self.dialog.functions.close_window)
        self.dialog.jury_trial_only_no_radioButton.toggled.connect(
            self.functions.show_hide_final_pretrial,
        )
        self.dialog.jury_trial_only_yes_radioButton.toggled.connect(
            self.functions.show_hide_final_pretrial,
        )
        self.dialog.final_pretrial_dateEdit.dateChanged.connect(
            self.functions.update_trial_date,
        )


class FinalJuryNoticeHearingSlotFunctions(BaseDialogSlotFunctions):
    """Class for that contains all signals for the Final Jury Notice of Hearing."""

    def update_trial_date(self):
        if self.dialog.judicial_officer.last_name == 'Rohrer':
            trial_date = self.set_trial_date('Tuesday', 'Trial')
        if self.dialog.judicial_officer.last_name == 'Hemmeter':
            trial_date = self.set_trial_date('Thursday', 'Trial')
        try:
            self.dialog.trial_dateEdit.setDate(trial_date)
        except UnboundLocalError as error:
            logger.warning(error)

    def set_trial_date(self, day_to_set: str, event_to_set: str) -> 'QDate':
        days_to_event = EVENT_DICT.get(event_to_set)
        event_date = self.dialog.final_pretrial_dateEdit.date().addDays(days_to_event)
        while event_date.dayOfWeek() != DAY_DICT.get(day_to_set):
            event_date = event_date.addDays(1)
        return event_date

    def show_hide_final_pretrial(self):
        if self.dialog.jury_trial_only_no_radioButton.isChecked():
            self.dialog.final_pretrial_dateEdit.setHidden(False)
            self.dialog.final_pretrial_date_label.setHidden(False)
            self.dialog.final_pretrial_time_label.setHidden(False)
            self.dialog.final_pretrial_time_box.setHidden(False)
        else:
            self.dialog.final_pretrial_dateEdit.setHidden(True)
            self.dialog.final_pretrial_date_label.setHidden(True)
            self.dialog.final_pretrial_time_label.setHidden(True)
            self.dialog.final_pretrial_time_box.setHidden(True)


class FinalJuryNoticeHearingCaseInformationUpdater(CaseInformationUpdater):
    """Class for that sets the Case Information model for the Final Jury Notice of Hearing."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.view = dialog
        self.update_model_with_case_information_frame_data()

    def update_model_with_case_information_frame_data(self):
        self.set_case_number_and_date()
        self.set_party_information()
        self.set_defense_counsel_information()
        self.set_scheduling_dates()

    def set_case_number_and_date(self):
        self.model.case_number = self.view.case_number_lineEdit.text()
        self.model.plea_trial_date = self.view.plea_trial_date.date().toString('MMMM dd, yyyy')

    def set_party_information(self):
        self.model.defendant.first_name = self.view.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.view.defendant_last_name_lineEdit.text()

    def set_defense_counsel_information(self):
        self.model.defense_counsel = self.view.defense_counsel_name_box.currentText()

    def set_scheduling_dates(self):
        self.model.trial_date = self.view.trial_dateEdit.date().toString('MMMM dd, yyyy')
        self.model.final_pretrial_date = self.view.final_pretrial_dateEdit.date().toString(
            'MMMM dd, yyyy',
        )
        self.model.final_pretrial_time = self.view.final_pretrial_time_box.currentText()
        if self.view.jury_trial_only_no_radioButton.isChecked():
            self.model.jury_trial_only = 'No'
        elif self.view.jury_trial_only_yes_radioButton.isChecked():
            self.model.jury_trial_only = 'Yes'


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
