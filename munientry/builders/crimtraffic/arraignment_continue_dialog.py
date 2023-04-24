"""Builder module for the Arraignment Continuance Dialog."""
from PyQt6.QtCore import QDate

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.checkers.crim_checks import DefenseCounselChecks
from munientry.loaders.cms_case_loaders import CrimCmsNoChargeLoader
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

    def update_arraignment_date(self) -> None:
        cont_length = self.dialog.continuance_length_box.currentText()
        arraignment_time_dict = {
            '1 Week': 7,
            '2 Weeks': 14,
        }
        days_to_add = arraignment_time_dict.get(cont_length, 0)
        today = QDate.currentDate()
        self.dialog.new_arraignment_date_box.setDate(today.addDays(days_to_add))

    def show_hide_length_date_boxes(self) -> None:
        visibility_mapping = {
            'to arrange for an interpreter for defendant': False,
            'general continuance - denied untimely': False,
        }
        current_text = self.dialog.continuance_reason_box.currentText()
        should_show = visibility_mapping.get(current_text, True)
        widgets = [
            self.dialog.continuance_length_box,
            self.dialog.new_arraignment_date_box,
            self.dialog.new_arraignment_date_label,
            self.dialog.continuance_label,
        ]
        for widget in widgets:
            widget.setVisible(should_show)


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


class ArraignmentContinueCheckList(DefenseCounselChecks):
    """Check list for Arraignment Continuance Dialog."""

    check_list = [
        'check_defense_counsel',
    ]


class ArraignmentContinueDialog(crim.CrimTrafficDialogBuilder, Ui_ArraignmentContinueDialog):
    """Dialog builder class for Arraignment Continuance Entry."""

    _case_information_model = ArraignmentContinueEntryCaseInformation
    _case_loader = CrimCmsNoChargeLoader
    _info_checker = ArraignmentContinueCheckList
    _model_updater = ArraignmentContinueDialogUpdater
    _signal_connector = ArraignmentContinueDialogSignalConnector
    _slots = ArraignmentContinueDialogSlotFunctions
    _view_modifier = ArraignmentContinueDialogViewModifier
    dialog_name = 'Arraignment Continuance Entry'

    def additional_setup(self) -> None:
        self.functions.update_arraignment_date()
        self.functions.show_hide_length_date_boxes()
        today = QDate.currentDate()
        self.current_arraignment_date_box.setDate(today)
