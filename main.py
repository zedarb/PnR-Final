from gopigo import *
import time

class Pigo(object):
    MIDPOINT = 90

    def __init__(self):
        print("Pigo online!")
        fwd()
        time.sleep(1)
        stop()


variableName = Pigo()


