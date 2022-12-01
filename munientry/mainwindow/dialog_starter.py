"""Module for starting dialogs when the dialog button is pressed (released)."""
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
from munientry.builders.workflows.community_control_dw_dialog import ComControlWorkflowDialog
from munientry.checkers import dialog_preload_checkers as precheck
from munientry.loaders import dialog_loader as loader


def start_dialog(sender, mainwindow):
    """Function that is bound to each dialog button to start the dialog load process.

    The dialog load process and associated preload checks are governed by the subclass of the
    dialog (in some cases Dialog Builder - TODO: rename all to dialog builder classes).

    If a dialog is a subclass of a particular base class, then it attemps to load the dialog, in
    some cases only after precheck conditions are met (i.e. the appropriate judicial officer is
    selected, and/or a case list is selected.
    """
    if issubclass(sender, CrimTrafficDialogBuilder):
        if precheck.CrimTrafficPreloadChecker(mainwindow).checks:
            mainwindow.dialog = loader.CrimTrafficDialogLoader(mainwindow).dialog
            mainwindow.dialog.exec()
    elif issubclass(sender, SchedulingDialogBuilder):
        if precheck.SchedulingPreloadChecker(mainwindow).checks:
            mainwindow.dialog = loader.SchedulingDialogLoader(mainwindow).dialog
            mainwindow.dialog.exec()
    elif issubclass(sender, JuryPaymentDialog):
        if precheck.AdminPreloadChecker(mainwindow).checks:
            mainwindow.dialog = loader.AdminJuryDialogLoader(mainwindow).dialog
            mainwindow.dialog.exec()
    elif issubclass(sender, DrivingPrivilegesDialog):
        if precheck.AdminPreloadChecker(mainwindow).checks:
            mainwindow.dialog = loader.AdminDrivingDialogLoader(mainwindow).dialog
            mainwindow.dialog.exec()
    elif issubclass(sender, AdminFiscalDialog):
        if precheck.AdminFiscalPreloadChecker(mainwindow).checks:
            mainwindow.dialog = loader.AdminFiscalDialogLoader(mainwindow).dialog
            mainwindow.dialog.exec()
    elif issubclass(sender, MattoxWorkflowDialog):
        mainwindow.dialog = loader.ProbationWorkflowDialogLoader(mainwindow).dialog
        mainwindow.dialog.exec()
    elif issubclass(sender, ComControlWorkflowDialog):
        mainwindow.dialog = loader.ProbationWorkflowDialogLoader(mainwindow).dialog
        mainwindow.dialog.exec()
    elif issubclass(sender, HemmeterWorkflowDialog):
        mainwindow.dialog = loader.DigitalWorkflowDialogLoader(mainwindow).dialog
        mainwindow.dialog.exec()
