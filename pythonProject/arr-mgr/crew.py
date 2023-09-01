from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Crew:
    name: str  # discord name
    role: List[str] = field(default_factory=list)  # crew role
    is_staff: bool = False  # whether this user is
    is_active: bool = False
    is_assigned: bool = False
    is_ready: bool = False


@dataclass
class YardMaster(Crew):
    location: str | None = None  # the name of the yard
    id_yard: int | None = None  # the id of the
    set_talking_priority: bool = False  # (relates to discord channel)
    create_switch_list: bool = False  # allows to create switch list from demands
    assign_switch_list: bool = False  # allows to assign switch list to switcher crew
    assign_switch_crew: bool = False  # allows to assign switch crew to switcher
    assign_local_crew: bool = False  # allows to assign switcher crew to the local consist

    def __str__(self) -> str:
        if self.location is not None:
            return f'This is yard {self.location} and the yard master is {self.name}'
        else:
            return f'This is yard master {self.name} has no location assigned yet'


@dataclass
class Switcher(Crew):
    yard: str | None = None  # yard name where the switcher is assigned to
    engine_assigned: int | None = None  # engine road number
    switch_list: list[str] | None = None  # list of cars that need to be switched
    switch_list_id: int | None = None # id of the assigned switch list
    has_tasks: bool = False  # flag to indicate if the switcher has tasks
    has_switch_list: bool = False  # flag to indicate if the switcher has switch list

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

    set_management_role: bool = False  # flag to indicate if the dispatcher has management role
    set_talking_priority: bool = False  # flag to indicate if the dispatcher has talking priority
    set_routes: bool = False  # flag to indicate if the dispatcher can set up train routes according to the timetable
    set_read_consists_list: bool = False  # flag to indicate if the dispatcher has access to the consists list
    set_roster_access: bool = False  # flag to indicate if the dispatcher

    assign_engineer_to_consist: bool = False  # flag to indicate role to assign engineer to a certain consist is set
    assign_conductor_to_consist: bool = False  # flag to indicate role to assign conductor to a certain consist is set

    update_timetable_state: bool = False  # flag to indicate that role to update the timetable state is set
    
    def __str__(self) -> str:
        if self.is_active is True:
            return f"Today's  dispatcher is {self.name}"
        else:
            return f"No dispatcher is not signed in request a player with the dispatcher role to sign in"


@dataclass
class RoadEngineer(Crew):
    consist_assigned: int | None = None  # consist id the engineer is assigned to
    engine_assigned: int | None = None  # engine road number the engineer is assigned to
    assign_engineer_role: bool = False  # assign the engineer role on discord, so they can enter their consist channel
    
    def __str__(self) -> str:
        if self.active is False:
            return f"Engineer is {self.name} is not online"
        elif self.is_active is True and self.is_assigned is False:
            if self.is_ready is False:
                return f"Engineer is {self.name} is online"
            else :
                return f"Engineer is {self.name} is online and ready for job"
        else :
            return f"Engineer is {self.name} is online and assigned to consist {self.consist_assigned} and engine {self.engine_assigned}"


@dataclass
class RoadConductor(Crew):
    consist_assigned: int | None = None    # consist id the Conductor is assigned to.
    assign_conductor_role: bool = False   # assign the Conductor role on discord.
    
    def __str__(self) -> str:
        if self.is_active is False:
            return f"Conductor is {self.name} is not online"
        elif self.is_active is True and self.is_assigned is False:
            if self.is_ready is False:
                return f"Conductor is {self.name} is online"
            else :
                return f"Conductor is {self.name} is online and ready for job"
        else :
            return f"Conductor is {self.name} is online and assigned to consist {self.consist_assigned}."
    

@dataclass
class IndustryOperator(Crew):
    industry_id: int | None = None  # industry id the operator is assigned to
    industry_name: str | None = None  # industry name the operator is assigned to
    set_order_materials: bool = False  # to order raw materials  for user to produce products
    set_demand_access: bool = False  # to see the orders from customers

    def __str__(self) -> str:
        if self.is_active is False:
            return f"Industry operator is {self.name} is not online"
        elif self.is_active is True and self.is_ready is False:
            return f"Industry operator is {self.name} is online and ready to get assigned"
        else:
            return f"Industry operator is {self.name} is operating  {self.industry_name}"


@dataclass
class Management(Crew):
    set_access_orders: bool = False  # set access orders table
    set_access_inventory: bool = False  # set access inventory table
    set_access_consists: bool = False  # set access consists table
    set_access_cars: bool = False  # set access assets table
    set_access_engines: bool = False  # set access engines table
    set_access_industries: bool = False  # set access industries table
    set_access_operations_manager: bool = False  # this is the main tool to manage the rail layout.
    set_access_crew: bool = False  # sets the access to the crew table to see who is online and in what roles.

    def __str__(self) -> str:
        if self.is_active is False:
            return f"Manager is {self.name} is not online, plzz ask a staff member to sign into that role"
        else :
            return f"Management is {self.name} is online and ready to manage the railroad"


@dataclass
class MaintenanceOfWay(Crew):
    set_access_tracks: bool = False  # set access ticket manager for track maintenance.
    set_access_derailments: bool = False  # set access derailments ticket manager.

    def __str__(self) -> str:
        if self.is_active is False:
            return f"Maintenance of Way is {self.name} is not online, plzz ask a staff member to sign into that role"
        else :
            return f"Maintenance of Way is {self.name} is online and ready to maintain the railroad"


@dataclass
class Finance(Crew):
    set_access_financial_report: bool = False # set access financial dashboard
    set_access_buy_assets: bool = False # set access to be able to buy cars and engines
    set_access_roster: bool = False # set access to asset management (roster)

    def __str__(self) -> str:
        if self.is_active is False:
            return f"Finance is {self.name} is not online, plzz ask a staff member to sign into that role"
        else :
            return f"Finance is {self.name} is online and ready to receive orders of procurement"
        

@dataclass
class Mentor(Crew):
    set_access_roles: bool = False # set access to role management

    def __str__(self) -> str:
        if self.is_active is False:
            return f"Mentor is {self.name} is not online, plzz ask a staff member to sign into that role"
        else :
            return f"Mentor is {self.name} is online and ready to help."




