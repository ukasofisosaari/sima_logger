"""sensor.py

@author Saku Rautiainen <saku.rautiainen@iki.fi>
"""

import sqlite3
from threading import Timer


from constants import TEMPERATURE_DATABASE_NAME, SENSOR_ID_LOCATIONS, SENSOR_TIMING

class sensor(object):
    """ Sensor class. Used for dealing with indiividual sensors. 
        Will hold information such as sensor id, what to do 
        when saving time etc.
        Note that this is baseclass. For each sensor type create its own class.
        Also, if sensor placement/usage dictates different way of saving information, then also
        inherit.
    """

    def __init__(self, sensor_id, descr_str):
        """
        Used to initialize sensor.
        """
        self._sensor_id = sensor_id
        self._descr_str = descr_str

    def save_temperature(self):
        """
            Virtual class
        """
        assert(False)

class ds18b20_sensor(sensor):
    """
        Dallas instruments DS18B20 Temperature sensor handler.
    """
    def __init__(self, sensor_id, descr_str):
        sensor.__init__(self, sensor_id, descr_str)
        #TODO: Check that this sensor is connected, if not throw exception.

    def save_temperature(self):
        """
            Gets Temperature from the sensor and saves it to the database
        """
        assert(False)
