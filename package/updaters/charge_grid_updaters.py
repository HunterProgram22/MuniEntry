"""Module that contains the updaters for the different charge grids used by dialogs."""

from package.models.case_information import CriminalCharge
from package.updaters.base_updaters import CBD


class BaseGridUpdater(object):
    """Charge Grid base updater class that contains methods common to dialogs with a charge grid."""

    row_offense = 0
    row_statute = 1
    row_degree = 2
    row_plea = 3
    row_finding = 4

    def __init__(self, dialog: CBD) -> None:
        self.grid = dialog.charges_gridLayout
        self.model = dialog.entry_case_information

    def set_charge_grid_column(self, col: int) -> int:
        """Function required because the grid_layout in Qt adds blank (unseen) columns."""
        while self.grid.itemAtPosition(self.row_offense, col) is None:
            col += 1
        return col

    def update_model_with_statute_data(self) -> None:
        col = 1
        for charge in self.model.charges_list:
            col = self.set_charge_grid_column(col)
            charge.statute = self.grid.itemAtPosition(self.row_statute, col).widget().get_text()
            col += 1

    def update_model_with_degree_data(self) -> None:
        col = 1
        for charge in self.model.charges_list:
            col = self.set_charge_grid_column(col)
            charge.degree = self.grid.itemAtPosition(self.row_degree, col).widget().currentText()
            col += 1

    def update_model_with_plea_data(self) -> None:
        col = 1
        for charge in self.model.charges_list:
            col = self.set_charge_grid_column(col)
            charge.plea = self.grid.itemAtPosition(self.row_plea, col).widget().currentText()
            col += 1

    def update_model_with_finding_data(self) -> None:
        col = 1
        for charge in self.model.charges_list:
            col = self.set_charge_grid_column(col)
            charge.finding = self.set_charge_finding(col)
            col += 1

    def set_charge_finding(self, col: int) -> str:
        if self.charge_is_dismissed(col):
            return ''
        return self.grid.itemAtPosition(self.row_finding, col).widget().currentText()

    def charge_is_dismissed(self, col: int) -> bool:
        plea = self.grid.itemAtPosition(self.row_plea, col).widget().currentText()
        return bool(plea == 'Dismissed')


class NotGuiltyGridModelUpdater(BaseGridUpdater):
    """Class for Not Guilty Bond Dialog grid that sets rows based on reduced charges grid."""

    row_plea = 3

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_model_with_statute_data()
        self.update_model_with_degree_data()
        self.update_model_with_plea_data()


class LeapAdmissionPleaGridModelUpdater(BaseGridUpdater):
    """Class for Leap Admission Plea Dialog that sets rows for charges grid."""

    row_dismissed_box = 3
    row_plea = 4
    row_amend_button = 5
    row_delete_button = 6

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_model_with_statute_data()
        self.update_model_with_degree_data()
        self.update_model_with_plea_data()


class PleaOnlyGridModelUpdater(BaseGridUpdater):
    """Class for Plea Only Dialog that sets rows for charges grid."""

    row_dismissed_box = 3
    row_allied_box = 4
    row_plea = 5
    row_finding = 6
    row_amend_button = 7
    row_delete_button = 8

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_model_with_statute_data()
        self.update_model_with_degree_data()
        self.update_model_with_plea_data()
        self.update_model_with_finding_data()


class FineOnlyGridModelUpdater(BaseGridUpdater):
    """Class for Fine Only Plea Dialog that sets rows for charges grid."""

    row_dismissed_box = 3
    row_allied_box = 4
    row_plea = 5
    row_finding = 6
    row_fine = 7
    row_fine_suspended = 8
    row_amend_button = 9
    row_delete_button = 10

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_model_with_statute_data()
        self.update_model_with_degree_data()
        self.update_model_with_plea_data()
        self.update_model_with_finding_data()
        self.update_model_with_fines_data()
        self.update_model_with_fines_suspended_data()

    def update_model_with_fines_data(self):
        col = 1
        for charge in self.model.charges_list:
            col = self.set_charge_grid_column(col)
            charge.fines_amount = self.set_fines_amount(charge, col)
            col += 1

    def update_model_with_fines_suspended_data(self):
        col = 1
        for charge in self.model.charges_list:
            col = self.set_charge_grid_column(col)
            charge.fines_suspended = self.set_fines_suspended_amount(charge, col)
            col += 1

    def set_fines_amount(self, charge: CriminalCharge, col: int) -> str:
        if self.charge_is_dismissed(col):
            return ''
        if self.grid.itemAtPosition(self.row_fine, col).widget().text() == '':
            charge.fines_amount = '0'
        else:
            charge.fines_amount = self.grid.itemAtPosition(self.row_fine, col).widget().text()
        return f'$ {charge.fines_amount}'

    def set_fines_suspended_amount(self, charge: CriminalCharge, col: int) -> str:
        if self.charge_is_dismissed(col):
            return ''
        if self.grid.itemAtPosition(self.row_fine_suspended, col).widget().text() == '':
            charge.fines_suspended = '0'
        else:
            charge.fines_suspended = (
                self.grid.itemAtPosition(self.row_fine_suspended, col).widget().text()
            )
        return f'$ {charge.fines_suspended}'


class JailCCGridModelUpdater(FineOnlyGridModelUpdater):
    """Extends the FineOnlyGridModelUpdater by adding updates for jail days."""

    row_jail_days = 9
    row_jail_days_suspended = 10
    row_amend_button = 11
    row_delete_button = 12

    def __init__(self, dialog: CBD) -> None:
        super().__init__(dialog)
        self.update_model_with_jail_days_data()
        self.update_model_with_jail_days_suspended_data()

    def update_model_with_jail_days_data(self) -> None:
        col = 1
        for charge in self.model.charges_list:
            col = self.set_charge_grid_column(col)
            charge.jail_days = self.set_jail_days_amount(charge, col)
            col += 1

    def update_model_with_jail_days_suspended_data(self) -> None:
        col = 1
        for charge in self.model.charges_list:
            col = self.set_charge_grid_column(col)
            charge.jail_days_suspended = self.set_jail_days_suspended_amount(charge, col)
            col += 1

    def set_jail_days_amount(self, charge: CriminalCharge, col: int) -> str:
        if self.charge_is_dismissed(col):
            return ''
        if self.grid.itemAtPosition(self.row_jail_days, col).widget().text() == '':
            charge.jail_days = 'None'
        else:
            charge.jail_days = self.grid.itemAtPosition(self.row_jail_days, col).widget().text()
        return charge.jail_days

    def set_jail_days_suspended_amount(self, charge: CriminalCharge, col: int) -> str:
        if self.charge_is_dismissed(col):
            return ''
        if self.grid.itemAtPosition(self.row_jail_days_suspended, col).widget().text() == '':
            charge.jail_days_suspended = 'None'
        else:
            charge.jail_days_suspended = (
                self.grid.itemAtPosition(self.row_jail_days_suspended, col).widget().text()
            )
        return charge.jail_days_suspended


class DiversionGridModelUpdater(JailCCGridModelUpdater):
    """Extends JailCCGridModelUpdater, but not additional actions performed."""
