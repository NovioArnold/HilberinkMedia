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
    max_hold_output_1: int
    output_2: str | None
    in_stock_output_2: int | None
    max_hold_output_2: int | None

    def __str__(self):
        prt_str = f'{self.name_location} has in stock demands {self.input_1} {self.in_stock_input_1} / {self.max_hold_input_1}\n'
        if self.input_2 is not None:
            i2 = f'{self.name_location} has in stock demands {self.input_2} {self.in_stock_input_2} / {self.max_hold_input_2}\n'
            prt_str = prt_str+i2
            return prt_str
        if self.input_3 is not None:
            i3 = f'{self.name_location} has in stock demands {self.input_2} {self.in_stock_input_2} / {self.max_hold_input_2}\n'
            prt_str = prt_str+i3
            return prt_str
        prt_str = prt_str+f'{self.name_location} produced {self.output_1} {self.in_stock_output_1} / {self.max_hold_output_1}\n'
        if self.output_2 is not None:
            o2 = f'{self.name_location} produced {self.output_2} {self.in_stock_output_2} / {self.max_hold_output_2}\n'
            prt_str = prt_str+o2
            return prt_str

        return prt_str










@dataclass
class Track(Location):
    type_of_track: str
    track_prefix: str
    track_number: int
    max_cars: int
    is_occupied: bool
    number_of_rollingstock: int = 0

    def __str__(self):
        prt_str = f'track {self.track_prefix}{self.track_number} is'
        str_end = f'this is a {self.type_of_track} track and can holds a maximum of {self.max_cars} cars.'
        if self.is_occupied is True:
            prt_str = prt_str+f' occupied by {self.number_of_rollingstock}.\n'+str_end
            return prt_str
        else:
            prt_str = prt_str+f' not occupied.\n'+str_end
            return prt_str






