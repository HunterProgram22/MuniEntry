"""Module containing all SQL Server queries used throughout the application."""
from loguru import logger


def general_case_search_query(case_number: str) -> str:
    return f"""
    SELECT DISTINCT
    sc.Id AS SubCaseID,
    v.Id AS ViolationID,
    cm.CaseNumber,
    sc.SubCaseNumber,
    v.SectionCode AS Statute,
    sc.ChargeDescription AS Charge,
    d.DegreeCode,
	cp.FirstName AS DefFirstName,
	cp.LastName AS DefLastName,
    CONCAT(att.FirstName, ' ', att.LastName) as DefenseCounsel,
    IIF (sc.AttorneyTypeID = '476', 1,0) AS PubDef

    FROM [AuthorityCourt].[dbo].[CaseMaster] cm
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[SubCase] sc
    ON cm.Id = sc.CaseMasterID
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[Violation] v
    ON sc.ViolationId = v.Id
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[ViolationDetail] vd
    ON vd.ViolationID = v.Id and vd.EndDate IS NULL and vd.IsActive = '1'
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[Degree] d
    ON d.Id = vd.DegreeID
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[Attorney] att
    ON sc.AttorneyID = att.Id
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[CasePerson] cp
    ON cp.CaseMasterID = sc.CaseMasterID and cp.PersonTypeID = '1'
    WHERE CaseNumber = '{case_number}'
    """


if __name__ == "__main__":
    logger.log("IMPORT", f"{__name__} run directly.")
else:
    logger.log("IMPORT", f"{__name__} imported.")
