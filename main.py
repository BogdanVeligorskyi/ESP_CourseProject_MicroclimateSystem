#!/usr/bin/python
# Python scripts for running Microclimate System.

import sys
import Adafruit_DHT
import time
import datetime

import connection
import roomsDb
import modelsDb
import sensorsDb
import measurementsDb


#roomsDb.create_rooms_table()
#modelsDb.create_models_table()
#sensorsDb.create_sensors_table()
#measurementsDb.create_measurements_table()

#roomsDb.insert_to_rooms_table("Hall", 4.5, 4.5, 2.5, 18.25)
#modelsDb.insert_to_models_table("DHT11", "Humidity", 0, 100)

#modelsDb.update_in_models_table(1, "DHT11", "Humidity", 20, 90)
#modelsDb.insert_to_models_table("DHT11", "Temperature", 0, 50)

#sensorsDb.insert_to_sensors_table(1, 1, 1)
#sensorsDb.delete_from_sensors_table(4)
#measurementsDb.insert_to_measurements_table(1, 25, "18:08")

# default time between two measurements, s
step_s = 10

# parsing command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
# if only 3 arguments were written
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
# if additional 4th argument was written
elif len(sys.argv) == 4 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
    step_s = (sys.argv[3])
else:
    print('Usage: python3 main.py [11|22|2302] <GPIO pin number> <step>')
    print('Example 1: python3 main.py 11 4 - Read from an DHT11 connected to GPIO pin #4')
    print('Example 2: python3 main.py 11 4 15 - Read each 15 seconds from an DHT11 connected to GPIO pin #4')
    sys.exit(1)


# reading temperature and humidity values each 'step_s' seconds
while 1:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    current_datetime = datetime.datetime.now()

    # converting the temperature to Fahrenheit.
    # temperature = temperature * 9/5.0 + 32

    if humidity is not None and temperature is not None:
        print(current_datetime.strftime("%d-%m-%Y %H:%M:%S") +
              ' Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        measurementsDb.insert_to_measurements_table\
            (1, str(humidity),
             str(current_datetime.strftime("%d-%m-%Y %H:%M:%S")))
        measurementsDb.insert_to_measurements_table\
            (2, str(temperature),
             str(current_datetime.strftime("%d-%m-%Y %H:%M:%S")))
    else:
        print('Failed to read humidity or temperature data. Try again!')
        sys.exit(1)
    time.sleep(int(step_s))
