## Left, right, forward, backward

You need to figure out which is your left motor and which is your right motor. You also need to know which way they are driving to go forward, and which way they are driving to go backwards.

--- task ---
Choose one of the motors. Use a marker pen to label it 'right' and draw an arrow on it to indicate which way is forward. Label the other motor 'left' and draw an arrow on it pointing in the same direction as your first one.

![labeled motors](images/motors_labelled.jpg)
--- /task ---

--- task ---
Now open **mu** from the Raspberry Pi **Programming menu**. 
--- /task ---

--- task ---
Type the following to import the `Robot` class and create a `Robot` object. You can name it anything you like. In this resource, the robot is called `robby`.

```python
from gpiozero import Robot
robby = Robot(left=(7,8), right=(9,10))
```
--- /task ---

--- task ---
Save you file and call it `robby.py` or something similar. You can then run it by clicking **Run**.
--- /task ---

--- task ---
Now open a python shell by clicking the terminal icon in the taskbar at the top of the screen, then type 'python' and press `Enter`. Now type the following to observe which way the motors turn.

```python
robby.forward()
```

You can stop them by typing `robot.stop()`.

![motors turning](images/motor-test.gif)
--- /task ---

--- task ---
Now, type the following command, and note which motor changes direction on the second command. 

```python
robby.forward(0.4)
robby.right(0.4)
```
The `0.4` makes the motors go a little slower, so it is easy to see which way they turn.
--- /task ---

--- task ---
The motor that changed direction is the right-hand motor. If that was the one you labeled **'right'**, then there's nothing to change yet. If it was the one you labeled **'left'**, you need to alter your `Robot` object in your file to switch around the `left` and `right` pin numbers:


```python
## e.g. change
robby = Robot(left=(7,8), right=(9,10))
## to
robby = Robot(left=(9,10), right=(7,8))
```
--- /task --- 

Now that you have the 'left' and 'right' sorted, you need to make sure you have **forward** and **backward** set up correctly.

--- task ---
Again drive both motors forward.

```python
robby.forward(0.4)
```

Check that both motors are turning in the direction shown in the diagram below.

![direction of motors](images/motor_direction.png)

If the right-hand motor is turning in the wrong direction, alter your `robot` object by switching the order of the GPIO pin numbers. For instance:

```python
## e.g. change
robby = Robot(left=(9,10), right=(7,8))
## to
robby = Robot(left=(9,10), right=(8,7))
```

If the left-hand motor is turning the wrong way, then do the same for its pin numbers.
--- /task ---
