## Using a Line Sensor

A line sensor works by shining infrared light onto the ground and then measuring the amount of light that is reflected back. If enough light is reflected back then the sensor must be over a white or shiny surface and if little light is reflected back then it must be over a dark or non-reflective surface.

Some line sensors you can buy are analogue sensors, meaning they will tell you how much light is being reflected back. These can be tricky to work with on a Raspberry Pi, although it is possible.

The line sensor used in this project is a digital sensor. This means it will return a `1` or a `0` depending on whether it is over a dark surface or a light surface. Some digital line sensors can be tuned, although the one is this project is preset.

## Connecting your line sensor

1. The line sensor is easy to set up. Using male-to-female jumper leads, connect the pin labelled GND on the sensor to any GND pin on yout Raspberry Pi.

1. Next connect the pin labelled VCC to the 3v3 pin on your Raspberry Pi.

1. Lastly you can connect the pin labelled OUT to any GPIO pin on your Pi. Here pin 18 is used.

## Testing you line sensor

1. A line sensor has also been included in the gpiozero library, so it's easy to test that your line sensor is working correctly. First import the `LineSensor` class and then create an object for the line sensor on pin 18.

	```python
	from gpiozero import LineSensor
	ls = linesensor(18)
	```
2. There are a few methods that you can use with the a linesensor. For instance you can halt your program until a the line sensor is over a line.

	```python
	ls.wait_for_line()
	print('Found a line')
	```
	
3. Draw a thick black line on a piece of paper, or use black tape. Then with the line sensor face down on the paper, run your script and then move the line sensor so that it passes slowly over the black line. You should see `Found a line` printed in the shell. There's a similar method called `wait_for_no_line()`. See if you can get this one to work.

4. Another useful method is `when_line` and `when_no_line`. These can be used to run functions that you have written. Have a play with the code below, and try and understadn what is happening.

	```
	from gpiozero import LineSensor
	ls = LineSensor(18)

	def a_line():
		print('Found a line')

	def no_line():
		print('No line')

	when_line = a_line
	when_no_line = no_line
	```
	
## What Next?

You can now include the Line Sensor in your robot project. If that's as muchas you want to do, then you can build your robot's chasis and then start coding it to follow a line. Have a look at the links below to see where to go next.

1. Using an ultrasonic sensor to detect obstacles
1. Using a line sensor to follow lines
1. Building a chasis for your robot
1. Programming your buggy to avoid obstacles
1. Programming your buggy to follow a line
1. Programming yout buggy to use a Wiimote
1. Programming your buggy to do everything


