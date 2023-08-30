from dataclasses import dataclass
@dataclass
class Location:
    name_location: str
    description: str
    track_plan: str


@dataclass
class Industry(Location):
    input_1 : str
    in_stock_input_1 : int
    max_hold_input_1 : int
    input_2: str | None
    in_stock_input_2: int | None
    max_hold_input_2: int | None
    input_3: str | None
    in_stock_input_3: int | None
    max_hold_input_3: int | None
    output_1: str
    in_stock_output_1: int
    output_1: str | None
    in_stock_output_1: int | None


@dataclass
class Track(Location):
    type_of_track: str
    track_prefix: str
    track_number: int
    max_cars: int
    is_occupied: bool




