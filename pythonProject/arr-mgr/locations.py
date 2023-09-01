from dataclasses import dataclass
@dataclass
class Location:
    name_location: str
    description: str
    track_plan: str


@dataclass
class Industry(Location):
    input_1: str | None = None
    in_stock_input_1: int = 0
    max_hold_input_1: int = 0
    input_2: str | None = None
    in_stock_input_2: int = 0
    max_hold_input_2: int = 0
    input_3: str | None = None
    in_stock_input_3: int = 0
    max_hold_input_3: int = 0
    output_1: str | None = None
    in_stock_output_1: int = 0
    max_hold_output_1: int = 0
    output_2: str | None = None
    in_stock_output_2: int = 0
    max_hold_output_2: int = 0

    def __str__(self) -> str:
        prt_str = (f'{self.name_location} has in stock demands '
                   f'{self.input_1} {self.in_stock_input_1} / {self.max_hold_input_1}\n')
        if self.input_2 is not None:
            i2 = (f'{self.name_location} has in stock demands '
                  f'{self.input_2} {self.in_stock_input_2} / {self.max_hold_input_2}\n')
            prt_str = prt_str+i2
            return prt_str
        if self.input_3 is not None:
            i3 = (f'{self.name_location} has in stock demands '
                  f'{self.input_2} {self.in_stock_input_2} / {self.max_hold_input_2}\n')
            prt_str = prt_str+i3
            return prt_str
        prt_str = prt_str+(f'{self.name_location} produced '
                           f'{self.output_1} {self.in_stock_output_1} / {self.max_hold_output_1}\n')
        if self.output_2 is not None:
            o2 = f'{self.name_location} produced {self.output_2} {self.in_stock_output_2} / {self.max_hold_output_2}\n'
            prt_str = prt_str+o2
            return prt_str

        return prt_str

    def load_car(self, car: Car) -> Car:
        if self.in_stock_output_1 > 0 and car.is_loaded is False:
            car.is_loaded = True
            car.cargo_name = self.output_1
            car.cargo_quantity = 6
            self.in_stock_output_1 -= 6
            return car
        else:
            return car

    def unload_car(self, car: Car) -> Car:
        if self.in_stock_input_1 < self.max_hold_input_1 and car.is_loaded is True:
            car.is_loaded = False
            car.cargo_name = 'Empty'
            car.cargo_quantity = 0
            self.in_stock_input_1 += 6
            return car
        else:
            return car

@dataclass
class Yard(Location):
    name_yard: str | None = None
    type_of_yard: str | None = None
    number_of_tracks: int = 0
    number_of_tracks_occupied: int = 0
    number_of_engines: int = 0
    number_of_cars: int = 0
    number_of_rollingstock: int = 0
    max_cars_per_track: int = 0

    def __str__(self) -> str:
        prt_str = f'{self.name_yard} at {self.name_location} has {self.number_of_tracks} tracks.\n'
        if self.number_of_tracks_occupied > 0:
            prt_str = prt_str+f'{self.number_of_tracks_occupied} are occupied.\n'
        else:
            prt_str = prt_str+'No tracks are occupied.\n'
        prt_str = prt_str+f'{self.number_of_engines} engines are in the yard.\n'
        prt_str = prt_str+f'{self.number_of_cars} cars are in the yard.\n'
        prt_str = prt_str+f'{self.number_of_rollingstock} rollingstock are in the yard.\n'
        return prt_str


@dataclass
class Siding(Location):
    name_sidings: str | None = None
    number_of_tracks: int = 0
    number_of_tracks_occupied: int = 0
    max_train_length_per_track: int = 0

    def __str__(self) -> str:
        prt_str = f'{self.name_sidings} at {self.name_location} has {self.number_of_tracks} tracks.\n'
        if self.number_of_tracks_occupied > 0:
            prt_str = prt_str+f'{self.number_of_tracks_occupied} are occupied.\n'
        else:
            prt_str = prt_str+'No tracks are occupied.\n'
        return prt_str


@dataclass
class ControlPoint(Location):
    name_control_point: str | None = None
    control_point_prefix: str | None = None
    control_point_number: int = 0

    def __str__(self) -> str:
        return (f'{self.name_control_point} radio name is {self.control_point_prefix}{self.control_point_number}'
                f' is a control point at {self.name_location}.\n')


@dataclass
class Mainline(Location):
    name_mainline: str | None = None
    mainline_prefix: str | None = None
    mainline_number: int = 0
    number_of_tracks: int = 0
    start_location: str | None = None
    end_location: str | None = None

    def __str__(self) -> str:
        return (f'{self.name_mainline} radio name is {self.mainline_prefix}{self.mainline_number}'
                f' is a mainline at {self.name_location}.\n '
                f'And runs from {self.start_location} to {self.end_location}.\n')


@dataclass
class Track(Location):
    type_of_track: str | None = None
    track_prefix: str | None = None
    track_number: int = 0
    max_cars: int = 0
    is_occupied: bool = False
    is_ouy_of_service: bool = False
    number_of_rollingstock: int = 0

    def __str__(self) -> str:
        prt_str = f'track {self.track_prefix}{self.track_number} is'
        str_end = f'this is a {self.type_of_track} track and can holds a maximum of {self.max_cars} cars.'
        if self.is_occupied is True:
            prt_str = prt_str+f' occupied by {self.number_of_rollingstock}.\n'+str_end
            return prt_str
        else:
            prt_str = prt_str+f' not occupied.\n'+str_end
            return prt_str









