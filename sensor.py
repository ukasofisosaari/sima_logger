"""sensor.py
    Implementation of base sensor class.
    Also holds all sensor sub classes.
@author Saku Rautiainen <saku.rautiainen@iki.fi>
"""
import os, time, glob
from threading import Timer

#Not sure of the database and what kind it should be yet so import everything.
import database
from constants import SENSOR_ID_LOCATIONS, SENSOR_TIMINGS


DS18B20_BASE_DIR = '/sys/bus/w1/devices/'
DS18B20_DEVICE_FOLDER = glob.glob(DS18B20_BASE_DIR + '28*')[0]
DS18B20_DEVICE_FILE = DS18B20_DEVICE_FOLDER + '/w1_slave'

class sensor(object):
    """ Sensor class. Used for dealing with indiividual sensors. 
        Will hold information such as sensor id, what to do 
        when saving time etc.
        Note that this is baseclass. For each sensor type create its own class.
        Also, if sensor placement/usage dictates different way of saving information, then also
        inherit.
    """

    def __init__(self, sensor_id, descr_str, timing):
        """
        Used to initialize sensor.
        """
        self._sensor_id = sensor_id
        self._descr_str = descr_str
        self._timer = Timer(SENSOR_TIMINGS[sensor_id], sensor.save_value, ())
        self._timer.start()
        
    def __del__(self):
        self._timer.cancel()

    def save_value(self):
        """
            Virtual class
        """
        assert(False)

class ds18b20_sensor(sensor):
    """
        Dallas instruments DS18B20 Temperature sensor handler.
        Used Adafruit code for getting temperature values and 
        converting to celsius code as an example.
        
    """
    
    def __init__(self, sensor_id, descr_str):
        sensor.__init__(self, sensor_id, descr_str)
        #TODO: Check that this sensor is connected, if not throw exception.

    def _get_temperature(self):
        f = open(DS18B20_DEVICE_FILE, 'r')
        lines = f.readlines()
        f.close()
        return lines
        
    def save_value(self):
        """
            Gets Temperature from the sensor and saves it to the database
        """
        #TODO: Create fetching of temperature
        
        lines = self._get_temperature()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self._get_temperature()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            print temp_c
        
        
class weight_sensor(sensor):
    """
        This will be custom weight sensor created using normal scale.
        Hardware not ready yet as such implementation cannot be done.
    """
    def __init__(self, sensor_id, descr_str):
        sensor.__init__(self, sensor_id, descr_str)
        #TODO: Check that this sensor is connected, if not throw exception.
