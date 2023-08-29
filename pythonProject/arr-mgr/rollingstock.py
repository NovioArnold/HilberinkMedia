from dataclasses import dataclass

@dataclass
class Rollingstock():
    railroad_company: str
    road_number_prefix: str
    road_number: int
    is_assigned_to_consist: bool
    location: object

@dataclass
class Engine(Rollingstock):

    type: str
    name: str
    fuel_type: str
    wheel_configuration: str
    is_assigned_to_crew:  bool
    has_tender: bool
    last_time_serviced: str


    def __str__(self):
        return (f'Engine name: {self.name}\n'
                f'Railroad: {self.railroad_company}\n'
                f'Road number: {self.road_number_prefix}{self.road_number}\n'
                f'Location: {self.location} \n'
                f'Is currently assigned?'
                f'\nCrew: {self.is_assigned_to_crew} '
                f'\nConsist: {self.is_assigned_to_consist}\n')

@dataclass
class Car(Rollingstock):
    type: str
    is_loaded: bool
    load: tuple
    destination: object


    def __str__(self):
        return (f'Railroad: {self.railroad_company}\n'
                f'Road number: {self.road_number_prefix}{self.road_number}\n'
                f'Type of car: {self.type}\n'
                f'Is loaded: {self.is_loaded}\n'
                f'load: {self.load}\n'
                f'Location: {self.location}\n'
                f'destination : {self.destination}\n'
                f'Assigned to consist: {self.is_assigned_to_consist}\n'
                )





