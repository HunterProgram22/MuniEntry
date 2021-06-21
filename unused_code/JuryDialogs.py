from pyuifiles.jury_instructions_dialog_ui import Ui_JuryInstructionsDialog


class JuryInstructionsDialog(BaseDialog, Ui_JuryInstructionsDialog):
    template = JURY_INSTRUCTIONS_TEMPLATE
    #saved_doc = JURY_INSTRUCTIONS_SAVED_DOC

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def getDialogFields(self):
        defendant_name = self.DefendantName_lineEdit.text()
        case_no = self.CaseNo_lineEdit.text()
        complaint_date = self.ComplaintDate_lineEdit.text()
        first_charge = self.FirstCharge_comboBox.currentText()
        second_charge = self.SecondCharge_comboBox.currentText()
        self.populateInstructions(JuryInstructionsDialog.template)
        count_one_instructions = getText("Saved/Populated_Jury_Instructions.docx")
        return { 'defendant_name' : defendant_name,
                    'case_no' : case_no,
                    'first_charge' : first_charge,
                    'second_charge' : second_charge,
                    'complaint_date' : complaint_date,
                    'count_one_instructions' : count_one_instructions,
                    }

    def populateInstructions(self, instructions):
        defendant_name = self.DefendantName_lineEdit.text()
        fields_dict = { 'defendant_name' : defendant_name,
                    }
        doc = DocxTemplate(instructions)
        doc.render(fields_dict)
        doc.save("Saved/Jury_Instructions_Test.docx")
