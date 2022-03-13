class NoJailPleaFindingFines:
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

    @classmethod
    def add(cls, dialog):
        column = 1
        for index, charge in enumerate(dialog.entry_case_information.charges_list):
            while dialog.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_offense, column) is None:
                column += 1
            charge.statute = dialog.charges_gridLayout.itemAtPosition(
                NoJailPleaFindingFines.row_statute, column).widget().text()
            charge.degree = dialog.charges_gridLayout.itemAtPosition(
                NoJailPleaFindingFines.row_degree, column).widget().currentText()
            charge.plea = dialog.charges_gridLayout.itemAtPosition(
                NoJailPleaFindingFines.row_plea, column).widget().currentText()
            if dialog.charges_gridLayout.itemAtPosition(
                    NoJailPleaFindingFines.row_plea, column).widget().currentText() == "Dismissed":
                charge.finding = ""
                charge.fines_amount = " " # A space is used here b/c otherwise puts 0
                charge.fines_suspended = " " # A space is used here b/c otherwise puts 0
            else:
                charge.finding = dialog.charges_gridLayout.itemAtPosition(
                    NoJailPleaFindingFines.row_finding, column).widget().currentText()
                if dialog.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine, column).widget().text() == "":
                    charge.fines_amount = 0
                    charge.fines_amount = f"$ {charge.fines_amount}"
                else:
                    charge.fines_amount = (
                        dialog.charges_gridLayout.itemAtPosition(
                            NoJailPleaFindingFines.row_fine, column).widget().text()
                    )
                    charge.fines_amount = f"$ {charge.fines_amount}"
                if dialog.charges_gridLayout.itemAtPosition(NoJailPleaFindingFines.row_fine_suspended, column).widget().text() == "":
                    charge.fines_suspended = 0
                    charge.fines_suspended = f"$ {charge.fines_suspended}"
                else:
                    charge.fines_suspended = (
                        dialog.charges_gridLayout.itemAtPosition(
                            NoJailPleaFindingFines.row_fine_suspended, column).widget().text()
                    )
                    charge.fines_suspended = f"$ {charge.fines_suspended}"
            column += 1


class JailAddPleaFindingsFinesJail:
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

    @classmethod
    def add(cls, dialog):
        column = 1
        for index, charge in enumerate(dialog.entry_case_information.charges_list):
            while dialog.charges_gridLayout.itemAtPosition(JailAddPleaFindingsFinesJail.row_offense, column) is None:
                column += 1
            charge.statute = dialog.charges_gridLayout.itemAtPosition(
                JailAddPleaFindingsFinesJail.row_statute, column).widget().text()
            charge.degree = dialog.charges_gridLayout.itemAtPosition(
                JailAddPleaFindingsFinesJail.row_degree, column).widget().currentText()
            charge.plea = dialog.charges_gridLayout.itemAtPosition(
                JailAddPleaFindingsFinesJail.row_plea, column).widget().currentText()
            if dialog.charges_gridLayout.itemAtPosition(
                    JailAddPleaFindingsFinesJail.row_plea, column).widget().currentText() == "Dismissed":
                charge.finding = ""
                charge.fines_amount = " " # A space is used here b/c otherwise puts 0
                charge.fines_suspended = " " # A space is used here b/c otherwise puts 0
                charge.jail_days = " " # A space is used here b/c otherwise puts None
                charge.jail_days_suspended = " " # A space is used here b/c otherwise puts None
            else:
                charge.finding = dialog.charges_gridLayout.itemAtPosition(
                    JailAddPleaFindingsFinesJail.row_finding, column).widget().currentText()
                if dialog.charges_gridLayout.itemAtPosition(JailAddPleaFindingsFinesJail.row_fine,
                                                            column).widget().text() == "":
                    charge.fines_amount = 0
                    charge.fines_amount = f"$ {charge.fines_amount}"
                else:
                    charge.fines_amount = (
                        dialog.charges_gridLayout.itemAtPosition(
                            JailAddPleaFindingsFinesJail.row_fine, column).widget().text()
                    )
                    charge.fines_amount = f"$ {charge.fines_amount}"
                if dialog.charges_gridLayout.itemAtPosition(JailAddPleaFindingsFinesJail.row_fine_suspended, column).widget().text() == "":
                    charge.fines_suspended = 0
                    charge.fines_suspended = f"$ {charge.fines_suspended}"
                else:
                    charge.fines_suspended = (
                        dialog.charges_gridLayout.itemAtPosition(
                            JailAddPleaFindingsFinesJail.row_fine_suspended, column).widget().text()
                    )
                    charge.fines_suspended = f"$ {charge.fines_suspended}"
                if dialog.charges_gridLayout.itemAtPosition(JailAddPleaFindingsFinesJail.row_jail_days, column).widget().text() == "":
                    charge.jail_days = "None"
                else:
                    charge.jail_days = dialog.charges_gridLayout.itemAtPosition(
                        JailAddPleaFindingsFinesJail.row_jail_days, column).widget().text()
                if dialog.charges_gridLayout.itemAtPosition(JailAddPleaFindingsFinesJail.row_jail_days_suspended, column).widget().text() == "":
                    charge.jail_days_suspended = "None"
                else:
                    charge.jail_days_suspended = dialog.charges_gridLayout.itemAtPosition(
                        JailAddPleaFindingsFinesJail.row_jail_days_suspended, column).widget().text()
            column += 1


class NotGuiltyAddPlea:
    row_offense = 0
    row_statute = 1
    row_degree = 2
    row_plea = 3

    @classmethod
    def add(cls, dialog):
        column = 1
        for index, charge in enumerate(dialog.entry_case_information.charges_list):
            while dialog.charges_gridLayout.itemAtPosition(NotGuiltyAddPlea.row_offense, column) is None:
                column += 1
            charge.statute = dialog.charges_gridLayout.itemAtPosition(
                NotGuiltyAddPlea.row_statute, column).widget().text()
            charge.degree = dialog.charges_gridLayout.itemAtPosition(
                NotGuiltyAddPlea.row_degree, column).widget().currentText()
            charge.plea = dialog.charges_gridLayout.itemAtPosition(
                NotGuiltyAddPlea.row_plea, column).widget().currentText()
            column += 1