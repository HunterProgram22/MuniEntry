import os
import time

from PyQt5.QtSql import QSqlQuery
from db.databases import extract_data
from docxtpl import DocxTemplate
from loguru import logger
from db.databases import open_charges_db_connection, create_offense_list, create_statute_list
from package.controllers.helper_functions import InfoChecker, check_if_diversion_program_selected, set_document_name
from package.views.custom_widgets import RequiredBox
from settings import SAVE_PATH
from win32com import client


class CriminalSlotFunctions:
    """Class for common criminal functions that are connected to slots/buttons in a dialog."""
    @classmethod
    @logger.catch
    def clear_case_information_fields(cls, dialog):
        """Clears the text in the fields in the top cms_case information frame and resets the cursor
        to the first text entry (defendant_first_name_lineEdit) box."""
        dialog.defendant_first_name_lineEdit.clear()
        dialog.defendant_last_name_lineEdit.clear()
        dialog.case_number_lineEdit.clear()
        dialog.defendant_first_name_lineEdit.setFocus()

    @classmethod
    @logger.catch
    def create_entry_process(cls, _bool, dialog):
        """The info_checks variable is either "Pass" or "Fail" based on the checks performed by the
        update_info_and_perform_checks method (found in helper_functions.py)."""
        info_checks = cls.update_info_and_perform_checks(dialog)
        if info_checks == "Pass":
            create_entry(dialog)

    @classmethod
    @logger.catch
    def print_entry_process(cls, _bool, dialog):
        info_checks = cls.update_info_and_perform_checks(dialog)
        if info_checks == "Pass":
            create_entry(dialog, print_doc=True)

    @classmethod
    @logger.catch
    def update_info_and_perform_checks(cls, dialog):
        dialog.update_case_information()
        if InfoChecker.check_defense_counsel(dialog) == "Fail":
            return "Fail"
        if check_if_diversion_program_selected(dialog) is False:
            return "Fail"
        if InfoChecker.check_plea_and_findings(dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_insurance(dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_bond_amount(dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_additional_conditions_ordered(dialog) == "Fail":
            return "Fail"
        if InfoChecker.check_jail_days(dialog) == "Fail":
            return "Fail"
        dialog.update_case_information()
        return "Pass"

    @classmethod
    @logger.catch
    def close_dialog(cls, dialog):
        dialog.close_event()


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


def print_document(docname):
    word = client.Dispatch("Word.Application")
    word.Documents.Open(SAVE_PATH + docname)
    word.ActiveDocument.PrintOut()
    time.sleep(1)
    word.ActiveDocument.Close()
    word.Quit()


@logger.catch
def create_entry(dialog, print_doc=False):
    """Loads the proper template and creates the entry."""
    doc = DocxTemplate(dialog.template.template_path)
    case_data = dialog.entry_case_information.get_case_information()
    extract_data(case_data)
    doc.render(case_data)
    docname = set_document_name(dialog)
    try:
        doc.save(SAVE_PATH + docname)
        if print_doc is True:
            print_document(docname)
        os.startfile(SAVE_PATH + docname)
    except PermissionError:
        message = RequiredBox("An entry for this case is already open in Word."
                              " You must close the Word document first.")
        message.exec()


def close_databases():
    """This function is duplicate of the one in base_dialogs.py"""
    charges_database.close()
    charges_database.removeDatabase("QSQLITE")


if __name__ == "__main__":
    print("Slot Functions ran directly")
else:
    print("Slot Functions imported")
    charges_database = open_charges_db_connection()