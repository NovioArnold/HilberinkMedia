from dataclasses import dataclass


@dataclass(frozen=True)
class Product:
    name_product: str
    produced_by: str
    type_of_car: str
    max_hold_car: int

    def __str__(self) -> str:
        return f'{self.name_product} is produced by {self.produced_by}'


logs = Product('Logs', 'Logging_camp', 'Flatcar', 6)
cordwood = Product('Firewood', 'Logging_camp', 'wall_flatcar', 8)
lumber = Product('Lumber', 'Sawmill', 'Stake_flatcar', 6)
beams = Product('Beams', 'Sawmill', 'Stake_flatcar', 3)
iron_ore = Product('Iron_ore', 'Iron Mine', 'Hopper', 10)
rails = Product('Rails', 'Smelter', 'Stake_flatcar', 10)
iron = Product('Iron', 'Smelter', 'Stake_flatcar', 10)
coal = Product('Coal', 'Coal Mine', 'Hopper', 10)
pipe = Product('Pipe', 'Steel Mill', 'Flatcar', 6)
tools = Product('Tools', 'Steel Mill', 'Boxcar', 30)
crude_oil = Product('Oil', 'Oil Well', 'Tankcar', 12)
oil_barrels = Product('Oil Barrels', 'Oil Refinery', 'Wall_flatcar', 16)

