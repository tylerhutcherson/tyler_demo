## Tyler Demo
from skafossdk import *

ska = Skafos()
ska.engine.create_view(
    "power_datum", 
    {"keyspace": "power", "table": "hist_load"}, 
    DataSourceType.Cassandra).result()


print('Query some data!!!')
power = ska.engine.query("SELECT * from power_datum limit 10").result()

print(power['data'])


