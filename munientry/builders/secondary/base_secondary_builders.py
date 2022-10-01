"""Contains base classes for secondary dialogs."""
from loguru import logger

from munientry.builders.base_builders import BaseDialogBuilder
from munientry.settings import WIDGET_TYPE_ACCESS_DICT


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


class SecondaryDialogBuilder(BaseDialogBuilder):
    """The base class for secondary dialogs called from other dialogs.

    Secondary Dialogs: AddConditionsDialog, AddCommunityControlDialog, AddJailOnlyDialog,
        AddSpecialBondConditionsDialog
    """

    def __init__(self, main_dialog, parent):
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)
        logger.dialog(f'{self.dialog_name} Opened')
