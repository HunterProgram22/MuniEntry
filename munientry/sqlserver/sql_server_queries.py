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
	cm.InsuranceStatus AS FraInFile,
	vd.IsMoving AS MovingBool,
    CONCAT(att.FirstName, ' ', att.LastName) AS DefenseCounsel,
    IIF (sc.AttorneyTypeID = '476', 1,0) AS PubDef

    FROM [AuthorityCourt].[dbo].[CaseMaster] cm
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[SubCase] sc
    ON cm.Id = sc.CaseMasterID and sc.IsDeleted = '0'
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


def driving_case_search_query(case_number: str) -> str:
    return f"""
    SELECT DISTINCT cm.CaseNumber,
      cp.LastName as DefLastName,
      cp.FirstName as DefFirstName,
      cp.MiddleName as DefMiddleName,
      cp.Suffix as DefSuffix,
	  FORMAT (cp.BirthDate, 'd','us') as DefBirthDate,
      ti.DefendantCity as DefCity,
      ti.DefendantState as DefState,
      ti.DefendantZip as DefZipcode,
      ti.DefendantPresentAddress as DefAddress,
      ti.DefendantDLNumber as DefLicenseNumber,
      cp.AddressLine1 as CaseAddress,
      cp.City as CaseCity,
--       cp.StateID as CaseState,
      cd.Code as CaseState,
      cp.ZipCode as CaseZipcode

    FROM [AuthorityCourt].[dbo].[CaseMaster] cm
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[SubCase] sc
    ON cm.Id = sc.CaseMasterID
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[CasePerson] cp
    ON cp.CaseMasterID = sc.CaseMasterID and cp.PersonTypeID = '1'
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[TicketImport] ti
    ON cp.LastName = ti.DefendantLastName AND cp.FirstName = ti.DefendantFirstName
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[Codes] cd
    ON cd.Id = cp.StateID
    WHERE CaseNumber='{case_number}'
    """


def event_type_report_query(report_date: str, event_codes: str) -> str:
    return f"""
    SELECT DISTINCT
    FORMAT(ce.EventTime, 'hh:mm') as Time
    ,cm.CaseNumber
	,cp.FirstName + ' ' + cp.LastName as DefFullName
	,sc.SubCaseNumber
    ,sc.ChargeDescription AS Charge
    ,EventID
    ,sc.JudgeID as JudgeID
    ,CONCAT(att.FirstName, ' ', att.LastName) AS DefenseCounsel
    FROM [AuthorityCourt].[dbo].[CaseMaster] cm
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[CaseEvent] ce 
    ON cm.Id = ce.CaseMasterID and ce.IsDeleted = '0'
	LEFT OUTER JOIN [AuthorityCourt].[dbo].[SubCase] sc
    ON cm.Id = sc.CaseMasterID
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[Violation] v
    ON sc.ViolationId = v.Id
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[ViolationDetail] vd
    ON vd.ViolationID = v.Id and vd.EndDate IS NULL and vd.IsActive = '1'
	LEFT OUTER JOIN [AuthorityCourt].[dbo].[CasePerson] cp
	ON cp.CaseMasterID = sc.CaseMasterID 
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[Attorney] att
    ON sc.AttorneyID = att.Id
    WHERE EventID in {event_codes} and EventDate = '{report_date}' and SubCaseNumber LIKE '%-A'
    """


def get_case_docket_query(case_number: str) -> str:
    return f"""
    SELECT
    de.Date,
    de.Remark
    FROM [AuthorityCourt].[dbo].[CaseMaster]cm
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[Docket]d
    ON cm.Id = d.CaseMasterID
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[DocketEntry]de
    ON d.Id = de.DocketId
    WHERE CaseNumber = '{case_number}'
    ORDER BY de.Date
    """


def daily_case_list_query(report: str) -> str:
    return f"""
        USE [AuthorityCourt]
        DECLARE	@return_value int
        EXEC	@return_value = {report}
        SELECT	'Return Value' = @return_value;
    """


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')