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
    IIF (sc.AttorneyTypeID = '476', 1, 0) AS PubDef

	FROM [AuthorityCourt].[dbo].[CaseMaster] cm
	JOIN [AuthorityCourt].[dbo].[SubCase] sc
    ON cm.Id = sc.CaseMasterID
	JOIN [AuthorityCourt].[dbo].[Violation] v
    ON sc.ViolationId = v.Id
	JOIN [AuthorityCourt].[dbo].[ViolationDetail] vd
    ON v.Id = vd.ViolationID
	JOIN [AuthorityCourt].[dbo].[Degree] d
    ON vd.DegreeID = d.Id
	JOIN [AuthorityCourt].[dbo].[CasePerson] cp
    ON cm.Id = cp.CaseMasterID
	LEFT JOIN [AuthorityCourt].[dbo].[Attorney] att
    ON sc.AttorneyID = att.Id
    
	WHERE cm.CaseNumber = '{case_number}' AND sc.IsDeleted = '0' 
	ORDER BY SubCaseNumber
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


def general_civil_case_query(case_number: str) -> str:
    return f"""
    SELECT 
        LTRIM(RTRIM([c_CaseNumber_str])) AS CaseNumber,
	    [p_IsIndividualFlag_str],
	    CASE
			WHEN [p_IsIndividualFlag_str] = 'Y' 
				THEN LTRIM(RTRIM([p_FirstName_str])) + SPACE(1) + LTRIM(RTRIM([p_LastName_str])) 
			ELSE LTRIM(RTRIM([p_BusinessName1_str] ))
		END AS PartyName,
	    CASE
			WHEN [c_PrimaryPlaintiffFK_int] = [cp_CaseParticipantPK_int] 
				THEN 'Plaintiff'
			WHEN [c_PrimaryDefendantFK_int] = [cp_CaseParticipantPK_int] 
				THEN 'Defendant'
			ELSE 'Non-Primary Party'
		END as PartyType

	FROM [AuthorityCivil].[dbo].[Case] AS c
	LEFT OUTER JOIN [AuthorityCivil].[dbo].[CaseParticipants] AS cp
	ON [c_PrimaryDefendantFK_int] = [cp_CaseParticipantPK_int] or [c_PrimaryPlaintiffFK_int] = [cp_CaseParticipantPK_int]
	LEFT OUTER JOIN [AuthorityCivil].[dbo].[Participants] AS p
	ON [cp_ParticipantFK_int] = [p_ParticipantPK_int]

	WHERE c.c_CaseNumber_str = '{case_number}' 
    """


def batch_fta_query(event_date: str, next_day: str) -> str:
    return f"""
    SELECT DISTINCT cm.CaseNumber 
    FROM [AuthorityCourt].[dbo].[CaseMaster] cm
    LEFT JOIN [AuthorityCourt].[dbo].[SubCase] sc ON cm.Id = sc.CaseMasterID
    LEFT JOIN [AuthorityCourt].[dbo].[Violation] v ON sc.ViolationId = v.Id
    LEFT JOIN [AuthorityCourt].[dbo].[ViolationDetail] vd ON vd.ViolationID = v.Id AND vd.EndDate IS NULL AND vd.IsActive = '1'
    LEFT JOIN [AuthorityCourt].[dbo].[ChargeDetail] cd ON v.ChargeID = cd.ChargeId
    WHERE EXISTS (
        SELECT 1
        FROM [AuthorityCourt].[dbo].[CaseMaster] cm2
        RIGHT JOIN [AuthorityCourt].[dbo].[CaseEvent] ce ON cm2.Id = ce.CaseMasterID
        WHERE ce.EventID IN ('27', '28', '77', '263', '361', '474') AND CAST(ce.EventDate AS DATE) = '{event_date}'
        AND cm.CaseNumber = cm2.CaseNumber AND cm.CaseStatusID = '1' AND ce.IsDeleted = '0' AND (vd.IsMandAppear = '1' OR cm.CaseType = '3')
    )
    AND NOT EXISTS (
        SELECT 1
        FROM [AuthorityCourt].[dbo].[CaseEvent] ce
        WHERE ce.CaseMasterID = cm.Id AND CAST(ce.EventDate AS DATE) >= '{next_day}'
    )
    ORDER BY cm.CaseNumber
"""


if __name__ == '__main__':
    logger.info(f'{__name__} run directly.')
