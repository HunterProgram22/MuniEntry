"""Module for checking entries and moving into workflow."""

from munientry.paths import DW_MATTOX

SCRAM_PATH = f'{DW_MATTOX}/Scram_Gps//'
COMM_CONTROL_PATH = f'{DW_MATTOX}/Comm_Control//'


class WorkflowCheck(object):

    scram_gps_entries = [
        'NotGuiltyBondEntryCaseInformation',
        'NoPleaBondEntryCaseInformation',
        'BondHearingEntryCaseInformation'
    ]

    comm_control_entries = [
        'JailCCEntryCaseInformation',
        'SentencingOnlyEntryCaseInformation',
        'TrialSentencingEntryCaseInformation',
    ]

    def __init__(self, case_information):
        self.case_information = case_information

    def check_for_probation_workflow(self) -> (bool, str):
        if self.case_information.__class__.__name__ in self.scram_gps_entries:
            if self.case_information.bond_conditions.monitoring is True:
                return (True, SCRAM_PATH)
        if self.case_information.__class__.__name__ in self.comm_control_entries:
            if self.case_information.community_control.ordered is True:
                return (True, COMM_CONTROL_PATH)
        return (False, 'NONE')
