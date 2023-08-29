'''this contains all tests '''
from rollingstock import Rollingstock, Engine, Car
from dataclasses_serialization.json import JSONSerializer



test_engine = Engine(
    railroad_company = 'Canadian National',
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
    load=('logs', 6),
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
    load=(),
    location='logging_camp',
    destination='lumbermill',

)


print(test_engine)
test_engine.is_assigned_to_crew = True
print(test_engine)
print(test_car_loaded)
print(test_car_not_loaded)

serial = JSONSerializer.serialize(test_engine)

print(serial)
with open("rollingstock.json", "a") as file:
    file.write(str(serial))




