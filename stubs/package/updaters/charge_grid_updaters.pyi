from typing import Any

class BaseGridUpdater:
    row_offense: int
    row_statute: int
    row_degree: int
    grid: Any
    model: Any
    def __init__(self, updater) -> None: ...
    def update_model_with_plea_finding_grid_data(self) -> None: ...

class NotGuiltyGridModelUpdater(BaseGridUpdater):
    row_plea: int
    def __init__(self, updater) -> None: ...
    def update_model_with_plea_grid_data(self) -> None: ...

class PleaOnlyGridModelUpdater(BaseGridUpdater):
    row_dismissed_box: int
    row_allied_box: int
    row_plea: int
    row_finding: int
    row_amend_button: int
    row_delete_button: int
    def __init__(self, updater) -> None: ...

class FineOnlyGridModelUpdater(BaseGridUpdater):
    row_dismissed_box: int
    row_allied_box: int
    row_plea: int
    row_finding: int
    row_fine: int
    row_fine_suspended: int
    row_amend_button: int
    row_delete_button: int
    def __init__(self, updater) -> None: ...
    def update_model_with_fine_grid_data(self) -> None: ...
    def update_model_with_fines(self, charge, col) -> None: ...
    def update_model_with_fines_suspended(self, charge, col) -> None: ...

class JailCCGridModelUpdater(FineOnlyGridModelUpdater):
    row_jail_days: int
    row_jail_days_suspended: int
    row_amend_button: int
    row_delete_button: int
    def __init__(self, updater) -> None: ...
    def update_model_with_jail_grid_data(self) -> None: ...
    def update_model_with_jail_imposed(self, charge, col) -> None: ...
    def update_model_with_jail_suspended(self, charge, col) -> None: ...

class DiversionGridModelUpdater(JailCCGridModelUpdater):
    def __init__(self, updater) -> None: ...
