"""Module for performing checks prior to a dialog loading."""
from loguru import logger
from munientry.widgets.message_boxes import RequiredBox


class DialogPreloadChecker(object):
    """Interface for performing checks to make sure necessary options selected prior to load."""

    def __init__(self, mainwindow):
        self.mainwindow = mainwindow

    def perform_checks(self):
        """Method used in subclasses to run preload checks."""
        raise NotImplementedError

    def is_daily_case_list_selected(self):
        """Checks if daily case list is selected if loading case from daily case lists.

        Returns True if loading from case_search_tab.
        """
        if self.mainwindow.cases_tab_widget.currentWidget().objectName() == 'case_list_tab':
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
    """Pre Dialog Load checks for CrimTraffic Tab Dialog Buttons."""

    def __init__(self, mainwindow):
        super().__init__(mainwindow)

    def perform_checks(self) -> bool:
        if self.is_crimtraffic_officer_selected():
            if self.is_daily_case_list_selected():
                return True
        return False

    def is_crimtraffic_officer_selected(self) -> bool:
        if any(button.isChecked() for button in self.mainwindow.court_staff.judicial_officer_buttons):
            return True
        RequiredBox('You must select judicial officer.', 'Judicial Officer Required').exec()
        return False


class CivilPreloadChecker(DialogPreloadChecker):
    """Pre Dialog Load checks for Civil Tab Dialog Buttons."""

    def __init__(self, mainwindow):
        super().__init__(mainwindow)

    def perform_checks(self) -> bool:
        if self.is_judicial_officer_selected():
            return True
        return False

    def is_judicial_officer_selected(self) -> bool:
        if any(button.isChecked() for button in self.mainwindow.court_staff.judicial_officer_buttons):
            return True
        RequiredBox('You must select a judicial officer.', 'Judicial Officer Required').exec()
        return False


class SchedulingPreloadChecker(DialogPreloadChecker):
    """Pre Dialog Load checks for Scheduling Tab Dialog Buttons."""

    def __init__(self, mainwindow):
        super().__init__(mainwindow)

    def perform_checks(self) -> bool:
        if self.is_scheduling_officer_selected():
            if self.is_daily_case_list_selected():
                return True
        return False

    def is_scheduling_officer_selected(self) -> bool:
        if any(button.isChecked() for button in self.mainwindow.court_staff.assignment_commissioner_buttons):
            return True
        RequiredBox(
            'You must select an assignment commissioner.', 'Assignment Commissioner Required',
        ).exec()
        return False


class ProbationPreloadChecker(DialogPreloadChecker):
    """Pre Dialog Load checks for Probation Tab Dialog Buttons."""

    def __init__(self, mainwindow):
        super().__init__(mainwindow)

    def perform_checks(self) -> bool:
        if self.is_scheduling_officer_selected():
            if self.is_daily_case_list_selected():
                return True
        return False

    def is_scheduling_officer_selected(self) -> bool:
        if any(button.isChecked() for button in self.mainwindow.court_staff.probation_staff_buttons):
            return True
        RequiredBox(
            'You must select a community control officer.', 'Community Control Officer Required',
        ).exec()
        return False


class AdminPreloadChecker(DialogPreloadChecker):
    """Pre Dialog Load checks for Admin Tab Dialog Buttons that load a case."""

    def __init__(self, mainwindow):
        super().__init__(mainwindow)

    def perform_checks(self) -> bool:
        if self.is_admin_officer_selected():
            if self.is_daily_case_list_selected():
                return True
        return False

    def is_admin_officer_selected(self) -> bool:
        if any(button.isChecked() for button in self.mainwindow.court_staff.administrative_staff_buttons):
            return True
        RequiredBox(
            'You must select an administrative staff person.', 'Administrative Staff Required',
        ).exec()
        return False


class AdminFiscalPreloadChecker(DialogPreloadChecker):
    """Pre Dialog Load checks for Admin Tab Fiscal Dialog Button."""

    def __init__(self, mainwindow):
        super().__init__(mainwindow)

    def perform_checks(self) -> bool:
        if self.is_admin_officer_selected():
            return True
        return False

    def is_admin_officer_selected(self) -> bool:
        if any(button.isChecked() for button in self.mainwindow.court_staff.administrative_staff_buttons):
            return True
        RequiredBox(
            'You must select an administrative staff person.', 'Administrative Staff Required',
        ).exec()
        return False
