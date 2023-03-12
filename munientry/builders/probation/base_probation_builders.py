"""Base Classes for Probation Entries."""
from loguru import logger

from munientry.builders import base_builders as base
from munientry.entrycreators.entry_creator import ProbationEntryCreator
from munientry.models.template_types import TEMPLATE_DICT
from munientry.appsettings.pyqt_constants import TODAY
from munientry.widgets.message_boxes import InfoBox


class ProbationDialogBuilder(base.BaseDialogBuilder):
    """The base class for all probation main entry dialogs."""

    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        """Self.case_table must be set before the call to super().__init__.

        The init of BaseDialog, called by super().__init__ calls ModifyView for the specific dialog
        which will use the case table.
        """
        self.case_table = case_table
        super().__init__(parent)
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        loaded_case = cms_case.case_number
        logger.info(
            f'Loaded Case {loaded_case} from {self.case_table};'
        )
        self.load_entry_case_information_model()
        self.entry_case_information.judicial_officer = self.judicial_officer
        try:
            self.defense_counsel_name_box.load_attorneys()
        except AttributeError as error:
            logger.warning(error)
        self.load_cms_data_to_view()
        self.criminal_charge = None
        self.popup_dialog = None
        self.additional_setup()

    def additional_setup(self):
        """Abstract base method used in subclasses for additional setup after init."""


class ProbationViewModifier(base.BaseDialogViewModifier):
    """Base View Builder for Probation Entries."""


class ProbationSlotFunctions(base.BaseDialogSlotFunctions):
    """Base set of functions for Probation Entries."""

    def create_entry_process(self) -> None:
        ProbationEntryCreator(self.dialog).create_entry_process()


class ProbationSignalConnector(base.BaseDialogSignalConnector):
    """Extends Base Dialog Signal Connector for Probation Entries."""

    def connect_main_dialog_common_signals(self):
        super().connect_main_dialog_common_signals()
