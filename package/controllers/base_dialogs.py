"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""
from PyQt5.QtWidgets import QDialog

from settings import WIDGET_TYPE_ACCESS_DICT


class BaseDialog(QDialog):
    """This class is a base class for all dialog windows."""

    def __init__(self, parent: QDialog = None) -> None:
        super().__init__(parent)
        self.modify_view()
        self.create_dialog_slot_functions()
        self.connect_signals_to_slots()

    def modify_view(self):
        raise NotImplementedError

    def create_dialog_slot_functions(self):
        raise NotImplementedError

    def connect_signals_to_slots(self):
        raise NotImplementedError

    def transfer_view_data_to_model(self, model_class: object) -> None:
        """Takes data in the view fields and transfers to appropriate model class attribute.

        Method loops through all items in terms list which are maps of a model attribute to
        a view field. The appropriate transfer method is obtained from the WIDGET_TYPE_ACCESS_DICT

        Args:
            model_class: A dataclass object that has a terms_list attribute mapping
                view fields to model attributes.
        """
        for (model_attribute, view_field) in model_class.terms_list:
            key = getattr(self, view_field).__class__.__name__
            view = getattr(self, view_field)
            setattr(model_class, model_attribute, getattr(view, WIDGET_TYPE_ACCESS_DICT.get(key))())
