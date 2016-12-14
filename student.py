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
    MIDPOINT = 86
    STOP_DIST = 30
    speed = 100
    TURNSPEED = 185
    scan = [None] * 180
    '''
    turn_track = 0
    TIME_PER_DEGREE = 0.00466667
    TURN_MODIFIER =
    '''

    # CONSTRUCTOR (I moved this to be on the top as you said)
    # This method starts my robot
    def __init__(self):
        print("Piggy has be instantiated!")
        # this method makes sure Piggy is looking forward
        #self.calibrate()
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.menu()


    #This method adjusts robot motors when turning right or left
    def setSpeed(selfself, X):
        self.speed = complex
        #I edited the speed to a decimal as you said
        set_left_speed(self.speed * 0.8)
        #I'm trying to get rid of my drift going forward changing the speed of the left motor
        set_right_speed(self.speed)

    def getSpeed(selfself):
        return self.speed
    '''
        #Adjusts robot motors when turning right or left
        #Newer setSpeed
        def setSpeed(self, left, right):
            print("Left speed: " + str(left))
            print("Right speed: " +str(right))
            set_left_speed(int(left))
            set_right_speed(int(right))
            #Below slows down robot before crashing into something
            time.sleep(0.05)
    '''

    # HANDLE IT
    # This method gives me the menu when I type in python3 student.py
    def menu(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like
        menu = {"1": ("Navigate forward", self.nav),
                "2": ("Rotate", self.rotate),
                "3": ("Dance", self.dance),
                "4": ("Calibrate servo", self.calibrate),
                "5": ("Test Scan", self.chooseBetter),
                "q": ("Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

    # A SIMPLE DANCE ALGORITHM
    # This method is my dance method
    def dance(self):
        print("Piggy dance")
        ##### WRITE YOUR FIRST PROJECT HERE
        print("Is it clear?")
        for x in range(100, 200, 25):
            if not self.isClear():
                print("Omgorsh, it's not safe!")
                break
            print('Speed is set to: ' + str(x))
            servo(87)
            set_speed(x)
            self.encF(3)
            self.encB(3)
            self.encL(10)
            servo(20)
            self.encR(10)
            servo(120)
            self.encF(2)
            servo(87)
            self.encB(2)
            servo(20)
            self.encL(20)
            servo(20)
            self.encR(20)
            servo(120)
            self.encL(10)
            servo(20)
            servo(87)
            self.encR(10)
            servo(120)
            self.encF(1)
            servo(10)
            self.encB(1)
            servo(100)
            self.encF(2)
            servo(55)
            self.encB(2)
            servo(20)
            self.encF(3)
            servo(120)
            self.encB(3)
            servo(56)
            self.encF(1)
            servo(120)
            self.encB(1)
            servo(87)
            self.encF(1)
            self.encR(5)
            time.sleep(.1)
    # AUTONOMOUS DRIVING

    # Central logic loop of my navigation
    #Older nav
    def nav(self):
        #main app loop
        print("Piggy nav")
        #Just trying to scan for a wall
        print("Is it clear?")
        #Check that its clear
        while True:
            while self.isClear():
                #lets go forward just a little bit
                self.encF(5)
                #Trying to have my robot not stop if there is a wall and just go left or right
            answer= self.choosePath()
            if answer =="left":
                self.encL(2)
            elif answer == "right":
                self.encR(2)
    '''
    #Central logic loop of my navigation
        #Newer nav
        def nav(self):
            #main app loop
            print("Parent nav")
            while True:
                #I copied this code from the board in class
                #I'm trying to speed up my robot
                if(self.isClear()):
                    print("It looks clear ahead of me. I'm going to cruise")
                    self.cruise()
                #IF I HAD TO STOP, PICK A BETTER PATH
                turn_target = self.kenny()
                if turn_target < 0:
                    self.turnR(abs(turn_target))
                else:
                    self.turnL(turn_target)
    '''

    '''
    ##### MY NEW TURN METHODS because enR and encL just don't cut it
            #takes a number of degrees and turns accordingly
        #This method defines turning right through degrees
        def turnR(self, deg):
            self.turn_track += deg
            print("The exit is " + str(self.turn_track) + "degrees away.")
            self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER,
                          self.RIGHT_SPEED * self.TURN_MODIFIER)
            right_rot()
            time.sleep(deg * self.TIME_PER_DEGREE)
            self.stop()
            self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)
        #This method defines turning left through degrees
        def turnL(self, deg):
            #adjust the tracker so we know how many degrees away our exit is
            self.turn_track -= deg
            print("The exit is " + str(self.turn_track) + "degrees away.")
            #slow down for more exact turning
            self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER,
                          self.RIGHT_SPEED * self.TURN_MODIFIER)
            #do turn stuff
            left_rot()
            #use our experiments to calculate the time needed to turn
            time.sleep(deg * self.TIME_PER_DEGREE)
            self.stop()
            self.setSpeed(self.LEFT_SPEED, self.RIGHT_SPEED)
    '''

    ##### Our code to make the robot go forward and find openings to not just rely on previous turns
    #This method is my scanning method to make sure my robot doesn't smash into things or get stuck
    #################################
    def chooseBetter(self):
        self.flushScan()
        ###Tryig to speed up the scan
        for x in range(self.MIDPOINT-60, self.MIDPOINT+60, 5):
            servo(x)
            time.sleep(.1)
            self.scan[x] = us_dist(15)
            time.sleep(.05)
        count = 0
        option = [0]
        for x in range(self.MIDPOINT-60, self.MIDPOINT+60, 5):
            if self.scan[x] > self.STOP_DIST:
                count += 1
            else:
                count=0
            if count> 9:
                print("Found an option from "+ str(x-20)+" to "+ str(x)+ " degrees")
                count = 0
                option.append(x)
                self.dataBase()

    """
    #Our new code to make the robot go forward and find openings to not just rely on previous turns
    #this method is my scanning method to make sure my robot doesn't smash into things or get stuck
    #################################
    ### THE KENNY METHOD OF SCANNING - experimental
    def kenny(self):
        #Activate our scanner!
        self.wideScan()
        # count will keep track of contigeous positive readings
        count = 0
        # list of all the open paths we detect
        option = [0]
        #YOU DECIDE: What do we add to STOP_DIST when looking for a path fwd?
        SAFETY_BUFFER = 30
        #YOU DECIDE: what increment do you have your wideScan set to?
        INC = 2
        ###########################
        ######### BUILD THE OPTIONS
        #loop from the 60 deg right of our middle to 60 deg left of our middle
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
                #YOU DECIDE: Is 16 degrees the right size to consider as a safe window?
                if count > (16 / INC) - 1:
                    # SUCCESS! I've found enough positive readings in a row
                    print("---FOUND OPTION: from " + str(x - 16) + " to " + str(x))
                    #set the counter up again for next time
                    count = 0
                    #add this option to the list
                    option.append(x - 8)
        ####################################
        ############## PICK FROM THE OPTIONS - experimental
        #The biggest angle away from our midpoint we could possibly see is 90
        bestoption = 90
        #the turn it would take to get us aimed back toward the exit - experimental
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
    """

    """ Code I'm not using, but had in previous code
    # AUTONOMOUS DRIVING
    def cruise(self):
        # do I check is Clear before?
        servo(self.MIDPOINT)
        time.sleep(0.5)
        fwd()
        while True:
            if us_dist(15) < self.STOP_DIST:
                break
            time.sleep(0.05)
        self.stop()
    #Back up method reverses the robot so if the robot gets too close to something
    def backUp(self):
        if us_dist(15) < 10:
            print("Too close. Backing up for half a second")
            bwd()
            time.sleep(.5)
            self.stop()
    """

    #########Ben and I shared the code Mr. A (you) helped create.
    ######Below is copied from Ben's code to select a path
    ########I shared him the code above to start this new process
    #This method is a remote control for my robot
    def dataBase(self):
        menu = {"1": (" Direction Left Four", self.leftTurn4),
                "2": (" Direction Left Two", self.leftTurn2),
                "3": (" Direction Forward Four", self.forward4),
                "4": (" Direction Forward Eight", self.forward8),
                "5": (" Direction Right Two", self.rightTurn2),
                "6": (" Direction Right Four", self.rightTurn4)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()
        # ans = input("Your selection: ")
        # option.get(ans, [None, error])[1]()
    def rightTurn4(self):
        self.encR(4)
    def rightTurn2(self):
        self.encR(2)
    def leftTurn4(self):
        self.encL(4)
    def leftTurn2(self):
        self.encL(2)
    def forward4(self):
        self.encF(4)
    def forward8(self):
        self.encF(8)
    ####################################################
    ############### STATIC FUNCTIONS

def error():
    print('Error in input')
def quit():
    raise SystemExit

####################################################
# THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()