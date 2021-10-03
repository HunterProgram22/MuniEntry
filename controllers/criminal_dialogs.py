"""The module that contains all controller classes that are commmon to criminal
cases (criminal includes traffic). """
import os
import pathlib
from docxtpl import DocxTemplate

from PyQt5.QtWidgets import QDialog


PATH = str(pathlib.Path().absolute())
TEMPLATE_PATH = PATH + "\\resources\\Templates\\"
SAVE_PATH = PATH + "\\resources\\Saved\\"
DB_PATH = PATH + "\\resources\\db\\"
CHARGES_DATABASE = DB_PATH + "\\charges.sqlite"


class BaseCriminalDialog(QDialog):
    """This class is a base class to provide methods that are used by some or
    all class controllers that are used in the application. This class is never
    instantiated as its own dialog, but the init contains the setup for all
    inherited class controllers."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.doc = None
        self.docname = None

    def close_window(self):
        """Function connected to a button to close the window. Can be connected
        to any button press/click/release to close a window."""
        self.close()

    def create_entry(self):
        """The standard function used to create an entry when a create entry
        button is press/click/released."""
        self.doc = DocxTemplate(self.template.template_path)
        self.doc.render(self.case_information.get_case_information())
        self.set_document_name()
        self.doc.save(SAVE_PATH + self.docname)
        os.startfile(SAVE_PATH + self.docname)

    def set_document_name(self):
        """Sets document name based on the case number and name of the template
        must include '.docx' to make it a Word document."""
        self.docname = (
            self.case_information.case_number + "_" + self.template.template_name + ".docx"
        )

    def set_case_information_banner(self):
        """Sets the banner on a view of the interface. It modifies label
        widgets on the view to text that was entered."""
        self.defendant_name_label.setText(
            "State of Ohio v. {defendant_first_name} {defendant_last_name}".format(
                defendant_first_name = self.case_information.defendant_first_name,
                defendant_last_name = self.case_information.defendant_last_name
                )
            )
        self.case_number_label.setText(self.case_information.case_number)
        if self.case_information.defendant_attorney_name is not None:
            self.defendant_attorney_name_label.setText(
                "Attorney: " + self.case_information.defendant_attorney_name
            )
        else:
            self.defendant_attorney_name_label.setText("Attorney: None")

    def update_case_information(self):
        """Placeholder for future use to refactor out of other dialogs and reduce
        code reuse."""
