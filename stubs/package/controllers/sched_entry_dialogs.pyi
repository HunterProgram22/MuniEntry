from PyQt5.QtCore import QDate
from package.controllers.base_dialogs import BaseDialog as BaseDialog
from package.controllers.cms_case_loaders import CmsNoChargeLoader as CmsNoChargeLoader
from package.controllers.signal_connectors import BaseDialogSignalConnector as BaseDialogSignalConnector
from package.controllers.slot_functions import BaseDialogSlotFunctions as BaseDialogSlotFunctions
from package.controllers.view_modifiers import BaseDialogViewModifier as BaseDialogViewModifier
from package.models.scheduling_information import SchedulingCaseInformation as SchedulingCaseInformation
from package.models.template_types import TEMPLATE_DICT as TEMPLATE_DICT
from package.updaters.general_updaters import CaseInformationUpdater as CaseInformationUpdater
from package.views.scheduling_entry_dialog_ui import Ui_SchedulingEntryDialog as Ui_SchedulingEntryDialog
from typing import Any

TODAY: Any
SPEEDY_TRIAL_TIME_DICT: Any
DAY_DICT: Any
EVENT_DICT: Any
PRETRIAL_TIME_DICT: Any

class SchedulingEntryDialog(BaseDialog, Ui_SchedulingEntryDialog):
    case_table: Any
    dialog_name: Any
    judicial_officer: Any
    cms_case: Any
    template: Any
    entry_case_information: Any
    def __init__(self, judicial_officer: Any | None = ..., dialog_name: Any | None = ..., cms_case: Any | None = ..., case_table: Any | None = ..., parent: Any | None = ...) -> None: ...
    def load_cms_data_to_view(self): ...
    def modify_view(self): ...
    functions: Any
    def create_dialog_slot_functions(self) -> None: ...
    def connect_signals_to_slots(self) -> None: ...
    def update_entry_case_information(self): ...

class SchedulingEntryDialogViewModifier(BaseDialogViewModifier):
    dialog: Any
    def __init__(self, dialog) -> None: ...
    def set_view_dates(self) -> None: ...

class SchedulingEntryDialogSignalConnector(BaseDialogSignalConnector):
    dialog: Any
    functions: Any
    def __init__(self, dialog) -> None: ...

class SchedulingEntryDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    def __init__(self, dialog) -> None: ...
    def set_pretrial_scheduled(self) -> None: ...
    def update_all_scheduled_dates(self) -> None: ...
    def update_final_pretrial_and_pretrial_only(self) -> None: ...
    def set_event_date(self, day_to_set: str, event_to_set: str) -> QDate: ...
    def get_pretrial_time(self) -> int: ...
    def get_speedy_trial_date(self) -> QDate: ...
    def set_speedy_trial_date_label(self) -> None: ...
    def get_speedy_trial_days(self) -> int: ...
    def get_days_in_jail(self) -> int: ...
    def get_continuance_days(self) -> int: ...

class SchedulingEntryDialogCaseInformationUpdater(CaseInformationUpdater):
    def __init__(self, dialog) -> None: ...
    def update_model_with_case_information_frame_data(self) -> None: ...
    def set_case_number_and_date(self) -> None: ...
    def set_party_information(self) -> None: ...
    def set_defense_counsel_information(self) -> None: ...
    def set_scheduling_dates(self) -> None: ...