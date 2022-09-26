"""Module that contains ViewModifier classes. ViewModifier classes are called for a dialog
after the setupUI is called. This class makes changes to the view that are outside the the specific
view file. Modifications to the view are placed in the ViewModifier class so that they don't need to
be updated each time a view file is recompiled through the pyuic5 command."""
from loguru import logger
from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel
from munientry.builders.crimtraffic.base_crimtraffic_builders import BaseDialogViewModifier

TODAY = QtCore.QDate.currentDate()


class AddSpecialBondConditionsDialogViewModifier(BaseDialogViewModifier):
    def __init__(self, dialog):
        super().__init__(dialog)
        self.set_special_bond_conditions_case_information_banner()
        self.load_existing_data_to_dialog()

    def set_special_bond_conditions_case_information_banner(self):
        column = self.dialog.charges_gridLayout.columnCount() + 1
        for charge in self.dialog.charges_list:
            logger.debug(charge)
            charge = vars(charge)
            if charge is not None:
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("offense")), 0, column)
                self.dialog.charges_gridLayout.addWidget(QLabel(charge.get("statute")), 1, column)
                column += 1

    def load_existing_data_to_dialog(self):
        CONDITIONS_CLASSES = [
            ("other_conditions_checkBox", "other_conditions"),
            ("admin_license_suspension_checkBox", "admin_license_suspension"),
            ("domestic_violence_checkBox", "domestic_violence_conditions"),
            ("vehicle_seizure_checkBox", "vehicle_seizure"),
            ("no_contact_checkBox", "no_contact"),
            ("custodial_supervision_checkBox", "custodial_supervision"),
        ]
        for item in CONDITIONS_CLASSES:
            (condition_checkbox, model_class) = item
            if getattr(self.dialog.main_dialog, condition_checkbox).isChecked():
                model_class = getattr(self.dialog.main_dialog.entry_case_information, model_class)
                self.transfer_model_data_to_view(model_class)
            else:
                continue


if __name__ == "__main__":
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
