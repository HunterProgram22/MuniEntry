"""Module containing all SQL Server queries used throughout the application."""
from loguru import logger

def general_case_search_query(case_number: str) -> str:
    return f"""
    SELECT
    sc.Id AS SubCaseID,
    v.Id AS ViolationID,
    CaseMaster.CaseNumber,
    sc.SubCaseNumber,
    cp.LastName as DefLastName,
    cp.FirstName as DefFirstName,
    cp.MiddleName as DefMiddleName,
    cp.Suffix as DefSuffix

    FROM [AuthorityCourt].[dbo].[CaseMaster]
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[SubCase] sc
    ON CaseMaster.Id = sc.CaseMasterID
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[Violation] v
    ON sc.ViolationId = v.Id
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[CasePerson] cp
    ON cp.CaseMasterID = sc.CaseMasterID and cp.PersonTypeID = '1'
    WHERE CaseNumber = '{case_number}'
    """