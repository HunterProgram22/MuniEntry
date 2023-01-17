import types

### Authority Court Database Event Codes and Ids ###

# Arraignment (ARR) - 27, Arraignment (ARRV) - 28
# Continuance Arraignment (CONA) - 77
# Reset Case Arraignment (RSET) - 361
ARRAIGNMENT_EVENT_IDS = "('27', '28', '77', '361')"

# Final Pretrial A (FPTN2 - 160, Final Pretrial B (FPT2NB - 161
# 334 and 335 is Pretrial/ALS for A
# 336 and  is a Pretrial/ALS for B
FINAL_PRETRIAL_EVENT_IDS = "('160', '161', '334', '335', '336', '337')"

# Trial to Court A (TCN) - 412
# Trial to Court B (TCNB) - 413
# Trial to Court C (TCNC) - 414
TRIAL_TO_COURT_EVENT_IDS = "('412', '413', '414')"

# Plea in A - 292, Plea in B - 293, Plea in C - 294
PLEA_EVENT_IDS = "('292', '293', '294')"

# Jury Trial in A - 201, Jury Trial in B - 202
JURY_TRIAL_EVENT_IDS = "('201', '202')"

######


EVENT_IDS = types.MappingProxyType({
    'Arraignments': ARRAIGNMENT_EVENT_IDS,
    'Final Pretrials': FINAL_PRETRIAL_EVENT_IDS,
    'Trials To Court': TRIAL_TO_COURT_EVENT_IDS,
    'Pleas': PLEA_EVENT_IDS,
    'Jury Trials': JURY_TRIAL_EVENT_IDS,
})
