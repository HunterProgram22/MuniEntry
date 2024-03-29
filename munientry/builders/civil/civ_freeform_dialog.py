"""Builder module for the Civil Freeform Entry Dialog."""

from munientry.builders.civil import base_civil_builders as civil
from munientry.checkers.civil_checks import CivilBaseChecks
from munientry.loaders.cms_case_loaders import CivCmsLoader
from munientry.models.case_information.civil_case_information import CivFreeformEntryCaseInformation
from munientry.updaters.civil_updaters import CivFreeformDialogUpdater
from munientry.views.civ_freeform_dialog_ui import Ui_CivFreeformDialog


class CivFreeformDialogViewModifier(civil.CivilViewModifier):
    """View builder for Civil Freeform Entry Dialog."""


class CivFreeformDialogSlotFunctions(civil.CivilSlotFunctions):
    """Additional functions for Civil Freeform Entry Dialog."""


class CivFreeformDialogSignalConnector(civil.CivilSignalConnector):
    """Signal Connector for Civil Freeform Entry Dialog."""


class CivFreeformCheckList(CivilBaseChecks):
    """Check list for Civil Freeform Entry."""

    check_list = []


class CivFreeformDialog(civil.CivilDialogBuilder, Ui_CivFreeformDialog):
    """Dialog builder class for Civil Freeform Entry."""

    _case_information_model = CivFreeformEntryCaseInformation
    _case_loader = CivCmsLoader
    _info_checker = CivFreeformCheckList
    _model_updater = CivFreeformDialogUpdater
    _signal_connector = CivFreeformDialogSignalConnector
    _slots = CivFreeformDialogSlotFunctions
    _view_modifier = CivFreeformDialogViewModifier
    dialog_name = 'Civil Freeform Entry'
