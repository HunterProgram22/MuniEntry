Deployment Overview
===================

The MuniEntry application as used at the Delaware Municipal Court is deployed to the 
M: drive (MunicipalCourt) of the City Network. 

________________________
##Deployment Directories
________________________


The application uses two directories for deployment and use of the application.

**Users must have access to both directories in order to access and use all features of the
application.**

*************************
**Application Directory**

In addition to subdirectories for deployment and testing of the application, the MuniEntry_Files directory 
also contains a copy of the shortcut for the production version of the application. This shortcut points to the 
MuniEntry_app.exe file that is in the MuniEntry_app subdirectory. This shortcut should be copied and pasted 
to any new user's Desktop to allow them to access the application. 


*******************
*MuniEntry_Files*

The main directory for deployment of the application is:

   ``M:\Admin\Information_Technology\MuniEntry_Files``
   
Within this directory there are a number of subdirectories used for the deployed application.


*****************
*MuniEntry_app*

The MuniEntry_app directory is the deployed application. It is the current production version 
of the application that is in use. 


********************
*Hot_Swap_Version*

The Hot_Swap_Version directory contains the prior stable version build of the application. Generally,
this will be the prior 0.X-1.0 version of the application. For example if the current version 
of the application is 0.42.0, then the Hot Swap version should be 0.41.0. 

The Hot Swap version should be the latest stable prior verision that includes any bug fix
releases. Thus, if the last release of Version 0.41 was 0.41.2, that should be the Hot 
Swap version in the Hot_Swap_Version directory. 

..  note::
    As of Version 0.42.0, the application when deployed contains a db directory in which the Daily Case
    List reports (SSRS Files generated from the AuthorityCourtDB) are populated each morning at 8:00 a.m. If
    the Hot Swap Version is deployed after 8 a.m., the Daily Case List Reports must be moved from the production
    verion into the Hot_Swap_Version prior to switching over. In a future release, the SSRS Files will be
    saved into the DB directory in the MuniEntry_Files directory to avoid the need to copy the files over.


*****************
*TEST_Versions*

The TEST_Versions directory is used for deploying a compiled build for live testing. 


******************
*MuniEntry_Logs*

The MuniEntry_Logs directory is the location where the MuniEntry application logs are saved.


**********************
*Prior_Version_Data*

The Prior_Version_Data directory was used until Version 0.40.0 for storing prior version data such as 
saved entries and logs. Starting with Version 0.40.0 the saving of data was moved to external directories 
and moving prior version data to this directory prior to deployment of a new build was eliminated.

..  note::
    This directory will eventually be deleted once all prior version data is moved to the appropriate
    directory.

****
*DB*

The DB directory contains internal application database (MuniEntryDB.sqlite) for MuniEntry. 

..  note::
    In a future version, this directory will also contain the Daily Case List reports (SSRS Files generated
    from the AuthorityCourtDB).


********
*Config*

The Config directory will be used in the future for storing application specific config files.

..  warning::
    As of Version 0.42.0, the config file stored in this directory is not used by the application and the
    config file (config.ini) is stored internally within the application MuniEntry_app directory.**

___

## Entries Directory

The Entries directory is located at:

``M:\Entries``

The Entries directory contains subdirectories where the application saves documents that are created by 
the user with the application.

*Batch*

A directory for saving entries created by the application's batch processes.

*CrimTraffic*

A directory for saving entries created from the CrimTraffic Tab of the application.

*DigitalWorkflow*

A directory for saving entries to be used in the Digital Workflow process. **Note:** This currently in use 
in a limited capacity, and may be changed, moved, renamed or deleted in a future version.

*DrivingPrivileges*

A directory for saving Driving Privileges entries that are created by the application.

*Fiscal*

A directory for saving Fiscal Entries (Administrative Journal Entries authorizing release of funds) that 
are created by the application.

*JuryPay* 

A directory for saving Jury Payment entries created by the application.

*Scheduling*

A directory for saving entries created from the Scheduling Tab of the application.

____

## Deployment

The deployment process is for distribution of a new version of the application that has been properly built 
as described in the Build documentation.

**Note: Until the Daily Case Lists (SSRS Files from AuthorityCourtDB) are set to populate in the MuniEntry_Files/DB 
directory, then deployment should be done prior to 8:00 a.m. each day to insure a working instance of the 
application is in place for the Daily Cases Lists to populate.**

Prior to starting the deployment process, make sure that no computer has an instance of the application open
and running. 

### Create Hot Swap Version

If the version being deployed is a new minor release (i.e. 0.X+1.0) then the current version in production
(0.X.0) must be copied over to the Hot Swap Version that is currently in the Hot_Swap_Version directory.

**Reminder:** The entire MuniEntry_app directory must be copied and moved.

Make sure to copy and paste the production version over to the Hot_Swap_Version directory, do not cut and paste. 
Cutting and pasting may not work properly if the current version of the application is open on a user's computer. 

### Delete Current Production Version

Delete the current production version of the application - the MuniEntry_app directory.

If the current production version of the application cannot be completely deleted, this is an indication that an 
instance of the application is still open on a user's desktop. Determine where the application is open and close it.
Then try to delete the current production version again.

### Move New Version Into Production

Copy and paste the current build of that application that is on the developer's computer. The entire MuniEntry_app 
directory must be moved from the developer's computer to the MuniEntry_Files directory. 

Test that the application opens properly from the shortcut. 

If the application doesn't open properly, check the logs for the application first. If the logs do not provide 
any indication of why the application won't open, then try running the MuniEntry_app.exe file from the command line 
to see what is causing the application to fail to load.

If the application does load successfully from the shortcut, then deployment is complete. 
