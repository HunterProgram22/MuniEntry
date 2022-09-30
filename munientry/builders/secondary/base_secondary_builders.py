"""Contains base classes for secondary dialogs."""
from __future__ import annotations

from typing import Any

from loguru import logger
from munientry.builders.base_builders import BaseDialogBuilder
from munientry.settings import WIDGET_TYPE_ACCESS_DICT


class SecondaryDialogBuilder(BaseDialogBuilder):
    """The base class for all secondary dialogs called from other dialogs."""
    def __init__(self, main_dialog, parent):
        self.charges_list = main_dialog.entry_case_information.charges_list
        self.main_dialog = main_dialog
        super().__init__(parent)

    def transfer_view_data_to_model(self, model_class: type[Any]) -> None:
        """Takes data in the view fields and transfers to appropriate model class attribute.

        Method loops through all items in terms list which are maps of a model attribute to
        a view field. The appropriate transfer method is obtained from the WIDGET_TYPE_ACCESS_DICT

        Args:
            model_class: A dataclass object that has a terms_list attribute mapping
                view fields to model attributes.
        """
        for (model_attribute, view_field) in model_class.terms_list:
            widget_type = getattr(self, view_field).__class__.__name__
            view = getattr(self, view_field)
            view_field_data = getattr(view, WIDGET_TYPE_ACCESS_DICT.get(widget_type, 'None'))()
            class_name = model_class.__class__.__name__
            setattr(model_class, model_attribute, view_field_data)
            logger.info(f'{class_name} {model_attribute} set to: {view_field_data}.')