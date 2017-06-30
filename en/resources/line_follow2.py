from gpiozero import LineSensor, Robot
from time import sleep, time

robot = Robot(left=(7, 8), right=(9, 10))
line = LineSensor(18)

speed = 0.8

def on_line():
    print('running on')
    robot.forward(speed)

def find_line():
    print('running find')
    robot.stop()
    sleep(0.2)
    period = 0.05
    while True:

        start = time()
        robot.right(speed+0.1)
        while time() < (start + period):
            print('Searching right with period,',period)      
            if line.line_detected:
                robot.stop()
                print('line detected')
                return 1
            pass
        period += 0.05
        robot.stop()
        start = time()
        robot.left(speed)
        while time() < (start + period):
            print('Searching right with period,',period)
            if line.line_detected:
                robot.stop()
                print('line detected')
                return 1
            pass
        robot.stop()
        period += 0.05

while True:
    if line.line_detected:
        on_line()
    else:
        find_line()
