## Program your robot

You can now write a program to control your robot and make it do any number of things.

Here's a simple script to make it go in a square shape (you may need to change the `sleep` functions slightly):

```python
from gpiozero import Robot
from time import sleep
robot = Robot(left = (7, 8), right = (9, 10))
while True:
	robot.forward()
	sleep(3)
	robot.stop()
	robot.right()
	sleep(1)
	robot.stop()
```
