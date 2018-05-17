import RPi.GPIO as GPIO
from time import sleep
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
button = 18
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

yellowLed = 27 #put pin connected to the yellow LED in variable
redLed = 17

GPIO.setup(yellowLed, GPIO.OUT) #set the LED pin as output
GPIO.setup(redLed, GPIO.OUT)

def LedRoutine():
    for i in range(4): 
    #blink LED 
        GPIO.output(redLed, True)
        sleep(0.1)
        GPIO.output(redLed, False)
        sleep(0.1)
        GPIO.output(yellowLed, True)
        sleep(0.1)
        GPIO.output(yellowLed, False)
        sleep(0.1)
    for i in range(4): 
        GPIO.output(redLed, True)
        sleep(0.8)
        GPIO.output(redLed, False)
        sleep(0.8)
    for i in range(4): 
        GPIO.output(redLed, True)
        sleep(0.2)
        GPIO.output(redLed, False)
        sleep(0.2)
    GPIO.output(yellowLed, True)
    GPIO.output(redLed, True)
    sleep(1.2)
    GPIO.output(yellowLed, False)
    GPIO.output(redLed, False)

while True:
    input_state = GPIO.input(button)
    if input_state == True:
        LedRoutine()
        sleep(.4)

GPIO.cleanup()
