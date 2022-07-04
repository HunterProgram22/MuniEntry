from munientry.builders.base_dialogs import CriminalBaseDialog as CriminalBaseDialog
from typing import Any, TypeVar

CBD = TypeVar('CBD', bound=CriminalBaseDialog)

class BaseDialogUpdater:
    dialog: Any
    model: Any
    def __init__(self, dialog: CBD) -> None: ...
