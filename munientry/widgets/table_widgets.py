from PyQt5 import QtGui, QtPrintSupport
from PyQt5.QtWidgets import QWidget, QTableWidget, QAbstractScrollArea, QSizePolicy, QHeaderView, QPushButton, QGridLayout
from loguru import logger
from munientry.settings import ICON_PATH


class ReportWindow(QWidget):
    def __init__(self, rows, cols, report_name):
        QWidget.__init__(self)
        self.report_name = report_name
        self.setWindowTitle(self.tr(self.report_name))
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        self.table = ReportTable(rows, cols, self.report_name, self)
        self.buttonPrint = QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QGridLayout(self)
        layout.addWidget(self.table, 0, 0, 1, 2)
        layout.addWidget(self.buttonPrint, 1, 0)
        layout.addWidget(self.buttonPreview, 1, 1)
        self.resize(1000, 800)

    def handlePrint(self):
        dialog = QtPrintSupport.QPrintDialog()
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.handlePaintRequest(dialog.printer())

    def handlePreview(self):
        dialog = QtPrintSupport.QPrintPreviewDialog()
        dialog.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        dialog.resize(1000, 800)
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def handlePaintRequest(self, printer):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        h1_style = '{text-align: center; font-family: "Palatino Linotype", Palatino, serif;}'
        title = cursor.insertHtml(f'''
            <style>
                h1 {h1_style}
            </style>
            <h1>DELAWARE MUNICIPAL COURT</h1>
            <br>
            <h3>{self.report_name}</h3>
           <hr> 
            ''')
        if self.table.rowCount() > 0:
            table = cursor.insertTable(self.table.rowCount(), self.table.columnCount())
            for row in range(table.rows()):
                for col in range(table.columns()):
                    cursor.insertText(self.table.item(row, col).text())
                    cursor.movePosition(QtGui.QTextCursor.NextCell)
        document.print_(printer)


class ReportTable(QTableWidget):
    def __init__(self, rows, cols, title, parent=None):
        super(QTableWidget, self).__init__(rows, cols, parent)
        self.title = title
        self.set_up_widget()
        logger.info(self.title)

    def set_up_widget(self):
        self.setWindowIcon(QtGui.QIcon(ICON_PATH + 'gavel.ico'))
        self.setWindowTitle(self.title)
        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        header = self.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.setSortingEnabled(False)
        self.setAlternatingRowColors(True)
        self.resize(1000, 800)
