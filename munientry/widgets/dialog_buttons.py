"""Module for custom PushButtons used for dialogs."""
from loguru import logger
from PyQt6.QtWidgets import QPushButton

from munientry.builders.crimtraffic.fine_only_plea_dialog import FineOnlyPleaDialog
from munientry.builders.crimtraffic.jail_cc_plea_dialog import JailCCPleaDialog
from munientry.checkers.dialog_preload_checkers import CrimTrafficPreloadChecker
from munientry.loaders.dialog_loader import DialogButtonLoader


BUTTON_DICT = {
    'FineOnlyPleaButton': FineOnlyPleaDialog,
    'JailCCPleaButton': JailCCPleaDialog,
}



class DialogButton(QPushButton):
    """Custom QPushButton used for loading dialogs."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_up_widget()

    def set_up_widget(self):
        self.released.connect(self.load_dialog)

    def load_dialog(self):
        button = self.sender()
        mainwindow = self.window()


class CrimDialogButton(DialogButton):

    def __init__(self, parent=None):
        super().__init__(parent)

    def load_dialog(self):
        button = self.sender()
        dialog = BUTTON_DICT.get(button.objectName())
        mainwindow = self.window()
        if CrimTrafficPreloadChecker(mainwindow).perform_checks():
            load_data = DialogButtonLoader(mainwindow).get_case_data()
            judicial_officer, cms_case_data, case_table, workflow_status = load_data
            dialog(
                judicial_officer,
                cms_case_data,
                case_table,
                workflow_status,
            ).exec()
