"""Module for building the view of the MainWindow."""
from PyQt6.QtGui import QIcon

from munientry.builders.administrative import (
    admin_fiscal_dialog,
    driving_privileges_dialog,
    jury_payment_dialog,
)
from munientry.builders.civil import (
    civ_freeform_dialog,
)
from munientry.builders.crimtraffic import (
    arraignment_continue_dialog,
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
from munientry.builders.workflows import bunner_dw_dialog as bunner
from munientry.builders.workflows import hemmeter_dw_dialog as hemmeter
from munientry.builders.workflows import probation_dw_dialogs as probation
from munientry.builders.workflows import rohrer_dw_dialog as rohrer
from munientry.models.party_types import JudicialOfficer
from munientry.appsettings.paths import ICON_PATH
from munientry.appsettings.settings import VERSION_NUMBER


class MainWindowViewModifier(object):
    """Class that modifies the view file."""

    def __init__(self, mainwindow: object) -> None:
        self.mainwindow = mainwindow
        self.mainwindow.setupUi(self.mainwindow)
        self.create_daily_case_lists()
        self.mainwindow.setWindowIcon(QIcon(f'{ICON_PATH}gavel.ico'))
        self.mainwindow.setWindowTitle(f'MuniEntry - Version {VERSION_NUMBER}')
        self.mainwindow.judicial_officer_buttons_dict = self.connect_judicial_officers()
        self.mainwindow.dialog_buttons_dict = self.connect_dialog_buttons()
        self.mainwindow.daily_case_lists = [
            self.mainwindow.arraignments_cases_box,
            self.mainwindow.slated_cases_box,
            self.mainwindow.pleas_cases_box,
            self.mainwindow.pcvh_fcvh_cases_box,
            self.mainwindow.final_pretrial_cases_box,
            self.mainwindow.trials_to_court_cases_box,
        ]

    def connect_judicial_officers(self) -> dict:
        return {
            self.mainwindow.bunner_radioButton: JudicialOfficer('Amanda', 'Bunner', 'Magistrate'),
            self.mainwindow.pelanda_radioButton: JudicialOfficer('Kevin', 'Pelanda', 'Magistrate'),
            self.mainwindow.kudela_radioButton: JudicialOfficer('Justin', 'Kudela', 'Magistrate'),
            self.mainwindow.rohrer_radioButton: JudicialOfficer('Kyle', 'Rohrer', 'Judge'),
            self.mainwindow.hemmeter_radioButton: JudicialOfficer('Marianne', 'Hemmeter', 'Judge'),
            self.mainwindow.visiting_judge_radioButton:
                JudicialOfficer('None', 'Assigned', 'Judge'),
            self.mainwindow.dattilo_radioButton:
                JudicialOfficer('Pat', 'Dattilo', 'Assignment Commissioner'),
            self.mainwindow.patterson_radioButton:
                JudicialOfficer('Kathryn', 'Patterson', 'Assignment Commissioner'),
            self.mainwindow.none_radioButton:
                JudicialOfficer('None', 'Assigned', 'Assignment Commissioner'),
            self.mainwindow.assn_comm_dattilo_radioButton:
                JudicialOfficer('Pat', 'Dattilo', 'Assignment Commissioner'),
            self.mainwindow.assn_comm_patterson_radioButton:
                JudicialOfficer('Kathryn', 'Patterson', 'Assignment Commissioner'),
            self.mainwindow.court_admin_kudela_radioButton:
                JudicialOfficer('Justin', 'Kudela', 'Court Administrator'),
            self.mainwindow.jury_comm_patterson_radioButton:
                JudicialOfficer('Kathryn', 'Patterson', 'Jury Commissioner'),
            self.mainwindow.none_admin_radioButton:
                JudicialOfficer('None', 'Assigned', 'Admin Staff Person'),
            self.mainwindow.bunner_admin_radioButton:
                JudicialOfficer('A', 'B', 'Admin Staff Person'),
        }

    def connect_dialog_buttons(self):
        return {
            ###CrimTraffic###
            self.mainwindow.ArraignmentContinueButton:
                arraignment_continue_dialog.ArraignmentContinueDialog,
            self.mainwindow.FineOnlyPleaButton: fine_only_plea_dialog.FineOnlyPleaDialog,
            self.mainwindow.JailCCPleaButton: jail_cc_plea_dialog.JailCCPleaDialog,
            self.mainwindow.DiversionButton: diversion_dialog.DiversionPleaDialog,
            self.mainwindow.NotGuiltyBondButton: not_guilty_bond_dialog.NotGuiltyBondDialog,
            self.mainwindow.FailureToAppearButton: failure_to_appear_dialog.FailureToAppearDialog,
            self.mainwindow.ProbationViolationBondButton:
                probation_violation_bond_dialog.ProbationViolationBondDialog,
            self.mainwindow.BondHearingButton: bond_hearing_dialog.BondHearingDialog,
            self.mainwindow.PleaOnlyButton: plea_only_future_sentence_dialog.PleaOnlyDialog,
            self.mainwindow.NoPleaBondButton: no_plea_bond_dialog.NoPleaBondDialog,
            self.mainwindow.LeapAdmissionButton: leap_plea_dialog.LeapAdmissionPleaDialog,
            self.mainwindow.LeapAdmissionValidButton: leap_plea_valid_dialog.LeapPleaValidDialog,
            self.mainwindow.LeapSentencingButton: leap_sentencing_dialog.LeapSentencingDialog,
            self.mainwindow.TrialSentencingButton: trial_sentencing_dialog.TrialSentencingDialog,
            self.mainwindow.SentencingOnlyButton: sentencing_only_dialog.SentencingOnlyDialog,
            self.mainwindow.FreeformEntryButton: freeform_dialog.FreeformDialog,

            ###Civil###
            self.mainwindow.CivFreeformEntryButton: civ_freeform_dialog.CivFreeformDialog,

            ###Scheduling###
            self.mainwindow.hemmeter_schedulingEntryButton:
                sched_entry_dialogs.SchedulingEntryDialog,
            self.mainwindow.rohrer_schedulingEntryButton:
                sched_entry_dialogs.SchedulingEntryDialog,
            self.mainwindow.hemmeter_final_jury_hearingButton:
                final_jury_hearing_notice_dialog.FinalJuryNoticeHearingDialog,
            self.mainwindow.rohrer_final_jury_hearingButton:
                final_jury_hearing_notice_dialog.FinalJuryNoticeHearingDialog,
            self.mainwindow.hemmeter_general_hearingButton:
                general_hearing_notice_dialog.GeneralNoticeOfHearingDialog,
            self.mainwindow.rohrer_general_hearingButton:
                general_hearing_notice_dialog.GeneralNoticeOfHearingDialog,
            self.mainwindow.hemmeter_trial_court_hearingButton:
                trial_to_court_hearing_notice_dialog.TrialToCourtHearingDialog,
            self.mainwindow.rohrer_trial_court_hearingButton:
                trial_to_court_hearing_notice_dialog.TrialToCourtHearingDialog,

            ###Admin###
            self.mainwindow.limited_driving_privilegesButton:
                driving_privileges_dialog.DrivingPrivilegesDialog,
            self.mainwindow.juror_paymentButton: jury_payment_dialog.JuryPaymentDialog,
            self.mainwindow.fiscal_entriesButton: admin_fiscal_dialog.AdminFiscalDialog,

            ###Workflow###
            self.mainwindow.hemmeter_workflowButton: hemmeter.HemmeterWorkflowDialog,
            self.mainwindow.rohrer_workflowButton: rohrer.RohrerWorkflowDialog,
            self.mainwindow.bunner_workflowButton: bunner.BunnerWorkflowDialog,
            self.mainwindow.pretrial_workflowButton: probation.PretrialWorkflowDialog,
            self.mainwindow.community_control_workflowButton: probation.ComControlWorkflowDialog,

        }

    def create_daily_case_lists(self) -> None:
        self.mainwindow.arraignments_cases_box.setup_combo_box(
            'arraignments',
            self.mainwindow.arraignments_radioButton,
            self.mainwindow,
        )
        self.mainwindow.slated_cases_box.setup_combo_box(
            'slated',
            self.mainwindow.slated_radioButton,
            self.mainwindow,
        )
        self.mainwindow.final_pretrial_cases_box.setup_combo_box(
            'final_pretrials',
            self.mainwindow.final_pretrial_radioButton,
            self.mainwindow,
        )
        self.mainwindow.pleas_cases_box.setup_combo_box(
            'pleas',
            self.mainwindow.pleas_radioButton,
            self.mainwindow,
        )
        self.mainwindow.trials_to_court_cases_box.setup_combo_box(
            'trials_to_court',
            self.mainwindow.trials_to_court_radioButton,
            self.mainwindow,
        )
        self.mainwindow.pcvh_fcvh_cases_box.setup_combo_box(
            'pcvh_fcvh',
            self.mainwindow.pcvh_fcvh_radioButton,
            self.mainwindow,
        )
