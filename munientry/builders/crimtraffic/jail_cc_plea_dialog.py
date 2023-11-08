"""Builder module for the Jail CC Plea Dialog."""
from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QWidget, QDialog, QInputDialog
from loguru import logger

from munientry.builders.crimtraffic import base_crimtraffic_builders as crim
from munientry.builders.secondary.add_jail_only_dialog import AddJailOnlyDialog
from munientry.widgets.message_boxes import DateInputDialog
from munientry.checkers.crim_checks import JailTimeChecks
from munientry.helper_functions import set_future_date
from munientry.loaders.cms_case_loaders import CmsFraLoader
from munientry.models.case_information.sentencing_entries import JailCCEntryCaseInformation
from munientry.settings.business_constants import DIVERSION_ADD_DAYS
from munientry.settings.pyqt_constants import MAX_JAIL_TIME_VALIDATOR
from munientry.updaters.grid_case_updaters import JailCCDialogUpdater
from munientry.views.jail_cc_plea_dialog_ui import Ui_JailCCPleaDialog


class JailCCDialogViewModifier(crim.CrimTrafficViewModifier):
    """View builder for Jail CC Plea Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_appearance_reason()
        self.set_diversion_fine_pay_date()
        self.set_diversion_jail_report_date()

    def set_diversion_fine_pay_date(self):
        """Diversion pay date is set to the first Tuesday after 97 days.

        90 days to comply, plus 7 days to process paperwork (per Judge Hemmeter).
        """
        today = QDate.currentDate()
        diversion_pay_days_to_add = set_future_date(DIVERSION_ADD_DAYS, 'Tuesday')
        self.dialog.diversion_fine_pay_date.setDate(
            today.addDays(diversion_pay_days_to_add),
        )

    def set_diversion_jail_report_date(self):
        """Diversion jail report date is set to the first Friday after 97 days.

        90 days to comply, plus 7 days to process paperwork (per Judge Hemmeter).
        """
        today = QDate.currentDate()
        jail_report_days_to_add = set_future_date(DIVERSION_ADD_DAYS, 'Friday')
        self.dialog.diversion_jail_report_date.setDate(
            today.addDays(jail_report_days_to_add),
        )


class JailCCDialogSlotFunctions(crim.CrimTrafficSlotFunctions, crim.FineCostsMixin):
    """Additional functions for Jail CC Plea Dialog."""

    def show_companion_case_fields(self):
        if self.dialog.add_companion_cases_checkBox.isChecked():
            self.dialog.companion_cases_box.show()
            self.dialog.companion_cases_sentence_box.show()
            self.dialog.companion_cases_sentence_label.show()
        else:
            self.dialog.companion_cases_box.hide()
            self.dialog.companion_cases_sentence_box.hide()
            self.dialog.companion_cases_sentence_label.hide()

    def _toggle_frame(self, frame, check_box, show):
        for child in frame.children():
            if isinstance(child, QWidget) and child != check_box:
                if show:
                    child.show()
                else:
                    child.hide()

    def toggle_specific_frame(self, frame, check_box):
        show = check_box.isChecked()
        self._toggle_frame(frame,check_box, show)

    def check_appearance_reason(self):
        """Checks the appearance reason that is selected and triggers action to update UI."""
        if self.dialog.appearance_reason_box.currentText() == 'sentencing only (already plead)':
            self.get_plea_date()
        elif self.dialog.appearance_reason_box.currentText() == 'trial to court':
            self.set_trial_to_court()

    def get_plea_date(self):
        date_dialog = DateInputDialog(self.dialog)
        plea_date, ok_input = date_dialog.getText(self.dialog, 'Plea Date', 'Enter Plea Date:')
        if ok_input:
            self.dialog.entry_case_information.plea_date = plea_date
            self.dialog.plea_label.setText(f'Plead on {plea_date}:')
            self.dialog.finding_label.setText(f'Finding on {plea_date}:')

    def set_trial_to_court(self):
        self.dialog.plea_label.setText('Tried To:')

    def set_report_date_boxes(self):
        if self.dialog.report_type_box.currentText() == 'future date':
            self.show_report_date_boxes()
        else:
            self.hide_report_date_boxes()

    def show_report_date_boxes(self):
        self.dialog.report_date_box.show()
        self.dialog.report_time_box.show()
        self.dialog.report_date_label.show()
        self.dialog.report_time_label.show()

    def hide_report_date_boxes(self):
        self.dialog.report_date_box.hide()
        self.dialog.report_time_box.hide()
        self.dialog.report_date_label.hide()
        self.dialog.report_time_label.hide()

    def show_report_days_notes_box(self):
        if self.dialog.jail_sentence_execution_type_box.currentText() == 'consecutive days':
            self.dialog.jail_report_days_notes_box.hide()
        else:
            self.dialog.jail_report_days_notes_box.show()


class JailCCDialogSignalConnector(crim.CrimTrafficSignalConnector):
    """Signal Connector for Jail CC Plea Dialog."""

    def __init__(self, dialog):
        super().__init__(dialog)
        self.connect_main_dialog_common_signals()
        self.connect_plea_all_button_signals()
        self.connect_fra_signals()
        self.connect_court_cost_signals()
        self.checkbox_frame_pairs = [
            (self.dialog.diversion_frame, self.dialog.diversion_check_box),
            (self.dialog.license_suspension_frame, self.dialog.license_suspension_check_box),
            (self.dialog.jail_reporting_frame, self.dialog.jail_reporting_check_box),
            (self.dialog.jail_credit_frame, self.dialog.jail_credit_check_box),
            (self.dialog.community_control_frame, self.dialog.community_control_check_box),
            (self.dialog.impoundment_frame, self.dialog.impoundment_check_box),
            (self.dialog.victim_notification_frame, self.dialog.victim_notification_check_box),
            (self.dialog.community_service_frame, self.dialog.community_service_check_box),
            (self.dialog.other_conditions_frame, self.dialog.other_conditions_check_box),
        ]
        self.connect_dialog_specific_signals()

    def connect_dialog_specific_signals(self):
        self.dialog.jail_reporting_check_box.toggled.connect(
            self.dialog.functions.conditions_checkbox_toggle
        ) # TODO: This is used to set jail reporting to True - Should be moved?
        self.dialog.add_companion_cases_checkBox.toggled.connect(
            self.dialog.functions.show_companion_case_fields,
        )

        for frame, checkbox in self.checkbox_frame_pairs:
            checkbox.toggled.connect(
                lambda checked, f=frame, cb=checkbox: self.dialog.functions.toggle_specific_frame(
                    f, cb,
                )
            )

        self.dialog.report_type_box.currentTextChanged.connect(
            self.dialog.functions.set_report_date_boxes,
        )
        self.dialog.jail_sentence_execution_type_box.currentTextChanged.connect(
            self.dialog.functions.show_report_days_notes_box,
        )
        self.dialog.appearance_reason_box.currentTextChanged.connect(
            self.dialog.functions.check_appearance_reason,
        )


class JailCCPleaCheckList(JailTimeChecks):
    """Check list for Jail CC Plea Dialog."""

    check_list = [
        'check_defense_counsel',
        'check_if_no_plea_entered',
        'check_if_no_finding_entered',
        'check_insurance',
        'check_additional_conditions_ordered',
        'check_if_jail_suspended_more_than_imposed',
        'check_if_days_in_jail_blank_but_in_jail',
        'check_if_in_jail_blank_but_has_jail_days',
        'check_if_apply_jail_credit_blank_but_in_jail',
        'check_if_jail_reporting_required',
        'check_if_jail_equals_suspended_and_imposed',
        'check_if_jail_credit_more_than_imposed',
        'check_if_in_jail_and_reporting_set',
    ]
    conditions_list = [
        ('license_suspension', 'license_type', 'License Suspension'),
        ('community_service', 'hours_of_service', 'Community Service'),
        ('other_conditions', 'terms', 'Other Conditions'),
        ('community_control', 'term_of_control', 'Community Control'),
        ('impoundment', 'vehicle_make_model', 'Immobilize/Impound'),
    ]


class JailCCPleaDialog(crim.CrimTrafficDialogBuilder, Ui_JailCCPleaDialog):
    """Dialog builder class for 'Jail and/or Community Control' dialog."""

    _case_information_model = JailCCEntryCaseInformation
    _case_loader = CmsFraLoader
    _info_checker = JailCCPleaCheckList
    _model_updater = JailCCDialogUpdater
    _signal_connector = JailCCDialogSignalConnector
    _slots = JailCCDialogSlotFunctions
    _view_modifier = JailCCDialogViewModifier
    dialog_name = 'Jail CC Judgment Entry'

    def additional_setup(self):
        """TODO: Remove additional conditions list at some point as it is not going to be used.

        TODO: Refactor frames_list as it is also in slot connections.
        """
        validator = MAX_JAIL_TIME_VALIDATOR
        self.jail_time_credit_box.setValidator(validator)
        self.additional_conditions_list = [
            ('community_control_checkBox', self.entry_case_information.community_control),
            ('license_suspension_check_box', self.entry_case_information.license_suspension),
            ('community_service_checkBox', self.entry_case_information.community_service),
            ('other_conditions_checkBox', self.entry_case_information.other_conditions),
            ('jail_reporting_check_box', self.entry_case_information.jail_terms),
            ('impoundment_checkBox', self.entry_case_information.impoundment),
            ('victim_notification_checkBox', self.entry_case_information.victim_notification),
        ]
        self.frames_list = [
            (self.license_suspension_frame, self.license_suspension_check_box),
            (self.diversion_frame, self.diversion_check_box),
            (self.jail_reporting_frame, self.jail_reporting_check_box),
            (self.jail_credit_frame, self.jail_credit_check_box),
            (self.community_control_frame, self.community_control_check_box),
            (self.impoundment_frame, self.impoundment_check_box),
            (self.victim_notification_frame, self.victim_notification_check_box),
            (self.community_service_frame, self.community_service_check_box),
            (self.other_conditions_frame, self.other_conditions_check_box),
        ]
        for frame_tuple in self.frames_list:
            self.functions.toggle_specific_frame(frame_tuple[0], frame_tuple[1])
        if self.case_table == 'slated':
            self.in_jail_box.setCurrentText('Yes')
