from gpiozero import Robot, DistanceSensor, LineSensor
from time import sleep, time
from threading import Thread

remy = Robot(left=(9, 10), right = (7,8))
#line = LineSensor(18)

#robot.source_delay = 0.5
#speed = 0.6

#ef look_for_line():
#    while True:
#        yield (1, 0.5)  # left motor full speed, right motor half speed
#        yield (0.5, 1)  # left motor half speed, right motor full speed

#while True:
#   robot.forward(speed)
#    line.wait_for_no_line()  # go forward until the line is lost
#    robot.source = look_for_line()  # alternate between slight left and slight right
#    line.wait_for_line()  # until the line is found
#    robot.source = None # unset the source to stop looking left and right
