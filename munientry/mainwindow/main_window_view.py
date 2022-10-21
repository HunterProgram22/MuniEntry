"""Module for building the view of the MainWindow."""
from PyQt6 import QtGui

from munientry.builders.administrative import (
    driving_privileges_dialog,
    admin_fiscal_dialog,
)
from munientry.builders.crimtraffic import (
    bond_hearing_dialog,
    diversion_dialog,
    failure_to_appear_dialog,
    fine_only_plea_dialog,
    freeform_dialog,
    jail_cc_plea_dialog,
    leap_plea_dialog,
    leap_plea_valid_dialog,
    leap_sentencing_dialog,
    no_plea_bond_dialog,
    not_guilty_bond_dialog,
    plea_only_future_sentence_dialog,
    probation_violation_bond_dialog,
    sentencing_only_dialog,
    trial_sentencing_dialog,
)
from munientry.builders.scheduling import (
    final_jury_hearing_notice_dialog,
    general_hearing_notice_dialog,
    sched_entry_dialogs,
    trial_to_court_hearing_notice_dialog,
)
from munientry.digitalworkflow import hemmeter_dw_dialog as hemmeter
from munientry.digitalworkflow import bunner_dw_dialog as bunner
from munientry.digitalworkflow import rohrer_dw_dialog as rohrer
from munientry.digitalworkflow import probation_dw_dialog as probation
from munientry.models.party_types import JudicialOfficer
from munientry.settings import ICON_PATH, VERSION_NUMBER


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
        self.main_window.admin_dialog_buttons_dict = self.connect_admin_dialog_buttons()
        self.main_window.admin_dialog_no_case_buttons_dict = self.connect_admin_no_case_dialog_buttons()
        self.main_window.digital_workflow_buttons_dict = self.connect_digital_workflow_dialog_buttons()
        self.main_window.probation_workflow_buttons_dict = self.connect_probation_workflow_dialog_buttons()
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
            self.main_window.assn_comm_dattilo_radioButton:
                JudicialOfficer('Pat', 'Dattilo', 'Assignment Commissioner'),
            self.main_window.assn_comm_patterson_radioButton:
                JudicialOfficer('Kathryn', 'Patterson', 'Assignment Commissioner'),
            self.main_window.court_admin_kudela_radioButton:
                JudicialOfficer('Justin', 'Kudela', 'Court Administrator'),
            self.main_window.jury_comm_patterson_radioButton:
                JudicialOfficer('Kathryn', 'Patterson', 'Jury Commissioner'),
        }

    def connect_crim_traffic_dialog_buttons(self) -> dict:
        return {
            self.main_window.FineOnlyPleaButton: fine_only_plea_dialog.FineOnlyPleaDialog,
            self.main_window.JailCCPleaButton: jail_cc_plea_dialog.JailCCPleaDialog,
            self.main_window.DiversionButton: diversion_dialog.DiversionPleaDialog,
            self.main_window.NotGuiltyBondButton: not_guilty_bond_dialog.NotGuiltyBondDialog,
            self.main_window.FailureToAppearButton: failure_to_appear_dialog.FailureToAppearDialog,
            self.main_window.ProbationViolationBondButton:
                probation_violation_bond_dialog.ProbationViolationBondDialog,
            self.main_window.BondHearingButton: bond_hearing_dialog.BondHearingDialog,
            self.main_window.PleaOnlyButton: plea_only_future_sentence_dialog.PleaOnlyDialog,
            self.main_window.NoPleaBondButton: no_plea_bond_dialog.NoPleaBondDialog,
            self.main_window.LeapAdmissionButton: leap_plea_dialog.LeapAdmissionPleaDialog,
            self.main_window.LeapAdmissionValidButton: leap_plea_valid_dialog.LeapPleaValidDialog,
            self.main_window.LeapSentencingButton: leap_sentencing_dialog.LeapSentencingDialog,
            self.main_window.TrialSentencingButton: trial_sentencing_dialog.TrialSentencingDialog,
            self.main_window.SentencingOnlyButton: sentencing_only_dialog.SentencingOnlyDialog,
            self.main_window.FreeformEntryButton: freeform_dialog.FreeformDialog,
        }

    def connect_scheduling_dialog_buttons(self) -> dict:
        return {
            self.main_window.hemmeter_schedulingEntryButton:
                sched_entry_dialogs.SchedulingEntryDialog,
            self.main_window.rohrer_schedulingEntryButton:
                sched_entry_dialogs.SchedulingEntryDialog,
            self.main_window.hemmeter_final_jury_hearingButton:
                final_jury_hearing_notice_dialog.FinalJuryNoticeHearingDialog,
            self.main_window.rohrer_final_jury_hearingButton:
                final_jury_hearing_notice_dialog.FinalJuryNoticeHearingDialog,
            self.main_window.hemmeter_general_hearingButton:
                general_hearing_notice_dialog.GeneralNoticeOfHearingDialog,
            self.main_window.rohrer_general_hearingButton:
                general_hearing_notice_dialog.GeneralNoticeOfHearingDialog,
            self.main_window.hemmeter_trial_court_hearingButton:
                trial_to_court_hearing_notice_dialog.TrialToCourtHearingDialog,
            self.main_window.rohrer_trial_court_hearingButton:
                trial_to_court_hearing_notice_dialog.TrialToCourtHearingDialog,
        }

    def connect_admin_dialog_buttons(self) -> dict:
        return {
            self.main_window.limited_driving_privilegesButton:
                driving_privileges_dialog.DrivingPrivilegesDialog,
        }

    def connect_admin_no_case_dialog_buttons(self) -> dict:
        return {
            self.main_window.fiscal_entriesButton:
                admin_fiscal_dialog.AdminFiscalDialog,
        }

    def connect_digital_workflow_dialog_buttons(self) -> dict:
        return {
            self.main_window.hemmeter_workflowButton:
                hemmeter.HemmeterWorkflowDialog,
            self.main_window.rohrer_workflowButton:
                rohrer.RohrerWorkflowDialog,
            self.main_window.bunner_workflowButton:
                bunner.BunnerWorkflowDialog,
        }

    def connect_probation_workflow_dialog_buttons(self) -> dict:
        return {
            self.main_window.probation_workflowButton:
                probation.ProbationWorkflowDialog,
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
