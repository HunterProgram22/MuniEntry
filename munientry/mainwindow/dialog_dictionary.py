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
from munientry.builders.probation import terms_comm_control_dialog, notice_cc_violation_dialog
from munientry.dialogs.workflows import admin_judge_dw_dialog as admin
from munientry.dialogs.workflows import probation_dw_dialogs as probation

DIALOG_BUTTON_DICT = {
    'FineOnlyPleaButton': fine_only_plea_dialog.FineOnlyPleaDialog,
    'JailCCPleaButton': jail_cc_plea_dialog.JailCCPleaDialog,
    'ArraignmentContinueButton': arraignment_continue_dialog.ArraignmentContinueDialog,
    'DiversionButton': diversion_dialog.DiversionPleaDialog,
    'NotGuiltyBondButton': not_guilty_bond_dialog.NotGuiltyBondDialog,
    'FailureToAppearButton': failure_to_appear_dialog.FailureToAppearDialog,
    'ProbationViolationBondButton': probation_violation_bond_dialog.ProbationViolationBondDialog,
    'BondHearingButton': bond_hearing_dialog.BondHearingDialog,
    'PleaOnlyButton': plea_only_future_sentence_dialog.PleaOnlyDialog,
    'NoPleaBondButton': no_plea_bond_dialog.NoPleaBondDialog,
    'LeapAdmissionButton': leap_plea_dialog.LeapAdmissionPleaDialog,
    'LeapAdmissionValidButton': leap_plea_valid_dialog.LeapPleaValidDialog,
    'LeapSentencingButton': leap_sentencing_dialog.LeapSentencingDialog,
    'TrialSentencingButton': trial_sentencing_dialog.TrialSentencingDialog,
    'SentencingOnlyButton': sentencing_only_dialog.SentencingOnlyDialog,
    'FreeformEntryButton': freeform_dialog.FreeformDialog,
    'CriminalSealingButton': criminal_sealing_dialog.CriminalSealingDialog,

    # Civil
    'CivFreeformEntryButton': civ_freeform_dialog.CivFreeformDialog,

    # Scheduling
    'hemmeter_schedulingEntryButton': sched_entry_dialogs.SchedulingEntryDialog,
    'rohrer_schedulingEntryButton': sched_entry_dialogs.SchedulingEntryDialog,
    'hemmeter_final_jury_hearingButton': final_jury_hearing_notice_dialog.FinalJuryNoticeHearingDialog,
    'rohrer_final_jury_hearingButton': final_jury_hearing_notice_dialog.FinalJuryNoticeHearingDialog,
    'hemmeter_general_hearingButton': general_hearing_notice_dialog.GeneralNoticeOfHearingDialog,
    'rohrer_general_hearingButton': general_hearing_notice_dialog.GeneralNoticeOfHearingDialog,
    'hemmeter_trial_court_hearingButton': trial_to_court_hearing_notice_dialog.TrialToCourtHearingDialog,
    'rohrer_trial_court_hearingButton': trial_to_court_hearing_notice_dialog.TrialToCourtHearingDialog,

    # Probation
    'terms_comm_control_btn': terms_comm_control_dialog.TermsCommControlDialog,
    'notice_comm_control_violation_btn': notice_cc_violation_dialog.NoticeCCViolationDialog,

    # Admin
    'limited_driving_privilegesButton': driving_privileges_dialog.DrivingPrivilegesDialog,
    'juror_paymentButton': jury_payment_dialog.JuryPaymentDialog,
    'fiscal_entriesButton': admin_fiscal_dialog.AdminFiscalDialog,

    # Workflow
    'admin_entries_workflow_btn': admin.AdminWorkflowDialog,
    'md_adopt_workflow_btn': admin.MagistrateAdoptionWorkflowDialog,
    # 'rohrer_workflowButton': rohrer.RohrerWorkflowDialog,
    # 'bunner_workflowButton': bunner.BunnerWorkflowDialog,
    'pretrial_workflowButton': probation.PretrialWorkflowDialog,
    'community_control_workflowButton': probation.ComControlWorkflowDialog,
    }
