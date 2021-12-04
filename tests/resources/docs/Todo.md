APPLICATION TODO LIST for version 0.4.0
* Updated dialogs/templates for Not Guilty per AB Notes.
* Add Warning if add condition boxes are checked but conditions have not been added.


GENERAL PERIODIC CLEANUP
* Move general methods to helper functions
* Remove magic numbers throughout - Look to check_plea_and_findings method as an example.
* Add new tests - fix test amend offense because button is now in grid.


FEATURE/CHANGE LIST - for Version 0.5.0
* Add DUI sub-dialog
* Make statutes hyperlink
* Updated dialogs/templates for FTA per AB Notes.
* Add community control conditions checkboxes
* Add Jail entries
* Add Yellow Sheet templates (CC Violation)


DEPLOY TODO LIST
* Add dependencies list file
* Setup Virtual Environment and reinstall dependencies
* Determine File Structure (for M: drive at work)
* General instructions for all developer Setup
* Look into Setup.py for distribution to Amanda
* Create config file with all dependencies

NOTES
* Objects need both data and behavior - otherwise use data
structure (list, tuple, dict), dataclass, or function
* When doing tests make sure if changes to main resources are
made that test/resources is also updated.
