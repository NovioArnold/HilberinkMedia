

from locations import Industry
from rollingstock import Car
from products import logs, cordwood, lumber, beams, iron_ore, rails, iron, coal, pipe, tools, crude_oil, oil_barrels

logging_camp = Industry(
    name_location='Logging Camp',
    description='This is where logs are harvested',
    track_plan='not implemented yet',
    output_1=logs.name_product,
    max_hold_output_1=100,
    in_stock_output_1=100,
    output_2=cordwood.name_product,
    max_hold_output_2=100,
    in_stock_output_2=100,
)

sawmill = Industry(
    name_location='Sawmill',
    description='This is where logs are turned into lumber and beams',
    track_plan='not implemented yet',
    input_1=logs.name_product,
    max_hold_input_1=100,
    in_stock_input_1=0,
    output_1=lumber.name_product,
    max_hold_output_1=100,
    in_stock_output_1=0,
    output_2=beams.name_product,
    max_hold_output_2=100,
    in_stock_output_2=0,
)

iron_mine = Industry(
    name_location='Iron Mine',
    description='This is where iron ore is mined',
    track_plan='not implemented yet',
    input_1=lumber.name_product,
    max_hold_input_1=100,  # TODO: check this number next time in game
    in_stock_input_1=0,
    input_2=beams.name_product,
    max_hold_input_2=100,  # TODO: check this number next time in game
    in_stock_input_2=0,
    output_1=iron_ore.name_product,
    max_hold_output_1=100,  # TODO: check this number next time in game
    in_stock_output_1=0,

)

smelter = Industry(
    name_location='Smelter',
    description='This is where iron ore is turned into iron and rails',
    track_plan='not implemented yet',
    input_1=iron_ore.name_product,
    max_hold_input_1=100,  # TODO: check this number next time in game
    in_stock_input_1=0,
    input_2=cordwood.name_product,
    max_hold_input_2=100,  # TODO: check this number next time in game
    in_stock_input_2=0,
)

coal_mine = Industry(
    name_location='Coal Mine',
    description='This is where coal is mined',
    track_plan='not implemented yet',
    input_1=beams.name_product,
    max_hold_input_1=100,  # TODO: check this number next time in game
    in_stock_input_1=0,
    input_2=rails.name_product,
    max_hold_input_2=100,  # TODO: check this number next time in game
    in_stock_input_2=0,
    output_1=coal.name_product,
    max_hold_output_1=100,  # TODO: check this number next time in game
)

steel_mill = Industry(
    name_location='Steel Mill',
    description='This is where iron and coal are turned into pipe and tools',
    track_plan='not implemented yet',
    input_1=iron.name_product,
    max_hold_input_1=100,  # TODO: check this number next time in game
    in_stock_input_1=0,
    input_2=coal.name_product,
    max_hold_input_2=100,  # TODO: check this number next time in game
    in_stock_input_2=0,
    output_1=pipe.name_product,
    max_hold_output_1=100,  # TODO: check this number next time in game
    in_stock_output_1=0,
    output_2=tools.name_product,
    max_hold_output_2=100,  # TODO: check this number next time in game
    in_stock_output_2=0,
)








