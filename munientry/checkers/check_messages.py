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

Click the Add Conditions button to add details, or uncheck the {0} box if there is no {0} in this \
case."""

DEF_COUNSEL_TITLE = 'Does Defendant Have Counsel?'
DEF_COUNSEL_MSG = """There is no attorney selected for the Defendant.

Did the Defendant appear without counsel or waive his right to counsel?

If you select No you must enter a name for Defense Counsel."""

INSURANCE_TITLE = 'Was Insurance Shown in Court?'
INSURANCE_MSG = """The information provided currently indicates that insurance was \
not shown at the time of the offense.

Did the defendant show proof of insurance in Court?"""

BOND_REQUIRED_TITLE = 'Bond Amount Required'
BOND_REQUIRED_MSG = """The bond type that was selected requires that you set an amount of bond.

Please specify a bond amount other than None."""

BOND_AMOUNT_TITLE = 'Improper Bond Type Selected'
BOND_AMOUNT_MSG = """An amount for bond was selected, but the bond type selected does not permit
a bond amount.

Please either change the bond type to 10% Deposit Bond, or a Cash or Surety Bond, \
or set the bond amount to None."""

BOND_MODIFICATION_TITLE = 'Bond Modification Decision Required'
BOND_MODIFICATION_MSG = """A decision on the bond modification motion was not selected.

Please choose an option from the Decision on Bond box."""

DV_BOND_TITLE = 'Domestic Violence Bond Condition Not Set'
DV_BOND_MSG = """The Special Condition Domestic Violence Restrictions is checked, but the details 
of the Domestic Violence Restrictions have not been selected.

Click the Add Conditions button to add details, or uncheck the Domestic Violence Restrictions box \
if there are no restrictions in this case."""

MISSING_PLEA_TITLE = 'Plea Required for Offense'
MISSING_PLEA_MSG = 'You must enter a plea for {0}.'

MISSING_FINDING_TITLE = 'Finding Required for Offense'
MISSING_FINDING_MSG = 'You must enter a finding for {0}.'

EXCESS_JAIL_SUSP_TITLE = 'Suspended Jail Days Exceeds Jail Days Imposed'
EXCESS_JAIL_SUSP_MSG = """The total number of jail days suspended is {0}, which exceeds the total \
jail days imposed in the case of {1}.

Please adjust the jail days suspended or the jail days imposed."""

EXCESS_JAIL_CREDIT_TITLE = 'Excessive Jail Credit Entered'
EXCESS_JAIL_CREDIT_MSG = """The Defendant is set to have {0} days of jail time credit applied to a \
sentence, but a total of only {1} jail days are set to be imposed in the case. The total jail days \
imposed is less than the jail time credit that is being applied to the sentence.

Please impose additional jail days or change the Apply JTC to box to Costs and Fines."""

JAIL_DAYS_REQUIRED_TITLE = 'Days in Jail is Required'
JAIL_DAYS_REQUIRED_MSG = """The Jail Credit and Reporting box indicates the Defendant is currently \
in jail, but the number of Days in Jail is blank.

Please enter the number of Days in Jail and select whether to apply the Jail Time Credit to \
Sentence or Costs and Fines."""

JAIL_SET_NO_JAIL_TITLE = 'Turn Off Report to Jail?'
JAIL_SET_NO_JAIL_MSG = """The total jail days imposed is equal to the total jail days \
suspended and total jail time credit. 

The Defendant does not appear to have any jail days left to serve but the Jail Reporting Terms \
are set. 

Press 'Yes' if the Defendant should report to jail, or press 'No' and the Jail Reporting Terms \
will be unchecked.'"""

