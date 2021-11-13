"""This module is used to create the charges table.

TODO: Right now it manually needs the rows in range changed
when charges are added, need to update to call len or something
similar.

TODO: Also, eventually should this be called on load so charges
could be added somewhere by anyone and the db created each time
the application is loaded to account for new charges. May be
a bit unnecessary - but perhaps adding charges by user to a shared
db could be done."""
import sys
import pathlib
from loguru import logger

from openpyxl import load_workbook

from PyQt5.QtSql import QSqlDatabase, QSqlQuery


PATH = str(pathlib.Path().absolute())

EXCEL_FILE = PATH + "\Arraignments.xlsx"


@logger.catch
def return_data_from_excel(excel_file):
    data = []
    workbook = load_workbook(excel_file)
    worksheet = workbook.active
    for row in range(2, 21):
        case_number = worksheet.cell(row=row, column=1)
        defendant_last_name = worksheet.cell(row=row, column=3)
        defendant_first_name = worksheet.cell(row=row, column=4)
        case = (case_number.value,
                defendant_last_name.value,
                defendant_first_name.value,
                )
        data.append(case)
    return data

# Connecting both an alphabetical (offense) and numerical (statute) ordered database
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName(PATH + "\\arraignments.sqlite")


if not con.open():
    print("Unable to connect to database")
    sys.exit(1)


# Create a query and execute it right away using .exec()
createTableQuery = QSqlQuery()
createTableQuery.exec(
    """
    CREATE TABLE cases (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        case_number VARCHAR(20) NOT NULL,
        defendant_last_name VARCHAR(50) NOT NULL,
        defendant_first_name VARCHAR(50) NOT NULL
    )
    """
)

insertDataQuery = QSqlQuery()
insertDataQuery.prepare(
    """
    INSERT INTO cases (
        case_number,
        defendant_last_name,
        defendant_first_name
    )
    VALUES (?, ?, ?)
    """
)


# TO POPULATE A COMBO BOX http://www.voidynullness.net/blog/2013/02/05/qt-populate-combo-box-from-database-table/
# https://python-forum.io/thread-11659.html
# Create two tables one for alpha sort and one for num sort - defintely a better way to do this
data_from_table = return_data_from_excel(EXCEL_FILE)
print(data_from_table)

# Use .addBindValue() to insert data
for case_number, defendant_last_name, defendant_first_name in data_from_table:
    insertDataQuery.addBindValue(case_number)
    insertDataQuery.addBindValue(defendant_last_name)
    insertDataQuery.addBindValue(defendant_first_name)
    insertDataQuery.exec()
