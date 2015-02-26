"""main.py

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

def init_tables():
    #TODO: Check if table has been created alread

    #if not then create


def init():

    #Create class for each sensor and then create timer.
    for sensor in SENSOR_TIMING.keys():
        Timer(SENSOR_TIMING[sensor], print_time, ()).start()

def main():

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    #Save something to database
    cursor.execute("CREATE TABLE DS18B20( measurement_id INT NOT NULL AUTO_INCREMENT, \
                      sensor_id INT NOT NULL, \
                      date DATE NOT NULL, \
                      time TIME NOT NULL, \
                      value varchar(50), \
                      PRIMARY KEY ( measurement_id ))")
    conn.commit()

    

    #Retrieve what was saved to confirm it works.
    cursor.execute("SELECT * FROM Cars")

    rows = cursor.fetchall()

    for row in rows:
        print "Id: %d, Model: %s, Price: %d" % (row[0], row[1], row[2])
    if conn:
        conn.close()
    

if __name__ == "__main__":
    main()
