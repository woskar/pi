import RPi.GPIO as GPIO #import GPIO library
from time import sleep #import time module
GPIO.setmode(GPIO.BCM) #set pin numbering system

yellowLed = 17 #put pin connected to the yellow LED in variable
blinkTimes = range(6) #create list and put it in a variable

GPIO.setup(yellowLed, GPIO.OUT) #set the LED pin as output

#iterate through list held in blinkTimes variable
for i in blinkTimes: 
	#blink LED 
    	GPIO.output(yellowLed, True)
    	sleep(0.3)
    	GPIO.output(yellowLed, False)
    	sleep(0.3)
