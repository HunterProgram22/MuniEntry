"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""
from typing import Any

from PyQt5.QtWidgets import QDialog
from package.models.case_information import CriminalCaseInformation
from package.views.custom_widgets import DefenseCounselComboBox, NoScrollComboBox

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

    def transfer_view_data_to_model(self, model_class: type[Any]) -> None:
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


class CriminalBaseDialog(BaseDialog):
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        self.case_table = case_table
        super().__init__(parent)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        self.entry_case_information = CriminalCaseInformation(self.judicial_officer)
        self.load_cms_data_to_view()
        self.defense_counsel_name_box.__class__ = DefenseCounselComboBox
        self.defense_counsel_name_box.load_attorneys()
        self.appearance_reason_box.__class__ = NoScrollComboBox
        self.defense_counsel_type_box.__class__ = NoScrollComboBox
        self.criminal_charge = None
        self.popup_dialog = None

    def load_cms_data_to_view(self):
        raise NotImplementedError

    def update_entry_case_information(self):
        raise NotImplementedError

    def perform_info_checks(self):
        raise NotImplementedError

    # TO BE REFACTORED #
    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.defense_counsel_name_box.setFocus()
