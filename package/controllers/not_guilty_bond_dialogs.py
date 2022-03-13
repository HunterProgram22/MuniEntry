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
