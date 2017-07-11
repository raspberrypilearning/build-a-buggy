## Left, right, forward, backward

- It is important to know which is your left motor and which is your right motor. You also need to know which way they are driving to go forward, and which way they are driving to go backwards.

- Choose either of the motors. Use a marker pen to label it 'right' and draw an arrow on it to indicate which way is forward. Label the other motor 'left' and draw an arrow on it pointing in the same direction as your first one.

![labelled motors](images/motors_labelled.jpg)

- Now open a Python shell by clicking **Menu** > **Programming** > **Python 3 (IDLE)**.

- In the shell, type the following to import the `Robot` class and create your `robot`.

	```python
	from gpiozero import Robot
	robot = Robot(left = (7, 8), right = (9, 10))
	```
- Now type the following, and observe which way the motors turn.

	```python
	robot.forward(0.4)
	```

- Now, type the following command, and note which motor changes direction.

	```python
	robot.right(0.4)
	```
- The motor that changed direction is the right-hand motor. If that was the one you labelled **'right'**, then there's nothing to change yet. If it was the one you labelled **'left'**, you need to alter your `robot` object as shown below.

	```python
	robot = Robot(left = (9, 10), right = (7, 8))
	```

Now that you have the 'left' and 'right' sorted, you need to make sure you have **forward** and **backward** setup correctly.

- Again, drive both motors forward.

	```python
	robot.forward(0.4)
	```

- Check that both motors are turning in the direction shown in the diagram below.

![direction of motors](images/motor_direction.png)

- If the right-hand motor is turning in the wrong direction, alter your `robot` object by switching the order of the GPIO pins. For instance:

	```python
	robot = Robot(left = (9, 10), right = (8, 7))
	```

- You would do the same to the order of the pins of the left-hand motor if it was going in the wrong direction.
