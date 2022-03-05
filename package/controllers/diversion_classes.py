from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QIntValidator
from loguru import logger
from package.controllers.base_dialogs import CriminalSlotFunctions
from package.controllers.helper_functions import set_future_date


class BaseDialogViewModifier(object):
    def __init__(self, dialog):
        dialog.plea_trial_date.setDate(QtCore.QDate.currentDate())
        if dialog.case_table == "final_pretrials":
            dialog.appearance_reason_box.setCurrentText("change of plea")


class DiversionDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        diversion_pay_days_to_add = set_future_date(97, None, 1)
        dialog.diversion_fine_pay_date_box.setDate(QDate.currentDate().addDays(diversion_pay_days_to_add))
        jail_report_days_to_add = set_future_date(97, None, 4)
        dialog.diversion_jail_report_date_box.setDate(QDate.currentDate().addDays(jail_report_days_to_add))
        dialog.show_jail_report_date_box()
        dialog.show_other_conditions_box()


#
# class DiversionDialogSignalConnector(object):
#     def __init__(self, dialog):
#         dialog.cancel_Button.pressed.connect(dialog.close_event)
#         dialog.clear_fields_case_Button.pressed.connect(
#             lambda dialog=dialog: CriminalSlotFunctions.clear_case_information_fields(dialog))
#         dialog.create_entry_Button.clicked.connect(
#             lambda _bool, dialog=dialog: CriminalSlotFunctions.create_entry_process(_bool, dialog))
#         dialog.close_dialog_Button.pressed.connect(
#             lambda dialog=dialog: CriminalSlotFunctions.close_dialog(dialog))
#         dialog.add_charge_Button.clicked.connect(dialog.start_add_charge_dialog)
#         dialog.defense_counsel_waived_checkBox.toggled.connect(dialog.set_defense_counsel)
#         dialog.diversion_jail_imposed_checkBox.toggled.connect(dialog.show_jail_report_date_box)
#         dialog.other_conditions_checkBox.toggled.connect(dialog.show_other_conditions_box)
#         dialog.guilty_all_Button.pressed.connect(dialog.set_plea_and_findings_process)
#         dialog.fra_in_file_box.currentTextChanged.connect(dialog.set_fra_in_file)
#         dialog.fra_in_court_box.currentTextChanged.connect(dialog.set_fra_in_court)
#         dialog.no_contest_all_Button.pressed.connect(dialog.set_plea_and_findings_process)
#
#
# class DiversionDialogSlotFunctions(CriminalSlotFunctions):
#
#     @classmethod
#     def show_other_conditions_box(cls, dialog):
#         if dialog.other_conditions_checkBox.isChecked():
#             dialog.other_conditions_textEdit.setHidden(False)
#             dialog.other_conditions_textEdit.setFocus()
#         else:
#             dialog.other_conditions_textEdit.setHidden(True)
#
#     @classmethod
#     def show_jail_report_date_box(cls, dialog):
#         if dialog.diversion_jail_imposed_checkBox.isChecked():
#             dialog.diversion_jail_report_date_box.setHidden(False)
#             dialog.diversion_jail_report_date_label.setHidden(False)
#         else:
#             dialog.diversion_jail_report_date_box.setHidden(True)
#             dialog.diversion_jail_report_date_label.setHidden(True)
#
#     @classmethod
#     def add_charge_to_grid(cls, dialog):
#         dialog.charges_gridLayout.add_charge_only_to_grid(dialog)
#         dialog.defense_counsel_name_box.setFocus()
#
#     # @logger.catch
#     # def add_plea_findings_and_fines_to_entry_case_information(self):
#     #     return JailAddPleaFindingsFinesJail.add(self) # self is dialog
#     #
#     # @logger.catch
#     # def update_case_information(self):
#     #     """"Ovverrides CriminalSentencingDialog update so add_additional_conditions method is not called."""
#     #     self.add_plea_findings_and_fines_to_entry_case_information()
#     #     self.transfer_field_data_to_model(self.entry_case_information.diversion)
#     #     self.entry_case_information.diversion.program_name = self.entry_case_information.diversion.get_program_name()
#     #     self.transfer_field_data_to_model(self.entry_case_information.other_conditions)
#     #     return CasePartyUpdater(self)
#     #
#     # @logger.catch
#     # def set_fra_in_file(self, current_text):
#     #     """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
#     #     that the FRA was shown in the complaint of file."""
#     #     if current_text == "Yes":
#     #         self.entry_case_information.fra_in_file = True
#     #         self.fra_in_court_box.setCurrentText("No")
#     #     elif current_text == "No":
#     #         self.entry_case_information.fra_in_file = False
#     #     else:
#     #         self.entry_case_information.fra_in_file = None
#     #
#     # @logger.catch
#     # def set_fra_in_court(self, current_text):
#     #     """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
#     #     that the FRA was shown in court."""
#     #     if current_text == "Yes":
#     #         self.entry_case_information.fra_in_court = True
#     #     elif current_text == "No":
#     #         self.entry_case_information.fra_in_court = False
#     #     else:
#     #         self.entry_case_information.fra_in_court = None