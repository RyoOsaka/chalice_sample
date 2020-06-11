from dataclasses import dataclass


@dataclass
class Employee():
    employee_id: int
    first_name: str
    last_name: str
    mail: str
