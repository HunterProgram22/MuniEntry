"""Builder module for the Terms of Community Control Entry Dialog."""
from munientry.builders.probation import base_probation_builders as prob
from munientry.loaders.cms_case_loaders import CmsNoChargeLoader
from munientry.models.case_information.probation_case_information import TermsCommControlEntryCaseInformation
from munientry.updaters.probation_updaters import ProbationDialogCaseInformationUpdater
from munientry.views.terms_comm_control_dialog_ui import Ui_TermsCommControlDialog


class TermsCommControlDialogViewModifier(prob.ProbationViewModifier):
    """View builder for TermsCommControl Entry Dialog."""


class TermsCommControlDialogSlotFunctions(prob.ProbationSlotFunctions):
    """Additional functions for TermsCommControl Entry Dialog."""


class TermsCommControlDialogSignalConnector(prob.ProbationSignalConnector):
    """Signal Connector for TermsCommControl Entry Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()


class TermsCommControlDialog(prob.ProbationDialogBuilder, Ui_TermsCommControlDialog):
    """Dialog builder class for TermsCommControl Entry."""

    _case_information_model = TermsCommControlEntryCaseInformation
    _case_loader = CmsNoChargeLoader
    _info_checker = None
    _model_updater = ProbationDialogCaseInformationUpdater
    _signal_connector = TermsCommControlDialogSignalConnector
    _slots = TermsCommControlDialogSlotFunctions
    _view_modifier = TermsCommControlDialogViewModifier
    dialog_name = 'Terms Of Community Control Entry'
