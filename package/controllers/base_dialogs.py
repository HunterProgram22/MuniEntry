"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""
from PyQt5.QtWidgets import QDialog, QComboBox, QCheckBox, QLineEdit, QTextEdit, QDateEdit, QTimeEdit, QRadioButton

from db.databases import open_charges_db_connection
from package.controllers.slot_functions import charges_database
from package.models.case_information import CriminalCharge


def close_databases():
    charges_database.close()
    charges_database.removeDatabase("QSQLITE")


class BaseDialog(QDialog):
    """This class is a base class to provide methods that are used by some criminal controllers
     in the application. This class is never instantiated as its own dialog, but the init contains
     the setup for all inherited class controllers."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.modify_view()
        self.create_dialog_slot_functions()
        self.connect_signals_to_slots()

    def modify_view(self):
        """The modify view method updates the view that is created on init with self.setupUI.
        Place items in this method that can't be added directly in QtDesigner (or are more easily added later)
        so that they don't need to be changed in the view file each time pyuic5 is run."""
        raise NotImplementedError

    def create_dialog_slot_functions(self):
        raise NotImplementedError

    def connect_signals_to_slots(self):
        raise NotImplementedError

    def transfer_field_data_to_model(self, terms_object):
        """Function that loops through a list of fields and transfers the data in the field
        to the appropriate model attribute. The function uses the appropriate pyqt method for the field type.
        Format of item in terms_list is a list of tuples (item[0] = model data,
        item[1] = view field that contains the data)

        The try/except block accounts for dialogs that may not have an attribute from a terms_list."""
        terms_list = getattr(terms_object, "terms_list")
        for item in terms_list:
            (model_attribute, view_field) = item
            try:
                if isinstance(getattr(self, view_field), QComboBox):
                    setattr(terms_object, model_attribute, getattr(self, view_field).currentText())
                elif isinstance(getattr(self, view_field), QCheckBox):
                    setattr(terms_object, model_attribute, getattr(self, view_field).isChecked())
                elif isinstance(getattr(self, view_field), QRadioButton):
                    setattr(terms_object, model_attribute, getattr(self, view_field).isChecked())
                elif isinstance(getattr(self, view_field), QLineEdit):
                    setattr(terms_object, model_attribute, getattr(self, view_field).text())
                elif isinstance(getattr(self, view_field), QTextEdit):
                    plain_text = getattr(self, view_field).toPlainText()
                    try:
                        if plain_text[-1] == '.':
                            plain_text = plain_text[:-1]
                    except IndexError:
                        pass
                    setattr(terms_object, model_attribute, plain_text)
                elif isinstance(getattr(self, view_field), QDateEdit):
                    setattr(terms_object, model_attribute, getattr(self, view_field).date().toString("MMMM dd, yyyy"))
                elif isinstance(getattr(self, view_field), QTimeEdit):
                    setattr(terms_object, model_attribute, getattr(self, view_field).time().toString("hh:mm A"))
            except AttributeError:
                pass


class CMSLoader:
    """Uses the cms_case number selected to get the cms_case object from main and load cms_case data."""
    def __init__(self, dialog):
        self.cms_case = dialog.cms_case
        self.criminal_charge = None
        self.load_cms_data(dialog)

    def load_cms_data(self, dialog):
        if self.cms_case.case_number is not None:
            dialog.case_number_lineEdit.setText(self.cms_case.case_number)
            dialog.defendant_first_name_lineEdit.setText(self.cms_case.defendant.first_name)
            dialog.defendant_last_name_lineEdit.setText(self.cms_case.defendant.last_name)
            self.add_cms_criminal_charges_to_entry_case_information(dialog)
        else:
            return None

    def add_cms_criminal_charges_to_entry_case_information(self, dialog):
        """Loads the data from the cms_case object that is created from the sql table.
        self.criminal_charge.type = self.set_offense_type() FIGURE OUT FOR COSTS"""
        for charge in self.cms_case.charges_list:
            self.criminal_charge = CriminalCharge()
            (self.criminal_charge.offense, self.criminal_charge.statute,
             self.criminal_charge.degree, self.criminal_charge.type) = charge
            dialog.entry_case_information.add_charge_to_list(self.criminal_charge)
            dialog.add_charge_to_grid()


class CMS_FRALoader(CMSLoader):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.add_fra_data(dialog)

    def add_fra_data(self, dialog):
        fra_value_dict = {"Y": "Yes", "N": "No", "U": "N/A"}
        if self.cms_case.case_number is None:
            dialog.fra_in_file_box.setCurrentText("N/A")
        elif self.cms_case.case_number[2:5] == "CRB":
            dialog.fra_frame.setHidden(True)
        elif self.cms_case.fra_in_file in fra_value_dict:
            dialog.fra_in_file_box.setCurrentText(fra_value_dict[self.cms_case.fra_in_file])
        else:
            dialog.fra_in_file_box.setCurrentText("N/A")
        dialog.functions.set_fra_in_file(dialog.fra_in_file_box.currentText())
        dialog.functions.set_fra_in_court(dialog.fra_in_court_box.currentText())


if __name__ == "__main__":
    print("Base Dialogs ran directly")
else:
    print("Base Dialogs imported")
    """Databases must be opened first in order for them to be accessed
    when the UI is built so it can populate fields."""
    charges_database = open_charges_db_connection()
