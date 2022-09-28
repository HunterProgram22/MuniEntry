"""Module for building the view of the MainWindow."""
import munientry.builders.crimtraffic.bond_hearing_dialog
import munientry.builders.crimtraffic.failure_to_appear_dialog
import munientry.builders.crimtraffic.freeform_dialog
import munientry.builders.crimtraffic.leap_plea_valid_dialog
import munientry.builders.crimtraffic.leap_sentencing_dialog
import munientry.builders.crimtraffic.no_plea_bond_dialog
import munientry.builders.crimtraffic.probation_violation_bond_dialog
import munientry.builders.crimtraffic.sentencing_only_dialog
import munientry.builders.crimtraffic.trial_sentencing_dialog
from PyQt5 import QtGui

from munientry.builders.scheduling.final_jury_hearing_notice_dialog import (
    FinalJuryNoticeHearingDialog,
)
from munientry.builders.scheduling.general_hearing_notice_dialog import (
    GeneralNoticeOfHearingDialog,
)
from munientry.builders.scheduling.driving_privileges_dialog import DrivingPrivilegesDialog
from munientry.builders.scheduling.sched_entry_dialogs import SchedulingEntryDialog
from munientry.builders.scheduling.trial_to_court_hearing_notice_dialog import (
    TrialToCourtHearingDialog,
)
from munientry.models.party_types import JudicialOfficer
from munientry.settings import ICON_PATH, VERSION_NUMBER
import munientry.builders.crimtraffic.fine_only_plea_dialog
import munientry.builders.crimtraffic.diversion_dialog
import munientry.builders.crimtraffic.jail_cc_plea_dialog
import munientry.builders.crimtraffic.leap_plea_dialog
import munientry.builders.crimtraffic.not_guilty_bond_dialog
import munientry.builders.crimtraffic.plea_only_future_sentence_dialog


class MainWindowViewModifier(object):
    """Class that modifies the view file."""

    def __init__(self, main_window: object) -> None:
        self.main_window = main_window
        self.main_window.setupUi(self.main_window)
        self.create_daily_case_lists()
        self.main_window.setWindowIcon(QtGui.QIcon(f'{ICON_PATH}gavel.ico'))
        self.main_window.setWindowTitle(f'MuniEntry - Version {VERSION_NUMBER}')
        self.main_window.judicial_officer_buttons_dict = self.connect_judicial_officers()
        self.main_window.crim_traffic_dialog_buttons_dict = (
            self.connect_crim_traffic_dialog_buttons()
        )
        self.main_window.scheduling_dialog_buttons_dict = self.connect_scheduling_dialog_buttons()
        self.main_window.daily_case_lists = [
            self.main_window.arraignments_cases_box,
            self.main_window.slated_cases_box,
            self.main_window.pleas_cases_box,
            self.main_window.pcvh_fcvh_cases_box,
            self.main_window.final_pretrial_cases_box,
            self.main_window.trials_to_court_cases_box,
        ]

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
            self.main_window.FineOnlyPleaButton: munientry.builders.crimtraffic.fine_only_plea_dialog.FineOnlyPleaDialog,
            self.main_window.JailCCPleaButton: munientry.builders.crimtraffic.jail_cc_plea_dialog.JailCCPleaDialog,
            self.main_window.DiversionButton: munientry.builders.crimtraffic.diversion_dialog.DiversionPleaDialog,
            self.main_window.NotGuiltyBondButton: munientry.builders.crimtraffic.not_guilty_bond_dialog.NotGuiltyBondDialog,
            self.main_window.FailureToAppearButton: munientry.builders.crimtraffic.failure_to_appear_dialog.FailureToAppearDialog,
            self.main_window.ProbationViolationBondButton: munientry.builders.crimtraffic.probation_violation_bond_dialog.ProbationViolationBondDialog,
            self.main_window.BondHearingButton: munientry.builders.crimtraffic.bond_hearing_dialog.BondHearingDialog,
            self.main_window.PleaOnlyButton: munientry.builders.crimtraffic.plea_only_future_sentence_dialog.PleaOnlyDialog,
            self.main_window.NoPleaBondButton: munientry.builders.crimtraffic.no_plea_bond_dialog.NoPleaBondDialog,
            self.main_window.LeapAdmissionButton: munientry.builders.crimtraffic.leap_plea_dialog.LeapAdmissionPleaDialog,
            self.main_window.LeapAdmissionValidButton: munientry.builders.crimtraffic.leap_plea_valid_dialog.LeapPleaValidDialog,
            self.main_window.LeapSentencingButton: munientry.builders.crimtraffic.leap_sentencing_dialog.LeapSentencingDialog,
            self.main_window.TrialSentencingButton: munientry.builders.crimtraffic.trial_sentencing_dialog.TrialSentencingDialog,
            self.main_window.SentencingOnlyButton: munientry.builders.crimtraffic.sentencing_only_dialog.SentencingOnlyDialog,
            self.main_window.FreeformEntryButton: munientry.builders.crimtraffic.freeform_dialog.FreeformDialog,
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
            self.main_window.limited_driving_privilegesButton: DrivingPrivilegesDialog,
        }

    def create_daily_case_lists(self) -> None:
        self.main_window.arraignments_cases_box.setup_combo_box(
            'arraignments',
            self.main_window.arraignments_radioButton,
            self.main_window,
        )
        self.main_window.slated_cases_box.setup_combo_box(
            'slated',
            self.main_window.slated_radioButton,
            self.main_window,
        )
        self.main_window.final_pretrial_cases_box.setup_combo_box(
            'final_pretrials',
            self.main_window.final_pretrial_radioButton,
            self.main_window,
        )
        self.main_window.pleas_cases_box.setup_combo_box(
            'pleas',
            self.main_window.pleas_radioButton,
            self.main_window,
        )
        self.main_window.trials_to_court_cases_box.setup_combo_box(
            'trials_to_court',
            self.main_window.trials_to_court_radioButton,
            self.main_window,
        )
        self.main_window.pcvh_fcvh_cases_box.setup_combo_box(
            'pcvh_fcvh',
            self.main_window.pcvh_fcvh_radioButton,
            self.main_window,
        )
