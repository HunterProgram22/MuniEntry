"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""
from __future__ import annotations

from typing import Any

from loguru import logger
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import QDialog

from munientry.settings import TYPE_CHECKING, WIDGET_TYPE_ACCESS_DICT

if TYPE_CHECKING:
    pass


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
    """Base Signal Connector for CrimTraffic Entries."""

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

    def connect_fra_signals(self):
        self.dialog.fra_in_file_box.currentTextChanged.connect(
            self.dialog.functions.set_fra_in_file,
        )
        self.dialog.fra_in_court_box.currentTextChanged.connect(
            self.dialog.functions.set_fra_in_court,
        )

    def connect_plea_all_button_signals(self):
        self.dialog.add_charge_Button.released.connect(
            self.dialog.functions.start_add_charge_dialog,
        )
        self.dialog.guilty_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_pleas,
        )
        self.dialog.guilty_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_findings,
        )
        self.dialog.no_contest_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_pleas,
        )
        self.dialog.no_contest_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_findings,
        )

    def connect_not_guilty_all_button(self):
        self.dialog.not_guilty_all_Button.pressed.connect(
            self.dialog.charges_gridLayout.set_all_pleas,
        )

    def connect_add_charge_button(self):
        self.dialog.add_charge_Button.released.connect(
            self.dialog.functions.start_add_charge_dialog,
        )

    def connect_court_cost_signals(self):
        self.dialog.ability_to_pay_box.currentTextChanged.connect(
            self.dialog.functions.set_fines_costs_pay_date,
        )
        self.dialog.costs_and_fines_Button.released.connect(
            self.dialog.functions.show_costs_and_fines,
        )

    def connect_main_dialog_additional_condition_signals(self):
        self.dialog.license_suspension_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.community_service_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.other_conditions_checkBox.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle,
        )
        self.dialog.add_conditions_Button.pressed.connect(
            self.dialog.functions.start_add_conditions_dialog,
        )

    def connect_condition_dialog_main_signals(self):
        self.dialog.add_conditions_Button.pressed.connect(self.dialog.functions.add_conditions)
        self.dialog.add_conditions_Button.released.connect(self.dialog.functions.close_window)

    def connect_community_service_days_update(self):
        self.dialog.community_service_days_to_complete_box.currentIndexChanged.connect(
            self.dialog.functions.update_community_service_due_date
        )


class BaseDialogSignalConnectorOld:
    def __init__(self, dialog):
        dialog.cancel_Button.released.connect(dialog.functions.close_window)

    def connect_main_dialog_common_signals(self, dialog):
        dialog.clear_fields_case_Button.released.connect(dialog.functions.clear_case_information_fields)
        dialog.create_entry_Button.released.connect(dialog.functions.create_entry_process)
        dialog.close_dialog_Button.released.connect(dialog.functions.close_window)
        dialog.defense_counsel_waived_checkBox.toggled.connect(dialog.functions.set_defense_counsel)

    def connect_fra_signals(self, dialog):
        dialog.fra_in_file_box.currentTextChanged.connect(dialog.functions.set_fra_in_file)
        dialog.fra_in_court_box.currentTextChanged.connect(dialog.functions.set_fra_in_court)

    def connect_plea_all_button_signals(self, dialog):
        dialog.add_charge_Button.released.connect(dialog.functions.start_add_charge_dialog)
        dialog.guilty_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_pleas)
        dialog.guilty_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_findings)
        dialog.no_contest_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_pleas)
        dialog.no_contest_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_findings)

    def connect_not_guilty_all_button(self, dialog):
        dialog.not_guilty_all_Button.pressed.connect(dialog.charges_gridLayout.set_all_pleas)

    def connect_court_cost_signals(self, dialog):
        dialog.ability_to_pay_box.currentTextChanged.connect(dialog.functions.set_fines_costs_pay_date)
        dialog.costs_and_fines_Button.released.connect(dialog.functions.show_costs_and_fines)

    def connect_main_dialog_additional_condition_signals(self, dialog):
        dialog.license_suspension_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.community_service_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.other_conditions_checkBox.toggled.connect(dialog.functions.conditions_checkbox_toggle)
        dialog.add_conditions_Button.pressed.connect(dialog.functions.start_add_conditions_dialog)

    def connect_condition_dialog_main_signals(self, dialog):
        dialog.add_conditions_Button.pressed.connect(dialog.functions.add_conditions)
        dialog.add_conditions_Button.released.connect(dialog.functions.close_window)


    def connect_community_service_days_update(self, dialog):
        dialog.community_service_days_to_complete_box.currentIndexChanged.connect(
            dialog.functions.update_community_service_due_date
        )


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
