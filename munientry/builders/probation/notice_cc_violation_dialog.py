"""Builder module for the Notice of Community Control Violation Dialog."""
from munientry.builders.probation import base_probation_builders as prob
from munientry.loaders.cms_case_loaders import ProbationCrimCmsLoader
from munientry.checkers.probation_checks import ProbationBaseChecks
from munientry.models.case_information.probation_case_information import NoticeCCViolationCaseInformation
from munientry.updaters.probation_updaters import ProbationModelUpdater
from munientry.views.notice_cc_violation_dialog_ui import Ui_NoticeCCViolationDialog


class NoticeCCViolationViewModifier(prob.ProbationViewModifier):
    """View builder for Notice of CC Violation Entry Dialog."""


class NoticeCCViolationSlotFunctions(prob.ProbationSlotFunctions):
    """Additional functions for Notice of CC Violation Entry Dialog."""


class NoticeCCViolationSignalConnector(prob.ProbationSignalConnector):
    """Signal Connector for Notice of CC Violation Entry Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()


class NoticeCCViolationCheckList(ProbationBaseChecks):
    """Check list for Notice CC Violation."""

    check_list = []


class NoticeCCViolationDialog(prob.ProbationDialogBuilder, Ui_NoticeCCViolationDialog):
    """Dialog builder class for Notice of CC Violation Entry."""

    _case_information_model = NoticeCCViolationCaseInformation
    _case_loader = ProbationCrimCmsLoader
    _info_checker = NoticeCCViolationCheckList
    _model_updater = ProbationModelUpdater
    _signal_connector = NoticeCCViolationSignalConnector
    _slots = NoticeCCViolationSlotFunctions
    _view_modifier = NoticeCCViolationViewModifier
    dialog_name = 'Notice Of Community Control Violation Entry'
