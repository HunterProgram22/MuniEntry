"""Builder module for the Arraignment Continuance Dialog."""
from loguru import logger

from munientry.appsettings.pyqt_constants import TODAY
from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.base_checks import ArraignmentContinueDialogInfoChecker
from munientry.loaders.cms_case_loaders import CmsNoChargeLoader
from munientry.models.case_information.plea_entries import ArraignmentContinueEntryCaseInformation
from munientry.updaters.no_grid_case_updaters import ArraignmentContinueDialogUpdater
from munientry.views.arraignment_continue_dialog_ui import Ui_ArraignmentContinueDialog


class ArraignmentContinueDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Arraignment Continuance Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()



class ArraignmentContinueDialogSlotFunctions(crim.CrimTrafficSlotFunctions):
    """Additional functions for Arraignment Continuance Dialog."""

    def update_arraignment_date(self):
        cont_length = self.dialog.continuance_length_box.currentText()
        ARRAIGNMENT_CONT_DICT = {
            '1 Week': 7,
            '2 Weeks': 14,
        }
        days_to_add = ARRAIGNMENT_CONT_DICT.get(cont_length)
        self.dialog.new_arraignment_date_box.setDate(TODAY.addDays(days_to_add))

    def show_hide_length_date_boxes(self):
        if self.dialog.continuance_reason_box.currentText() == 'to arrange for an interpreter for defendant':
            self.dialog.continuance_length_box.setHidden(True)
            self.dialog.new_arraignment_date_box.setHidden(True)
            self.dialog.arraignment_date_label.setHidden(True)
            self.dialog.continuance_label.setHidden(True)
        else:
            self.dialog.continuance_length_box.setVisible(True)
            self.dialog.new_arraignment_date_box.setVisible(True)
            self.dialog.arraignment_date_label.setVisible(True)
            self.dialog.continuance_label.setVisible(True)


class ArraignmentContinueDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Arraignment Continuance Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.dialog.continuance_length_box.currentTextChanged.connect(
           self.dialog.functions.update_arraignment_date,
        )
        self.dialog.continuance_reason_box.currentTextChanged.connect(
            self.dialog.functions.show_hide_length_date_boxes,
        )


class ArraignmentContinueDialog(crim.CrimTrafficDialogBuilder, Ui_ArraignmentContinueDialog):
    """Dialog builder class for Arraignment Continuance Entry."""

    _case_information_model = ArraignmentContinueEntryCaseInformation
    _case_loader = CmsNoChargeLoader
    _info_checker = ArraignmentContinueDialogInfoChecker
    _model_updater = ArraignmentContinueDialogUpdater
    _signal_connector = ArraignmentContinueDialogSignalConnector
    _slots = ArraignmentContinueDialogSlotFunctions
    _view_modifier = ArraignmentContinueDialogViewModifier
    dialog_name = 'Arraignment Continuance Dialog'

    def additional_setup(self):
        self.functions.update_arraignment_date()
        self.functions.show_hide_length_date_boxes()


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
