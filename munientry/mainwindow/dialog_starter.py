"""Module for starting dialogs when the dialog button is pressed (released)."""
from loguru import logger
import munientry.loaders.civil_dialog_loader
from munientry.builders.administrative.admin_fiscal_dialog import AdminFiscalDialog
from munientry.builders.administrative.driving_privileges_dialog import (
    DrivingPrivilegesDialog,
)
from munientry.builders.administrative.jury_payment_dialog import JuryPaymentDialog
from munientry.builders.civil.civ_freeform_dialog import CivFreeformDialog
from munientry.builders.crimtraffic.base_crimtraffic_builders import (
    CrimTrafficDialogBuilder,
)
from munientry.builders.scheduling.base_scheduling_builders import (
    SchedulingDialogBuilder,
)
from munientry.builders.workflows.hemmeter_dw_dialog import HemmeterWorkflowDialog
from munientry.builders.workflows.probation_dw_dialogs import ProbationWorkflowDialog
from munientry.checkers import dialog_preload_checkers as precheck
from munientry.loaders import dialog_loader as loader


def start_dialog(sender, mainwindow):
    """Function that is bound to each dialog button to start the dialog load process.

    The dialog load process and associated preload checks are governed by the subclass of the
    dialog (in some cases Dialog Builder - TODO: rename all to dialog builder classes).

    If a dialog is a subclass of a particular base class, then it attempts to load the dialog,
    in some cases only after precheck conditions are met (i.e. the appropriate judicial officer
    is selected, and/or a case list is selected).
    """
    precheckers = {
        CrimTrafficDialogBuilder: precheck.CrimTrafficPreloadChecker,
        SchedulingDialogBuilder: precheck.SchedulingPreloadChecker,
        JuryPaymentDialog: precheck.AdminPreloadChecker,
        DrivingPrivilegesDialog: precheck.AdminPreloadChecker,
        AdminFiscalDialog: precheck.AdminFiscalPreloadChecker,
    }
    loaders = {
        CrimTrafficDialogBuilder: loader.CrimTrafficDialogLoader,
        SchedulingDialogBuilder: loader.SchedulingDialogLoader,
        JuryPaymentDialog: loader.AdminJuryDialogLoader,
        DrivingPrivilegesDialog: loader.AdminDrivingDialogLoader,
        AdminFiscalDialog: loader.AdminFiscalDialogLoader,
        ProbationWorkflowDialog: loader.ProbationWorkflowDialogLoader,
        HemmeterWorkflowDialog: loader.DigitalWorkflowDialogLoader,
        CivFreeformDialog: munientry.loaders.civil_dialog_loader.CivilDialogLoader,
    }
    for dialog_type, precheck_class in precheckers.items():
        if issubclass(sender, dialog_type):
            if precheck_class(mainwindow).checks:
                mainwindow.dialog = loaders[dialog_type](mainwindow).dialog
                mainwindow.dialog.exec()
            break
    else:
        for dialog_type, loader_class in loaders.items():
            if issubclass(sender, dialog_type):
                mainwindow.dialog = loader_class(mainwindow).dialog
                mainwindow.dialog.exec()
                break
