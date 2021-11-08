APPLICATION TODO LIST for version 0.3.0
* Add Yellow Sheet templates (FTA/Bond, Not Guilty/Bond, CC Violation)
* Add functionality for allied offenses
* Add community control conditions checkboxes
* Remove magic numbers throughout.
* Wire up amend offense dialog again - works on basic level - need to move signals to dialog
and perhaps update the actual original charge to indicate amended.
* Move create entry and other general methods to helper functions
* Add Warning if add condition boxes are checked but conditions have not been added.
* Add Warning if plea and finding boxes are None
* Add new tests - fix test amend offense because button is now in grid.




FEATURE/CHANGE LIST - for Version 0.4.0




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
