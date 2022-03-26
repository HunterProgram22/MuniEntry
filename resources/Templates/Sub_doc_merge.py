from docxtpl import DocxTemplate



TEMPLATE_PATH = f"/resources/Templates\\"


tpl = DocxTemplate(TEMPLATE_PATH + "Base_Template.docx")

sd = tpl.new_subdoc(TEMPLATE_PATH + "Sub_Doc_Template.docx")




context = {
    'mysubdoc': sd,
}

tpl.render(context)
tpl.save('.\subdoc.docx')