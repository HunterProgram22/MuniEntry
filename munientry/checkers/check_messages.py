"""Message constants for dialog check lists."""

TRIAL_FUTURE_TITLE = 'Must Set Trial Date in Future'
TRIAL_FUTURE_MSG = """The Trial Date is Today, but must be a date in the future.

Please enter a date in the Trial Date box after today."""

FINAL_FUTURE_TITLE = 'Must Set Final PreTrial Date in Future'
FINAL_FUTURE_MSG = """The Final PreTrial Date is Today, but must be a date in the future.

Please enter a date in the Final PreTrial Date box after today."""

PLEA_PAST_TITLE = 'Must Set Plea Date in the Past'
PLEA_PAST_MSG = """The Plea Date is Today, but must be a date prior to Today.

Please enter a date in the Plea Date box prior to today."""

LEAP_PAST_TITLE = 'Must Set LEAP Plea Date in the Past'
LEAP_PAST_MSG = """The Leap Plea Date is Today, but must be a date prior to Today.

Please enter a date in the Leap Plea Date box prior to today."""

DIVERSION_SET_TITLE = 'Must Select a Diversion Program'
DIVERSION_SET_MSG = """No Diversion program was selected.

Please select one of the Diversion programs to proceed."""

ADD_CONDITIONS_TITLE = 'Additional Condition Not Set'
ADD_CONDITIONS_MSG = """The additional condition {0} is checked, but the details of
the {0} have not been entered.

Click the Add Conditions button to add details, or uncheck the {0} box if there is no {0} in this
case."""

DEF_COUNSEL_TITLE = 'Does Defendant Have Counsel?'
DEF_COUNSEL_MSG = """There is no attorney selected for the Defendant.

Did the Defendant appear without counsel or waive his right to counsel?

If you select No you must enter a name for Defense Counsel."""

INSURANCE_TITLE = 'Was Insurance Shown in Court?'
INSURANCE_MSG = """The information provided currently indicates that insurance was 
not shown at the time of the offense.

Did the defendant show proof of insurance in Court?"""

BOND_REQUIRED_TITLE = 'Bond Amount Required'
BOND_REQUIRED_MSG = """The bond type that was selected requires that you set an amount of bond.

Please specify a bond amount other than None."""

BOND_AMOUNT_TITLE = 'Improper Bond Type Selected'
BOND_AMOUNT_MSG = """An amount for bond was selected, but the bond type selected does not permit
a bond amount.

Please either change the bond type to 10% Deposit Bond, or a Cash or Surety Bond, 
or set the bond amount to None."""