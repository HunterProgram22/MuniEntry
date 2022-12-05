"""Contains common base classes from which other dialogs inherit."""
from __future__ import annotations

from typing import Any

from loguru import logger
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QDialog

from munientry.entrycreators.entry_creator import BaseEntryCreator
from munientry.appsettings.settings import WIDGET_TYPE_ACCESS_DICT
from munientry.appsettings.paths import ICON_PATH


class BaseDialogBuilder(QDialog):
    """This class is a base class for all dialog windows."""

    def __init__(self, parent: QDialog = None) -> None:
        super().__init__(parent)
        self._view_modifier(self)
        self.functions = self._slots(self)
        self._signal_connector(self)
        logger.dialog(f'{self.dialog_name} Opened')

    def load_entry_case_information_model(self):
        self.entry_case_information = self._case_information_model()

    def load_cms_data_to_view(self) -> None:
        self._case_loader(self)

    def update_entry_case_information(self) -> None:
        self._model_updater(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = self._info_checker(self)

    def close(self):
        """Closes window by calling closeEvent in BaseDialog."""
        logger.dialog(f'{self.dialog_name} Closed')
        super().close()

    def transfer_view_data_to_model(self, model_class: type[Any]) -> None:
        """Takes data in the view fields and transfers to appropriate model class attribute.

        Method loops through all items in terms list which are maps of a model attribute to
        a view field. The appropriate transfer method is obtained from the WIDGET_TYPE_ACCESS_DICT

        Args:
            model_class: A dataclass object that has a terms_list attribute mapping
                view fields to model attributes.
        """
        for (model_attribute, view_field) in model_class.terms_list:
            widget_type = getattr(self, view_field).__class__.__name__
            view = getattr(self, view_field)
            view_field_data = getattr(view, WIDGET_TYPE_ACCESS_DICT.get(widget_type, 'None'))()
            class_name = model_class.__class__.__name__
            setattr(model_class, model_attribute, view_field_data)
            logger.info(f'{class_name} {model_attribute} set to: {view_field_data}.')


class BaseDialogViewModifier(object):
    """Base View builder that contains setupUI and common dialog view features."""

    def __init__(self, dialog):
        self.dialog = dialog
        self.dialog.setWindowIcon(QIcon(f'{ICON_PATH}gavel.ico'))
        self.dialog.setWindowFlags(
            self.dialog.windowFlags()
            | Qt.WindowType.CustomizeWindowHint
            | Qt.WindowType.WindowMaximizeButtonHint
            | Qt.WindowType.WindowCloseButtonHint,
        )
        self.dialog.setupUi(self.dialog)


class BaseDialogSlotFunctions(object):
    """Base functions used by all dialogs."""

    def __init__(self, dialog):
        self.dialog = dialog

    def clear_case_information_fields(self):
        self.dialog.defendant_first_name_lineEdit.clear()
        self.dialog.defendant_last_name_lineEdit.clear()
        self.dialog.case_number_lineEdit.clear()
        self.dialog.defendant_first_name_lineEdit.setFocus()

    def create_entry_process(self) -> None:
        """Calls the class for creating an entry triggered when create entry button is pressed."""
        BaseEntryCreator(self.dialog).create_entry_process()

    def show_hide_checkbox_connected_fields(self):
        """Gets list of boxes tied to condition checkbox and sets to show or hidden."""
        checkbox = self.dialog.sender()
        boxes = self.dialog.condition_checkbox_dict.get(checkbox.objectName())
        for field in boxes:
            hidden_checkbox = getattr(self.dialog, field)
            if checkbox.isChecked():
                hidden_checkbox.setEnabled(True)
                hidden_checkbox.setHidden(False)
                hidden_checkbox.setFocus()
            else:
                hidden_checkbox.setEnabled(False)
                hidden_checkbox.setHidden(True)


class BaseDialogSignalConnector(object):
    """Base Signal Connector."""

    def __init__(self, dialog):
        self.dialog = dialog
        self.dialog.cancel_Button.released.connect(self.dialog.close)

    def connect_main_dialog_common_signals(self):
        self.dialog.close_dialog_Button.released.connect(self.dialog.close)
        self.dialog.clear_fields_case_Button.released.connect(
            self.dialog.functions.clear_case_information_fields,
        )
        self.dialog.create_entry_Button.released.connect(
            self.dialog.functions.create_entry_process,
        )


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
