"""constants.py

File for all the constants

@author Saku Rautiainen <saku.rautiainen@iki.fi>
"""

#Database parameters
TEMPERATURE_DATABASE_NAME = "simaattori_temperature.db"

#Timer, key is sensor id, value is time in seconds. How often temperature values are saved.
SENSOR_TIMING = {"28-000006564895": 60*60}
#Sensor information
SENSOR_ID_LOCATIONS = { "28-000006564895" : "Waterproof DS18B20 sensor" }
