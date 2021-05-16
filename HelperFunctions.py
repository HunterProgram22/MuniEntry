from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH

def getText(filename):
    "There are formatting issues that need to be fixed."
    doc = Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)
