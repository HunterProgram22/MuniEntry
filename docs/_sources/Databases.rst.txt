===================
Databases Overview
===================

The MuniEntry application has an internal Sqlite database for storing data. The application also
accesses external databases for loading data. This section covers how the application acceses the
various databases.

MuniEntryDB.sqlite
__________________

The MuniEntryDB.sqlite database is the application's internal database. It is located at:

..  code-block:: python

    'M:\Admin\Information_Technology\MuniEntry_Files\DB'


AuthorityCourt.dbo
__________________

The AuthorityCourt.dbo is the external database used by the Authority Court case managment system. The
MuniEntry application connects to the database and loads case data from the database for Criminal and Traffic
cases.
