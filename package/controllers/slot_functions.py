import os

from PyQt5.QtSql import QSqlQuery

from db.databases import extract_data
from docxtpl import DocxTemplate
from loguru import logger
from db.databases import open_charges_db_connection
from package.controllers.base_dialogs import charges_database
from package.controllers.helper_functions import InfoChecker, check_if_diversion_program_selected, set_document_name

from package.views.custom_widgets import RequiredBox

from settings import SAVE_PATH


class BaseDialogSlotFunctions(object):
    def __init__(self, dialog):
        self.dialog = dialog

    @logger.catch
    def start_add_charge_dialog(self):
        from package.controllers.signal_connectors import AddChargeDialog
        self.dialog.update_case_information()
        AddChargeDialog(self.dialog).exec()

    @logger.catch
    def start_amend_offense_dialog(self):
        from package.controllers.signal_connectors import AmendChargeDialog
        self.dialog.update_case_information()
        AmendChargeDialog(self.dialog).exec()

    def close_event(self):
        self.close_window()

    def close_window(self):
        """Function connected to a button to close the window. Can be connected
        to any button press/click/release to close a window. This can also be called
        at the end of the close_event process to close the dialog."""
        self.dialog.close()

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






def close_databases():
    """This function is duplicate of the one in base_dialogs.py"""
    charges_database.close()
    charges_database.removeDatabase("QSQLITE")


if __name__ == "__main__":
    print("Slot Functions ran directly")
else:
    print("Slot Functions imported")
    charges_database = open_charges_db_connection()


