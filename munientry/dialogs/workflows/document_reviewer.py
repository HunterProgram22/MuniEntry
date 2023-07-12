from loguru import logger

from PyQt6.QtWidgets import QApplication, QDialog, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt, QProcess

class DocumentReviewDialog(QDialog):
    def __init__(self):
        super().__init__()

        # Set up the UI of the dialog
        self.setWindowTitle('Document Review')
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.accept_button = QPushButton('Accept')
        self.reject_button = QPushButton('Reject')
        self.accept_button.clicked.connect(self.accept_document)
        self.reject_button.clicked.connect(self.reject_document)
        button_layout.addWidget(self.accept_button)
        button_layout.addWidget(self.reject_button)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)
        self.layout().addWidget(self.accept_button)
        self.layout().addWidget(self.reject_button)

    def accept_document(self):
        # Perform any necessary actions to accept the document
        self.accept()

    def reject_document(self):
        # Perform any necessary actions to reject the document
        self.reject()


def open_word_document(doc_path):
    # Launch Microsoft Word and open the document
    process = QProcess()
    logger.debug(doc_path)
    return_value = process.start(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE", [doc_path])
    logger.debug(return_value)

    # process.waitForFinished()
    # Create and show the document review dialog
    dialog = DocumentReviewDialog()
    result = dialog.exec()

    # Handle the user's selection
    if result == QDialog.DialogCode.Accepted:
        # User accepted the document
        # Need to call the accept_document first then terminate process.
        process.waitForFinished()  # Does not finsihed until Word closed, need to close word.
        process.terminate()
    else:
        # User rejected the document
        process.waitForFinished()
        process.terminate()
        # process.kill()
