import os
import sqlite3
import sys
from abc import ABC, abstractmethod

from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from loguru import logger
from openpyxl import load_workbook
from package.models.case_information import CriminalCaseInformation
from settings import CHARGES_DATABASE, DB_PATH

DATABASE_TABLE_LIST = [
    ("Arraignments.xlsx", "arraignments"),
    ("Slated.xlsx", "slated"),
    ("Final_Pretrials.xlsx", "final_pretrials"),
]


class CaseSQLRetriever(ABC):

    @abstractmethod
    def set_case_type(self):
        raise NotImplementedError

    @abstractmethod
    def get_case_data(self):
        raise NotImplementedError

    @abstractmethod
    def load_data_into_case(self, query):
        raise NotImplementedError

    @abstractmethod
    def load_case(self):
        raise NotImplementedError


class CriminalCaseSQLRetriever(CaseSQLRetriever):
    """Gets cms_case data from a database and loads it into a criminal cms_case object."""
    def __init__(self, case_number, case_table, database):
        self.case_number = case_number
        self.case_table = case_table
        self.database = database
        self.case = self.set_case_type()
        self.get_case_data()

    def set_case_type(self):
        return CriminalCaseInformation()

    def get_case_data(self):
        """Query database based on cms_case number to return the data to load for the dialog.
        Current - Query.value(0) is id, then 1 is case_number, 2 is last_name, 3 is first_name."""
        key = self.case_number
        query = QSqlQuery(self.database)
        query_string = f"""
            SELECT *
            FROM {self.case_table}
            WHERE case_number = '{key}'
            """
        query.prepare(query_string)
        query.bindValue(key, key)
        query.exec()
        self.load_data_into_case(query)
        query.finish()

    def load_data_into_case(self, query):
        case_number = None
        while query.next():
            if case_number is None:
                self.case.case_number = query.value(1)
                case_number = self.case.case_number
                self.case.defendant.last_name = query.value(2)
                self.case.defendant.first_name = query.value(3)
                self.case.fra_in_file = query.value(7)
            offense = query.value(4)
            statute = query.value(5)
            degree = query.value(6)
            new_charge = (offense, statute, degree)
            self.case.charges_list.append(new_charge)

    def load_case(self):
        return self.case


def open_daily_case_list_db_connection():
    daily_case_list_database_connection = QSqlDatabase.database("con1", open=True)
    return daily_case_list_database_connection


@logger.catch
def create_daily_case_list_db_connection():
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


def create_database_connections():
    """The databases for the application are created upon import of the module, which is done
    on application startup when base_dialog is imported into main. The connections to the databases
    are created, but opening and closing is handled with init or close functions in controller dialogs."""
    offense_database_connection = QSqlDatabase.addDatabase("QSQLITE", "con_offenses")
    offense_database_connection.setDatabaseName(CHARGES_DATABASE)
    return offense_database_connection


def extract_data(case_data):
    wb_name = "Case_Data.xlsx"
    wb_name = DB_PATH + wb_name
    wb = load_workbook(wb_name)
    page = wb.active
    case_number = case_data.get('case_number')
    judicial_officer = case_data.get('judicial_officer').last_name
    charges_list = case_data.get('charges_list')
    max_row = page.max_row
    max_row = max_row + 1
    for index, charge in enumerate(charges_list):
        page.cell(row=max_row+index, column=1, value=case_number)
        page.cell(row=max_row+index, column=2, value=judicial_officer)
        page.cell(row=max_row+index, column=3, value=charge.get('offense'))
        page.cell(row=max_row+index, column=4, value=charge.get('statute'))
        page.cell(row=max_row+index, column=5, value=charge.get('degree'))
        page.cell(row=max_row+index, column=6, value=charge.get('plea'))
        page.cell(row=max_row+index, column=7, value=charge.get('finding'))
        page.cell(row=max_row+index, column=8, value=charge.get('fines_amount'))
        page.cell(row=max_row+index, column=9, value=charge.get('fines_suspended'))
        page.cell(row=max_row+index, column=10, value=charge.get('jail_days'))
        page.cell(row=max_row+index, column=11, value=charge.get('jail_days_suspended'))
    try:
        wb.save(filename=wb_name)
    except PermissionError:
        pass


def create_offense_list():
    conn = sqlite3.connect(CHARGES_DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT offense, statute FROM charges")
    offense_list = cursor.fetchall()
    clean_offense_list = []
    for i in offense_list:
        clean_offense_list.append(i[0])
    clean_offense_list.sort()
    conn.close()
    return clean_offense_list


def create_statute_list():
    conn = sqlite3.connect(CHARGES_DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT offense, statute FROM charges")
    statute_list = cursor.fetchall()
    clean_statute_list = []
    for i in statute_list:
        clean_statute_list.append(i[1])
    clean_statute_list.sort()
    conn.close()
    return clean_statute_list


def create_daily_cases_list(database, table):
    conn = sqlite3.connect(DB_PATH + database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT DISTINCT defendant_last_name, defendant_first_name, case_number FROM {table}")
    cases_list = cursor.fetchall()
    clean_cases_list = []
    for i in cases_list:
        name = i[0] + " - " + i[2]
        clean_cases_list.append(name)
    clean_cases_list.sort()
    conn.close()
    clean_cases_list.insert(0, None)
    return clean_cases_list


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
    """This clears all data from the table."""
    return f"""
        DELETE FROM {table};
        """


def main():
    con1 = create_daily_case_list_db_connection()

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
    from db import create_charges_table
    main()
    print("Imported Daily Case List Tables")
