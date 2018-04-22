from time import sleep
from threading import Thread
import os

drumroll = "mpg321 sounds/drumroll.mp3"
partyhorn = "mpg321 sounds/partyhorn.mp3"

def routine():
    print('starting')
    sleep(3)
    Thread(target = roll).start()
    print('test')
    sleep(3)
    print('test2')
    sleep(3)

def roll():
    print('Working')
    os.system(drumroll)
    sleep(1)
    print('test')
    sleep(1)
    print('Working')

def horn():
    print('Working')
    os.system(partyhorn)

if __name__ == '__main__':
    routine()
    #Thread(target = func2).start()
    #Thread(target = func1).start()