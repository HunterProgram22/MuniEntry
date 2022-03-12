import os
import time

from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QDialog

from db.databases import extract_data
from docxtpl import DocxTemplate
from loguru import logger
from db.databases import open_charges_db_connection, create_offense_list, create_statute_list
from package.controllers.helper_functions import InfoChecker, check_if_diversion_program_selected, set_document_name

from package.views.custom_widgets import RequiredBox
from package.views.add_charge_dialog_ui import Ui_AddChargeDialog
from package.views.amend_charge_dialog_ui import Ui_AmendChargeDialog
from package.controllers.view_modifiers import AddChargeDialogViewModifier, AmendChargeDialogViewModifier
# from package.controllers.signal_connectors import AddChargeDialogSignalConnector, AmendChargeDialogSignalConnector

from settings import SAVE_PATH
from win32com import client


class BaseDialogSlotFunctions(object):
    def __init__(self, dialog):
        self.dialog = dialog

    @logger.catch
    def start_add_charge_dialog(self):
        self.dialog.update_case_information()
        print(self.dialog)
        AddChargeDialog(self.dialog).exec()

    @logger.catch
    def start_amend_offense_dialog(self):
        self.update_case_information()
        AmendChargeDialog(self).exec()

    def close_event(self):
        self.close_window()

    def close_window(self):
        """Function connected to a button to close the window. Can be connected
        to any button press/click/release to close a window. This can also be called
        at the end of the close_event process to close the dialog."""
        self.close()

    @logger.catch
    def clear_case_information_fields(self):
        self.dialog.defendant_first_name_lineEdit.clear()
        self.dialog.defendant_last_name_lineEdit.clear()
        self.dialog.case_number_lineEdit.clear()
        self.dialog.defendant_first_name_lineEdit.setFocus()

    @logger.catch
    def create_entry(self):
        """Loads the proper template and creates the entry."""
        doc = DocxTemplate(self.dialog.template.template_path)
        case_data = self.dialog.entry_case_information.get_case_information()
        extract_data(case_data)
        doc.render(case_data)
        docname = set_document_name(self.dialog)
        try:
            doc.save(SAVE_PATH + docname)
            os.startfile(SAVE_PATH + docname)
        except PermissionError:
            message = RequiredBox("An entry for this case is already open in Word."
                                  " You must close the Word document first.")
            message.exec()

    @logger.catch
    def create_entry_process(self):
        """The info_checks variable is either "Pass" or "Fail" based on the checks performed by the
        update_info_and_perform_checks method (found in helper_functions.py)."""
        info_checks = self.update_info_and_perform_checks()
        if info_checks == "Pass":
            self.create_entry()

    @logger.catch
    def update_info_and_perform_checks(self):
        self.dialog.update_case_information()
        if InfoChecker.check_defense_counsel(self.dialog) == "Fail":
            return "Fail"
        if check_if_diversion_program_selected(self.dialog) is False:
            return "Fail"
        if InfoChecker.check_plea_and_findings(self.dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_insurance(self.dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_bond_amount(self.dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_additional_conditions_ordered(self.dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_jail_days(self.dialog) == "Fail":
            return "Fail"
        self.dialog.update_case_information()
        return "Pass"

    @logger.catch
    def close_dialog(self):
        self.dialog.close_event()


    @classmethod
    @logger.catch
    def set_statute_and_offense(cls, key, dialog):
        """:key: is the string that is passed by the function each time the field
        is changed on the view."""
        field = None
        if dialog.freeform_entry_checkBox.isChecked():
            return None
        if dialog.sender() == dialog.statute_choice_box:
            field = 'statute'
        elif dialog.sender() == dialog.offense_choice_box:
            field = 'offense'
        query = QSqlQuery(charges_database)
        query_string = f"SELECT * FROM charges WHERE {field} LIKE '%' || :key || '%'"
        query.prepare(query_string)
        query.bindValue(":key", key)
        query.bindValue(field, field)
        query.exec()
        while query.next():
            offense = query.value(1)
            statute = query.value(2)
            degree = query.value(3)
            if field == 'offense':
                if offense == key:
                    dialog.statute_choice_box.setCurrentText(statute)
            elif field == 'statute':
                if statute == key:
                    dialog.offense_choice_box.setCurrentText(offense)
            dialog.degree_choice_box.setCurrentText(degree)
            query.finish()
            break


class BaseChargeDialog(QDialog):
    @logger.catch
    def __init__(self, main_dialog, button_index=None, parent=None):
        super().__init__(parent)
        print(main_dialog)
        self.button_index = button_index
        self.main_dialog = main_dialog
        charges_database.open()
        self.modify_view()
        self.create_dialog_slot_functions()
        self.connect_signals_to_slots()
        self.set_statute_and_offense_choice_boxes()

    def set_statute_and_offense_choice_boxes(self):
        self.statute_choice_box.addItems(create_statute_list())
        self.offense_choice_box.addItems(create_offense_list())
        self.statute_choice_box.setCurrentText("")
        self.offense_choice_box.setCurrentText("")


class AddChargeDialog(BaseChargeDialog, Ui_AddChargeDialog):
    def __init__(self, main_dialog, parent=None):
        print(f"Add charge main dialog is {main_dialog}")
        super().__init__(main_dialog, parent)

    def modify_view(self):
        return AddChargeDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = BaseDialogSlotFunctions(self)

    @logger.catch
    def connect_signals_to_slots(self):
        return AddChargeDialogSignalConnector(self)

    @logger.catch
    def add_charge_process(self):
        """The order of functions that are called when the add_charge_Button is
        clicked(). The order is important to make sure the information is
        updated before the charge is added and the data cleared from the fields."""
        self.add_charge_to_entry_case_information()
        self.main_dialog.add_charge_to_grid()
        self.close_event()

    @logger.catch
    def add_charge_to_entry_case_information(self):
        """TODO: self.criminal_charge_type needs to be fixed to add back in to get costs calculator to work
        again eventually."""
        self.criminal_charge = CriminalCharge()
        self.criminal_charge.offense = self.offense_choice_box.currentText()
        self.criminal_charge.statute = self.statute_choice_box.currentText()
        self.criminal_charge.degree = self.degree_choice_box.currentText()
        # self.criminal_charge.type = self.set_offense_type()
        self.main_dialog.entry_case_information.add_charge_to_list(self.criminal_charge)

    @logger.catch
    def clear_add_charge_fields(self):
        self.statute_choice_box.clearEditText()
        self.offense_choice_box.clearEditText()


class AmendChargeDialog(BaseChargeDialog, Ui_AmendChargeDialog):
    def __init__(self, main_dialog, parent=None):
        super().__init__(main_dialog, parent)
        self.amend_offense_details = AmendOffenseDetails()
        self.charge = self.sender().charge
        self.current_offense_name = self.sender().charge.offense
        self.original_charge_label.setText(self.current_offense_name)

    def modify_view(self):
        return AmendChargeDialogViewModifier(self)

    def create_dialog_slot_functions(self):
        self.functions = BaseDialogSlotFunctions(self)

    @logger.catch
    def connect_signals_to_slots(self):
        return AmendChargeDialogSignalConnector(self)

    @logger.catch
    def clear_amend_charge_fields(self):
        """Clears the fields in the view."""
        self.statute_choice_box.clearEditText()
        self.offense_choice_box.clearEditText()

    @logger.catch
    def amend_offense(self):
        """Adds the data entered for the amended offense to the AmendOffenseDetails
        object then points the entry_case_information object to the AmendOffenseDetails
        object."""
        self.amend_offense_details.original_charge = self.current_offense_name
        self.amend_offense_details.amended_charge = self.offense_choice_box.currentText()
        self.amend_offense_details.motion_disposition = self.motion_decision_box.currentText()
        self.main_dialog.entry_case_information.amend_offense_details = self.amend_offense_details
        if self.motion_decision_box.currentText() == "Granted":
            amended_charge = f"{self.current_offense_name} - AMENDED to {self.amend_offense_details.amended_charge}"
            setattr(self.charge, 'offense', amended_charge)
            self.main_dialog.entry_case_information.amended_charges_list.append(
                (self.amend_offense_details.original_charge, self.amend_offense_details.amended_charge)
            )
            for columns in range(self.main_dialog.charges_gridLayout.columnCount()):
                if (
                    self.main_dialog.charges_gridLayout.itemAtPosition(0, columns) is not None
                    and self.main_dialog.charges_gridLayout.itemAtPosition(
                        0, columns).widget().text() == self.current_offense_name
                ):
                    self.main_dialog.charges_gridLayout.itemAtPosition(0, columns).widget().setText(amended_charge)
                    self.main_dialog.charges_gridLayout.itemAtPosition(1, columns).widget().setText(self.statute_choice_box.currentText())
                    self.main_dialog.charges_gridLayout.itemAtPosition(2, columns).widget().setCurrentText(self.degree_choice_box.currentText())
        self.close_event()



def close_databases():
    """This function is duplicate of the one in base_dialogs.py"""
    charges_database.close()
    charges_database.removeDatabase("QSQLITE")


if __name__ == "__main__":
    print("Slot Functions ran directly")
else:
    print("Slot Functions imported")
    charges_database = open_charges_db_connection()