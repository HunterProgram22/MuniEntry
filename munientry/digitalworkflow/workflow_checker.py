"""Module for checking entries and moving into workflow."""

from munientry.settings.paths import DW_PROBATION

SCRAM_PATH = f'{DW_PROBATION}/Scram_Gps//'
COMM_CONTROL_PATH = f'{DW_PROBATION}/Comm_Control//'


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
        """Checks conditions for sending an entry into probation workflow.

        For bond entries - all TRC cases, and other case types where defendant must report to
        probation.

        For sentencing entries - all entries that impose community control.
        """
        if self.case_information.__class__.__name__ in self.scram_gps_entries:
            if 'TRC' in self.case_information.case_number:
                return (True, SCRAM_PATH)
            if self.case_information.bond_conditions.monitoring is True:
                return (True, SCRAM_PATH)
            if self.case_information.bond_conditions.alcohol_drugs_assessment is True:
                return (True, SCRAM_PATH)
            if self.case_information.bond_conditions.mental_health_assessment is True:
                return (True, SCRAM_PATH)
            if self.case_information.bond_conditions.specialized_docket is True:
                return (True, SCRAM_PATH)
        if self.case_information.__class__.__name__ in self.comm_control_entries:
            if self.case_information.community_control.ordered is True:
                return (True, COMM_CONTROL_PATH)
        return (False, 'NONE')
