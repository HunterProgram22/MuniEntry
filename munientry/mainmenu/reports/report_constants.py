import types

### Authority Court Database Event Codes and Ids ###

# Arraignment (arr) - 27, Arraignment (arrv) - 28
# Continuance Arraignment (cona) - 77, 474
# Reset Case Arraignment (rest) - 361
ARRAIGNMENT_EVENT_IDS = "('27', '28', '77', '361', '474')"

# Final Pretrial A (FPTN2 - 160, 477) Final Pretrial B (FPT2NB - 161, 478)
# 334 and 335 is Pretrial/ALS for A
# 336 and  is a Pretrial/ALS for B
FINAL_PRETRIAL_EVENT_IDS = "('160', '161', '334', '335', '336', '337', '477', '478')"

# Trial to Court A (TCN) - 412, 492
# Trial to Court B (TCNB) - 413, 493
# Trial to Court C (TCNC) - 414, 494
TRIAL_TO_COURT_EVENT_IDS = "('412', '413', '414', '492', '493', '494')"

# Plea in A - 292, 486 Plea in B - 293,, 487 Plea in C - 294, 488
PLEA_EVENT_IDS = "('292', '293', '294', '486', '487', '488')"

# Jury Trial in A - 201, 479 Jury Trial in B - 202, 480
JURY_TRIAL_EVENT_IDS = "('201', '202', '479', '480')"

######


EVENT_IDS = types.MappingProxyType({
    'Arraignments': ARRAIGNMENT_EVENT_IDS,
    'Final Pretrials': FINAL_PRETRIAL_EVENT_IDS,
    'Trials To Court': TRIAL_TO_COURT_EVENT_IDS,
    'Pleas': PLEA_EVENT_IDS,
    'Jury Trials': JURY_TRIAL_EVENT_IDS,
})



### MuniEntry Sqllite DB Constants ###

COURTROOM_REPORT_HEADERS = ('Event', 'Time', 'Case Number', 'Defendant Name')

COURTROOM_NAME = types.MappingProxyType({
    1: 'A',
    2: 'B',
    3: 'C',
})

### End MuniEntry Sqllite DB Constants ###
