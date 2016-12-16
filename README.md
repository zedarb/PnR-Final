# PnR-Final
The final project for my Programming and Robotics class
OVERVIEW
    The goal of this project was to be able to use Mr. A's code as a base for us to build upon.
    Eventually leading to our robots successfully navigating through a maze.
    In order to use Mr. A's code as a base we adopted a "pigo" file and a class called GoPiggy.
        This GoPiggy class inherits all of Mr. A's code - the parent class.
        We don't edit this code, but we can make improvements and changes iun our "student.py" this is where OUR code is.
        This allows us to continually update the pigo class without losing the work and progress we've made.
            It's like the pigo.py file is our bones and our student.py is our muscles. We can always improve and make our
            muscles bigger, but it is nothing without the bones.
COMMUNICATIONS
    We use the GoPiGo API to speak to our robot. This is the connection between what we type, and what our robot does.
INSTANCE VARIABLES
    These are variables that are universal throughout our code.
        MIDPOINT - the angle where the robot's head is looking forward.
        STOP_DIST - how close the robot can get to an object (in cm) before it stops
        RIGHT AND LEFT SPEED - the number the motors are set to to make the robot move straight
        turn_track - keeps track of turns
        TIME_PER_DEGREE - the time it takes the robot to turn 1 degree
        TURN_MODIFIER - the number multiplied by the motor speeds to reduced speed for more accurate turns
        scan - data of all scans robot has previously made
METHODS
    menu(self) - this is a list of the several commands the robot can complete
        navigate - commands the robot to navigate through obstacles
        rotate - commands the robot to simply turn
        dance - commands robot to do a pre-ade dance
        calibrate - re-centers robot
        status - checks robot power voltage
        quit - allows robot to end its session

    turn(R + L) - method for robot to turn right/left respectively
                    calculates how many degrees needs to turn
                    uses self.setSpeed method to slow down for turn
                    multiplies turn degrees by TIME_PER_DEGREE and actually turns
                    again resets speed to normal
    setSpeed - adjust the robot's speed
    nav - robot's method to move through and navigate through obstacles
                    loops through isClear method to see if it i safe to move forward
                    if so, it proceeds forward using the cruise method
                    if not, the robot backs using self.backup to become a safe distance from object
                    then using kenny's method - sets turn track
                        depending on the scan then turns right or left
    cruise - method to move forward and assist the nav method





