from gopigo import *
import time

MIDPOINT = 90


def calibrate():
    print("Pigo online!")
    servo(MIDPOINT)
    response = input("Am I looking straight ahead? (y/n): ")
    if response == 'n':
        while True:
            response = '"{}"'.format(input("Turn right, left, or am I done? (r/l/d): "))
            if response == "r":
                MIDPOINT += 1
                servo(MIDPOINT)
            elif response == "l":
                MIDPOINT -= 1
                servo(MIDPOINT)
            else:
                print("Midpoint now saved to: " + MIDPOINT)


calibrate()



