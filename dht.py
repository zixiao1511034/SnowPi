import sys
import Adafruit_DHT
import time

import threading

_lock = threading.Lock()

with _lock:
    while True:

        # humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 5)
        humidity, temperature = Adafruit_DHT.read_retry(11, 5)
        if not humidity or not temperature:
            print("error")
        print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
        time.sleep(2.0)
        # print(time.ctime())