"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""
from PyQt5.QtWidgets import QDialog, QComboBox, QCheckBox, QLineEdit, QTextEdit, \
    QDateEdit, QTimeEdit, QRadioButton

from db.databases import open_charges_db_connection
from package.controllers.slot_functions import charges_database
from package.models.case_information import CriminalCharge


def close_databases():
    charges_database.close()
    charges_database.removeDatabase("QSQLITE")


class BaseDialog(QDialog):
    """This class is a base class for all dialog windows. Every window must have a view loaded
    (modify view), slot functions created, and then the functions connected to signals."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.modify_view()
        self.create_dialog_slot_functions()
        self.connect_signals_to_slots()

    def modify_view(self):
        """The modify view method runs the self.setupUI method to setup the UI.
        Place items in this returned class that can't be added directly in QtDesigner (or are
        more easily added later) so that they don't need to be changed in the view file each
        time pyuic5 is run."""
        raise NotImplementedError

    def create_dialog_slot_functions(self):
        """Each dialog has functions tied to certain slots (i.e. buttons, checkboxes, etc.) the
        functions are placed in a class and returned to the main dialog so that they can be
        connected to the signals."""
        raise NotImplementedError

    def connect_signals_to_slots(self):
        """Each dialog has its own signal connector class that connects the signals to the
        slot functions class for that dialog."""
        raise NotImplementedError

    def transfer_field_data_to_model(self, terms_object):
        """Function that loops through a list of fields and transfers the data in the field
        to the appropriate model attribute. The function uses the appropriate pyqt method for
        the field type. Format of item in terms_list is a list of tuples (item[0] = model data,
        item[1] = view field that contains the data)

        The try/except block accounts for dialogs that may not have an attribute from a
        terms_list."""
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
                    setattr(terms_object, model_attribute, getattr(self, view_field).date(
                        ).toString("MMMM dd, yyyy"))
                elif isinstance(getattr(self, view_field), QTimeEdit):
                    setattr(terms_object, model_attribute, getattr(self, view_field).time(
                        ).toString("hh:mm A"))
            except AttributeError:
                pass


class CmsLoader:
    """Uses the cms_case number selected to get the cms_case object from main_window and
    load cms_case data."""
    def __init__(self, dialog):
        self.cms_case = dialog.cms_case
        self.criminal_charge = None
        self.load_cms_data(dialog)

    def load_cms_data(self, dialog):
        if self.cms_case.case_number is not None:
            dialog.case_number_lineEdit.setText(self.cms_case.case_number)
            dialog.defendant_first_name_lineEdit.setText(self.cms_case.defendant.first_name)
            dialog.defendant_last_name_lineEdit.setText(self.cms_case.defendant.last_name)
            dialog.defense_counsel_name_box.addItem(self.cms_case.defense_counsel)
            dialog.defense_counsel_name_box.setCurrentText(self.cms_case.defense_counsel)
            if self.cms_case.defense_counsel_type == "PD":
                dialog.defense_counsel_type_box.setCurrentText("Public Defender")
            else:
                dialog.defense_counsel_type_box.setCurrentText("Private Counsel")
            self.add_cms_criminal_charges_to_entry_case_information(dialog)

    def add_cms_criminal_charges_to_entry_case_information(self, dialog):
        """Loads the data from the cms_case object that is created from the sql table."""
        for charge in self.cms_case.charges_list:
            self.criminal_charge = CriminalCharge()
            (self.criminal_charge.offense, self.criminal_charge.statute,
             self.criminal_charge.degree, self.criminal_charge.type) = charge
            self.criminal_charge.type = self.set_offense_type_from_daily_case_list()
            dialog.entry_case_information.add_charge_to_list(self.criminal_charge)
            dialog.add_charge_to_grid()
            dialog.setFocus()


    def set_offense_type_from_daily_case_list(self):
        """TODO: This is currently setting the charge type to Moving if CMS provides
        'No Data', but perhaps should be set to Non-moving?"""
        if self.criminal_charge.type == "False":
            if self.cms_case.case_number[2:5] == "CRB":
                return "Criminal"
            else:
                return "Non-moving"
        elif self.criminal_charge.type == "True":
            return "Moving"
        else:
            return "Moving"


class CmsFraLoader(CmsLoader):
    """This subclass is used for the Fine Only Plea and Jail CC Plea Dialogs to load the
    FRA (insurance) data for the case."""
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
    charges_database = open_charges_db_connection()
else:
    print("Base Dialogs imported")
    charges_database = open_charges_db_connection()
