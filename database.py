"""main.py

    For handling database. Either SQL or stick with JSON, depending on 
    do I want to edit lines later on.
@author Saku Rautiainen <saku.rautiainen@iki.fi>
"""

import sqlite3

def init_tables():
    #TODO: Check if table has been created already

    #TODO: if not then create
    
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