"""Module contains all versions of QGridLayout that are used as charges grids on dialogs."""

import munientry.widgets.combo_boxes
from loguru import logger
from PyQt5.QtWidgets import QGridLayout, QLabel

from munientry.models.criminal_charge_models import CriminalCharge
from munientry.widgets import custom_widgets as cw



class BaseChargeGrid(QGridLayout):
    """The base format of the charges_gridLayout used for a main_entry_dialog.

    The ChargesGrid subclasses the QGridLayout and provides methods for manipulating the grid.
    Each main_entry_dialog that has a ChargesGrid (self.charges_gridLayout) has a specific
    subclassed version that is set by changing the class of the QGridLayout to the class of
    the specific subclassed ChargesGrid. This avoids having to initialize the grid during the
    setupUI method called by the main_entry_dialog classes modify_view method. The class is
    set prior to loading the case data during the main_entry_dialog load_cms_data_to_view method.
    """

    def check_if_column_empty(self, column: int) -> bool:
        return bool(self.itemAtPosition(0, column) is None)

    def check_if_charge_dismissed(self, column: int) -> bool:
        try:
            return self.itemAtPosition(self.row_dismissed_box, column).widget().isChecked()
        except AttributeError as error:
            logger.warning(error)
        return False

    def check_if_allied_offense(self, column: int) -> bool:
        try:
            return self.itemAtPosition(self.row_allied_box, column).widget().isChecked()
        except AttributeError as error:
            logger.warning(error)
        return False

    def get_plea(self) -> str:
        """Returns copy of the label of the plea button after stripping ' All' from end.

        Ex. "Guilty All" button is returned as "Guilty" to be used as the plea.
        """
        return self.sender().text().replace(' All', '')

    def set_all_pleas(self, plea=None) -> None:
        """Sets the plea for all charges based on the button pressed.

        Ex. Pressing 'No Contest All' sets all pleas to No Contest.
        """
        logger.button(f'{self.sender().text()} Pressed')
        if plea == None:
            plea = self.get_plea()
        for column in range(0, self.columnCount()):
            column += 1
            if self.check_if_column_empty(column):
                continue
            plea_box = self.itemAtPosition(self.row_plea, column).widget()
            if self.check_if_charge_dismissed(column):
                continue
            plea_box.setCurrentText(plea)

    def set_all_findings(self) -> None:
        """Sets the findings for all charges to either Guilty or Guilty - Allied Offense."""
        for column in range(0, self.columnCount()):
            column += 1
            if self.check_if_column_empty(column):
                continue
            finding_box = self.itemAtPosition(self.row_finding, column).widget()
            if self.check_if_charge_dismissed(column):
                continue
            if self.check_if_allied_offense(column):
                finding_box.setCurrentText('Guilty - Allied Offense')
            else:
                finding_box.setCurrentText('Guilty')
        self.set_cursor_to_first_fine_box()

    def set_cursor_to_first_fine_box(self) -> None:
        """Sets the cursor to the first non-dismissed charge's fine box.

        Column is immediately incremented because 1st column is grid labels.
        """
        for column in range(0, self.columnCount()):
            column += 1
            if self.check_if_column_empty(column):
                continue
            if self.check_if_charge_dismissed(column):
                continue
            try:
                self.itemAtPosition(self.row_fine, column).widget().setFocus()
            except AttributeError as error:
                logger.warning(error)
            break


class ChargeGridBuilder(BaseChargeGrid):
    """The class contains all the methods used to build a charge grid."""

    def add_charge_to_grid(self, column: int, charge: CriminalCharge) -> None:
        """Adds three required charge fields - offense, statute and degree - to the charge grid."""
        self.addWidget(QLabel(charge.offense), self.row_offense, column)
        self.addWidget(cw.StatuteLineEdit(charge.statute), self.row_statute, column)
        self.addWidget(munientry.widgets.combo_boxes.DegreeComboBox(charge.degree), self.row_degree, column)

    def add_delete_button_to_grid(self, column: int, charge: CriminalCharge, dialog) -> None:
        self.addWidget(
            cw.ChargeGridDeleteButton(column, charge, dialog),
            self.row_delete_button,
            column,
        )

    def add_plea_box_to_grid(self, column: int, dialog) -> None:
        self.addWidget(munientry.widgets.combo_boxes.PleaComboBox(column, dialog), self.row_plea, column)

    def add_amend_button_to_grid(self, column: int, charge: CriminalCharge, dialog) -> None:
        self.addWidget(
            cw.ChargeGridAmendButton(column, charge, dialog),
            self.row_amend_button,
            column,
        )

    def add_dismissed_checkbox_to_grid(self, column: int, dialog) -> None:
        self.addWidget(cw.DismissedCheckbox(column, dialog), self.row_dismissed_box, column)

    def add_finding_box_to_grid(self, column: int) -> None:
        self.addWidget(munientry.widgets.combo_boxes.FindingComboBox(), self.row_finding, column)

    def add_allied_checkbox_to_grid(self, column: int, dialog) -> None:
        self.addWidget(cw.AlliedCheckbox(column, dialog), self.row_allied_box, column)


class NotGuiltyPleaGrid(ChargeGridBuilder):
    """Charge Grid for NotGuiltyPleaBond Dialog.

    The dialog does not enter a finding, so the grid is only 5 rows total and the rows are
    renumbered accordingly for this class.
    """

    row_offense = 0
    row_statute = 1
    row_degree = 2
    row_plea = 3
    row_delete_button = 4

    def add_fields_to_charges_grid(self, dialog) -> None:
        column = self.columnCount() + 1
        charge = dialog.entry_case_information.charges_list[-1]
        self.add_charge_to_grid(column, charge)
        self.add_plea_box_to_grid(column, dialog)
        self.add_delete_button_to_grid(column, charge, dialog)


    def set_pleas_to_not_guilty(self) -> None:
        """Sets all pleas to Not Guilty for Not Guilty Plea / Bond Dialog."""
        logger.button(f'{self.sender().text()} Pressed')
        plea = 'Not Guilty'
        for column in range(0, self.columnCount()):
            column += 1
            if self.check_if_column_empty(column):
                continue
            plea_box = self.itemAtPosition(self.row_plea, column).widget()
            plea_box.setCurrentText(plea)


class LeapAdmissionPleaGrid(ChargeGridBuilder):
    """Charge Grid for LeapAdmissionPlea Dialog.

    The dialog does not enter a finding, but does allow for dismissal and amending of charges so
    the rows are renumbered accordingly for this class.
    """

    row_offense = 0
    row_statute = 1
    row_degree = 2
    row_dismissed_box = 3
    row_plea = 4
    row_amend_button = 5
    row_delete_button = 6

    def add_fields_to_charges_grid(self, dialog) -> None:
        charge = dialog.entry_case_information.charges_list[-1]
        column = self.columnCount() + 1
        self.add_charge_to_grid(column, charge)
        self.add_dismissed_checkbox_to_grid(column, dialog)
        self.add_plea_box_to_grid(column, dialog)
        self.add_amend_button_to_grid(column, charge, dialog)
        self.add_delete_button_to_grid(column, charge, dialog)


class PleaOnlyGrid(ChargeGridBuilder):
    """Charge Grid for the PleaOnly Dialog.

    The dialog has a plea and finding, but no sentencing fields (fines and jail days)
    it does allow for dismissal and amending of charges so the rows are renumbered
    accordingly for this class.
    """

    row_offense = 0
    row_statute = 1
    row_degree = 2
    row_dismissed_box = 3
    row_allied_box = 4
    row_plea = 5
    row_finding = 6
    row_amend_button = 7
    row_delete_button = 8

    def add_fields_to_charges_grid(self, dialog) -> None:
        charge = dialog.entry_case_information.charges_list[-1]
        column = self.columnCount() + 1
        self.add_charge_to_grid(column, charge)
        self.add_dismissed_checkbox_to_grid(column, dialog)
        self.add_allied_checkbox_to_grid(column, dialog)
        self.add_plea_box_to_grid(column, dialog)
        self.add_finding_box_to_grid(column)
        self.add_amend_button_to_grid(column, charge, dialog)
        self.add_delete_button_to_grid(column, charge, dialog)


class FineOnlyChargeGrid(ChargeGridBuilder):
    """Charge Grid for the FineOnly Dialog.

    The dialog has all fields, except for jail term boxes.
    """

    row_offense = 0
    row_statute = 1
    row_degree = 2
    row_dismissed_box = 3
    row_allied_box = 4
    row_plea = 5
    row_finding = 6
    row_fine = 7
    row_fine_suspended = 8
    row_amend_button = 9
    row_delete_button = 10

    def add_fields_to_charges_grid(self, dialog) -> None:
        charge = dialog.entry_case_information.charges_list[-1]
        column = self.columnCount() + 1
        self.add_charge_to_grid(column, charge)
        self.add_dismissed_checkbox_to_grid(column, dialog)
        self.add_allied_checkbox_to_grid(column, dialog)
        self.add_plea_box_to_grid(column, dialog)
        self.add_finding_box_to_grid(column)
        self.add_fine_boxes_to_grid(column, charge)
        self.add_amend_button_to_grid(column, charge, dialog)
        self.add_delete_button_to_grid(column, charge, dialog)

    def add_fine_boxes_to_grid(self, column: int, charge: CriminalCharge) -> None:
        self.addWidget(cw.FineLineEdit(charge.offense), self.row_fine, column)
        self.addWidget(cw.FineSuspendedLineEdit(), self.row_fine_suspended, column)


class JailChargesGrid(FineOnlyChargeGrid):
    """Charge Grid for the JailCCPlea Dialog.

    The dialog has all fields.
    """

    row_offense = 0
    row_statute = 1
    row_degree = 2
    row_dismissed_box = 3
    row_allied_box = 4
    row_plea = 5
    row_finding = 6
    row_fine = 7
    row_fine_suspended = 8
    row_jail_days = 9
    row_jail_days_suspended = 10
    row_amend_button = 11
    row_delete_button = 12

    def add_fields_to_charges_grid(self, dialog) -> None:
        charge = dialog.entry_case_information.charges_list[-1]
        column = self.columnCount() + 1
        self.add_charge_to_grid(column, charge)
        self.add_dismissed_checkbox_to_grid(column, dialog)
        self.add_allied_checkbox_to_grid(column, dialog)
        self.add_plea_box_to_grid(column, dialog)
        self.add_finding_box_to_grid(column)
        self.add_fine_boxes_to_grid(column, charge)
        self.add_jail_boxes_to_grid(column, charge)
        self.add_amend_button_to_grid(column, charge, dialog)
        self.add_delete_button_to_grid(column, charge, dialog)

    def add_jail_boxes_to_grid(self, column: int, charge: CriminalCharge) -> None:
        self.addWidget(cw.JailLineEdit(charge.offense), self.row_jail_days, column)
        self.addWidget(cw.JailSuspendedLineEdit(), self.row_jail_days_suspended, column)

    def set_all_trial_findings(self) -> None:
        logger.button(f'{self.sender().text()} Pressed')
        trial_finding = self.get_plea()
        for column in range(0, self.columnCount()):
            column += 1
            if self.check_if_column_empty(column):
                continue
            finding_box = self.itemAtPosition(self.row_finding, column).widget()
            if self.check_if_charge_dismissed(column):
                continue
            if self.check_if_allied_offense(column):
                if trial_finding == 'Guilty':
                    finding_box.setCurrentText('Guilty - Allied Offense')
                if trial_finding == 'Not Guilty':
                    finding_box.setCurrentText('Not Guilty - Allied Offense')
            else:
                finding_box.setCurrentText(trial_finding)


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
