'''this contains all tests '''
from dataclasses_serialization.json import JSONSerializer

from rollingstock import Engine, Car
from locations import Industry, Track

test_engine = Engine(
    railroad_company='Canadian National',
    road_number_prefix='CN',
    road_number=420,
    is_assigned_to_consist=False,
    location='lumbermill',
    type='geared steam engine',
    name='climax',
    fuel_type='wood',
    wheel_configuration='4-4',
    is_assigned_to_crew=False,
    has_tender=False,
    last_time_serviced='10-10-2020'
)

test_car_loaded = Car(
    railroad_company='Arnold Lumber Company',
    road_number_prefix='ALC',
    road_number=69,
    type='flatcar',
    is_assigned_to_consist=True,
    is_loaded=True,
    cargo_name='logs',
    cargo_quantity=6,
    location='logging_camp',
    destination='lumbermill',

)

test_car_not_loaded = Car(
    railroad_company='Arnold Lumber Company',
    road_number_prefix='ALC',
    road_number=70,
    type='flatcar',
    is_assigned_to_consist=False,
    is_loaded=False,
    cargo_name='Empty',
    cargo_quantity=0,
    location='logging_camp',
    destination='lumbermill',

)

test_industry = Industry(
    name_location='lumbermill',
    description='this turns logs into timber and beams',
    track_plan='not implemented yet',
    input_1='Logs',
    in_stock_input_1=0,
    max_hold_input_1=100,
    input_2=None,
    in_stock_input_2=None,
    max_hold_input_2=None,
    input_3=None,
    in_stock_input_3=None,
    max_hold_input_3=None,
    output_1='timber',
    in_stock_output_1=0,

)

print(test_engine)
test_engine.is_assigned_to_crew = True
print(test_engine)
print(test_car_loaded)
print(test_car_not_loaded)
print(test_industry)


# serial = JSONSerializer.serialize(test_engine)

# print(serial)
# with open("rollingstock.json", "a") as file:
#   file.write(str(serial))
print('hello does this object still exist? ', test_car_not_loaded)

def test_load_car(name: str, quantity: int):
    test_car_not_loaded.cargo_name = name
    test_car_not_loaded.cargo_quantity = quantity
    test_car_not_loaded.is_loaded = True
    return test_car_not_loaded

test_car_not_loaded = test_load_car('Coal', 10)

print('load car', test_car_not_loaded)

print(test_car_not_loaded)

def test_unload_car(name: str, quantity: int):
    test_car_not_loaded.cargo_name = name
    test_car_not_loaded.cargo_quantity = quantity
    test_car_not_loaded.is_loaded = False
    return test_car_not_loaded

test_car_not_loaded = test_unload_car('Empty', 0)

print('unloaded car:\n',test_car_not_loaded)


