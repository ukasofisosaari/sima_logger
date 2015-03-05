"""main.py

    Main file of the program. Will maybe have some terminal text based UI
    Or LCD and button based UI.
@author Saku Rautiainen <saku.rautiainen@iki.fi>
"""

from threading import Timer

from sensor import ds18b20_sensor, SENSOR_FAMILY_CODES
from constants import SENSOR_ID_LOCATIONS, SENSOR_TIMINGS

#List for storing sensor objects
sensor_list = []


def cleanup():
    pass

def init():

    #Create class for each sensor and then create timer.
    for sensor_id in SENSOR_ID_LOCATIONS.keys():
        #Checking what kind of sensor it is and then using correct constructor
        for sensor_family_code in SENSOR_FAMILY_CODES:
            #We check if sensor id starts with
            if sensor_id.startswith(sensor_family_code):
                sensor = SENSOR_FAMILY_CODES[sensor_family_code](sensor_id, SENSOR_ID_LOCATIONS[sensor_id])
                sensor_list.append()

def main():

    init()
    

if __name__ == "__main__":
    main()
