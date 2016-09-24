import pigo


# import time
# import random
# from gopigo import *

class GoPiggy(pigo.Pigo):
    def __init__(self):
        print("Piggy online!")
        self.calibrate()
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.handler()

    def handler(self):
        menu = {"1": ("Navigate forward", self.__nav),
                "2": ("Rotate", self.rotate),
                "3": ("Dance", self.dance),
                "4": ("Calibrate", self.calibrate),
                "5": ("Quit", quit)
                }
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])

        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

    def __nav(self):
        print("Piggy nav")


########################
#### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit

g = GoPiggy()
