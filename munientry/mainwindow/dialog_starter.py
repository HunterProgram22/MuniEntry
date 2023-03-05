"""Module for starting dialogs if required precheck conditions are satisfied."""
from types import MappingProxyType
from typing import Optional

from loguru import logger

from munientry.builders import administrative as admin
from munientry.builders import civil
from munientry.builders import crimtraffic as crim
from munientry.builders import scheduling as sched
from munientry.builders import workflows as work
from munientry.checkers import dialog_preload_checkers as precheck
from munientry.loaders import dialog_loader as loader

DIALOG_PRECHECKERS = MappingProxyType({
    civil.civ_freeform_dialog.CivFreeformDialog: precheck.CivilPreloadChecker,
    crim.base_crimtraffic_builders.CrimTrafficDialogBuilder: precheck.CrimTrafficPreloadChecker,
    sched.base_scheduling_builders.SchedulingDialogBuilder: precheck.SchedulingPreloadChecker,
    admin.jury_payment_dialog.JuryPaymentDialog: precheck.AdminPreloadChecker,
    admin.driving_privileges_dialog.DrivingPrivilegesDialog: precheck.AdminPreloadChecker,
    admin.admin_fiscal_dialog.AdminFiscalDialog: precheck.AdminFiscalPreloadChecker,
})
DIALOG_LOADERS = MappingProxyType({
    civil.civ_freeform_dialog.CivFreeformDialog: loader.CivilDialogLoader,
    crim.base_crimtraffic_builders.CrimTrafficDialogBuilder: loader.CrimTrafficDialogLoader,
    sched.base_scheduling_builders.SchedulingDialogBuilder: loader.SchedulingDialogLoader,
    admin.jury_payment_dialog.JuryPaymentDialog: loader.AdminJuryDialogLoader,
    admin.driving_privileges_dialog.DrivingPrivilegesDialog: loader.AdminDrivingDialogLoader,
    admin.admin_fiscal_dialog.AdminFiscalDialog: loader.AdminFiscalDialogLoader,
    work.probation_dw_dialogs.ProbationWorkflowDialog: loader.ProbationWorkflowDialogLoader,
    work.hemmeter_dw_dialog.AdminWorkflowDialog: loader.DigitalWorkflowDialogLoader,
})


def start_dialog(sender: type, mainwindow) -> None:
    """Function that handles loading and running preload dialog checks when a button is clicked.

    The dialog that is loaded is determined by the sender's subclass. Preload checks may be
    required for certain dialogs (e.g. selecting a judicial officer or a case list).

    Args:
        sender: the sender of the signal that started the dialog load process.
        mainwindow: the instance of the main window where the dialogs are displayed.

    Raises:
        ValueError: if no precheck or loader class is found for the sender. This means it likely
            just needs to be added to the MappingProxyTypes in this module.
    """
    precheck_class, loader_class = find_dialog_classes(sender, DIALOG_PRECHECKERS, DIALOG_LOADERS)
    if precheck_class and not precheck_class(mainwindow).checks:
        return None
    if precheck_class and precheck_class(mainwindow).checks:
        return load_dialog(mainwindow, loader_class)
    if loader_class:
        return load_dialog(mainwindow, loader_class)
    raise ValueError('No precheck or loader class was found')


def find_dialog_classes(
    sender: type, precheckers: MappingProxyType, loaders: MappingProxyType,
) -> tuple[Optional[type], Optional[type]]:
    """Find precheck and loader classes for a given dialog sender."""
    for dialog_precheck_type, precheck_class in precheckers.items():
        if issubclass(sender, dialog_precheck_type):
            return precheck_class, loaders.get(dialog_precheck_type)
    for dialog_type, loader_class in loaders.items():
        if issubclass(sender, dialog_type):
            return None, loader_class
    return None, None


def load_dialog(mainwindow, loader_class: Optional[type]) -> None:
    """Load the dialog using the given loader class."""
    if loader_class is not None:
        mainwindow.dialog = loader_class(mainwindow).dialog
        mainwindow.dialog.exec()
    else:
        logger.warning('No dialog was called.')
