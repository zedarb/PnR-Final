import pigo
import time
import random
from gopigo import *


'''
This class INHERITS your teacher's Pigo class. That means Mr. A can continue to
improve the parent class and it won't overwrite your work.
'''


class GoPiggy(pigo.Pigo):
    ##########################################
    # List of custom instance variables - instantiates a class
    ##########################################

    # Our servo turns the sensor. What angle of the servo( ) method sets it straight?
    MIDPOINT = 88
    # How close can an object get (cm) before we have to stop?
    STOP_DIST = 25
    # What right motor power helps straighten your fwd()?
    RIGHT_SPEED = 200
    #  What left motor power helps straighten your fwd()?
    LEFT_SPEED = 190
    # we wanted a better way to turn
    # lowercase because it changes overtime
    turn_track = 0
    # we found time for a 90 degree turn and adjusted it per degree
    TIME_PER_DEGREE = 0.01
    # robot has to go at speed 80 in order to run accurately
    TURN_MODIFIER = .4
    # list of all prior scans
    scan = [None] * 180

    #######################
    # CONSTRUCTOR - auto-runs when a class is initiated
    #######################
    def __init__(self):
        print("Piggy has be instantiated!")
        # this method makes sure Piggy is looking forward and drives straight
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.menu()

    ##### DISPLAY THE MENU, CALL METHODS BASED ON RESPONSE

    def menu(self):
        ## List of what the robot can be called to do
        menu = {"1": ("Navigate forward", self.nav),
                "2": ("Rotate", self.rotate),
                "3": ("Dance", self.dance),
                "4": ("Calibrate", self.calibrate),
                "5": ("Status", self.status),
                "s": ("Check status", self.status),
                "q": ("Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = input("Your selection: ")
        # activate the item selected
        menu.get(ans, [None, error])[1]()

    #############################
    # Methods that provide specific actions and instructions for the robot to complete
    #############################


    # Directions for how robot will dance
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

    # method for  printing status of battery power
    def status(self):
        print('My power is at  ' + str(volt())+ '  volts')



    ## NEW TURN METHODS because encR and encL aren't cutting it
    #takes number of degrees and turns accordingly
    def turnR(self, deg):
        # adjust tracker to see how many degrees away the turn is
        self.turn_track += deg
        print ("The exit is " + str(self.turn_track) + "degrees away!")
        # set speed so we can have a controlled turn
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER,
                      self.RIGHT_SPEED * self.TURN_MODIFIER)
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
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER,
                      self.RIGHT_SPEED * self.TURN_MODIFIER)
        #actually turn
        left_rot()
        #by using the data from our turn experiment calculate how long we need to turn for
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop
        #return to normal speed
        self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)

    def setSpeed(self, left, right):
        print("\nleft speed currently set to " + str(left) + "//" + "right speed currently set to " + str(right))
        set_left_speed(int(left))
        time.sleep(.05)
        set_right_speed(int(right))
        time.sleep(.05)

    #########################
    # AUTONOMOUS DRIVING
    # central logic loop of navigation
    #########################

    def nav(self):
        print("Piggy nav")
        #main app loop
        # loop to check the path is clear
        # CRUISE FORWARD
        while True:
            # check to see if clear
            if self.isClear():
                # if clear proceed forward
                self.cruise()
                # for extra safety precautions
            self.backUp()
            # if I had to stop, Pick a better path
            turn_target = self.kenny()
            # staying consistent with right being positive and left being negative
            if turn_target > 0:
                self.turnR(turn_target)
            else:
                self.turnL(abs(turn_target))

            #####################################
            # Comment out old code
            #####################################
            ## if choice == "right":
                # self.turnR(45)
                # self.turnR(turn_target)
            ### elif choice == "left":
                ### self.turnL(45)
                # self.turnR(turn_target)
            ### else:
                #print("no path ahead")
               # break
                # creating the cruise method

    def backUp(self):
        if us_dist(15) < 15:
            print("Too close. Backing up for half a second")
            bwd()
            time.sleep(.5)
            self.stop()


    def cruise(self):
        servo(self.MIDPOINT)
        # give the robot time to move
        time.sleep(.05)
        # start driving forward
        fwd()
        # start an infinite loop
        while True:
            # break the loop if the sensor reading is closer than our stop dist
            if us_dist(15) < self.STOP_DIST:
                break
            # YOU DECIDE: How many seconds do you wait in between a check?
            time.sleep(.05)
        # stop if the sensor loop broke
        self.stop()

    # replacement turn method
    def kenny(self):
        # Activate our scanner!
        self.wideScan()
        # count will keep track of contigeous positive readings
        count = 0
        # list of all the open paths we detect
        option = [0]
        # YOU DECIDE: What do we add to STOP_DIST when looking for a path fwd?
        SAFETY_BUFFER = 30
        # YOU DECIDE: what increment do you have your wideScan set to?
        INC = 3

        ###########################
        ######### BUILD THE OPTIONS
        # loop from the 60 deg right of our middle to 60 deg left of our middle
        for x in range(self.MIDPOINT - 60, self.MIDPOINT + 60):
            # ignore all blank spots in the list
            if self.scan[x]:
                # add 30 if you want, this is an extra safety buffer
                if self.scan[x] > (self.STOP_DIST + SAFETY_BUFFER):
                    count += 1
                # if this reading isn't safe...
                else:
                    # aww nuts, I have to reset the count, this path won't work
                    count = 0
                # YOU DECIDE: Is 16 degrees the right size to consider as a safe window?
                if count > (16 / INC) - 1:
                    # SUCCESS! I've found enough positive readings in a row
                    print("---FOUND OPTION: from " + str(x - 16) + " to " + str(x))
                    # set the counter up again for next time
                    count = 0
                    # add this option to the list
                    option.append(x - 8)

        ####################################
        ############## PICK FROM THE OPTIONS - experimental

        # The biggest angle away from our midpoint we could possibly see is 90
        bestoption = 90
        # the turn it would take to get us aimed back toward the exit - experimental
        ideal = -self.turn_track
        print("\nTHINKING. Ideal turn: " + str(ideal) + " degrees\n")
        # x will iterate through all the angles of our path options
        for x in option:
            # skip our filler option
            if x != 0:
                # the change to the midpoint needed to aim at this path
                turn = self.MIDPOINT - x
                # state our logic so debugging is easier
                print("\nPATH @  " + str(x) + " degrees means a turn of " + str(turn))
                # if this option is closer to our ideal than our current best option...
                if abs(ideal - bestoption) > abs(ideal - turn):
                    # store this turn as the best option
                    bestoption = turn
        if bestoption > 0:
            input("\nABOUT TO TURN RIGHT BY: " + str(bestoption) + " degrees")
        else:
            input("\nABOUT TO TURN LEFT BY: " + str(abs(bestoption)) + " degrees")
        return bestoption

    # scan method
    def wideScan(self):
        # dump all previous values
        self.flushScan()
        # YOU DECIDE: What increment should we use when scanning?
        for x in range(self.MIDPOINT-60, self.MIDPOINT+60, +3):
            # move the sensor that's mounted to our servo
            servo(x)
            # give some time for the servo to move
            time.sleep(.1)
            # take our first measurement
            scan1 = us_dist(15)
            time.sleep(.1)
            # double check the distance
            scan2 = us_dist(15)
            # if I found a different distance the second time....
            if abs(scan1 - scan2) > 2:
                scan3 = us_dist(15)
                time.sleep(.1)
                # take another scan and average? the three together - you decide
                scan1 = (scan1+scan2+scan3)/3
            self.scan[x] = scan1
            print("Degree: "+str(x)+", distance: "+str(scan1))
            time.sleep(.01)

    # isClear method that shows the thinking behind the robot on whether or not he camn move forward
    def isClear(self) -> bool:
        # YOU DECIDE: What range from our midpoint should we check?
        for x in range((self.MIDPOINT - 20), (self.MIDPOINT + 20), 5):
            # move the sensor
            servo(x)
            # Give a little time to turn the servo
            time.sleep(.1)
            # Take our first measurement
            scan1 = us_dist(15)
            # Give a little time for the measurement
            time.sleep(.1)
            # Take the same measurement
            scan2 = us_dist(15)
            # Give a little time for the measurement
            time.sleep(.1)
            # if there's a significant difference between the measurements
            if abs(scan1 - scan2) > 2:
                # take a third measurement
                scan3 = us_dist(15)
                time.sleep(.1)
                # take another scan and average? the three together - you decide
                scan1 = (scan1 + scan2 + scan3) / 3
            # store the measurement in our list
            self.scan[x] = scan1
            # print the finding
            print("Degree: " + str(x) + ", distance: " + str(scan1))
            # If any one finding looks bad
            if scan1 < self.STOP_DIST:
                print("\n--isClear method returns FALSE--\n")
                return False
        print("\n--isClear method returns TRUE--\n")
        return True

'''
    #checking surroundings while driving to speed up process
    def testDrive(self):
        print ("Here I go")
        fwd()
        while True:
            if us_dist(15) < self.STOP_DIST:
                break
            time.sleep(.05)
        self.stop()
    #quick test method
    def testTurn(selfself):
        self.turnR(50)
        self.turnL(60)
        input('Accurate reporting?')'''

####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
