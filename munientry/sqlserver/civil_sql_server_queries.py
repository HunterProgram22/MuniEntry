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
