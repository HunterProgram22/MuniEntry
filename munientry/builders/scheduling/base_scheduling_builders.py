"""Common base classes for Scheduling Dialogs."""
from loguru import logger

from munientry.builders import base_builders as base
from munientry.entrycreators.entry_creator import SchedulingEntryCreator


class SchedulingDialogBuilder(base.BaseDialogBuilder):
    """The base class for all Scheduling Dialogs."""

    def __init__(self, judicial_officer=None, cms_case=None, case_table=None, parent=None):
        self.case_table = case_table
        super().__init__(parent)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        self.load_entry_case_information_model()
        self.load_cms_data_to_view()
        case_number = cms_case.case_number
        logger.info(f'Loading {case_number} from {self.case_table}')
        self.functions.enable_language_box()
        self.additional_setup()

    def additional_setup(self):
        """Abstract base method used in subclasses for additional setup after init."""


class SchedulingViewModifier(base.BaseDialogViewModifier):
    """Base View Builder for Scheduling Dialogs."""


class SchedulingSignalConnector(base.BaseDialogSignalConnector):
    """Base Signal Connector for Scheduling Dialogs."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.dialog.interpreter_check_box.toggled.connect(self.dialog.functions.enable_language_box)


class SchedulingSlotFunctions(base.BaseDialogSlotFunctions):
    """Additional functions for Scheduling Dialogs."""

    def create_entry_process(self) -> None:
        SchedulingEntryCreator(self.dialog).create_entry_process()

    def enable_language_box(self):
        if self.dialog.interpreter_check_box.isChecked():
            self.dialog.language_box.show()
            self.dialog.language_box.setEnabled(True)
            self.dialog.language_box.setFocus()
        else:
            self.dialog.language_box.hide()
            self.dialog.language_box.setEnabled(False)