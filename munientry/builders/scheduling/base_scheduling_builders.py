from __future__ import annotations

from typing import Any

from loguru import logger
from munientry.builders.base_builders import BaseDialogBuilder
from munientry.models.template_types import TEMPLATE_DICT
from munientry.settings import WIDGET_TYPE_ACCESS_DICT


class SchedulingBaseDialog(BaseDialogBuilder):
    """The base class for all scheduling entries."""

    def __init__(self, judicial_officer=None, cms_case=None, case_table=None, parent=None):
        self.case_table = case_table
        super().__init__(parent)
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        self.load_entry_case_information_model()
        self.load_cms_data_to_view()
        case_number = cms_case.case_number
        logger.info(f'Loading {case_number} from {self.case_table}')
        self.additional_setup()

    def additional_setup(self):
        """Abstract base method used in subclasses for additional setup after init."""

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
