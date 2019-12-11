import sqlite3
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
TRIG = 16
GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)


conn = sqlite3.connect('echo.db')
c = conn.cursor()

c.execute('SELECT name, type, pin FROM sensors')
sensors = []


def getEcho(pin):
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)

    while GPIO.input(pin) == 0:
        pass
    start = time.time()

    while GPIO.input(pin) == 1:
        pass
    stop = time.time()
    return (stop-start)*170


for row in c:
    sensor_name, sensor_type, pin = row
    print('Found sensor: {0} of type: {1} on pin: {2}'.format(
        sensor_name, sensor_type, pin))
    if sensor_type == 'ultrasonic':
        GPIO.setup(pin, GPIO.IN)
    sensors.append((sensor_name, sensor_type, pin))

while True:
    for s in sensors:
        sensor_name, sensor_type, pin = s
        reading_time = time.time()
        distance = getEcho(pin)
        print('Sensor: {0} distance'.format(distance))
        c.execute('INSERT INTO readings VALUES (?, ?, ?)',
                  (reading_time, format(sensor_name), distance))
        conn.commit()
    time.sleep(1.0)
