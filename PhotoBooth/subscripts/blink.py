import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
Led = 17
GPIO.setup(Led, GPIO.OUT)
while True: 
	GPIO.output(Led, True) 
	sleep(0.5) 
	GPIO.output(Led, False) 
	sleep(0.5)
