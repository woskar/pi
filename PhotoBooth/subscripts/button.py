import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
button = 18
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
    input_state = GPIO.input(button)
    if input_state == True:
        print("button pressed")
        sleep(.4)
GPIO.cleanup()
