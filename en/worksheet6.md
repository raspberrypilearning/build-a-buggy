# Following a line

Robot's aren't programmed to follow lines, just for fun. There are real world uses for a robot that can follow a line autonomously (on it's own).

In warehouses all over the world, robots are programmed to follow lines, stickers and barcodes so that they can navigate with ease from one area to another.

<iframe width="560" height="315" src="https://www.youtube.com/embed/8gy5tYVR-28" frameborder="0" allowfullscreen></iframe>

## Installing your Line Sensor

1. You're going to need to cut a hole in the bottom of your container, to allow the line sensor wires to attach to the Raspberry Pi.

	![line sensor hole](ls-hole.jpg)

1. The line sensor can then be attached to the bottom of your robot, using a little blutac, and the jumper leads passed through the holw.

	![line sensor attached](ls-attached.jpg)

1. Then the jumper leads can be connected to your Raspberry Pi. Here the output pin of the line sensor is attached to GP18 on the Pi.

	![line sensor wired](ls-wired.jpg)

## Coding your line following robot.

There's no single way to code the line following algorithm, and you're going to need to experiment quite heavily, to produce one that is suited to your specific build.

Here is one method you coudl try though:

1. You can start with the basic code, that sets up your robot.

	```python
	from gpiozero import Robot, LineSensor

	remy = Robot(left = (7, 8), right = (9, 10))
	ls = linesensor(18)
	```

1. Now you need to try an figure out the basic algorithm that your robot will use. Try writing it down in structured English to begin with. Something along the lines of:

  1. If over line drive forward
  1. If not over line find line

1. Thinking ahead, the chances are that you'll want to be able to tweak the speed that the robot is running at, so it's probably best to set it as a variable at the start of the algorithm.

```python
speed = 0.5
```

1. The first part of the algorithm is fairly simple. If the robot is on a line, you need it to drive forwards. This can be easily packaged up into a simple function.

```python
def on_line():
    robot.forward(speed)
```

1. This can now be tested. You can use an infinite loop to tell the robot to drive forwards when it's on a line and stop when it loses the line.

```python
while True:
    if ls.line_detected:
        on_line()
    else:
        remy.stop()
```

1. Now you can test that it's all working okay. You'll have to pick up your robot and place it back on a line if it loses it though.

1. Next you need a function to find the line. This can also be broken down into structured English.
  1. Stop the robot
  1. Turn right for x seconds.
  1. Stop
  1. Turn left for 2x seconds.
  1. Stop
  1. Increase x
  1. Repeat until the line is found

1. With this algorithm the robot should scan left and right by every increasing amounts until it finds the line.

1. First you can define the function and stop the robot, giving it a little pause as well.

```python
def find_line():
    robot.stop()
	sleep(0.2)
```

1. Next you can set the time that the robot is going to take to turn right, in it's first scan. This will still be in the funtion.

```python
def find_line():
    robot.stop()
	sleep(0.2)
	periond = 0.25
```



```python
from gpiozero import LineSensor, Robot
from time import sleep, time

robot = Robot(left=(7, 8), right=(9, 10))
line = LineSensor(18)

speed = 0.8

def on_line():
    robot.forward(speed)

def find_line():
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
