# STUDENTS SHOULD NOT EDIT THIS FILE. IT WILL MAKE UPDATING MORE DIFFICULT

from gopigo import *
import time


##########################################################
#################### PIGO PARENT CLASS
#### (students will make their own class & inherit this)

class Pigo(object):
    MIDPOINT = 77
    scan = [None] * 180

    def __init__(self):
        # this makes sure the parent handler doesn't take over student's
        if __name__ == "__main__":
            print('-----------------------')
            print('------- PARENT --------')
            print('-----------------------')
            self.calibrate()
            # let's use an event-driven model, make a handler of sorts to listen for "events"
            while True:
                self.stop()
                self.handler()

    def handler(self):
        menu = {"1": ("Navigate forward", self.nav),
                "2": ("Rotate", self.rotate),
                "3": ("Dance", self.dance),
                "4": ("Calibrate", self.calibrate),
                "5": ("Quit", quit)
                }
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])

        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

    def nav(self):
        print("Pigo nav")
        self.wideSweep()
        self.thinkAloud()

    def rotate(self):
        print('Rotate')

    def dance(self):
        print('Dance')

    def flushScan(self):
        self.scan = [None]*180

    def wideSweep(self):
        #dump all values
        self.flushScan()
        for x in range(self.MIDPOINT-60, self.MIDPOINT+60, +2):
            servo(x)
            time.sleep(.1)
            scan = us_dist(15)
            self.scan[x] = scan
            print("Degree: "+str(x)+", distance: "+str(scan))
            time.sleep(.01)

    def thinkAloud(self):
        print('Considering options...')
        avgRight = 0;
        avgLeft = 0;
        for x in range(self.MIDPOINT-60, self.MIDPOINT):
            if self.scan[x]:
                avgRight += self.scan[x]
        avgRight /= 60
        print('The average dist on the right is '+str(avgRight)+'cm')
        for x in range(self.MIDPOINT, self.MIDPOINT+60):
            if self.scan[x]:
                avgLeft += self.scan[x]
        avgLeft /= 60
        print('The average dist on the left is ' + str(avgLeft) + 'cm')

    def stop(self):
        print('All stop.')
        for x in range(3):
            stop()
        servo(self.MIDPOINT)
        time.sleep(0.05)
        disable_servo()

    def calibrate(self):
        print("Calibrating...")
        servo(self.MIDPOINT)
        response = input("Am I looking straight ahead? (y/n): ")
        if response == 'n':
            while True:
                response = input("Turn right, left, or am I done? (r/l/d): ")
                if response == "r":
                    self.MIDPOINT += 1
                    print("Midpoint: " + str(self.MIDPOINT))
                    servo(self.MIDPOINT)
                    time.sleep(.01)
                elif response == "l":
                    self.MIDPOINT -= 1
                    print("Midpoint: " + str(self.MIDPOINT))
                    servo(self.MIDPOINT)
                    time.sleep(.01)
                else:
                    print("Midpoint now saved to: " + str(self.MIDPOINT))
                    break


########################
#### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


p = Pigo()
