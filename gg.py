import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(27,GPIO.OUT)

GPIO.output(27,GPIO.HIGH)
time.sleep(1)
GPIO.output(27,GPIO.LOW)
time.sleep(1)
GPIO.output(27,GPIO.HIGH)
time.sleep(1)
GPIO.output(27,GPIO.LOW)


