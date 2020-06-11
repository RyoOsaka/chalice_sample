from dataclasses import dataclass


@dataclass
class Project():
    project_id: int
    employee_id: int
    project_name: str
