"""Module for generating the comments for various reports."""
from abc import ABC, abstractmethod

NO_MATCH = 'Unclassified Possible Data Error in Case'


def get_comment_writer(event: str) -> object:
    """Returns an instance of a comment writer object based on the given event.

    Args:
        event (str): The name of the event for which to get the comment writer.

    Returns:
        An instance of a comment writer object corresponding to the given event. If the event does
        not match any of the defined events, a GeneralComments object is returned.
    """
    comment_writer = {
        'Arraignments': ArraignmentComments,
        'Final Pretrials': FinalPretrialComments,
        'Pleas': PleaComments,
        'Trials To Court': TrialToCourtComments,
        'Jury Trials': JuryTrialComments,
    }
    return comment_writer.get(event, GeneralComments)()


class BaseComment(ABC):
    """Abstract base class for generating comments for the comment field in reports."""

    no_judge = 0    # No Judge Assigned
    judge_ker = 31  # (KER) Judge Rohrer JudgeID
    judge_mth = 42  # (MTH) Judge Hemmeter JudgeID

    def get_comment(self, query) -> str:
        event = query.value('EventID')
        judge = query.value('JudgeID')
        return self.match_event_judge(event, judge)

    @abstractmethod
    def match_event_judge(self, event: int, judge: int) -> str:
        """Abstract method for matching event and judge codes."""


class ArraignmentComments(BaseComment):
    """Comments specific for Arraignments report."""

    arr = 27        # (ARR) Arraignment
    arrv = 28       # (ARRV) Arraignment
    cona = 77       # (CONA) Continuance Arraignment
    rest = 361      # (RSET) Reset Case Arriagnment
    cona_i = 474    # (CONA-I) Continuance Arriagnment Interpreter

    def match_event_judge(self, event: int, judge: int) -> str:
        match (event, judge):
            case (self.arr, _) | (self.arrv, _):
                comment = 'Arraignment'
            case (self.cona, _):
                comment = 'Arraignment - Previously Continued'
            case (self.rest, _):
                comment = 'Arraignment - Reset due to FTA or Other Reason'
            case (self.cona_i, _):
                comment = 'Arraignment - Previously Continued for Interpreter'
            case _:
                comment = NO_MATCH
        return comment


class FinalPretrialComments(BaseComment):
    """Comments specific for Final Pretrials report."""

    fptn2 = 160         # (FPTN2) Final Pretrial Courtroom A
    fptn2b = 161        # (FPTN2B) Final Pretrial Courtroom B
    ptn = 334           # (PTN) Pretrial/ALS Appeal Courtroom A
    ptn2 = 335          # (PTN2) Pretrial/ALS Appeal Courtroom A
    ptn2b = 336         # (PTN2B) Pretrial/ALS Appeal Courtroom B
    ptnb = 337          # (PTNB) Pretrial/ALS Appeal Courtroom B

    def match_event_judge(self, event: int, judge: int) -> str:
        match (event, judge):
            case (self.fptn2, self.judge_mth):
                comment = 'Data Issue: Judge Hemmeter assigned, FPT in CMI set for Courtroom A'
            case (self.fptn2b, self.judge_mth):
                comment = 'Courtroom B'
            case (
                (self.ptn, self.judge_mth) | (self.ptn2, self.judge_mth)
                | (self.ptn2b, self.judge_mth) | (self.ptnb, self.judge_mth),
            ):
                comment = 'Data Issue: Event in CMI is Pretrial/ALS - Check if should be FPTN2B'
            case (self.fptn2, self.judge_ker):
                comment = 'Courtroom A'
            case (self.fptn2b, self.judge_ker):
                comment = 'Data Issue: Judge Rohrer assigned, FPT in CMI is set for Courtroom B'
            case (
                (self.ptn, self.judge_ker) | (self.ptn2, self.judge_ker)
                | (self.ptn2b, self.judge_ker) | (self.ptnb | self.judge_ker),
            ):
                comment = 'Data Issue: Event in CMI is Pretrial - Check if should be FPTN2'
            case (self.fptn2, self.no_judge) | (self.fptn2b, self.no_judge):
                comment = 'No Judge Assigned to Case'
            case _:
                comment = NO_MATCH
        return comment


class PleaComments(BaseComment):
    """Comments specific for Pleas report."""

    phn = 292       # (PHN) Plea Hearing in Courtroom A
    phnb = 293      # (PHNB) Plea Hearing in Courtroom B
    phnc = 294      # (PHNC) Plea Hearing in Courtroom C

    def match_event_judge(self, event: int, judge: int) -> str:
        match (event, judge):
            case (self.phn, self.judge_ker):
                comment = 'Courtroom A'
            case (self.phnb, self.judge_ker):
                comment = 'Data Issue: Judge Rohrer Assigned, Plea in CMI is set for Courtroom B'
            case (self.phnb, self.judge_mth):
                comment = 'Courtroom B'
            case (self.phn, self.judge_mth):
                comment = 'Data Issue: Judge Hemmeter Assigned, Plea in CMI is set for Courtroom A'
            case (self.phnc, self.judge_mth) | (self.phnc, self.judge_ker):
                comment = 'Data Issue - Plea in CMI is set for Courtroom C and a Judge is Assigned'
            case (self.phnc, self.no_judge):
                comment = 'Plea in C - No Judge Assigned'
            case _:
                comment = NO_MATCH
        return comment


class TrialToCourtComments(BaseComment):
    """Comments specific for Trials to Court report."""

    tcn = 412       # (TCN) Trial to Court in Courtroom A
    tcnb = 413      # (TCNB) Trial to Court in Courtroom B
    tcnc = 414      # (TCNC) Trial to Court in Courtroom C

    def match_event_judge(self, event: int, judge: int) -> str:
        match (event, judge):
            case (self.tcnc, self.judge_ker) | (self.tcnc, self.judge_mth):
                comment = 'Courtroom C'
            case (self.tcnc, self.no_judge):
                comment = 'Trial to Court in C but No Judge Assigned'
            case (self.tcn, self.judge_ker):
                comment = 'Courtroom A - Trial to Court with Judge Rohrer'
            case (self.tcnb, self.judge_mth):
                comment = 'Courtroom B - Trial to Court with Judge Hemmeter'
            case _:
                comment = NO_MATCH
        return comment


class JuryTrialComments(BaseComment):
    """Comments specific for Jury Trials report."""

    jtn = 201       # (JTN) Jury Trial in Courtroom A
    jtnb = 202      # (JTNB) Jury Trial in Courtroom B

    def match_event_judge(self, event: int, judge: int) -> str:
        match (event, judge):
            case (self.jtn, self.judge_ker):
                comment = 'Courtroom A'
            case (self.jtn, self.judge_mth):
                comment = 'Data Issue: Judge Hemmeter assigned, CMI has Trial set in Courtroom A'
            case (self.jtnb, self.judge_mth):
                comment = 'Courtroom B'
            case (self.jtnb, self.judge_ker):
                comment = 'Data Issue: Judge Rohrer assigned, CMI has Trial set in Courtroom B'
            case _:
                comment = NO_MATCH
        return comment


class GeneralComments(BaseComment):
    """Default comments for reports that do not have a specific comment writer object."""

    def match_event_judge(self, event: int, judge: int) -> str:
        match (event, judge):
            case _:
                comment = NO_MATCH
        return comment
