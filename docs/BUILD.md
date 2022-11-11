# Build Overview

The MuniEntry application is written primarily in Python. In order to make the application 
accessible to a user without Python on their system, the application is complied to an 
executable (.exe file) using PyInstaller.


## Build Requirements

Python 3.11

Pyinstaller 5.6.1


## Build Process

The application should be built from the Main branch of the Git repository.

### Run Test Suite

Prior to any build, all tests in the test suite should be run and a build should
only be performed if tests pass 100%.

### Build Location

The build process must be performed in the virtual environment that has all of the 
proper packages listed in the requirements.txt file already installed. Generally, the 
test suite should not pass unless all requirements are up-to-date in the virtual 
environment.

### Build Commands

In the root directory of the application run the following command:

    pyinstaller --hidden-imports lxml._elementpath --splash ./resources/icons/gavel_splash.png MuniEntry_app.py

The --hidden-imports parameter requires pyinstaller to specifically install the lxml module, which is necessary, 
but not automatically included if not explictly added to the install without calling for it as a hidden-import
paramater. 

The --splash parameter provides the location of the icon that is used during the bootloader process that is 
run whenever the MuniEntry application is opened. The bootloader process is the precompiling of the python 
application that is run each time the MuniEntry_app.exe file is run. It pacakages the python interpreter and 
all required source code to allow the application to run on computers without Python installed.

### Spec File

If the pyinstaller build process completes sucessfully, it will create a file called 
MuniEntry_app.spec. 

The initial MuniEntry_app.spec file will be populated with a skeleton of data variables that the pyinstaller 
process determined are necessary to run the application. The initial version of the .spec file must be 
updated with the current version of the MasterSPEC_MuniEntry_app.spec file that is located in the 
resources directory of the application.

The MasterSPEC_MuniEntry_app.spec file contains all current data variables that are required for the application 
to run properly. The MasterSPEC_MuniEntry_app.spec file includes references to all templates, internal data sources, 
icons and other non-code internal items. It also includes executable settings (i.e. turning off the console window)
and file directories that should be excluded from the build (i.e. the test suite).

The contents of the MasterSPEC_MuniEntry_app.spec file should be copied and used to replace the contents 
of the MuniEntry_app.spec file. 

After the contents of the MasterSPEC_MuniEntry_app.spec file pasted into the MuniEntry_app.spec file, then run the
following command:

    pyinstaller MuniEntry_app.spec

The build process will ask if you want to repalce the contents of the dist directory. Choose yes.

### The Compiled Executable

After the build process is complete, the compiled application will be located in the dist directory within 
the root directory. In the dist directory there will be a single directory labeled MuniEntry_app. That directory
contains the entire application and required files necessary for the application to run. 

The MuniEntry_app directory can then be placed on any computer for a user to access and run the application 
directly without having Python installed. Within the MuniEntry_app directory there is a MuniEntryapp.exe file 
that loads the application. A shortcut can be created to that file that will allow a user to launch the application.

**The application has a config.ini file that contains path settings. The user must have access to the paths 
in the config file for the application to work properly.**

***SEE THE DEPLOYMENT PROCESS FOR CURRENT DEPLOYMENT REQUIREMENTS.***
