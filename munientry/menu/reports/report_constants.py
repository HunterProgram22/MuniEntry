import types

# Authority Court Database Event Codes

# Arraignment - 27, Arraignment - 28, Continuance Arraignment - 77, Reset Case Arraignment - 361
ARRAIGNMENT_EVENT_IDS = "('27', '28', '77', '361')"

# Final Pretrial A - 160, Final Pretrial B - 161, 335 is Pretrial/ALS for A, 336 is a Pretrial/ALS for B
FINAL_PRETRIAL_EVENT_IDS = "('160', '161', '334', '335', '336', '337')"

# Trial to Court A (TCN) - 412, Trial to Court B (TCNB) - 413, Trial to Court C (TCNC) 414
TRIAL_TO_COURT_EVENT_IDS = "('412', '413', '414')"

# Plea in A - 292, Plea in B - 293, Plea in C - 294
PLEA_EVENT_IDS = "('292', '293', '294')"


EVENT_IDS = types.MappingProxyType({
    'Arraignments': ARRAIGNMENT_EVENT_IDS,
    'Final Pretrials': FINAL_PRETRIAL_EVENT_IDS,
    'Trials To Court': TRIAL_TO_COURT_EVENT_IDS,
    'Pleas': PLEA_EVENT_IDS,
})
