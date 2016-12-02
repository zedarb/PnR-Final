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

    # we wanted a better way to turn
    turn_track = 0.0
    #we found time for a 90 degree turn and adjusted it per degree
    TIME_PER_DEGREE = 0.012
    #robot has to go at speed 80 in order to run accurately
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
        # let's use an event-driven model, make a handler of sorts to listen for "events"
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
        print ("The exit is " + str(self.turn_track) + "degrees away!")
        # set speed so we can have a controlled turn
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER, self.RIGHT_SPEED * self.TURN_MODIFIER)
        # actually turn
        right_rot()
        # by using the data from our turn experiment calculate how long we need to turn for
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop
        # return to normal speed
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)

    def turnL(self, deg):
        #adjust tracker to see how many degrees away the turn is
        self.turn_track -= deg
        print ("The exit is " + str(self.turn_track) + "degrees away!")
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
    #central logic loop of navigation
    def nav(self):
        print("Piggy nav")
        #main app loop
        ##### WRITE YOUR FINAL PROJECT HERE
        #TODO: if while loop fails check for other paths
        # loop to check the path is clear
        while True:
            #CRUISE FORWARD
            if self.isClear():
                #if clear proceed forward
                self.cruise()
           #if I had to stop, Pick a better path
            turn_target = self.kenny()

            if turn_target < 0:
                self.turnR(abs(turn_target))
            else:
                self.turnL(turn_target)


            ##if choice == "right":
            # TODO: replace 5 with a variable presenting a smarter option
                self.turnR(45)
                #self.turnR(turn_target)
            ###elif choice == "left":
                self.turnL(45)
                # self.turnR(turn_target)
            ###else:
                print("no path ahead")
                break
    #replacement turn method
    def kenny(self):
        #use built in wide scan
        self.wideScan()
        #count will keep track of contiguous positive readings
        count = 0
        #list of all the open paths we detect
        option = [0]
        SAFETY_BUFFER = 10
        INC = 2

        #######################################################
        ### Build the options
        #######################################################
        for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60):
            if self.scan[x]:
                #add number if you want extra safety buffer
                if self.scan[x] > (self.STOP_DIST + SAFETY_BUFFER)
                    count += 1
                # if this reading isn't safe..
                else:
                    #aww darn I have to reset count, this path won't work
                    count = 0
                if count == (20/INC)
                    # SUCCESS I've found enough positive readings in a row to count
                    print 'Found an option from' + str(x-20) + 'to' + str(x)
                    count = 0
                    option.apped(x-10)
        ###################################################
        ## PICK FROM OPTIONS
        ##########################################
        bestoption = 90
        for x in option:
            #skip our filler option
            if not x.__index__() == 0
                print("Choice # " + str(x.__index__()) + " is @" + str(x) + "degrees")
                ideal = self.turn_track + self.MIDPOINT
                print("My ideal choice would be " + (self.turn_track -(x - self.MIDPOINT)) )
            if bestoption > abs(ideal - x):
                 bestoption = abs(ideal - x)
                 winner = x - self.MIDPOINT
        return winner



    #creating the cruise method
    def cruise(self):
        self.setSpeed(120,120)
        if self.isClear():
            servo(self.MIDPOINT)
            time.sleep(.05)
            fwd()
            while True:
                if us_dist(15) < self.STOP_DIST:
                    break
                time.sleep(.05)
        self.stop()



    #checking surroundings while driving to speed up process
    def testDrive(self):
        print ("Here I go")
        fwd()
        while True:
            if us_dist(15) < self.STOP_DIST:
                break
            time.sleep(.05)
        self.stop()

    def testTurn(selfself):
        self.turnR(50)
        self.turnL(60)
        input('Accurate reporting?')

####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
