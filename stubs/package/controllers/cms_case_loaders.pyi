from package.models.case_information import CriminalCharge as CriminalCharge
from typing import Any
from PyQt5.QtWidgets import QDialog

class CmsNoChargeLoader:
    dialog: Any
    cms_case: Any
    def __init__(self, dialog: QDialog) -> None: ...
    def load_cms_data(self) -> None: ...
    def set_case_number(self) -> None: ...
    def set_defendant_name(self) -> None: ...
    def set_defense_counsel_name(self) -> None: ...
    def set_defense_counsel_type(self) -> None: ...

class CmsChargeLoader(CmsNoChargeLoader):
    criminal_charge: Any
    def __init__(self, dialog: QDialog) -> None: ...
    def load_cms_data(self) -> None: ...
    def add_cms_criminal_charges_to_entry_case_information(self) -> None: ...
    def set_offense_type(self): ...

class CmsFraLoader(CmsChargeLoader):
    def __init__(self, dialog) -> None: ...
    def load_fra_data(self) -> None: ...
    def hide_fra_if_criminal_case(self) -> None: ...
