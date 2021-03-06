"""Module for building the view of the MainWindow."""
from PyQt5 import QtGui

from munientry.builders import bond_dialogs as bond
from munientry.builders import general_entry_dialogs as general_entry
from munientry.builders import plea_only_dialogs as plea_only
from munientry.builders import plea_sentence_dialogs as plea_sentence
from munientry.builders import sentencing_only_dialogs as sentencing_only
from munientry.builders.final_jury_hearing_notice_dialog import (
    FinalJuryNoticeHearingDialog,
)
from munientry.builders.general_hearing_notice_dialog import (
    GeneralNoticeOfHearingDialog,
)
from munientry.builders.sched_entry_dialogs import SchedulingEntryDialog
from munientry.builders.trial_to_court_hearing_notice_dialog import (
    TrialToCourtHearingDialog,
)
from munientry.models.party_types import JudicialOfficer
from munientry.settings import ICON_PATH, VERSION_NUMBER


class MainWindowViewModifier(object):
    """Class that modifies the view file."""

    def __init__(self, main_window: object) -> None:
        self.main_window = main_window
        self.main_window.setupUi(self.main_window)
        self.main_window.setWindowIcon(QtGui.QIcon(f'{ICON_PATH}gavel.ico'))
        self.main_window.setWindowTitle(f'MuniEntry - Version {VERSION_NUMBER}')
        self.main_window.judicial_officer_buttons_dict = self.connect_judicial_officers()
        self.main_window.crim_traffic_dialog_buttons_dict = (
            self.connect_crim_traffic_dialog_buttons()
        )
        self.main_window.scheduling_dialog_buttons_dict = self.connect_scheduling_dialog_buttons()
        self.main_window.daily_case_list_buttons_dict = self.connect_daily_case_list_radio_buttons()
        self.main_window.database_table_dict = self.connect_database_tables_to_daily_case_lists()
        self.main_window.radio_buttons_case_lists_dict = (
            self.connect_radio_buttons_to_daily_case_lists()
        )

    def connect_judicial_officers(self) -> dict:
        return {
            self.main_window.bunner_radioButton: JudicialOfficer('Amanda', 'Bunner', 'Magistrate'),
            self.main_window.pelanda_radioButton: JudicialOfficer('Kevin', 'Pelanda', 'Magistrate'),
            self.main_window.kudela_radioButton: JudicialOfficer('Justin', 'Kudela', 'Magistrate'),
            self.main_window.rohrer_radioButton: JudicialOfficer('Kyle', 'Rohrer', 'Judge'),
            self.main_window.hemmeter_radioButton: JudicialOfficer('Marianne', 'Hemmeter', 'Judge'),
            self.main_window.visiting_judge_radioButton:
                JudicialOfficer('None', 'Assigned', 'Judge'),
            self.main_window.dattilo_radioButton:
                JudicialOfficer('Pat', 'Dattilo', 'Assignment Commissioner'),
            self.main_window.patterson_radioButton:
                JudicialOfficer('Kathryn', 'Patterson', 'Assignment Commissioner'),
            self.main_window.none_radioButton:
                JudicialOfficer('None', 'Assigned', 'Assignment Commissioner'),
        }

    def connect_crim_traffic_dialog_buttons(self) -> dict:
        return {
            self.main_window.FineOnlyPleaButton: plea_sentence.FineOnlyPleaDialog,
            self.main_window.JailCCPleaButton: plea_sentence.JailCCPleaDialog,
            self.main_window.DiversionButton: plea_sentence.DiversionPleaDialog,
            self.main_window.NotGuiltyBondButton: plea_only.NotGuiltyBondDialog,
            self.main_window.FailureToAppearButton: general_entry.FailureToAppearDialog,
            self.main_window.ProbationViolationBondButton: bond.ProbationViolationBondDialog,
            self.main_window.BondHearingButton: bond.BondHearingDialog,
            self.main_window.PleaOnlyButton: plea_only.PleaOnlyDialog,
            self.main_window.NoPleaBondButton: bond.NoPleaBondDialog,
            self.main_window.LeapAdmissionButton: plea_only.LeapAdmissionPleaDialog,
            self.main_window.LeapAdmissionValidButton: plea_only.LeapPleaValidDialog,
            self.main_window.LeapSentencingButton: sentencing_only.LeapSentencingDialog,
            self.main_window.TrialSentencingButton: sentencing_only.TrialSentencingDialog,
            self.main_window.SentencingOnlyButton: sentencing_only.SentencingOnlyDialog,
            self.main_window.FreeformEntryButton: general_entry.FreeformDialog,
        }

    def connect_scheduling_dialog_buttons(self) -> dict:
        return {
            self.main_window.hemmeter_schedulingEntryButton: SchedulingEntryDialog,
            self.main_window.rohrer_schedulingEntryButton: SchedulingEntryDialog,
            self.main_window.hemmeter_final_jury_hearingButton: FinalJuryNoticeHearingDialog,
            self.main_window.rohrer_final_jury_hearingButton: FinalJuryNoticeHearingDialog,
            self.main_window.hemmeter_general_hearingButton: GeneralNoticeOfHearingDialog,
            self.main_window.rohrer_general_hearingButton: GeneralNoticeOfHearingDialog,
            self.main_window.hemmeter_trial_court_hearingButton: TrialToCourtHearingDialog,
            self.main_window.rohrer_trial_court_hearingButton: TrialToCourtHearingDialog,
        }

    def connect_daily_case_list_radio_buttons(self) -> dict:
        return{
            self.main_window.arraignments_radioButton: 'arraignments',
            self.main_window.slated_radioButton: 'slated',
            self.main_window.final_pretrial_radioButton: 'final_pretrials',
            self.main_window.pleas_radioButton: 'pleas',
            self.main_window.trials_to_court_radioButton: 'trials_to_court',
            self.main_window.pcvh_fcvh_radioButton: 'pcvh_fcvh',
        }

    def connect_database_tables_to_daily_case_lists(self) -> dict:
        return {
            'arraignments': self.main_window.arraignments_cases_box,
            'slated': self.main_window.slated_cases_box,
            'final_pretrials': self.main_window.final_pretrial_cases_box,
            'pleas': self.main_window.pleas_cases_box,
            'trials_to_court': self.main_window.trials_to_court_cases_box,
            'pcvh_fcvh': self.main_window.pcvh_fcvh_cases_box,
        }

    def connect_radio_buttons_to_daily_case_lists(self) -> dict:
        return {
            self.main_window.arraignments_radioButton: self.main_window.arraignments_cases_box,
            self.main_window.slated_radioButton: self.main_window.slated_cases_box,
            self.main_window.final_pretrial_radioButton: self.main_window.final_pretrial_cases_box,
            self.main_window.pleas_radioButton: self.main_window.pleas_cases_box,
            self.main_window.trials_to_court_radioButton:
                self.main_window.trials_to_court_cases_box,
            self.main_window.pcvh_fcvh_radioButton: self.main_window.pcvh_fcvh_cases_box,
        }
