"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""
import os

from controllers.helper_functions import set_document_name
from docxtpl import DocxTemplate
from loguru import logger

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtGui
from settings import SAVE_PATH

# Slot Functions
@logger.catch
def create_entry_process(dialog):
    """The order of the create entry process is important to make sure the
    information is updated before the entry is created."""
    dialog.update_case_information()
    if dialog.charges_gridLayout.check_plea_and_findings() is None:
        return None
    create_entry(dialog)
    dialog.close_event()

@logger.catch
def create_entry(dialog):
    """Loads the proper template and creates the entry."""
    doc = DocxTemplate(dialog.template.template_path)
    doc.render(dialog.case_information.get_case_information())
    docname = set_document_name(dialog)
    doc.save(SAVE_PATH + docname)
    os.startfile(SAVE_PATH + docname)

@logger.catch
def clear_case_information_fields(dialog):
    """Clears the text in the fields in the top case information frame and resets the cursor
    to the first text entry (defendant_first_name_lineEdit) box."""
    dialog.defendant_first_name_lineEdit.clear()
    dialog.defendant_last_name_lineEdit.clear()
    dialog.case_number_lineEdit.clear()
    dialog.defendant_first_name_lineEdit.setFocus()


class BaseDialog(QDialog):
    """This class is a base class to provide methods that are used by some criminal controllers
     in the application. This class is never instantiated as its own dialog, but the init contains
     the setup for all inherited class controllers."""
    def __init__(self, judicial_officer, case=None, parent=None):
        """Databases must be opened first in order for them to be accessed
        when the UI is built so it can populate fields.The setupUI calls to
        the view to create the UI."""
        super().__init__(parent)
        self.setWindowIcon(QtGui.QIcon('./resources/icons/gavel.jpg'))
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowMaximizeButtonHint)
        self.judicial_officer = judicial_officer
        self.case = case
        self.setupUi(self)
        self.modify_view()
        self.connect_signals_to_slots()

    @logger.catch
    def modify_view(self):
        """The modify view method updates the view that is created on init with self.setupUI.
        Place items in this method that can't be added directly in QtDesigner (or are more easily added later)
        so that they don't need to be changed in the view file each time pyuic5 is run."""
        pass

    @logger.catch
    def connect_signals_to_slots(self):
        """This method includes buttons common to all dialogs. Buttons that are
        specific to only a certain dialog are added in the subclassed version of the method.

        The create entry process is connected with a lambda function because it needs the dialog to be
        passed as an argument (dialog = self) and if it is connected without lambda it would be called on
        dialog creation instead of upon button pressed."""
        self.cancel_Button.pressed.connect(self.close_event)
        self.clear_fields_case_Button.pressed.connect(lambda dialog=self: clear_case_information_fields(dialog))
        self.create_entry_Button.pressed.connect(lambda dialog=self: create_entry_process(dialog))

    def set_case_number_and_date(self):
        self.case_information.case_number = self.case_number_lineEdit.text()
        self.case_information.plea_trial_date = self.plea_trial_date.date().toString("MMMM dd, yyyy")

    @logger.catch
    def update_case_information(self):
        """"Docstring needs updating."""
        self.set_case_number_and_date()
        self.set_party_information()

    @logger.catch
    def set_party_information(self):
        """Updates the party information from the GUI(view) and saves it to the model."""
        self.case_information.defendant.first_name = self.defendant_first_name_lineEdit.text()
        self.case_information.defendant.last_name = self.defendant_last_name_lineEdit.text()

    @logger.catch
    def close_window(self):
        """Function connected to a button to close the window. Can be connected
        to any button press/click/release to close a window. This can also be called
        at the end of the close_event process to close the dialog."""
        self.close()

    @logger.catch
    def close_event(self):
        """Place any cleanup items (i.e. close_databases) here that should be
        called when the entry is created and the dialog closed."""
        self.close_window()
