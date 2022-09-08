"""Module for packaging data from SQL Server database for use in application."""

from loguru import logger
from PyQt5.QtSql import QSqlQuery

from munientry.data.connections import close_db_connection, open_db_connection
from munientry.data.sql_server_queries import general_case_search_query, driving_case_search_query
from munientry.data.excel_getters import clean_offense_name, clean_statute_name
from munientry.models.cms_models import CmsCaseInformation, DrivingPrivilegesInformation
from munientry.widgets.message_boxes import InfoBox


class CriminalCaseSQLServer(object):
    """Packages case data from the SQL Server Authority Court database.

    The class accepts the case number to identify the case, then retrieves
    the case information from the SQL Server (AuthorityCourtDBO) database and packages it for
    loading into the application.

    :case_number: The entered case number from the on the case search tab of the main window of
        the application.
    """

    def __init__(self, case_number: str) -> None:
        self.case_number = case_number
        self.database_connection_name = 'con_authority_court'
        self.database = open_db_connection(self.database_connection_name)
        self.case = CmsCaseInformation()
        self.query_case_data()
        self.load_query_data_into_case()
        self.query.finish()
        close_db_connection(self.database)

    def query_case_data(self) -> None:
        """Query database based on cms_case number to return the data to load for the dialog."""
        query_string = general_case_search_query(self.case_number)
        self.query = QSqlQuery(self.database)
        self.query.prepare(query_string)
        logger.database(f'Querying {self.database_connection_name}')
        logger.database(f'Query: {query_string}')
        self.query.bindValue(self.case_number, self.case_number)
        self.query.exec()

    def load_query_data_into_case(self) -> None:
        while self.query.next():
            if self.case.case_number is None:
                self.load_case_information()
            self.load_charge_information()

    def load_case_information(self) -> None:
        self.case.case_number = self.query.value('CaseNumber')
        self.case.defendant.last_name = self.query.value('DefLastName').title()
        self.case.defendant.first_name = self.query.value('DefFirstName').title()
        self.case.fra_in_file = self.query.value('FraInFile')
        self.case.defense_counsel = self.query.value('DefenseCounsel').title()
        self.case.defense_counsel_type = self.query.value('PubDef')

    def load_charge_information(self) -> None:
        offense = clean_offense_name(self.query.value('Charge'))
        statute = clean_statute_name(self.query.value('Statute'))
        degree = self.query.value('DegreeCode')
        moving_bool = self.query.value('MovingBool')
        charge = (offense, statute, degree, moving_bool)
        self.case.charges_list.append(charge)

    def load_case(self) -> CmsCaseInformation:
        return self.case


class DrivingInfoSQLServer(object):
    """Packages driving privileges case data from the SQL Server Authority Court database.

    The class accepts the case number to identify the case, then retrieves
    the case information from the SQL Server (AuthorityCourtDBO) database and packages it for
    loading into the application.

    :case_number: The entered case number from the on the case search tab of the main window of
        the application.
    """

    def __init__(self, case_number: str) -> None:
        self.case_number = case_number
        self.database_connection_name = 'con_authority_court'
        self.database = open_db_connection(self.database_connection_name)
        self.case = DrivingPrivilegesInformation()
        self.query_case_data()
        self.check_query_for_conflicts()
        self.load_query_data_into_case()
        self.query.finish()
        close_db_connection(self.database)

    def query_case_data(self) -> None:
        """Query database based on cms_case number to return the data to load for the dialog."""
        query_string = driving_case_search_query(self.case_number)
        self.query = QSqlQuery(self.database)
        self.query.prepare(query_string)
        logger.database(f'Querying {self.database_connection_name}')
        logger.database(f'Query: {query_string}')
        self.query.bindValue(self.case_number, self.case_number)
        self.query.exec()

    def check_query_for_conflicts(self):
        count = 0
        while self.query.next():
            count += 1
        logger.info(f'Conflict check found {count} addresses for Defendant.')
        if count <= 1:
            return None
        else:
            message = (
                'There are multiple addresses and/or driver license numbers associated with'
                + ' this case, please check fields closely and correct address fields if'
                + ' needed.'
            )
            msg_response = InfoBox(message, 'Multiple Addreses for Defendant').exec()
            return None

    def load_query_data_into_case(self) -> None:
        self.query.first()
        self.load_case_information()

    def load_case_information(self) -> None:
        self.case.case_number = self.query.value('CaseNumber')
        self.case.defendant.first_name = self.query.value('DefFirstName').title()
        self.case.defendant.last_name = self.query.value('DefLastName').title()
        self.case.defendant.birth_date = self.query.value('DefBirthDate')
        self.case.defendant.address = self.query.value('DefAddress')
        self.case.defendant.city = self.query.value('DefCity')
        self.case.defendant.state = self.query.value('DefState')
        self.case.defendant.zipcode = self.query.value('DefZipcode')
        self.case.defendant.license_number = self.query.value('DefLicenseNumber')

    def load_case(self) -> DrivingPrivilegesInformation:
        return self.case

if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
