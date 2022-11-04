"""Module for performing checks prior to a dialog loading."""
from munientry.widgets.message_boxes import RequiredBox


class DialogPreloadChecker(object):
    """Interface for performing checks to make sure necessary options selected prior to load."""

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow
        self.checks = self._perform_checks()

    def _perform_checks(self):
        pass

    def _is_daily_case_list_selected(self):
        """Checks if daily case list is selected if loading case from daily case lists.

        Returns True if loading from case_search_tab.
        """
        if self.mainwindow.search_tabWidget.currentWidget().objectName() == 'case_list_tab':
            daily_case_lists = self.mainwindow.daily_case_lists
            if not any(case_list.radio_button.isChecked() for case_list in daily_case_lists):
                RequiredBox(
                    'You must select a case list. If not loading a case in the case list '
                    + 'leave the case list field blank.', 'Daily Case List Required',
                ).exec()
                return False
            return True
        return True


class CrimTrafficPreloadChecker(DialogPreloadChecker):

    def _perform_checks(self) -> bool:
        if self._is_crimtraffic_officer_selected():
            if self._is_daily_case_list_selected():
                return True
        return False

    def _is_crimtraffic_officer_selected(self) -> bool:
        required_officers = [
            self.mainwindow.hemmeter_radioButton.isChecked(),
            self.mainwindow.rohrer_radioButton.isChecked(),
            self.mainwindow.bunner_radioButton.isChecked(),
            self.mainwindow.kudela_radioButton.isChecked(),
            self.mainwindow.visiting_judge_radioButton.isChecked(),
            self.mainwindow.pelanda_radioButton.isChecked(),
        ]
        if any(required_officers):
            return True
        RequiredBox('You must select judicial officer.', 'Judicial Officer Required').exec()
        return False


class SchedulingPreloadChecker(DialogPreloadChecker):

    def _perform_checks(self) -> bool:
        if self._is_scheduling_officer_selected():
            if self._is_daily_case_list_selected():
                return True
        return False

    def _is_scheduling_officer_selected(self) -> bool:
        required_officers = [
            self.mainwindow.dattilo_radioButton.isChecked(),
            self.mainwindow.patterson_radioButton.isChecked(),
            self.mainwindow.none_radioButton.isChecked(),
        ]
        if any(required_officers):
            return True
        RequiredBox(
            'You must select an assignment commissioner.', 'Assignment Commissioner Required',
        ).exec()
        return False


class AdminPreloadChecker(DialogPreloadChecker):

    def _perform_checks(self) -> bool:
        if self._is_admin_officer_selected():
            if self._is_daily_case_list_selected():
                return True
        return False

    def _is_admin_officer_selected(self) -> bool:
        required_officers = [
            self.mainwindow.assn_comm_dattilo_radioButton.isChecked(),
            self.mainwindow.assn_comm_patterson_radioButton.isChecked(),
            self.mainwindow.court_admin_kudela_radioButton.isChecked(),
            self.mainwindow.jury_comm_patterson_radioButton.isChecked(),
        ]
        if any(required_officers):
            return True
        RequiredBox(
            'You must select an administrative staff person.', 'Administrative Staff Required',
        ).exec()
        return False


class AdminFiscalPreloadChecker(DialogPreloadChecker):

    def _perform_checks(self) -> bool:
        if self._is_admin_officer_selected():
            return True

    def _is_admin_officer_selected(self) -> bool:
        required_officers = [
            self.mainwindow.assn_comm_dattilo_radioButton.isChecked(),
            self.mainwindow.assn_comm_patterson_radioButton.isChecked(),
            self.mainwindow.court_admin_kudela_radioButton.isChecked(),
            self.mainwindow.jury_comm_patterson_radioButton.isChecked(),
        ]
        if any(required_officers):
            return True
        RequiredBox(
            'You must select an administrative staff person.', 'Administrative Staff Required',
        ).exec()
        return False
