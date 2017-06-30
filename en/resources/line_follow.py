from gpiozero import LineSensor, Robot
from time import sleep, time

robot = Robot(left=(7, 8), right=(9, 10))
line = LineSensor(18)

speed = 0.5

def on_line():
    robot.stop()
    sleep(0.2)
    robot.forward(speed)

def find_line():
    robot.stop()
    sleep(0.2)
    robot.right()


line.when_line = on_line
line.when_no_line = find_line
