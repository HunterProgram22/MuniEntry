"""Module containing all the data structures for parties in cases."""

class Party(object):
    """The base object from which all other party objects are inherited."""

    def __init__(self, party_type):
        self.party_type = party_type


class Person(object):
    """A base class for all people of any party type."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
