#File with classes for storing case information to be used in Dialogs

class CaseInformation(object):
    """This object stores all the information for a case both at inception and
    as it is populated through the application."""
    def __init__(self):
        self.case_number = None
        self.plaintiff_name = None
        self.plaintiff_attorney_name = None
        self.defendant_name = None
        self.defendant_attorney_name = None
