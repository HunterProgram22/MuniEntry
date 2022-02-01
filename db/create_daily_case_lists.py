"""This module is used to create the slated table."""
import sys
import os
import pathlib

from loguru import logger
from openpyxl import load_workbook
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

from settings import DB_PATH

DATABASE_TABLE_LIST = [
    ("Arraignments.xlsx", "arraignments"),
    ("Slated.xlsx", "slated"),
    ("Final_Pretrials.xlsx", "final_pretrials"),
]

@logger.catch
def return_data_from_excel(excel_file):
    data = []
    workbook = load_workbook(excel_file)
    worksheet = workbook.active
    row_count = worksheet.max_row + 1
    for row in range(2, row_count):
        case_number = worksheet.cell(row=row, column=1)
        defendant_last_name = worksheet.cell(row=row, column=3)
        defendant_first_name = worksheet.cell(row=row, column=4)
        offense = worksheet.cell(row=row, column=5)
        if worksheet.cell(row=row, column=6).value is None:
            worksheet.cell(row=row, column=6).value = "No Data"
            statute = worksheet.cell(row=row, column=6)
        else:
            statute = worksheet.cell(row=row, column=6)
        if worksheet.cell(row=row, column=7).value is None:
            worksheet.cell(row=row, column=7).value = "No Data"
            degree = worksheet.cell(row=row, column=7)
        else:
            degree = worksheet.cell(row=row, column=7)
        if worksheet.cell(row=row, column=8).value is None:
            worksheet.cell(row=row, column=8).value = "U"
            fra_in_file = worksheet.cell(row=row, column=8)
        else:
            fra_in_file = worksheet.cell(row=row, column=8)
        case = (case_number.value,
                defendant_last_name.value,
                defendant_first_name.value,
                offense.value,
                statute.value,
                degree.value,
                fra_in_file.value,
                )
        data.append(case)
    return data


def create_table_sql_string(table):
    return f"""
      CREATE TABLE {table} (
          id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
          case_number VARCHAR(20) NOT NULL,
          defendant_last_name VARCHAR(50) NOT NULL,
          defendant_first_name VARCHAR(50) NOT NULL,
          offense VARCHAR(80) NOT NULL,
          statute VARCHAR(50) NOT NULL,
          degree VARCHAR(10) NOT NULL,
          fra_in_file VARCHAR(5) NOT NULL
      )
      """


def insert_table_sql_string(table):
    return f"""
        INSERT INTO {table}(
            case_number,
            defendant_last_name,
            defendant_first_name,
            offense,
            statute,
            degree,
            fra_in_file
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """


def delete_table_data_sql_string(table):
    return f"""
        DELETE FROM {table};
        """


def create_db_connection():
    database_name = f"{DB_PATH}daily_case_lists.sqlite"
    if os.path.exists(database_name):
        con1 = QSqlDatabase.addDatabase("QSQLITE", "con1")
        con1.setDatabaseName(database_name)
    else:
        print("The file does not exist")
        con1 = QSqlDatabase.addDatabase("QSQLITE", "con1")
        con1.setDatabaseName(database_name)
        if not con1.open():
            print("Unable to connect to database")
            sys.exit(1)
        else:
            create_table_query = QSqlQuery(con1)
            for item in DATABASE_TABLE_LIST:
                table = item[1]
                create_table_query.exec(create_table_sql_string(table))
    if not con1.open():
        print("Unable to connect to database")
        sys.exit(1)
    return con1


def main():
    con1 = create_db_connection()

    # excel_report = "Arraignments.xlsx"
    # table = "arraignments"

    for item in DATABASE_TABLE_LIST:
        excel_report = item[0]
        table = item[1]

        delete_old_data_query = QSqlQuery(con1)
        delete_old_data_query.prepare(delete_table_data_sql_string(table))
        delete_old_data_query.exec()

        insert_data_query = QSqlQuery(con1)
        insert_data_query.prepare(insert_table_sql_string(table))
        data_from_table = return_data_from_excel(f"{DB_PATH}{excel_report}")
        # Do not add comma to last value inserted
        for case_number, defendant_last_name, defendant_first_name, offense, \
                statute, degree, fra_in_file in data_from_table:
            insert_data_query.addBindValue(case_number)
            insert_data_query.addBindValue(defendant_last_name)
            insert_data_query.addBindValue(defendant_first_name)
            insert_data_query.addBindValue(offense)
            insert_data_query.addBindValue(statute)
            insert_data_query.addBindValue(degree)
            insert_data_query.addBindValue(fra_in_file)
            insert_data_query.exec()

    con1.close()
    con1.removeDatabase("QSQLITE")
    return None


if __name__ == "__main__":
    print("Daily Case Lists created directly from script")
else:
    main()
    print("Imported Daily Case List Tables")
