from dataclasses import dataclass, field
from typing import List, Dict
import datetime
from timetable import Timetable

'''
what does the dispatcher do?
    ----Timetable----
    - set up the timetable
    - add consist into timetable slot
    - edit the timetable
    - delete the timetable
    - view the timetable
    ----Consists----
    - set up the consists 
    - clear the consists (after the train has arrived at the destination)
    - view the consists
    - add cars to consist
    - add engines to consist
    - remove cars from consist
    - remove engines from consist
    - assign the consists to the crew
    - clear the consists crew (end of session)
    - view assigned crew
    ----Crew----
    - assign the crew
    - clear the crew
    - view the crew
    ----Switch lists----
    - generate the switch lists
    - view the switch lists
    - assign the switch lists to the yard master
    ----Generate Consist documentation----
    - generate the consists table
    - assign the consists table to the crew
    - clear the crew (end of session)
    - view the consists table
    - update the consists table
    ----Routes----
    - set up the routes
    - update the routes
    - clear routes
    - view the routes
    ----Roster----
    - see the roster
    ----Track----
    - see the track diagram
    - see track status
    - edit track status
    - clear track status (sets all track to unoccupied)
    ----Orders----
    - see the orders
    - edit the orders
    - clear the orders
    - assign the orders to the crew
'''

@dataclass
class TimetableManager:
    timetable: Timetable = Timetable() # the timetable object

    def create_timetable(self, name: str, date: str) -> None:
        self.timetable.session_name = name
        self.timetable.session_date = date

    def edit_timetable(self):
        pass

    def delete_timetable(self):
        pass

    def view_timetable(self):
        pass

    def add_consist_to_timetable(self):
        pass

    def remove_consist_from_timetable(self):
        pass
