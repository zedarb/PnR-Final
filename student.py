import pigo
import time
import random
from gopigo import *

'''
This class INHERITS your teacher's Pigo class. That means Mr. A can continue to
improve the parent class and it won't overwrite your work.
'''


class GoPiggy(pigo.Pigo):
    # CUSTOM INSTANCE VARIABLES GO HERE. You get the empty self.scan array from Pigo
    # You may want to add a variable to store your default speed
    MIDPOINT = 88
    STOP_DIST = 20


    # CONSTRUCTOR
    def __init__(self):
        print("Piggy has be instantiated!")
        # this method makes sure Piggy is looking forward
        #self.calibrate()
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.handler()

    ##### HANDLE IT
    def handler(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like
        menu = {"1": ("Navigate forward", self.nav),
                "2": ("Rotate", self.rotate),
                "3": ("Dance", self.dance),
                "4": ("Calibrate servo", self.calibrate),
                "5": ("status", self.status),
                "q": ("Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

    # A SIMPLE DANCE ALGORITHM
    def dance(self):
        print("Piggy dance")
        ##### WRITE YOUR FIRST PROJECT HERE
        print('it is safe to dance')
        for x in range(3):
            if not self.isClear():
                print ("its not safe brotha")
                break
            x = 175
        while self.isClear() and x <= 200:
            print ('speed is set to: ' +str(x))
            self.encL(20)
            self.encB(18)
            self.encF(14)
            self.encR(22)
            self.encL(22)
            servo(20)
            self.encL(15)
            self.encR(15)
            servo(88)
            self.encB(10)
            self.encF(10)
            self.encB(10)
            self.encF(10)
            self.encB(10)
            self.encF(10)
            self.encL(25)
            x += 25
            time.sleep(.1)
            stop()


    def status(self):
        print('My power is at  ' + str(volt())+ '  volts')

    # AUTONOMOUS DRIVING
    def nav(self):
        print("Piggy nav")
        ##### WRITE YOUR FINAL PROJECT HERE
        #TODO: if while loop fails check for other paths

        # loop to check the path is clear
        while True:
            while self.isClear():
            #go forward, but only a little
            self.encF(10)
            #if path is not clear move left or right
            answer = self. choosePath()
            if answer == "right":
                self.encR(6)
            if answer == "left":
                self.encL(6)


####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
