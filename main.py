from gopigo import *
import time

MIDPOINT = 90


def calibrate():
    print("Pigo online!")
    servo(self.MIDPOINT)
    response = input("Am I looking straight ahead? (y/n): ")
    if response == 'n':
        while True:
            response = '"{}"'.format(input("Turn right, left, or am I done? (r/l/d): "))
            if response == "r":
                self.MIDPOINT += 1
                servo(self.MIDPOINT)
            elif response == "l":
                self.MIDPOINT -= 1
                servo(self.MIDPOINT)
            else:
                print("Midpoint now saved to: " + self.MIDPOINT)


calibrate()



