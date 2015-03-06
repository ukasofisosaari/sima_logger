"""sensor.py
    Implementation of base sensor class.
    Also holds all sensor sub classes.
@author Saku Rautiainen <saku.rautiainen@iki.fi>
"""
import os, time, glob
from threading import Timer

#Not sure of the database and what kind it should be yet so import everything.
import database
from constants import SENSOR_ID_LOCATIONS, SENSOR_TIMINGS, DS18B20_BASE_DIR

class RepeatTimer(object):
    """ Timer that repeats after <interval>. Timer from threading doesnt do this,
        so this improved timer that uses threading.Timer does. """
    def __init__(self, interval, function, args=[], kwargs={}):
        """
        Used to initialize timer

        @param interval nada
        @param function nada
        @param args not needed right now, maybe later
        """
        self._interval = interval
        self._function = function
        self._timer = None
        self._args = args
        self._kwargs = kwargs

    def start(self):
        self._timer = Timer(self._interval, self._function,  *self._args, **self._kwargs)

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

        @param sensor_id nada
        @param descr_str nada
        """
        print("Creating sensor with id: %s, with timing: %d and description: %s" % (sensor_id, SENSOR_TIMINGS[sensor_id], descr_str))
        self._sensor_id = sensor_id
        self._descr_str = descr_str
        self._timer = RepeatTimer(SENSOR_TIMINGS[sensor_id], self.save_value, ())
        self._timer.start()

    def _get_value(self):
        """
            Virtual class.
        """
        assert(False)

    def save_value(self):
        """ Wrapper that handler commong operations for saving values and calls virtual function """
        value = self._get_value()
        print("From sensor: %s / %s got value: %s" % (self._sensor_id, self._descr_str, value))
        self._timer.start()

class ds18b20_sensor(sensor):
    """
        Dallas instruments DS18B20 Temperature sensor handler.
        Used Adafruit code for getting temperature values and 
        converting to celsius code as an example.
        
    """
    
    def __init__(self, sensor_id, descr_str):
        sensor.__init__(self, sensor_id, descr_str)
        self._device_file = glob.glob(DS18B20_BASE_DIR + sensor_id) + '/w1_slave'
        #TODO: Check that this sensor is connected, if not throw exception.

    def _get_raw_data(self):
        f = open(self._device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
        
    def _get_value(self):
        """
            Gets Temperature from the sensor and saves it to the database
            @return Returns the value from the sensor
        """
        #TODO: Create fetching of temperature
        
        lines = self._get_raw_data()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self._get_raw_data()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            return temp_c
        
        
class weight_sensor(sensor):
    """
        This will be custom weight sensor created using normal scale.
        Hardware not ready yet as such implementation cannot be done.
    """
    def __init__(self, sensor_id, descr_str):
        sensor.__init__(self, sensor_id, descr_str)
        #TODO: Check that this sensor is connected, if not throw exception.
