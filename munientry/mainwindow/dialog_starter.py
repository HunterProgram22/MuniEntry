"""Module for starting dialogs when the dialog button is pressed (released)."""
from __future__ import annotations
from typing import TYPE_CHECKING, Optional

from loguru import logger

from munientry.builders import administrative as admin
from munientry.builders import civil as civil
from munientry.builders import crimtraffic as crim
from munientry.builders import scheduling as sched
from munientry.builders import workflows as work
from munientry.checkers import dialog_preload_checkers as precheck
from munientry.loaders import dialog_loader as loader
from munientry.loaders.civil_dialog_loader import CivilDialogLoader

if TYPE_CHECKING:
    from munientry import mainwindow as app_mainwindow


def start_dialog(sender: type, mainwindow: 'app_mainwindow') -> None:
    """Function that handles loading and preloading dialogs when a button is clicked.

    The dialog that is loaded is determined by the sender's subclass. Preloading checks
    may be required for certain dialogs (e.g. selecting a judicial officer or a case list).

    Args:
        sender: the sender of the signal that started the dialog load process.
        mainwindow: the instance of the main window where the dialogs are displayed.
    """
    precheckers = {
        crim.base_crimtraffic_builders.CrimTrafficDialogBuilder: precheck.CrimTrafficPreloadChecker,
        sched.base_scheduling_builders.SchedulingDialogBuilder: precheck.SchedulingPreloadChecker,
        admin.jury_payment_dialog.JuryPaymentDialog: precheck.AdminPreloadChecker,
        admin.driving_privileges_dialog.DrivingPrivilegesDialog: precheck.AdminPreloadChecker,
        admin.admin_fiscal_dialog.AdminFiscalDialog: precheck.AdminFiscalPreloadChecker,
    }
    loaders = {
        crim.base_crimtraffic_builders.CrimTrafficDialogBuilder: loader.CrimTrafficDialogLoader,
        sched.base_scheduling_builders.SchedulingDialogBuilder: loader.SchedulingDialogLoader,
        admin.jury_payment_dialog.JuryPaymentDialog: loader.AdminJuryDialogLoader,
        admin.driving_privileges_dialog.DrivingPrivilegesDialog: loader.AdminDrivingDialogLoader,
        admin.admin_fiscal_dialog.AdminFiscalDialog: loader.AdminFiscalDialogLoader,
        work.probation_dw_dialogs.ProbationWorkflowDialog: loader.ProbationWorkflowDialogLoader,
        work.hemmeter_dw_dialog.HemmeterWorkflowDialog: loader.DigitalWorkflowDialogLoader,
        civil.civ_freeform_dialog.CivFreeformDialog: CivilDialogLoader,
    }
    precheck_class, loader_class = find_dialog_classes(sender, precheckers, loaders)
    if precheck_class and precheck_class(mainwindow).checks:
        load_dialog(mainwindow, loader_class)
    elif loader_class:
        load_dialog(mainwindow, loader_class)


def find_dialog_classes(
    sender: type, precheckers: dict, loaders: dict,
) -> tuple[Optional[type], Optional[type]]:
    """Find precheck and loader classes for a given dialog sender."""
    for dialog_precheck_type, precheck_class in precheckers.items():
        if issubclass(sender, dialog_precheck_type):
            return precheck_class, loaders.get(dialog_precheck_type)
    for dialog_type, loader_class in loaders.items():
        if issubclass(sender, dialog_type):
            return None, loader_class
    return None, None


def load_dialog(mainwindow: 'app_mainwindow', loader_class: Optional[type]) -> None:
    """Load the dialog using the given loader class."""
    if loader_class is not None:
        mainwindow.dialog = loader_class(mainwindow).dialog
        mainwindow.dialog.exec()
    else:
        logger.warning('None dialog was called.')
