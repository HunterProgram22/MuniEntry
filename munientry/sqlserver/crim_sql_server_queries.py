"""Module containing all Criminal SQL Server queries used throughout the application."""


def general_case_search_query(case_number: str) -> str:
    return f"""
   DROP TABLE IF EXISTS #MuniEntrySelect

    SELECT
        sc.SubCaseNumber,
        cm.CaseNumber,
        sc.Id AS SubCaseID,
        sc.ChargeDescription AS Charge,
        v.Id AS ViolationID,
        vd.Id AS ViolationDetailID,
        v.SectionCode AS Statute,
        v.IsActive as VIsActive,
        vd.IsActive as VDIsActive,
        d.DegreeCode,
        cp.FirstName AS DefFirstName,
        cp.LastName AS DefLastName,
        vd.IsMoving AS MovingBool,
        sc.ViolationDate,
        vd.EndDate,
        cm.InsuranceStatus AS FraInFile,
        CONCAT(att.FirstName, ' ', att.LastName) AS DefenseCounsel,
        IIF (sc.AttorneyTypeID = '476', 1, 0) AS PubDef,
        ROW_NUMBER() over(partition by sc.id order by sc.subcasenumber asc) as RowNumber

    INTO #MuniEntrySelect

    FROM [AuthorityCourt].[dbo].[CaseMaster] cm
        JOIN [AuthorityCourt].[dbo].[SubCase] sc ON cm.Id = sc.CaseMasterID
        JOIN [AuthorityCourt].[dbo].[Violation] v ON sc.ViolationId = v.Id
        JOIN [AuthorityCourt].[dbo].[ViolationDetail] vd ON v.Id = vd.ViolationID
        JOIN [AuthorityCourt].[dbo].[Degree] d ON vd.DegreeID = d.Id
        JOIN [AuthorityCourt].[dbo].[CasePerson] cp ON cp.CaseMasterID = cm.Id
        LEFT JOIN [AuthorityCourt].[dbo].[Attorney] att ON sc.AttorneyID = att.Id

    WHERE 
        cm.CaseNumber = '{case_number}'
        AND sc.IsDeleted = '0' 
        AND cp.PersonTypeID = '1'
        AND (vd.EndDate is NULL OR vd.EndDate >= sc.ViolationDate)

    Select * from #MuniEntrySelect
    WHERE RowNumber = 1
    ORDER BY SubCaseNumber ASC
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


def batch_fta_query(event_date: str, next_day: str) -> str:
    """Queries the database for arraignment cases for the event date and filters those cases.

    The Arraignment Cases are filtered by removing any cases that do not have a case event after
    arraignment, or are not in finished case status.

    Arraignment Codes: (27, 28, 77, 263, 361, 474).

    The query selects from the pending cases those that meet the critera for an FTA warrant, which
    is the following:
    1. Mandatory Appearance Cases
    2. Criminal Cases
    3. Traffic Cases that are not mandatory appear, but defebdabt has an out-of-state license from a
    non-compact state (MI, TN, GA, MA, WI, NV), or is a Commercial Vehicle (CDL) or is a No OL
    offense so license can't be canceled.
    """
    return f"""
    WITH ArraignmentCases AS (
    SELECT cm2.CaseNumber
    FROM [AuthorityCourt].[dbo].[CaseMaster] cm2
    JOIN [AuthorityCourt].[dbo].[CaseEvent] ce ON cm2.Id = ce.CaseMasterID
    WHERE ce.EventID IN ('27', '28', '77', '263', '361', '474')
        AND CAST(ce.EventDate AS DATE) = '{event_date}'
        AND cm2.CaseStatusID = '1'
        AND ce.IsDeleted = '0'
    ),
    PendingCases AS (
        SELECT cm.*
        FROM [AuthorityCourt].[dbo].[CaseMaster] cm
        JOIN ArraignmentCases ac ON cm.CaseNumber = ac.CaseNumber
        WHERE NOT EXISTS (
            SELECT 1
            FROM [AuthorityCourt].[dbo].[CaseEvent] ce
            WHERE ce.CaseMasterID = cm.Id AND CAST(ce.EventDate AS DATE) >= '{next_day}'
        )
    )
    SELECT DISTINCT
        pc.CaseNumber
    FROM PendingCases pc
    LEFT JOIN [AuthorityCourt].[dbo].[SubCase] sc ON pc.Id = sc.CaseMasterID
    LEFT JOIN [AuthorityCourt].[dbo].[Violation] v ON sc.ViolationId = v.Id
    LEFT JOIN [AuthorityCourt].[dbo].[ViolationDetail] vd ON vd.ViolationID = v.Id AND vd.EndDate IS NULL AND vd.IsActive = '1'
    LEFT JOIN [AuthorityCourt].[dbo].[CasePerson] cp ON cp.CaseMasterID = sc.CaseMasterID
    WHERE vd.IsMandAppear = '1'
        OR pc.CaseType = '3'
        OR (pc.CaseType = '9' AND cp.StateIdIssuingStateID in ('19229', '19240', '19241', '19247', '19261', '19268'))
        OR (pc.CaseType = '9' and pc.IsCommercialVehicle = '1')
        OR (pc.CaseType = '9' AND v.Id = '12368')
    ORDER BY pc.CaseNumber;
"""


def not_guilty_report_query(event_date: str) -> list[tuple]:
    return f"""
    SELECT DISTINCT
    cm.CaseNumber
	,cp.FirstName + ' ' + cp.LastName as DefFullName
	,de.Remark
    FROM [AuthorityCourt].[dbo].[CaseMaster] cm
	JOIN [AuthorityCourt].[dbo].[SubCase] sc
    ON cm.Id = sc.CaseMasterID
    LEFT OUTER JOIN [AuthorityCourt].[dbo].[CaseEvent] ce 
    ON cm.Id = ce.CaseMasterID
	LEFT OUTER JOIN [AuthorityCourt].[dbo].[Docket]d
	ON cm.Id = d.CaseMasterID
	LEFT OUTER JOIN [AuthorityCourt].[dbo].[DocketEntry]de
	ON d.Id = de.DocketID
	LEFT OUTER JOIN [AuthorityCourt].[dbo].[CasePerson] cp
	ON cp.CaseMasterID = sc.CaseMasterID 
	
    WHERE ce.EventID in ('27', '28', '77', '263', '361', '474') 
    AND ce.EventDate = '{event_date}' 
    AND de.Remark LIKE '%JOURNAL%' AND (de.Remark LIKE '%PLED%' or de.Remark LIKE '%CONTINUED%') 
    AND de.Date = '{event_date}' 
    AND cp.PersonTypeID = '1'
    """
