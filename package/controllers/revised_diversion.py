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
        return DiversionDialogViewModifier()

    @logger.catch
    def connect_signals_to_slots(self):
        """The method connects additional signals to slots. That are not
        included in the BaseDialog."""
        super().connect_signals_to_slots()
        self.connect_plea_signals_and_slots()
        self.diversion_jail_imposed_checkBox.toggled.connect(self.show_jail_report_date_box)
        self.other_conditions_checkBox.toggled.connect(self.show_other_conditions_box)

    def show_other_conditions_box(self):
        if self.other_conditions_checkBox.isChecked():
            self.other_conditions_textEdit.setHidden(False)
            self.other_conditions_textEdit.setFocus()
        else:
            self.other_conditions_textEdit.setHidden(True)

    def show_jail_report_date_box(self):
        if self.diversion_jail_imposed_checkBox.isChecked():
            self.diversion_jail_report_date_box.setHidden(False)
            self.diversion_jail_report_date_label.setHidden(False)
        else:
            self.diversion_jail_report_date_box.setHidden(True)
            self.diversion_jail_report_date_label.setHidden(True)

    def connect_plea_signals_and_slots(self):
        self.guilty_all_Button.pressed.connect(self.set_plea_and_findings_process)
        self.fra_in_file_box.currentTextChanged.connect(self.set_fra_in_file)
        self.fra_in_court_box.currentTextChanged.connect(self.set_fra_in_court)
        self.no_contest_all_Button.pressed.connect(self.set_plea_and_findings_process)

    def add_charge_to_grid(self):
        self.charges_gridLayout.add_charge_only_to_grid(self)
        self.defense_counsel_name_box.setFocus()

    @logger.catch
    def add_plea_findings_and_fines_to_entry_case_information(self):
        return JailAddPleaFindingsFinesJail.add(self) # self is dialog

    @logger.catch
    def update_case_information(self):
        """"Ovverrides CriminalSentencingDialog update so add_additional_conditions method is not called."""
        self.add_plea_findings_and_fines_to_entry_case_information()
        self.transfer_field_data_to_model(self.entry_case_information.diversion)
        self.entry_case_information.diversion.program_name = self.entry_case_information.diversion.get_program_name()
        self.transfer_field_data_to_model(self.entry_case_information.other_conditions)
        return CasePartyUpdater(self)

    @logger.catch
    def set_fra_in_file(self, current_text):
        """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
        that the FRA was shown in the complaint of file."""
        if current_text == "Yes":
            self.entry_case_information.fra_in_file = True
            self.fra_in_court_box.setCurrentText("No")
        elif current_text == "No":
            self.entry_case_information.fra_in_file = False
        else:
            self.entry_case_information.fra_in_file = None

    @logger.catch
    def set_fra_in_court(self, current_text):
        """Sets the FRA (proof of insurance) to true if the view indicates 'yes'
        that the FRA was shown in court."""
        if current_text == "Yes":
            self.entry_case_information.fra_in_court = True
        elif current_text == "No":
            self.entry_case_information.fra_in_court = False
        else:
            self.entry_case_information.fra_in_court = None