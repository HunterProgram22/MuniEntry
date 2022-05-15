from typing import Any

class Person:
    first_name: Any
    last_name: Any
    def __init__(self) -> None: ...

class Defendant(Person): ...

class JudicialOfficer(Person):
    first_name: Any
    last_name: Any
    officer_type: Any
    def __init__(self, first_name: str, last_name: str, officer_type: str) -> None: ...
