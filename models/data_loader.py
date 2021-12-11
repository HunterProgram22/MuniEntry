from abc import ABC, abstractmethod

from PyQt5.QtSql import QSqlQuery

from models.case_information import CriminalCaseInformation


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
    """Gets case data from a database and loads it into a criminal case object."""
    def __init__(self, case_number, database):
        self.case_number = case_number
        self.database = database
        self.case = self.set_case_type()
        self.get_case_data()

    def set_case_type(self):
        return CriminalCaseInformation()

    def get_case_data(self):
        """Query database based on case number to return the data to load for the
        dialog.
        Current - Query.value(0) is id, then 1 is case_number, 2 is last_name, 3 is first_name."""
        key = self.case_number
        query = QSqlQuery(self.database)
        query_string = f"""
            SELECT *
            FROM cases
            WHERE case_number = '{key}'
            """
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
