"""The BaseDialogs modules contains common base classes from which other dialogs inherit."""
from __future__ import annotations

from typing import Any

from loguru import logger
from PyQt5.QtGui import QCloseEvent, QIntValidator
from PyQt5.QtWidgets import QDialog

from munientry.models.scheduling_information import SchedulingCaseInformation
from munientry.settings import TYPE_CHECKING, WIDGET_TYPE_ACCESS_DICT
from munientry.models.template_types import TEMPLATE_DICT

if TYPE_CHECKING:
    from munientry.models.cms_models import CmsCaseInformation
    from munientry.models.party_types import JudicialOfficer


class BaseDialogBuilder(QDialog):
    """This class is a base class for all dialog windows."""

    def __init__(self, parent: QDialog = None) -> None:
        super().__init__(parent)
        self.build_attrs = self._get_dialog_attributes()
        self._modify_view()
        self._connect_signals_to_slots()
        self.dialog_name = self.build_attrs.get('dialog_name', None)
        self.template = TEMPLATE_DICT.get(self.dialog_name)

    def _get_dialog_attributes(self):
        return self.build_dict

    def _modify_view(self) -> None:
        self.build_attrs.get('view')(self)

    def _connect_signals_to_slots(self) -> None:
        self.functions = self.build_attrs.get('slots')(self)
        self.build_attrs.get('signals')(self)

    def load_entry_case_information_model(self):
        self.entry_case_information = self.build_attrs.get('case_information_model')()

    def load_cms_data_to_view(self) -> None:
        self.build_attrs.get('loader')(self)

    def update_entry_case_information(self) -> None:
        self.build_attrs.get('updater')(self)

    def perform_info_checks(self) -> None:
        self.dialog_checks = self.build_attrs.get('info_checker')(self)

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

    def closeEvent(self, event: QCloseEvent) -> None:
        """Extends pyqt close event method in order to log when a dialog closes."""
        logger.dialog(f'{self.objectName()} Closed by {event}')


class CriminalDialogBuilder(BaseDialogBuilder):
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


    # TO BE REFACTORED #
    def add_charge_to_grid(self):
        self.charges_gridLayout.add_fields_to_charges_grid(self)
        self.defense_counsel_name_box.setFocus()


class BaseDialog(QDialog):
    """This class is a base class for all dialog windows."""

    def __init__(self, parent: QDialog = None) -> None:
        super().__init__(parent)
        self._modify_view()
        self._connect_signals_to_slots()

    def _modify_view(self) -> None:
        """Abstract method that calls setupUI and creates the view.

        Raises:
            NotImplementedError: if the dialog does not implement the method.
        """
        raise NotImplementedError

    def _connect_signals_to_slots(self) -> None:
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
            widget_type = getattr(self, view_field).__class__.__name__
            view = getattr(self, view_field)
            view_field_data = getattr(view, WIDGET_TYPE_ACCESS_DICT.get(widget_type, 'None'))()
            class_name = model_class.__class__.__name__
            setattr(model_class, model_attribute, view_field_data)
            logger.info(f'{class_name} {model_attribute} set to: {view_field_data}.')

    def closeEvent(self, event: QCloseEvent) -> None:
        """Extends pyqt close event method in order to log when a dialog closes."""
        logger.dialog(f'{self.objectName()} Closed by {event}')


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


class SchedulingBaseDialog(BaseDialog):
    """The base class for all scheduling entries."""

    def __init__(self, judicial_officer=None, cms_case=None, case_table=None, parent=None):
        super().__init__(parent)
        self.case_table = case_table
        self.judicial_officer = judicial_officer
        self.entry_case_information = SchedulingCaseInformation()
        self.cms_case = cms_case
        case_number = cms_case.case_number
        logger.info(f'Loading {case_number} from {self.case_table}')
        self.load_cms_data_to_view()


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
