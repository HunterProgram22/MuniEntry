"""Module for creating the dialog dictionary."""
from munientry.builders.administrative import (
    admin_fiscal_dialog,
    driving_privileges_dialog,
    jury_payment_dialog,
)
from munientry.builders.civil import civ_freeform_dialog
from munientry.builders.crimtraffic import (
    arraignment_continue_dialog,
    bond_hearing_dialog,
    criminal_sealing_dialog,
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
from munientry.builders.workflows import admin_judge_dw_dialog as hemmeter
from munientry.builders.workflows import bunner_dw_dialog as bunner
from munientry.builders.workflows import probation_dw_dialogs as probation
from munientry.builders.workflows import rohrer_dw_dialog as rohrer


class DialogDict(object):
    """A container class for the mapping of all dialog buttons to their dialog."""

    def __init__(self, mainwindow):
        self.mw = mainwindow

    def create_dialog_button_dict(self):
        return {
            # CrimTraffic
            self.mw.ArraignmentContinueButton:
                arraignment_continue_dialog.ArraignmentContinueDialog,
            # self.mw.FineOnlyPleaButton: fine_only_plea_dialog.FineOnlyPleaDialog,
            # self.mw.JailCCPleaButton: jail_cc_plea_dialog.JailCCPleaDialog,
            self.mw.DiversionButton: diversion_dialog.DiversionPleaDialog,
            self.mw.NotGuiltyBondButton: not_guilty_bond_dialog.NotGuiltyBondDialog,
            self.mw.FailureToAppearButton: failure_to_appear_dialog.FailureToAppearDialog,
            self.mw.ProbationViolationBondButton:
                probation_violation_bond_dialog.ProbationViolationBondDialog,
            self.mw.BondHearingButton: bond_hearing_dialog.BondHearingDialog,
            self.mw.PleaOnlyButton: plea_only_future_sentence_dialog.PleaOnlyDialog,
            self.mw.NoPleaBondButton: no_plea_bond_dialog.NoPleaBondDialog,
            self.mw.LeapAdmissionButton: leap_plea_dialog.LeapAdmissionPleaDialog,
            self.mw.LeapAdmissionValidButton: leap_plea_valid_dialog.LeapPleaValidDialog,
            self.mw.LeapSentencingButton: leap_sentencing_dialog.LeapSentencingDialog,
            self.mw.TrialSentencingButton: trial_sentencing_dialog.TrialSentencingDialog,
            self.mw.SentencingOnlyButton: sentencing_only_dialog.SentencingOnlyDialog,
            self.mw.FreeformEntryButton: freeform_dialog.FreeformDialog,
            self.mw.CriminalSealingButton: criminal_sealing_dialog.CriminalSealingDialog,

            # Civil
            self.mw.CivFreeformEntryButton: civ_freeform_dialog.CivFreeformDialog,

            # Scheduling
            self.mw.hemmeter_schedulingEntryButton:
                sched_entry_dialogs.SchedulingEntryDialog,
            self.mw.rohrer_schedulingEntryButton:
                sched_entry_dialogs.SchedulingEntryDialog,
            self.mw.hemmeter_final_jury_hearingButton:
                final_jury_hearing_notice_dialog.FinalJuryNoticeHearingDialog,
            self.mw.rohrer_final_jury_hearingButton:
                final_jury_hearing_notice_dialog.FinalJuryNoticeHearingDialog,
            self.mw.hemmeter_general_hearingButton:
                general_hearing_notice_dialog.GeneralNoticeOfHearingDialog,
            self.mw.rohrer_general_hearingButton:
                general_hearing_notice_dialog.GeneralNoticeOfHearingDialog,
            self.mw.hemmeter_trial_court_hearingButton:
                trial_to_court_hearing_notice_dialog.TrialToCourtHearingDialog,
            self.mw.rohrer_trial_court_hearingButton:
                trial_to_court_hearing_notice_dialog.TrialToCourtHearingDialog,

            # Admin
            self.mw.limited_driving_privilegesButton:
                driving_privileges_dialog.DrivingPrivilegesDialog,
            self.mw.juror_paymentButton: jury_payment_dialog.JuryPaymentDialog,
            self.mw.fiscal_entriesButton: admin_fiscal_dialog.AdminFiscalDialog,

            # Workflow
            self.mw.admin_workflowButton: hemmeter.AdminWorkflowDialog,
            self.mw.rohrer_workflowButton: rohrer.RohrerWorkflowDialog,
            self.mw.bunner_workflowButton: bunner.BunnerWorkflowDialog,
            self.mw.pretrial_workflowButton: probation.PretrialWorkflowDialog,
            self.mw.community_control_workflowButton: probation.ComControlWorkflowDialog,
        }
