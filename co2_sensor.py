# Write your code here :-)
import RPi.GPIO as GPIO
import time

channel = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    print("CO2/Gas Detected")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)
while True:
        time.sleep(1)
        