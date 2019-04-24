from gpiozero import Robot
robot = Robot(left = (7, 8), right = (9, 10))
while True:
	robot.forward()
	sleep(3)
	robot.stop()
	robot.right()
	sleep(1)
	robot.stop()
