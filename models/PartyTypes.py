"""Module containing all the data structures for parties in cases."""

class Party(object):
    """The base object from which all other party objects are inherited."""

    def __init__(self, party_type):
        self.party_type = party_type


class Plaintiff(Party):
    """A type of party in a case. Generally the State of Ohio in a criminal
    case."""

    def __init__(self, party_type):
        super().__init__(party_type)


class Person(object):
    """A base class for all people of any party type."""

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Entity(object):
    """A base class for non-person parties
    (i.e. State of Ohio or a business)."""

    def __init__(self, entity_name):
        self.entity_name = entity_name
