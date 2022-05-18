from package.controllers.base_dialogs import BaseDialog as BaseDialog
from package.controllers.signal_connectors import AddCommunityControlDialogSignalConnector as AddCommunityControlDialogSignalConnector, AddConditionsDialogSignalConnector as AddConditionsDialogSignalConnector, AddJailOnlyDialogSignalConnector as AddJailOnlyDialogSignalConnector, AddSpecialBondConditionsDialogSignalConnector as AddSpecialBondConditionsDialogSignalConnector
from package.controllers.slot_functions import AddCommunityControlDialogSlotFunctions as AddCommunityControlDialogSlotFunctions, AddConditionsDialogSlotFunctions as AddConditionsDialogSlotFunctions, AddJailOnlyDialogSlotFunctions as AddJailOnlyDialogSlotFunctions, AddSpecialBondConditionsDialogSlotFunctions as AddSpecialBondConditionsDialogSlotFunctions
from package.controllers.view_modifiers import AddCommunityControlDialogViewModifier as AddCommunityControlDialogViewModifier, AddConditionsDialogViewModifier as AddConditionsDialogViewModifier, AddJailOnlyDialogViewModifier as AddJailOnlyDialogViewModifier, AddSpecialBondConditionsDialogViewModifier as AddSpecialBondConditionsDialogViewModifier
from package.views.add_community_control_dialog_ui import Ui_AddCommunityControlDialog as Ui_AddCommunityControlDialog
from package.views.add_conditions_dialog_ui import Ui_AddConditionsDialog as Ui_AddConditionsDialog
from package.views.add_jail_only_dialog_ui import Ui_AddJailOnly as Ui_AddJailOnly
from package.views.add_special_bond_conditions_dialog_ui import Ui_AddSpecialBondConditionsDialog as Ui_AddSpecialBondConditionsDialog
from typing import Any

def enable_condition_frames(conditions_dialog, main_dialog) -> None: ...

class AddConditionsDialog(BaseDialog, Ui_AddConditionsDialog):
    CONDITIONS_FRAMES: Any
    charges_list: Any
    main_dialog: Any
    def __init__(self, main_dialog, parent: Any | None = ...) -> None: ...
    def modify_view(self): ...
    functions: Any
    def create_dialog_slot_functions(self) -> None: ...
    def connect_signals_to_slots(self): ...

class AddJailOnlyDialog(BaseDialog, Ui_AddJailOnly):
    condition_checkbox_dict: Any
    charges_list: Any
    main_dialog: Any
    def __init__(self, main_dialog, parent: Any | None = ...) -> None: ...
    def modify_view(self): ...
    functions: Any
    def create_dialog_slot_functions(self) -> None: ...
    def connect_signals_to_slots(self): ...

class AddCommunityControlDialog(BaseDialog, Ui_AddCommunityControlDialog):
    CONDITIONS_FRAMES: Any
    condition_checkbox_dict: Any
    charges_list: Any
    main_dialog: Any
    def __init__(self, main_dialog, parent: Any | None = ...) -> None: ...
    def modify_view(self): ...
    functions: Any
    def create_dialog_slot_functions(self) -> None: ...
    def connect_signals_to_slots(self): ...

class AddSpecialBondConditionsDialog(BaseDialog, Ui_AddSpecialBondConditionsDialog):
    CONDITIONS_FRAMES: Any
    charges_list: Any
    main_dialog: Any
    def __init__(self, main_dialog, parent: Any | None = ...) -> None: ...
    def modify_view(self): ...
    functions: Any
    def create_dialog_slot_functions(self) -> None: ...
    def connect_signals_to_slots(self): ...