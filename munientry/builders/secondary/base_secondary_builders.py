"""Contains base classes for secondary dialogs."""
from loguru import logger
from PyQt5.QtWidgets import QLabel

from munientry.builders import base_builders as base
from munientry.settings import WIDGET_TYPE_ACCESS_DICT, WIDGET_TYPE_SET_DICT


def enable_condition_frames(conditions_dialog, main_dialog) -> None:
    """The function is called to hide frames on load of dialog.

    Hides conditions that have not been selected in the main dialog. This is necessary
    because the base view of a dialog contains all possible frames.
    """
    for frame_item in conditions_dialog.conditions_frames:
        (frame_checkbox, frame) = frame_item
        if getattr(main_dialog, frame_checkbox).isChecked():
            getattr(conditions_dialog, frame).setEnabled(True)
        else:
            frame = getattr(conditions_dialog, frame)
            frame.setParent(None)
            frame.deleteLater()


class SecondaryDialogBuilder(base.BaseDialogBuilder):
    """The base class for secondary dialogs called from other dialogs.

    Secondary Dialogs: AddConditionsDialog, AddCommunityControlDialog, AddJailOnlyDialog,
        AddSpecialBondConditionsDialog
    """

    def __init__(self, main_dialog, parent):
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)
        logger.dialog(f'{self.dialog_name} Opened')


class SecondaryViewModifier(base.BaseDialogViewModifier):
    """Base View Builder for Secondary Dialogs."""

    def set_conditions_case_information_banner(self):
        column = self.dialog.charges_gridLayout.columnCount() + 1
        for charge in self.dialog.charges_list:
            if charge is not None:
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.offense), 0, column)
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.statute), 1, column)
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.finding), 2, column)
                column += 1

    def hide_boxes(self):
        for condition in self.condition_checkbox_list:
            (condition_checkbox, condition_field) = condition
            if getattr(self.dialog, condition_checkbox).isChecked():
                getattr(self.dialog, condition_field).setEnabled(True)
                getattr(self.dialog, condition_field).setHidden(False)
            else:
                getattr(self.dialog, condition_field).setEnabled(False)
                getattr(self.dialog, condition_field).setHidden(True)

    def load_existing_data_to_dialog(self):
        for condition in self.condition_classes:
            (condition_checkbox, model_class) = condition
            if getattr(self.dialog.main_dialog, condition_checkbox).isChecked():
                model_class = getattr(self.dialog.main_dialog.entry_case_information, model_class)
                self.transfer_model_data_to_view(model_class)
            else:
                continue

    def transfer_model_data_to_view(self, model_class):
        """Loops through the terms_list for a model and loads data into the view of the dialog.

        This is to allow previously entered data to be shown if a user comes back to
        the dialog after having previously entered data.
        """
        for (model_attribute, view_field) in model_class.terms_list:
            key = getattr(self.dialog, view_field).__class__.__name__
            view = getattr(self.dialog, view_field)
            getattr(view, WIDGET_TYPE_SET_DICT.get(key))(getattr(model_class, model_attribute))


class SecondarySlotFunctions(base.BaseDialogSlotFunctions):
   """Base set of functions for Secondary Dialogs."""

