"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""
from PyQt5.QtWidgets import QDialog

from settings import WIDGET_TYPE_ACCESS_DICT

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

    def transfer_view_data_to_model(self, terms_object: object) -> None:
        """Loops through a model's terms list to transfer data from the view to the model using
        the appropriate method for the view widget."""
        terms_list = getattr(terms_object, "terms_list")
        for (model_attribute, view_field) in terms_list:
            key = getattr(self, view_field).__class__.__name__
            view = getattr(self, view_field)
            setattr(terms_object, model_attribute, getattr(view, WIDGET_TYPE_ACCESS_DICT.get(key))())


if __name__ == "__main__":
    print("Base Dialogs ran directly")
else:
    print("Base Dialogs imported")
