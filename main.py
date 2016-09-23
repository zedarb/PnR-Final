from gopigo import *
import time


class Pigo(object):
    MIDPOINT = 90

    def __init__(self):
        print("Pigo online!")
        servo(self.MIDPOINT)
        if input("Am I looking straight ahead? (y/n): ") == "n":
            while True:
                response = input("Turn right, left, or am I done? (r/l/d): ")
                if response == "r":
                    self.MIDPOINT += 1
                    servo(self.MIDPOINT)
                elif response == "l":
                    self.MIDPOINT -= 1
                    servo(self.MIDPOINT)
                else:
                    print("Midpoint now saved to: " + self.MIDPOINT)


variableName = Pigo()


