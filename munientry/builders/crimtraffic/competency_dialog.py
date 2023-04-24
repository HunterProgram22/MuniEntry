"""Builder module for the Competency Dialog."""
from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.crim_checks import DefenseCounselChecks
from munientry.loaders.cms_case_loaders import CrimCmsNoChargeLoader
from munientry.models.case_information.criminal_case_information import CriminalCaseInformation
from munientry.updaters.no_grid_case_updaters import CompetencyDialogUpdater
from munientry.views.competency_dialog_ui import Ui_CompetencyDialog


class CompetencyDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Competency Entry Dialog."""


class CompetencyDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Competency Entry Dialog."""


class CompetencyDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Competency Entry Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()


class CompetencyCheckList(DefenseCounselChecks):
    """Check list for Competency Entry Dialog."""

    check_list = [
        'check_defense_counsel',
    ]


class CompetencyDialog(crim.CrimTrafficDialogBuilder, Ui_CompetencyDialog):
    """Dialog builder class for Competency Entry."""
    _case_information_model = CriminalCaseInformation
    _case_loader = CrimCmsNoChargeLoader
    _info_checker = CompetencyCheckList
    _model_updater = CompetencyDialogUpdater
    _signal_connector = CompetencyDialogSignalConnector
    _slots = CompetencyDialogSlotFunctions
    _view_modifier = CompetencyDialogViewModifier
    dialog_name = 'Competency Entry'

    # def additional_setup(self):
