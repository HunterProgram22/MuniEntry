class DiversionPleaDialog(CriminalBaseDialog, Ui_DiversionPleaDialog):
    @logger.catch
    def __init__(self, judicial_officer, cms_case=None, case_table=None, parent=None):
        super().__init__(judicial_officer, cms_case, case_table, parent)
        self.charges_gridLayout.__class__ = JailChargesGrid # Use JailChargesGrid because same setup for Diversion
        self.dialog_name = 'Diversion Plea Dialog'
        self.template = TEMPLATE_DICT.get(self.dialog_name)
        self.entry_case_information.diversion.ordered = True
        self.load_cms_data_to_view()

    def modify_view(self):
        return DiversionDialogViewModifier(self)

    @logger.catch
    def connect_signals_to_slots(self):
        return DiversionDialogSignalConnector(self)

    def set_dialog_function(self):
        return DiversionDialogSlotFunctions(self)