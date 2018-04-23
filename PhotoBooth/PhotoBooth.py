# RaspberryPi PhotoBooth Project
# Created 22.April 2018

#import modules
import RPi.GPIO as GPIO
from time import sleep
import os
import picamera
import pytumblr
from fractions import Fraction
import threading


def drumrolling():
    os.system(drumroll)


def blinking1():
    for i in range(3): 
    #blink LED 
        GPIO.output(redLed, True)
        sleep(0.1)
        GPIO.output(redLed, False)
        sleep(0.1)
        GPIO.output(yellowLed, True)
        sleep(0.1)
        GPIO.output(yellowLed, False)
        sleep(0.1)
    sleep(0.2)

def blinking2():    
    for i in range(2): 
        GPIO.output(redLed, True)
        sleep(0.6)
        GPIO.output(redLed, False)
        sleep(0.6)
    for i in range(5): 
        GPIO.output(redLed, True)
        sleep(0.2)
        GPIO.output(redLed, False)
        sleep(0.2)
    GPIO.output(yellowLed, True)
    GPIO.output(redLed, True)
    sleep(1.2)
    GPIO.output(yellowLed, False)
    GPIO.output(redLed, False)

def camera():
    camera.start_preview() #start camera preview      
    camera.annotate_text = 'Get Ready!' #display text over preview screen
    camera.annotate_text = '1'
    # take 5 photos
    for i, filename in enumerate(camera.capture_continuous('image{counter:02d}.jpg')):
        sleep(2)
        if i == 1:
            camera.annotate_text = '2'
        elif i == 2:
            camera.annotate_text = '3'
        elif i == 3:
            camera.annotate_text = '4'
        elif i == 4:
            camera.annotate_text = '5'
        if i == 5:
            break
    camera.stop_preview() #stop preview 
    os.system(makeVid) #send command to convert images to GIF

def tumblr(): 
    #upload photo to Tumblr
    client.create_photo(
        'your_username', #update to your username
        state="draft",
        tags=["pi photobooth", "raspberry pi", "instructables"],
        data="animation.gif")
    print("uploaded") #let us know GIF has been uploaded

def Loop():
    #read button 
    while True:
        input_state = GPIO.input(button)
        if input_state == True:
            print('Button Pressed')
            sleep(0.2)
            blinking1()
            #if pressed blink yellow LED at two speeds
            #insert drumroll on different thread here
            thr = threading.Thread(target=drumrolling)
            thr.start()
            blinking2()
            for i in range(5): #change to the number of pictures in gif
                os.system(shutter)
            #camera()
            print('uploading') #let us know photo is about to start uploading

            GPIO.output(yellowLed, True)
            #tumblr() #uploading
            sleep(1)
            GPIO.output(yellowLed, False)
            os.system(partyhorn)
    
    GPIO.cleanup() #cleanup GPIO channels

if __name__ == '__main__':
    
    #create variables to hold commands 
    makeVid = "convert -delay 50 image*.jpg animation.gif"
    shutter = "mpg321 sounds/shutter.mp3"
    partyhorn = "mpg321 sounds/partyhorn.mp3"
    drumroll = "mpg321 sounds/drumroll.mp3"

    #create variables to hold pin numbers
    button = 18
    yellowLed = 27 #put pin connected to the yellow LED in variable
    redLed = 17

    # AuthenticateS via OAuth, copy from https://api.tumblr.com/console/calls/user/info
    client = pytumblr.TumblrRestClient(
      'your_consumer_key',
      'your_consumer_secret',
      'your_token',
      'your_token_secret'
    )

    #set up pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(yellowLed, GPIO.OUT) #set the LED pin as output
    GPIO.setup(redLed, GPIO.OUT)

    #camera = picamera.PiCamera() #initiate picamera module and class
    #camera.resolution = (640, 480) #set resolution of picture here
    #camera.brightness = 60 #set brightness settings to help with dark photos
    #camera.annotate_foreground = picamera.Color(y=0.2, u=0, v=0) #set color of annotation 

    Loop()

