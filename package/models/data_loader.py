from abc import ABC, abstractmethod

from PyQt5.QtSql import QSqlQuery, QSqlDatabase
from loguru import logger

from package.models.case_information import CriminalCaseInformation
from settings import CHARGES_DATABASE


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
        """Query database based on cms_case number to return the data to load for the
        dialog.
        Current - Query.value(0) is id, then 1 is case_number, 2 is last_name, 3 is first_name."""
        key = self.case_number
        query = QSqlQuery(self.database)
        query_string = f"""
            SELECT *
            FROM {self.case_table}
            WHERE case_number = '{key}'
            """
        print(query_string)
        query.prepare(query_string)
        query.bindValue(key, key)
        query.exec()
        self.load_data_into_case(query)
        query.finish()

    def load_data_into_case(self, query):
        """TODO: Can Refactor more."""
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


@logger.catch
def create_daily_case_list_database_connection():
    daily_case_list_database_connection = QSqlDatabase.database("con1", open=True)
    return daily_case_list_database_connection


@logger.catch
def create_database_connections():
    """The databases for the application are created upon import of the module, which is done
    on application startup. The connections to the databases are created, but the opening and
    closing of the databases is handled by the appropriate class dialog."""
    offense_database_connection = QSqlDatabase.addDatabase("QSQLITE", "offenses")
    offense_database_connection.setDatabaseName(CHARGES_DATABASE)
    return offense_database_connection