import pytest
from unittest.mock import Mock
from munientry.builders.administrative.admin_fiscal_dialog import AdminFiscalDialog
from munientry.builders.administrative.driving_privileges_dialog import DrivingPrivilegesDialog
from munientry.builders.administrative.jury_payment_dialog import JuryPaymentDialog
from munientry.builders.civil.civ_freeform_dialog import CivFreeformDialog
from munientry.builders.crimtraffic.base_crimtraffic_builders import CrimTrafficDialogBuilder
from munientry.builders.scheduling.base_scheduling_builders import SchedulingDialogBuilder
from munientry.builders.workflows.hemmeter_dw_dialog import HemmeterWorkflowDialog
from munientry.builders.workflows.probation_dw_dialogs import ProbationWorkflowDialog
from munientry.checkers import dialog_preload_checkers as precheck
from munientry.loaders import dialog_loader as loader
from munientry.mainwindow.dialog_starter import start_dialog


class TestStartDialog:
    def test_crimtraffic_dialog_builder_with_precheck(self):
        sender = CrimTrafficDialogBuilder
        mainwindow = Mock()
        precheck.CrimTrafficPreloadChecker = Mock(return_value=Mock(checks=True))
        loader.CrimTrafficDialogLoader = Mock(return_value=Mock(dialog=Mock(exec=Mock())))

        start_dialog(sender, mainwindow)

        precheck.CrimTrafficPreloadChecker.assert_called_once_with(mainwindow)
        loader.CrimTrafficDialogLoader.assert_called_once_with(mainwindow)
        mainwindow.dialog.exec.assert_called_once()

    def test_crimtraffic_dialog_builder_without_precheck(self):
        sender = CrimTrafficDialogBuilder
        mainwindow = Mock()
        precheck.CrimTrafficPreloadChecker = Mock(return_value=Mock(checks=False))
        loader.CrimTrafficDialogLoader = Mock(return_value=Mock(dialog=Mock(exec=Mock())))

        start_dialog(sender, mainwindow)

        precheck.CrimTrafficPreloadChecker.assert_called_once_with(mainwindow)
        loader.CrimTrafficDialogLoader.assert_not_called()
        mainwindow.dialog.exec.assert_not_called()

    # add more test cases for other dialog builders and scenarios
