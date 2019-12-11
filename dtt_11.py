import threading
import time

import Adafruit_DHT
import RPi.GPIO as GPIO
import sys

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 5,delay_seconds=.1)

    #print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    print(time.ctime())
    print(temperature, humidity)