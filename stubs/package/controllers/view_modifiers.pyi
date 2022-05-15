from PyQt5.QtWidgets import QCheckBox as QCheckBox, QComboBox as QComboBox, QDateEdit as QDateEdit, QLineEdit as QLineEdit, QRadioButton as QRadioButton, QTextEdit as QTextEdit, QTimeEdit as QTimeEdit
from package.controllers.helper_functions import set_future_date as set_future_date
from typing import Any

TODAY: Any

class BaseDialogViewModifier:
    dialog: Any
    def __init__(self, dialog) -> None: ...
    def set_appearance_reason(self) -> None: ...
    def set_case_information_banner(self) -> None: ...
    def set_conditions_case_information_banner(self) -> None: ...
    def set_report_date_view(self) -> None: ...
    def set_report_days_notes_box(self) -> None: ...
    @classmethod
    def hide_boxes(cls, dialog) -> None: ...
    def load_existing_data_to_dialog(self) -> None: ...
    def transfer_model_data_to_view(self, model_class) -> None: ...

class AddChargeDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog) -> None: ...

class AmendChargeDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog) -> None: ...

class FineOnlyDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog) -> None: ...

class PleaOnlyDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog) -> None: ...

class JailCCDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog) -> None: ...

class DiversionDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog) -> None: ...
    def set_diversion_fine_pay_date_box(self) -> None: ...
    def set_diversion_jail_report_date_box(self) -> None: ...

class NotGuiltyBondDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog) -> None: ...

class NoPleaBondDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog) -> None: ...

class BondHearingDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog) -> None: ...

class ProbationViolationBondDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog) -> None: ...

class FailureToAppearDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog) -> None: ...

class AddConditionsDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog) -> None: ...

class AddJailOnlyDialogViewModifier(BaseDialogViewModifier):
    condition_checkbox_list: Any
    def __init__(self, dialog) -> None: ...

class AddCommunityControlDialogViewModifier(BaseDialogViewModifier):
    condition_checkbox_list: Any
    def __init__(self, dialog) -> None: ...

class AddSpecialBondConditionsDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog) -> None: ...
    def set_special_bond_conditions_case_information_banner(self) -> None: ...
