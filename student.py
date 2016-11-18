import pigo
import time
import random
from gopigo import *

#TODO: FIX robots option to continue in another direction post obstacle

'''
This class INHERITS your teacher's Pigo class. That means Mr. A can continue to
improve the parent class and it won't overwrite your work.
'''


class GoPiggy(pigo.Pigo):
    # CUSTOM INSTANCE VARIABLES GO HERE. You get the empty self.scan array from Pigo
    # You may want to add a variable to store your default speed
    MIDPOINT = 88
    STOP_DIST = 20
    RIGHT_SPEED = 200
    LEFT_SPEED = 200

    turn_track = 0.0
    TIME_PER_DEGREE = 0.012
    TURN_MODIFIER = .4


    # CONSTRUCTOR
    def __init__(self):
        print("Piggy has be instantiated!")
        # this method makes sure Piggy is looking forward
        #self.calibrate()
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)
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



## NEW TURN METHODS because encR and encL aren't cutting it
    #takes number of degrees and turns accordingly
    def turnR(self, deg):
        # adjust tracker to see how many degrees away the turn is
        self.turn_track += deg
        print ("The exit is " + str.(self.turn_track) + "degrees away!")
        # set speed so we can have a controlled turn
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER, self.RIGHT_SPEED * self.TURN_MODIFIER)
        # actually turn
        right_rot()
        # by using the data from our turn experiment calculate how long we need to turn for
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop
        # return to normal speed
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)

    def turnL(self, tt):
        #adjust tracker to see how many degrees away the turn is
        self.turn_track -= deg
        print ("The exit is " + str.(self.turn_track) + "degrees away!")
        #set speed so we can have a controlled turn
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER, self.RIGHT_SPEED * self.TURN_MODIFIER)
        #actually turn
        left_rot()
        #by using the data from our turn experiment calculate how long we need to turn for
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop
        #return to normal speed
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)

    def setSpeed(self, left, right):
        print("left speed currently set to " + str(left))
        print("right speed currently set to " + str(right))
        set_left_speed(int(left))
        set_right_speed(int(right))
        time.sleep(.05)


# AUTONOMOUS DRIVING
    def nav(self):
        print("Piggy nav")
        ##### WRITE YOUR FINAL PROJECT HERE
        #TODO: if while loop fails check for other paths
        # loop to check the path is clear
        while True:
            choice = self.choosePath()
            if choice == "fwd":
                self.encF(18)
                while self.isClear():
                    self.encF(18)
            elif choice == "right"
                self.turnR(self, deg)
            elif choice == "left"
                self.turnL(self, deg)

#creating the cruise method
    def cruise(self):
        set_left_speed(120)
        set_right_speed(120)
        servo(self.MIDPOINT)
        time.sleep(.05)
        if self.isClear():
            fwd()
            while True:
                if us_dist(15) < self.STOP_DIST:
                    break
                time.sleep(.1)
        self.stop()



        print("Is it safe for me to go?")
        clear= self.isClear()
        print(clear)
        while True:
            if clear:
                print("Let's go boiii")
                fwd()
            if not self.isClear():
                print ("Bruh don't go")
                self.stop()
                answer = self.choosePath()
                if answer == "left":
                    self.encL(6)
                elif answer == "right":
                    self.encR(6)
#checking surroundings while driving to speed up process
    def testDrive(self):
        print ("Here I go")
        fwd()
        while True:
            if us_dist(15) < self.STOP_DIST:
                break
            time.sleep(.05)
        self.stop()
    def chooseBetter(selfself):
        se

####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
