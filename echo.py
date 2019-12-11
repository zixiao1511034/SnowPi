import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

TRIG = 16
ECHO = 26

GPIO.setup(TRIG, GPIO.OUT)
GPIO.output(TRIG, 0)

GPIO.setup(ECHO, GPIO.IN)

time.sleep(0.1)

print("Start")

GPIO.output(TRIG, 1)
time.sleep(0.00001)
GPIO.output(TRIG, 0)

while GPIO.input(ECHO) == 0:
    pass
start = time.time()

while GPIO.input(ECHO) == 1:
    pass
stop = time.time()

sound = 331.3 + 0.606 * (-2)
print("distance:", float((stop - start)*sound/2))

GPIO.cleanup()
