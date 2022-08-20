"""Module containing all SQL Server queries used throughout the application."""
from loguru import logger


def general_case_search_query(case_number: str) -> str:
    return f"""
    SELECT
    SubCase.Id AS SubCaseID,
    Violation.Id AS ViolationID,
    CaseMaster.CaseNumber,
    SubCase.SubCaseNumber,
    Violation.SectionCode AS Statute,
    Violation.Descr AS Charge,
    CasePerson.LastName as DefLastName,
    CasePerson.FirstName as DefFirstName,
    CasePerson.MiddleName as DefMiddleName,
    CasePerson.Suffix as DefSuffix
    FROM [AuthorityCourt].[dbo].[CaseMaster]
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[SubCase]
    ON CaseMaster.Id = SubCase.CaseMasterID
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[Violation]
    ON SubCase.ViolationId = Violation.Id
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[CasePerson]
    ON CasePerson.CaseMasterID = SubCase.CaseMasterID and CasePerson.PersonTypeID = '1'
    WHERE CaseNumber = '{case_number}'
    """


if __name__ == '__main__':
    logger.log('IMPORT', f'{__name__} run directly.')
else:
    logger.log('IMPORT', f'{__name__} imported.')
