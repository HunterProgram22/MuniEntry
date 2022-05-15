from PyQt5.QtWidgets import QGridLayout
from package.views.custom_widgets import AlliedCheckbox as AlliedCheckbox, ChargeGridAmendButton as ChargeGridAmendButton, ChargeGridDeleteButton as ChargeGridDeleteButton, DegreeComboBox as DegreeComboBox, DismissedCheckbox as DismissedCheckbox, FindingComboBox as FindingComboBox, FineLineEdit as FineLineEdit, FineSuspendedLineEdit as FineSuspendedLineEdit, JailLineEdit as JailLineEdit, JailSuspendedLineEdit as JailSuspendedLineEdit, PleaComboBox as PleaComboBox, StatuteLineEdit as StatuteLineEdit

class ChargesGrid(QGridLayout):
    row_offense: int
    row_statute: int
    row_degree: int
    row_dismissed_box: int
    row_allied_box: int
    row_plea: int
    row_finding: int
    row_fine: int
    row_fine_suspended: int
    row_amend_button: int
    row_delete_button: int
    def get_last_charge_in_charges_list(self, dialog): ...
    def set_plea(self): ...
    def set_cursor_to_fine_line_edit(self) -> None: ...
    def set_all_pleas(self) -> None: ...
    def set_all_findings(self, column) -> None: ...

class NotGuiltyPleaGrid(ChargesGrid):
    row_plea: int
    row_delete_button: int
    def add_charge_only_to_grid(self, dialog) -> None: ...
    def set_all_pleas(self) -> None: ...

class PleaOnlyGrid(ChargesGrid):
    row_dismissed_box: int
    row_allied_box: int
    row_plea: int
    row_finding: int
    row_amend_button: int
    row_delete_button: int
    def add_charge_only_to_grid(self, dialog) -> None: ...

class NoJailChargesGrid(ChargesGrid):
    row_dismissed_box: int
    row_allied_box: int
    row_plea: int
    row_finding: int
    row_fine: int
    row_fine_suspended: int
    row_amend_button: int
    row_delete_button: int
    def add_charge_only_to_grid(self, dialog) -> None: ...

class JailChargesGrid(NoJailChargesGrid):
    row_jail_days: int
    row_jail_days_suspended: int
    row_amend_button: int
    row_delete_button: int
    def add_charge_only_to_grid(self, dialog) -> None: ...

class DiversionChargesGrid(JailChargesGrid): ...
