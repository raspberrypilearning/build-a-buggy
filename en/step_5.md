# Following a line

Robot's aren't programmed to follow lines, just for fun. There are real world uses for a robot that can follow a line autonomously (on it's own).

In warehouses all over the world, robots are programmed to follow lines, stickers and barcodes so that they can navigate with ease from one area to another.

<iframe width="560" height="315" src="https://www.youtube.com/embed/8gy5tYVR-28" frameborder="0" allowfullscreen></iframe>

With only a single line-sensor, programming your robot to follow a line can be quite tricky. Have a look at the algorithm below, written in structured English, to see what the robot will have to do.

1. If I'm on a line - move forward
1. If I'm not on a line, turn right to look for the line
1. If the line can't be found, turn left to look for the line
1. Keep turning left and right by greater degrees until the line is found.

This can be be broken up into two basic functions - `on_line` and `find_line`. If the robot is on the line it will run `on_line` and if it loses the line if will run `find_line`

## Installing your Line Sensor

1. You're going to need to cut a hole in the bottom of your container, to allow the line sensor wires to attach to the Raspberry Pi.

	![line sensor hole](ls-hole.jpg)

1. The line sensor can then be attached to the bottom of your robot, using a little blutac, and the jumper leads passed through the holw.

	![line sensor attached](ls-attached.jpg)

1. Then the jumper leads can be connected to your Raspberry Pi. Here the output pin of the line sensor is attached to GP18 on the Pi.

	![line sensor wired](ls-wired.jpg)

## Coding your line following robot.

```python
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
```
