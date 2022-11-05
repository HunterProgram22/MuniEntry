"""Module for starting dialogs when the dialog button is pressed (released)."""
from loguru import logger

from munientry.builders.administrative.admin_fiscal_dialog import AdminFiscalDialog
from munientry.builders.administrative.driving_privileges_dialog import (
    DrivingPrivilegesDialog,
)
from munientry.builders.administrative.jury_payment_dialog import JuryPaymentDialog
from munientry.builders.crimtraffic.base_crimtraffic_builders import (
    CrimTrafficDialogBuilder,
)
from munientry.builders.scheduling.base_scheduling_builders import (
    SchedulingDialogBuilder,
)
from munientry.builders.workflows.hemmeter_dw_dialog import HemmeterWorkflowDialog
from munientry.builders.workflows.mattox_dw_dialog import MattoxWorkflowDialog
from munientry.checkers import dialog_preload_checkers as precheck
from munientry.loaders import dialog_loader as loader


def start_dialog(sender, mainwindow):
    """Function that is bound to each dialog button to start the dialog load process.

    The dialog load process and associated preload checks are governed by the subclass of the
    dialog (in some cases Dialog Builder - TODO: rename all to dialog builder classes).
    """
    if issubclass(sender, CrimTrafficDialogBuilder):
        if precheck.CrimTrafficPreloadChecker(mainwindow).checks:
            mainwindow.dialog = loader.CrimTrafficDialogLoader(mainwindow).dialog
            return mainwindow.dialog.exec()
    elif issubclass(sender, SchedulingDialogBuilder):
        if precheck.SchedulingPreloadChecker(mainwindow).checks:
            mainwindow.dialog = loader.SchedulingDialogLoader(mainwindow).dialog
            return mainwindow.dialog.exec()
    elif issubclass(sender, JuryPaymentDialog):
        if precheck.AdminPreloadChecker(mainwindow).checks:
            mainwindow.dialog = loader.AdminJuryDialogLoader(mainwindow).dialog
            return mainwindow.dialog.exec()
    elif issubclass(sender, DrivingPrivilegesDialog):
        if precheck.AdminPreloadChecker(mainwindow).checks:
            mainwindow.dialog = loader.AdminDrivingDialogLoader(mainwindow).dialog
            return mainwindow.dialog.exec()
    elif issubclass(sender, AdminFiscalDialog):
        if precheck.AdminFiscalPreloadChecker(mainwindow).checks:
            mainwindow.dialog = loader.AdminFiscalDialogLoader(mainwindow).dialog
            return mainwindow.dialog.exec()
    elif issubclass(sender, MattoxWorkflowDialog):
        mainwindow.dialog = loader.ProbationWorkflowDialogLoader(mainwindow).dialog
        return mainwindow.dialog.exec()
    elif issubclass(sender, HemmeterWorkflowDialog):
        mainwindow.dialog = loader.DigitalWorkflowDialogLoader(mainwindow).dialog
        return mainwindow.dialog.exec()
    # logger.debug(mainwindow.dialog)
    # return start_dialog_window(mainwindow.dialog)


# def start_dialog_window(dialog):
#     if dialog is None:
#         return None
#     return dialog.exec()
