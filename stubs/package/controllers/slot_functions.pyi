from package.controllers.helper_functions import set_future_date as set_future_date
from package.database_controllers.databases import extract_data as extract_data, open_db_connection as open_db_connection, sql_query_offense_type as sql_query_offense_type
from package.models.case_information import CriminalCharge as CriminalCharge
from package.views.custom_widgets import InfoBox as InfoBox, RequiredBox as RequiredBox
from typing import Any

class BaseDialogSlotFunctions:
    dialog: Any
    def __init__(self, dialog) -> None: ...
    def start_add_charge_dialog(self) -> None: ...
    def start_amend_offense_dialog(self) -> None: ...
    def close_dialog(self) -> None: ...
    def close_event(self) -> None: ...
    def close_window(self) -> None: ...
    def clear_case_information_fields(self) -> None: ...
    def create_entry(self) -> None: ...
    def create_entry_process(self) -> None: ...
    def set_document_name(self): ...
    def set_plea_and_findings_process(self) -> None: ...
    def set_fines_costs_pay_date(self, days_to_add_string) -> None: ...
    def get_days_to_add(self, days_to_add_string): ...
    def update_info_and_perform_checks(self): ...
    def set_defense_counsel(self) -> None: ...
    def set_fra_in_file(self, current_text) -> None: ...
    def set_fra_in_court(self, current_text) -> None: ...
    def show_costs_and_fines(self) -> None: ...
    def update_community_service_due_date(self, _index: Any | None = ...) -> None: ...
    @classmethod
    def set_statute_and_offense(cls, key, dialog) -> None: ...
    def conditions_checkbox_toggle(self) -> None: ...
    def set_report_date(self) -> None: ...
    def show_report_days_notes_box(self) -> None: ...
    def show_hide_checkbox_connected_fields(self) -> None: ...
    def set_freeform_entry(self) -> None: ...
    def show_bond_boxes(self, bond_mod_string) -> None: ...

class AddChargeDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    main_dialog: Any
    def __init__(self, dialog) -> None: ...
    def clear_add_charge_fields(self) -> None: ...
    def add_charge_process(self) -> None: ...
    criminal_charge: Any
    def add_charge_to_entry_case_information(self) -> None: ...
    def set_offense_type(self): ...
    def close_event(self) -> None: ...

class AmendChargeDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    main_dialog: Any
    def __init__(self, dialog) -> None: ...
    def clear_amend_charge_fields(self) -> None: ...
    def amend_offense_process(self) -> None: ...
    def update_criminal_charge_offense_name(self) -> None: ...
    def update_charges_grid_with_amended_charge(self) -> None: ...
    def add_charge_to_amended_charge_list(self) -> None: ...
    def set_amended_offense_details(self) -> None: ...
    def close_event(self) -> None: ...

class PleaOnlyDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    def __init__(self, dialog) -> None: ...

class FineOnlyDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    def __init__(self, dialog) -> None: ...
    def set_fines_credit_for_jail_field(self) -> None: ...
    def start_add_conditions_dialog(self) -> None: ...

class JailCCDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    def __init__(self, dialog) -> None: ...
    def show_companion_case_fields(self) -> None: ...
    def start_add_jail_report_dialog(self) -> None: ...
    def start_add_conditions_dialog(self) -> None: ...

class DiversionDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    def __init__(self, dialog) -> None: ...
    def show_other_conditions_box(self) -> None: ...
    def show_jail_report_date_box(self) -> None: ...

class ProbationViolationBondDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    def __init__(self, dialog) -> None: ...
    def hide_bond_conditions(self) -> None: ...
    def set_if_no_bond(self, dialog) -> None: ...

class FailureToAppearDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    def __init__(self, dialog) -> None: ...
    def hide_warrant_radius(self) -> None: ...
    def hide_bond_boxes(self) -> None: ...
    def set_bond_amount_box(self) -> None: ...

class NotGuiltyBondDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    def __init__(self, dialog) -> None: ...
    def start_add_special_bond_conditions_dialog(self) -> None: ...
    def hide_boxes(self) -> None: ...
    def show_hide_bond_conditions(self) -> None: ...

class NoPleaBondDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    def __init__(self, dialog) -> None: ...
    def start_add_special_bond_conditions_dialog(self) -> None: ...
    def hide_boxes(self) -> None: ...

class BondHearingDialogSlotFunctions(NotGuiltyBondDialogSlotFunctions):
    def __init__(self, dialog) -> None: ...

class AddConditionsDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    main_dialog: Any
    def __init__(self, dialog) -> None: ...
    def add_conditions(self) -> None: ...

class AddCommunityControlDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    main_dialog: Any
    def __init__(self, dialog) -> None: ...
    def add_conditions(self) -> None: ...

class AddSpecialBondConditionsDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    main_dialog: Any
    def __init__(self, dialog) -> None: ...
    def add_conditions(self) -> None: ...

class AddJailOnlyDialogSlotFunctions(BaseDialogSlotFunctions):
    dialog: Any
    main_dialog: Any
    def __init__(self, dialog) -> None: ...
    def add_conditions(self) -> None: ...

def close_databases() -> None: ...
