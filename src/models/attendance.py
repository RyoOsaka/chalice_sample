from dataclasses import dataclass
from datetime import datetime


@dataclass
class Employee():
    attendance_id: int
    employee_id: int
    clockin_time: datetime
    clockout_time: datetime
