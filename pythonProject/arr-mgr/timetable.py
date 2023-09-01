from dataclasses import dataclass, field
from typing import List, Dict
import datetime


@dataclass
class Timetable:
    session_name: str = 'Timetable'+field(default_factory=datetime.date.today)
    session_date: str = field(default_factory=datetime.date.today)
    session_is_active: bool = False
    consists: Dict[int:str] = field(default_factory=dict)

    def __str__(self) -> str:
        return f'This is the timetable for {self.session_name} on {self.session_date}'

    def add_consist(self, consist_id: int, consist_name: str) -> Dict[int:str] | ValueError:
        if consist_id not in self.consists.keys():
            self.consists[consist_id] = consist_name
            return self.consists
        else:
            return ValueError(f'This consist {consist_id} id already assigned to timetable')

    def remove_consist(self, consist_id: int) -> Dict[int:str] | ValueError:
        if consist_id in self.consists.keys():
            del self.consists[consist_id]
            return self.consists
        else:
            return ValueError(f'This consist {consist_id} id not in timetable')


