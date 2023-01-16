

def get_comment_writer(event):
    if event == 'Arraignments':
        return ArraignmentComments()
    elif event == 'Final Pretrials':
        return FinalPretrialComments()


class ArraignmentComments(object):

    def get_comment(self, query) -> str:
        event = query.value('EventID')
        judge = query.value('JudgeID')
        match (event, judge):
            case (27, 0) | (28, 0):
                return 'Arraignment'
            case (77, 0):
                return 'Arraignment - Previously Continued'
            case (361, 0):
                return 'Arraignment - Reset due to FTA or Other Reason'
            case _:
                return 'Unclassified Possible Data Error in Case'


class FinalPretrialComments(object):

    def get_comment(self, query) -> str:
        event = query.value('EventID')
        judge = query.value('JudgeID')
        match (event, judge):
            case (160, 42):  # Final pretrial for Judge H listed in Courtroom A
                return 'Possible Data Issue - Judge Hemmeter assigned, FPT in CMI is set for Courtroom A'
            case (161, 42):  # Final pretrial for Judge H listed in Courtroom B
                return 'Courtroom B'
            case (334, 42) | (335, 42) | (336, 42) | (337, 42):  # Pretrial/ALS code likely should be Final pretrial code
                return 'Possible Data Issue - Event in CMI is Pretrial/ALS - Should likely be FPTN2B'
            case (160, 31):  # Final pretrial for Judge R listed in Courtroom A
                return 'Courtroom A'
            case (161, 31):  # Final pretrial for Judge R listed in Courtroom B
                return 'Possible Data Issue - Judge Rohrer assigned, FPT in CMI is set for Courtroom B'
            case _:
                return 'Unclassified Possible Data Error in Case'




def get_comment_field(query) -> str:
    event = query.value('EventID')
    judge = query.value('JudgeID')  # Judge Rohrer = 31, Judge Hemmeter = 42
    match (event, judge):

        case (334, 31) | (335, 31) | (336, 31) | (337 | 31):  # Pretrial/ALS code likely should be Final pretrial code
            return 'Possible Data Issue - Event in CMI is Pretrial/ALS - Should likely be FPTN2'
        case (414, 31) | (414, 42):  # Trial to Court in C with Judge Assigned
            return 'Courtroom C'
        case (414, 0) | (414, 0):  # Trial to Court in C with No Judge Assigned
            return 'Trial to Court in C but No Judge Assigned'
        case (412, 31):  # Trial to Court in A with Judge Rohrer Assigned
            return 'Courtroom A - Trial to Court with Judge Rohrer'
        case (413, 42):  # Trial to Court in B with Judge Hemmeter Assigned
            return 'Courtroom B - Trial to Court with Judge Hemmeter'
        case (160, 0) | (161, 0):
            return 'No Judge Assigned to Case'
        case (292, 31):  # Plea for Judge Rohrer listed in Courtroom A
            return 'Courtroom A'
        case (293, 31):  # Plea for Judge Rohrer listed in Courtroom B
            return 'Possible Data Issue - Judge Rohrer Assigned, Plea in CMI is set for Courtroom B'
        case (293, 42):  # Plea for Judge Hemmeter listed in Courtroom B
            return 'Courtroom B'
        case (292, 42):  # Plea for Judge Hemmeter listed in Courtroom A
            return 'Possible Data Issue - Judge Hemmeter Assigned, Plea in CMI is set for Courtroom A'
        case (294, 42) | (294, 31):  # Plea for either judge listed in Courtroom C
            return 'Possible Data Issue - Plea in CMI is set for Courtroom C and a Judge is Assigned'
        case (294, 0):  # Plea for no judge listed in Courtroom C
            return 'Plea in C - No Judge Assigned'
        case _:
            return 'Unclassified Possible Data Error in Case'
