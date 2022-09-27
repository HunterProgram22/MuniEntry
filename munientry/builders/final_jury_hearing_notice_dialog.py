"""Module containing classes for hearing notices."""
from loguru import logger

from munientry.builders.base_dialogs import BaseDialogSignalConnectorOld
from munientry.builders.scheduling.base_scheduling_builders import SchedulingBaseDialog
from munientry.builders.crimtraffic.base_crimtraffic_builders import BaseDialogViewModifier, \
    BaseDialogSlotFunctions
from munientry.controllers.helper_functions import set_assigned_judge, set_courtroom
from munientry.data.cms_case_loaders import CmsNoChargeLoader
from munientry.models.template_types import TEMPLATE_DICT
from munientry.settings import DAY_DICT, EVENT_DICT, TODAY, TYPE_CHECKING
from munientry.updaters.general_updaters import CaseInformationUpdater
from munientry.views.final_jury_notice_of_hearing_dialog_ui import (
    Ui_FinalJuryNoticeOfHearingDialog,
)

if TYPE_CHECKING:
    from PyQt5.QtCore import QDate
    from PyQt5.QtWidgets import QDialog


class FinalJuryNoticeHearingDialog(SchedulingBaseDialog, Ui_FinalJuryNoticeOfHearingDialog):
    """Builder class for the Final and Jury Trial Notice of Hearing.

    The judicial_officer for this entry is the selected Assignment Commissioner.

    The assigned_judge and courtroom is set by the button pressed choosing the dialog and entry.
    """

    def __init__(
        self, judicial_officer=None, cms_case=None, case_table=None, parent=None,
    ) -> None:
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.dialog_name = 'Final And Jury Notice Of Hearing Entry'
        logger.info(f'Loaded Dialog: {self.dialog_name}')
        self.assigned_judge = set_assigned_judge(self.sender())
        self.courtroom = set_courtroom(self.sender())
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.setWindowTitle(f'{self.dialog_name} Case Information - {self.assigned_judge}')
        self.hearing_location_box.setCurrentText(self.courtroom)
        self.set_instructions_label()

    def set_instructions_label(self) -> None:
        if self.assigned_judge == 'Judge Marianne T. Hemmeter':
            self.instructions_label.setText(
                'INSTRUCTIONS: Set the final pretrial date and the jury trial date will'
                + 'automatically update to the next Thursday.',
            )
        if self.assigned_judge == 'Judge Kyle E. Rohrer':
            self.instructions_label.setText(
                'INSTRUCTIONS: Set the final pretrial date and the jury trial date will'
                + 'automatically update to the next Tuesday.',
            )

    def load_cms_data_to_view(self) -> None:
        CmsNoChargeLoader(self)

    def _modify_view(self) -> None:
        FinalJuryNoticeHearingViewModifier(self)

    def _connect_signals_to_slots(self) -> None:
        self.functions = FinalJuryNoticeHearingSlotFunctions(self)
        FinalJuryNoticeHearingSignalConnector(self)

    def update_entry_case_information(self) -> None:
        FinalJuryNoticeHearingCaseInformationUpdater(self)


class FinalJuryNoticeHearingViewModifier(BaseDialogViewModifier):
    """Class that sets and modifies the view for the Final Jury Notice of Hearing."""

    def __init__(self, dialog: 'QDialog') -> None:
        super().__init__(dialog)
        self.dialog = dialog
        self.set_view_dates()

    def set_view_dates(self) -> None:
        self.dialog.plea_trial_date.setDate(TODAY)
        self.dialog.trial_dateEdit.setDate(TODAY)
        self.dialog.final_pretrial_dateEdit.setDate(TODAY)


class FinalJuryNoticeHearingSignalConnector(BaseDialogSignalConnectorOld):
    """Class that connects all signals for the Final Jury Notice of Hearing."""

    def __init__(self, dialog: 'QDialog') -> None:
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

    def update_trial_date(self) -> None:
        if self.dialog.assigned_judge == 'Judge Kyle E. Rohrer':
            trial_date = self.set_trial_date('Tuesday', 'Trial')
        if self.dialog.assigned_judge == 'Judge Marianne T. Hemmeter':
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

    def show_hide_final_pretrial(self) -> None:
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

    def __init__(self, dialog: 'QDialog') -> None:
        super().__init__(dialog)
        self.view = dialog
        self.update_model_with_case_information_frame_data()

    def update_model_with_case_information_frame_data(self) -> None:
        self.set_case_number_and_date()
        self.set_party_information()
        self.set_defense_counsel_information()
        self.set_scheduling_dates()
        self.model.assigned_judge = self.view.assigned_judge
        self.model.courtroom = self.view.courtroom
        self.model.judicial_officer = self.view.judicial_officer

    def set_case_number_and_date(self) -> None:
        self.model.case_number = self.view.case_number_lineEdit.text()
        self.model.plea_trial_date = self.view.plea_trial_date.date().toString('MMMM dd, yyyy')

    def set_party_information(self) -> None:
        self.model.defendant.first_name = self.view.defendant_first_name_lineEdit.text()
        self.model.defendant.last_name = self.view.defendant_last_name_lineEdit.text()

    def set_defense_counsel_information(self) -> None:
        self.model.defense_counsel = self.view.defense_counsel_name_box.currentText()

    def set_scheduling_dates(self) -> None:
        self.model.hearing_location = self.view.hearing_location_box.currentText()
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
