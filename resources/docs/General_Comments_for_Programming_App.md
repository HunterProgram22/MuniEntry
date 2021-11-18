INSTRUCTIONS AND NOTES FOR PROGRAMMERS OF THE APPLICATION

Creating Views (References MainWindow but applies to all views)
* If changes to the view are made in QtDesigner then the command 'pyuic5 -o views/main_window_ui.py resources/ui/MainWindow.ui' must be run to update changes to the view file.
*     All slots and signals are connected after the view is created. Slots and signals can be linked in the view (using QtDesigner or directly in the view file after pyuic5 is run), however, connecting in MainWindow (class Window)
is cleaner and allows easier scaling of the application.
* Generally, connecting with pressed is preferred to clicked because a clicked event sends a bool
argument to the function. However, clicked is used in some instances because it is a press and release
of a button. Using pressed sometimes caused an event to be triggered twice.
