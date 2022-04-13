"""The BaseDialogs modules contains common base classes from which other dialogs
inherit."""
from PyQt5.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDialog,
    QLineEdit,
    QRadioButton,
    QTextEdit,
    QTimeEdit,
)


class BaseDialog(QDialog):
    """This class is a base class for all dialog windows. Every window must have a view loaded
    (modify view), slot functions created, and then the slot functions connected to signals."""

    def __init__(self, parent: QDialog = None) -> None:
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

    def transfer_field_data_to_model(self, terms_object: object) -> None:
        """Function that loops through a list of fields and transfers the data in the field
        to the appropriate model attribute. The function uses the appropriate pyqt method for
        the field type. Format of item in terms_list is a list of tuples (item[0] = model data,
        item[1] = view field that contains the data)."""
        terms_list = getattr(terms_object, "terms_list")
        for item in terms_list:
            (model_attribute, view_field) = item
            if view_field == "other_conditions_checkBox": # TODO: This exists to address OtherConditions using ordered in terms list
                continue
            elif isinstance(getattr(self, view_field), QComboBox):
                setattr(
                    terms_object,
                    model_attribute,
                    getattr(self, view_field).currentText(),
                )
            elif isinstance(getattr(self, view_field), QCheckBox):
                setattr(
                    terms_object,
                    model_attribute,
                    getattr(self, view_field).isChecked(),
                )
            elif isinstance(getattr(self, view_field), QRadioButton):
                setattr(
                    terms_object,
                    model_attribute,
                    getattr(self, view_field).isChecked(),
                )
            elif isinstance(getattr(self, view_field), QLineEdit):
                setattr(terms_object, model_attribute, getattr(self, view_field).text())
            elif isinstance(getattr(self, view_field), QTextEdit):
                plain_text = getattr(self, view_field).toPlainText()
                try:
                    if plain_text[-1] == ".":
                        plain_text = plain_text[:-1]
                except IndexError:
                    pass
                setattr(terms_object, model_attribute, plain_text)
            elif isinstance(getattr(self, view_field), QDateEdit):
                setattr(
                    terms_object,
                    model_attribute,
                    getattr(self, view_field).date().toString("MMMM dd, yyyy"),
                )
            elif isinstance(getattr(self, view_field), QTimeEdit):
                setattr(
                    terms_object,
                    model_attribute,
                    getattr(self, view_field).time().toString("hh:mm A"),
                )


if __name__ == "__main__":
    print("Base Dialogs ran directly")
else:
    print("Base Dialogs imported")
