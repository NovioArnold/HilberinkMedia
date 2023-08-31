from dataclasses import dataclass

@dataclass
class Crew:
    name: str #discord name
    role: list[str] # roles this user is qualified for
    is_staff: bool
    is_active: bool
    is_assigned: bool

@dataclass
class Yard_master(Crew):
    location: str | None = None # the name of the yard
    id_yard: int | None = None # the id of the
    set_talking_priority: bool = False#(relates to discord channel)
    create_switch_list  : bool = False #allows to create switch list from demands
    assign_switch_list   : bool = False #allows to assign switch list to switcher crew
    assign_switch_crew   : bool = False #allows to assign switch crew to switcher
    assign_local_crew : bool = False #allows to assign switcher crew to the local consist 

    def __str__(self) -> str:
        if self.location is not None:
            return f'This is yard {self.location} and the yard master is {self.name}'
        else:
            return f'This is yard master {self.name} has no location assigned yet'
@dataclass
class Switcher(Crew):
    yard: str | None = None #yard name where the switcher is assigned to
    engine_assigned: int | None = None #engine road number
    switch_list: list[str] | None #list of cars that need to be switched
    switch_list_id: int | None #id of the assigned switch list
    has_tasks: bool = False # flag to indicate if the switcher has tasks
    has_switch_list: bool = False # flag to indicate if the switcher has switch list

    def __str__(self) -> str:
        if self.yard is not None:
            if self.engine_assigned is not None:
                return f'This is switcher {self.name} and is assigned to {self.yard} and engine{self.engine_assigned}'
            else:
                return f'This is switcher {self.name} and is assigned to {self.yard} and has no engine assigned yet'
        else:
            return f'This is switcher {self.name} and has no yard assigned yet'

@dataclass
class Dispatcher(Crew):
    is_signed_in: bool = False #flag to indicate if the dispatcher is signed in

    set_management_role: bool = False #flag to indicate if the dispatcher has management role
    set_talking_priority: bool = False #flag to indicate if the dispatcher has talking priority (in the discord channel for dispatch)
    set_routes: bool = False #flag to indicate if the dispatcher can setup train routes according to the timetable
    set_read_consists_list: bool = False #flag to indicate if the dispatcher has access to the consists list

    assign_engineer_to_consist: bool = False #flag to indicate role to assign engineer to a certain consist is set
    assign_conductor_to_consist: bool = False #flag to indicate role to assign conductor to a certain consist is set

    update_timetable_state: bool = False #flag to indicate that role to update the timetable state is set (add or remove consists from timetable)
    
    def __str__(self) -> str:
        if self.is_signed_in is True:
            return f"Today's  dispatcher is {self.name}"
        else:
            return f"No dispatcher is not signed in request a player with the dispatcher role to sign in"

@dataclass
class Road_engineer(Crew):
    pass

@dataclass
class Road_conductor(Crew):
    pass

@dataclass
class Industry_operator(Crew):
    pass

@dataclass
class Management(Crew):
    pass
@dataclass
class MOW(Crew):
    pass
