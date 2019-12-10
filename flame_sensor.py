import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import RPi.GPIO as GPIO
import time

cred = credentials.Certificate('/home/pi/mu_code/smooth-helper-221215-firebase-adminsdk-ejyyb-a25fcbc542.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smooth-helper-221215.firebaseio.com/'
})

channel = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    print("Flame Detected")
    ref = db.reference('fireStatus')
    ref.update({
    'fireVar': 'true'
})

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback)

while True:
        time.sleep(1)