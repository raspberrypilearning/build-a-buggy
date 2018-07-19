## Challenge: program your robot

You can now write a program to control your robot and make it do any number of things.

Here's a simple script to make it go in a square shape (you may need to change the `sleep` functions slightly):

```python
from gpiozero import Robot
robot = Robot(left = (7, 8), right = (9, 10))
while True:
	robot.forward()
	sleep(3)
	robot.stop()
	robot.right()
	sleep(1)
	robot.stop()
```

--- challenge ---
Now is your opportunity to program your robot!

Try and complete one of the following challenges:
1. Make your robot drive in a perfect circle
1. Make your robot drive in a zigzag pattern
1. Make a small maze from household objects and program your robot to navigate it

Don't forget, there are only five basic commands to move your robot:

```python
robot.forward()
robot.backward()
robot.right()
robot.left()
robot.stop()
```
--- /challenge ---
