class ExtraditionEntryDialog(BaseDialog, Ui_ExtraditionEntryDialog):
    template = "Templates/Extradition_Entry.docx"
    template_name = "Extradition_Entry"

    def __init__(self, parent=None):
        super().__init__(parent)

    def getDialogFields(self):
        super(ExtraditionEntryDialog, self).getDialogFields()
        self.fields_dict['defendant_hold_date'] = self.defendant_hold_date.date().toString('MMMM d, yyyy')
        self.fields_dict['defendant_hold_time'] = self.defendant_hold_time.time().toString('h:mm AP')
        self.fields_dict['state_county_requestor'] = self.state_county_requestor.text()
        return self.fields_dict
