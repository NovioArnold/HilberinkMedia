from dataclasses import dataclass
from rollingstock import Car, Engine
@dataclass
class Consist:
    name: str | None
    start: str | None
    end: str | None
    engine: list[str] | None = None
    cars: list[str] | None = None

    def __str__(self):
        if self.name is None:
            return f'there is not consist'
        else:
            return (f'this is consist number {self.name}.\n Traveling from {self.start} to {self.end}.'
                    f'\nConsists of engine(s) {self.engine} and car(s) {self.cars}\n And has a total length of {len(self.engine)+len(self.cars)}.')



    def add_engine(self, engine: str) ->list[str]:
        e: list = []
        if self.engine is None:
            e.append(engine)
            self.engine = e
            return self.engine
        else:
            e = self.engine
            e.append(engine)
            self.engine = e
            return self.engine

    def remove_engine(self, engine: str) ->list[str]:
        print('plzz remove engine')
        if self.engine is None:
            raise Exception

        else:
            e = self.engine
            e.remove(engine)
            self.engine = e
            return self.engine

    def add_car(self, car: str) -> list[str]:
        c: list = []
        if self.cars is None:
            c.append(car)
            self.cars = c
            return self.cars
        else:
            c = self.cars
            c.append(car)
            self.cars = c
            return self.cars

    def remove_car(self, car: str) -> list[str]:
        c: list = []
        if self.cars is None:
            raise Exception
        else:
            c = self.cars
            c.remove(car)
            self.cars = c
            return self.cars

