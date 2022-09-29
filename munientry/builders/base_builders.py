"""Contains common base classes from which other dialogs inherit."""
from __future__ import annotations

from PyQt5.QtCore import Qt
from loguru import logger
from PyQt5.QtGui import QCloseEvent, QIcon
from PyQt5.QtWidgets import QDialog

from munientry.settings import ICON_PATH


class BaseDialogBuilder(QDialog):
    """This class is a base class for all dialog windows."""

    def __init__(self, parent: QDialog = None) -> None:
        super().__init__(parent)
        self.build_attrs = self._get_dialog_attributes()
        self._modify_view()
        self._connect_signals_to_slots()
        self.dialog_name = self.build_attrs.get('dialog_name', None)

    def _get_dialog_attributes(self) -> dict:
        """Returns a dict containing all classes used to build and work with a Dialog."""
        return self.build_dict

    def _modify_view(self) -> None:
        """Gets the ViewModifer class for the Dialog.

        Calls setupUI and creates the view.
        """
        self.build_attrs.get('view')(self)

    def _connect_signals_to_slots(self) -> None:
        """Gets the SlotFunctions and SignalConnector classes for the dialog.

        Connects the SlotFunctions to signals on the Dialog. Functions are accessible
        as self.functions.
        """
        self.functions = self.build_attrs.get('slots')(self)
        self.build_attrs.get('signals')(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = self.build_attrs.get('case_information_model')()

    def load_cms_data_to_view(self) -> None:
        self.build_attrs.get('loader')(self)

    def update_entry_case_information(self) -> None:
        self.build_attrs.get('updater')(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = self.build_attrs.get('info_checker')(self)

    def closeEvent(self, event: QCloseEvent) -> None:
        """Extends pyqt close event method in order to log when a dialog closes."""
        logger.dialog(f'{self.objectName()} Closed by {event}')


class BaseDialogSignalConnector(object):
    """Base Signal Connector."""

    def __init__(self, dialog):
        self.dialog = dialog
        self.dialog.cancel_Button.released.connect(self.dialog.functions.close_window)

    def connect_main_dialog_common_signals(self):
        self.dialog.clear_fields_case_Button.released.connect(
            self.dialog.functions.clear_case_information_fields,
        )
        self.dialog.create_entry_Button.released.connect(
            self.dialog.functions.create_entry_process,
        )
        self.dialog.close_dialog_Button.released.connect(self.dialog.functions.close_window)
        try:
            self.dialog.defense_counsel_waived_checkBox.toggled.connect(
                self.dialog.functions.set_defense_counsel,
            )
        except AttributeError as err:
            logger.warning(err)


class BaseDialogViewModifier(object):
    """Base View builder that contains setupUI and common dialog view features."""

    def __init__(self, dialog):
        self.dialog = dialog
        self.dialog.setWindowIcon(QIcon(f'{ICON_PATH}gavel.ico'))
        self.dialog.setWindowFlags(
            self.dialog.windowFlags()
            | Qt.CustomizeWindowHint
            | Qt.WindowMaximizeButtonHint
            | Qt.WindowCloseButtonHint,
        )
        self.dialog.setupUi(self.dialog)


class BaseDialogSlotFunctions(object):
    """Base functions used by all dialogs."""

    def __init__(self, dialog):
        self.dialog = dialog


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
