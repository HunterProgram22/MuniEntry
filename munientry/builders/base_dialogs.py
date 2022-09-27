"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""
from __future__ import annotations

from typing import Any

from loguru import logger
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QDialog

from munientry.settings import WIDGET_TYPE_ACCESS_DICT


class BaseDialogBuilder(QDialog):
    """This class is a base class for all dialog windows."""

    def __init__(self, parent: QDialog = None) -> None:
        super().__init__(parent)
        self.build_attrs = self._get_dialog_attributes()
        self._modify_view()
        self._connect_signals_to_slots()
        self.dialog_name = self.build_attrs.get('dialog_name', None)

    def _get_dialog_attributes(self) -> dict:
        return self.build_dict

    def _modify_view(self) -> None:
        self.build_attrs.get('view')(self)

    def _connect_signals_to_slots(self) -> None:
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

    def closeEvent(self, event: QCloseEvent) -> None:
        """Extends pyqt close event method in order to log when a dialog closes."""
        logger.dialog(f'{self.objectName()} Closed by {event}')


class BaseDialog(QDialog):
    """This class is a base class for all dialog windows."""

    def __init__(self, parent: QDialog = None) -> None:
        super().__init__(parent)
        self._modify_view()
        self._connect_signals_to_slots()

    def _modify_view(self) -> None:
        """Abstract method that calls setupUI and creates the view.

        Raises:
            NotImplementedError: if the dialog does not implement the method.
        """
        raise NotImplementedError

    def _connect_signals_to_slots(self) -> None:
        """Abstract method that connects signals to dialog slot functions.

        Raises:
            NotImplementedError: if the dialog does not implement the method.
        """
        raise NotImplementedError

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
        self.dialog.defense_counsel_waived_checkBox.toggled.connect(
            self.dialog.functions.set_defense_counsel,
        )


class BaseDialogSignalConnectorOld:
    def __init__(self, dialog):
        dialog.cancel_Button.released.connect(dialog.functions.close_window)

    def connect_main_dialog_common_signals(self, dialog):
        dialog.clear_fields_case_Button.released.connect(dialog.functions.clear_case_information_fields)
        dialog.create_entry_Button.released.connect(dialog.functions.create_entry_process)
        dialog.close_dialog_Button.released.connect(dialog.functions.close_window)
        dialog.defense_counsel_waived_checkBox.toggled.connect(dialog.functions.set_defense_counsel)


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')


