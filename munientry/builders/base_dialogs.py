"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""
from __future__ import annotations

from typing import Any

from loguru import logger
from PyQt5.QtGui import QCloseEvent, QIntValidator
from PyQt5.QtWidgets import QDialog

from munientry.models.cms_models import CmsCaseInformation
from munientry.models.party_types import JudicialOfficer
from munientry.settings import WIDGET_TYPE_ACCESS_DICT


class BaseDialog(QDialog):
    """This class is a base class for all dialog windows."""

    def __init__(self, parent: QDialog = None) -> None:
        super().__init__(parent)
        self.modify_view()
        self.connect_signals_to_slots()

    def modify_view(self) -> None:
        raise NotImplementedError

    def connect_signals_to_slots(self) -> None:
        """Abstract method that connects signals to dialog slot functions.

        Raises:
            NotImplementedError: if the dialog does not implement the method.
        """
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
            setattr(
                model_class,
                model_attribute,
                getattr(view, WIDGET_TYPE_ACCESS_DICT.get(key, 'None'))(),
            )

    def closeEvent(self, event: QCloseEvent) -> None:
        """Extends pyqt close event method in order to log when a dialog closes."""
        logger.dialog(f'{self.objectName()} Closed')


class CriminalBaseDialog(BaseDialog):
    """The base class for all criminal and traffic main entry dialogs."""

    def __init__(
        self,
        judicial_officer: JudicialOfficer,
        cms_case: CmsCaseInformation = None,
        case_table: str = None,
        parent: BaseDialog = None,
    ) -> None:
        """Self.case_table must be set before the call to super().__init__.

        The init of BaseDialog, called by super().__init__ calls ModifyView which will use the
        case table.
        """
        self.case_table = case_table
        logger.info(f'Loading case from {self.case_table}')
        super().__init__(parent)
        self.judicial_officer = judicial_officer
        self.cms_case = cms_case
        self.validator = QIntValidator(0, 1000, self)
        loaded_case = cms_case.case_number
        logger.info(f'Loaded Case {loaded_case}')
        self.load_entry_case_information_model()
        self.load_cms_data_to_view()
        try:
            self.defense_counsel_name_box.load_attorneys()
        except AttributeError as error:
            logger.warning(error)
        self.criminal_charge = None
        self.popup_dialog = None

    def load_entry_case_information_model(self):
        raise NotImplementedError

    def load_cms_data_to_view(self) -> None:
        raise NotImplementedError

    def update_entry_case_information(self) -> None:
        raise NotImplementedError

    def perform_info_checks(self) -> None:
        raise NotImplementedError

    # TO BE REFACTORED #
    def add_charge_to_grid(self):
        self.charges_gridLayout.add_fields_to_charges_grid(self)
        self.defense_counsel_name_box.setFocus()


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
