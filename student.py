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

    def nav(self):
        print("Piggy nav")


g = GoPiggy()
