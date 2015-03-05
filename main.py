"""main.py

    Main file of the program. Will maybe have some terminal text based UI
    Or LCD and button based UI.
@author Saku Rautiainen <saku.rautiainen@iki.fi>
"""

from threading import Timer

from sensor import ds18b20_sensor
from constants import SENSOR_ID_LOCATIONS, SENSOR_TIMINGS

#List for storing sensor objects
sensor_list = []
#Key is the sensor family code/etc. For ds18b20 sensors, id always starts with the family code 28-
#TODO: Figure out if this works for weight sensor as well and possible other sensors.
sensor_classes = {"28-": ds18b20_sensor}

def cleanup():
    pass

def init():

    #Create class for each sensor and then create timer.
    for sensor_id in SENSOR_ID_LOCATIONS.keys():
        #Checking what kind of sensor it is and then using correct constructor
        for sensor_family_code in sensor_classes:
            #We check if sensor id starts with
            if sensor_id.startswith(sensor_family_code):
                sensor = sensor_classes[sensor_family_code](sensor_id, SENSOR_ID_LOCATIONS[sensor_id])
                sensor_list.append()

def main():

    init()
    

if __name__ == "__main__":
    main()
