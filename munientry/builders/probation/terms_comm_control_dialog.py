"""Builder module for the Terms of Community Control Entry Dialog."""
from munientry.builders.probation import base_probation_builders as prob
from munientry.loaders.cms_case_loaders import ProbationCrimCmsLoader
from munientry.checkers.probation_checks import ProbationBaseChecks
from munientry.models.case_information.probation_case_information import TermsCommControlEntryCaseInformation
from munientry.updaters.probation_updaters import ProbationModelUpdater
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
        self.connect_terms_comm_control_signals()

    def connect_terms_comm_control_signals(self):
        checkboxes = [
            self.dialog.report_to_jail_check_box,
            self.dialog.no_contact_check_box,
            self.dialog.scram_ordered_check_box,
            self.dialog.specialized_docket_check_box,
            self.dialog.community_service_check_box,
        ]
        for checkbox in checkboxes:
            checkbox.toggled.connect(self.dialog.functions.show_hide_checkbox_connected_fields)


class TermsCommControlCheckList(ProbationBaseChecks):
    """Check list for Terms of Community Control."""

    check_list = []


class TermsCommControlDialog(prob.ProbationDialogBuilder, Ui_TermsCommControlDialog):
    """Dialog builder class for TermsCommControl Entry."""

    _case_information_model = TermsCommControlEntryCaseInformation
    _case_loader = ProbationCrimCmsLoader
    _info_checker = TermsCommControlCheckList
    _model_updater = ProbationModelUpdater
    _signal_connector = TermsCommControlDialogSignalConnector
    _slots = TermsCommControlDialogSlotFunctions
    _view_modifier = TermsCommControlDialogViewModifier
    dialog_name = 'Terms Of Community Control Entry'

    condition_checkbox_dict = {
        'report_to_jail_check_box': [
            'jail_report_date_box',
            'jail_days_serve_label',
            'jail_report_time_label',
            'jail_report_time_box',
            'jail_days_box',
        ],
        'no_contact_check_box': [
            'no_contact_with_box',
        ],
        'scram_ordered_check_box': [
            'scram_days_box',
        ],
        'specialized_docket_check_box': [
            'specialized_docket_box',
        ],
        'community_service_check_box': [
            'community_service_hours_box',
        ],
    }

    def additional_setup(self):
        for key, value in self.condition_checkbox_dict.items():
            for widget in value:
                checkbox = getattr(self, key)
                field = getattr(self, widget)
                if checkbox.isChecked():
                    field.setEnabled(True)
                    field.setHidden(False)
                    field.setFocus()
                else:
                    field.setEnabled(False)
                    field.setHidden(True)
