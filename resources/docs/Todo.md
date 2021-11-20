APPLICATION TODO LIST for version 0.3.0
* Remove magic numbers throughout - Look to check_plea_and_findings method as an example.
* Wire up amend offense dialog again - works on basic level - need to move signals to dialog
and perhaps update the actual original charge to indicate amended.
* Move general methods to helper functions
* Add Warning if add condition boxes are checked but conditions have not been added.
* Add new tests - fix test amend offense because button is now in grid.
* Fix database connection names in criminal dialogs and elsewhere - make clearer.
* Add charges_grid to Not guilty? - fix the bug on create entry.
* Updated dialogs/templates for Not Guilty and FTA per AB Notes.
* Add Max Min buttons to dialogs.




FEATURE/CHANGE LIST - for Version 0.4.0
* Add community control conditions checkboxes
* Add Jail entries
* Add DUI sub-dialog
* Make statutes hyperlink
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
* Add kite and linter atom packages
* When doing tests make sure if changes to main resources are
made that test/resources is also updated.
