import time
import helpers
import stairvalues
import random

def danceparty():
	while True:
		for s in range(1,17):
			helpers.set_stair_rgb(s,random.randint(0,255), random.randint(0,255),random.randint(0,255))

def minor_pulse(stairs, r, g, b, max_value):
	counter = 0
	while counter < max_value:
		for stair in stairs:
			helpers.set_stair_rgb(stair, r, g, b, counter)
		counter += 10
	while counter > 0:
		for stair in stairs:
			helpers.set_stair_rgb(stair, r, g, b, counter)
		counter -= 10

# transition()
# args:
# 	stair: 1-16, bottom step is 1, top step is 16
# 	rgb1: 3-ple of red, green, blue value for initial color
# 	rgb2: 3-ple of red, green, blue value for ending color
# 	speed: number of steps to reach the ending color
def transition_rgb(stair_range, rgb1, rgb2, duration):
	rgbpwm1 = helpers.convert_rgb_to_pwm(rgb1[0], rgb1[1], rgb1[2])
	rgbpwm2 = helpers.convert_rgb_to_pwm(rgb2[0], rgb2[1], rgb2[2])
	rgbratio = ((rgbpwm2[0]-rgbpwm1[0])/duration, (rgbpwm2[1]-rgbpwm1[1])/duration, (rgbpwm2[2]-rgbpwm1[2])/duration)

	for stair in stair_range:
		helpers.set_stair_rgb(stair, rgb1[0], rgb1[1], rgb1[2])
	for i in xrange(duration):
		for stair in stair_range:
			helpers.chips[helpers.stairs[stair]['r'][0]].setPWM( helpers.stairs[stair]['r'][1], 0, rgbpwm1[0] + rgbratio[0]*i)

			helpers.chips[helpers.stairs[stair]['g'][0]].setPWM( helpers.stairs[stair]['g'][1], 0, rgbpwm1[1] + rgbratio[1]*i)
			
			helpers.chips[helpers.stairs[stair]['b'][0]].setPWM( helpers.stairs[stair]['b'][1], 0, rgbpwm1[2] + rgbratio[2]*i)
	for stair in stair_range:
		helpers.set_stair_rgb(stair, rgb2[0], rgb2[1], rgb2[2])


def spring_pulse(r, g, b):
	for i in range(-1,16):
		if i > 2:
			helpers.set_stair_rgb(i-2,0,0,0)
		helpers.set_stair_rgb(i-1, r, g, b)
		helpers.set_stair_rgb(i, r, g, b)
		helpers.set_stair_rgb(i+1, r, g, b)
	for i in range(2,19):
		if i > 2:
			helpers.set_stair_rgb(17-(i-2),0,0,0)
		helpers.set_stair_rgb(17-(i-1), r, g, b)
		helpers.set_stair_rgb(17-i, r, g, b)
		helpers.set_stair_rgb(17-(i+1), r, g, b)

def treadmill(r, g, b, size):
	for i in range(0,17+size):
		helpers.set_stair_rgb(i-size,0,0,0)
		# helpers.set_stair_rgb(i-3,0,0,0)
		# helpers.set_stair_rgb(i-10,0,0,0)
		# helpers.set_stair_rgb(i-11,0,0,0)
		for x in range(0, size):
			helpers.set_stair_rgb(i-x, r, g, b)
		time.sleep(.05)

			# helpers.set_stair_rgb(i-5, r, g, b)	
			# helpers.set_stair_rgb(i-4, r, g, b)	
			# helpers.set_stair_rgb(i-3, r, g, b)	
			# helpers.set_stair_rgb(i-2, r, g, b)	
			# helpers.set_stair_rgb(i-1, r, g, b)
			# helpers.set_stair_rgb(i, r, g, b)

def calibrate(x):
		helpers.set_stair_rgb(x,255,0,0)
		time.sleep(.01)
		helpers.set_stair_rgb(x,0,0,0)
		helpers.set_stair_rgb(x,0,255,0)
		time.sleep(.01)
		helpers.set_stair_rgb(x,0,0,0)
		helpers.set_stair_rgb(x,0,0,255)
		time.sleep(.01)
		helpers.set_stair_rgb(x,0,0,0)
		helpers.set_stair_rgb(x,255,255,255)

def calibrate2(x):
		helpers.set_stair_rgb(x,255,0,0)
		time.sleep(.01)
		helpers.set_stair_rgb(x,0,0,0)
		helpers.set_stair_rgb(x,0,255,0)
		time.sleep(.01)
		helpers.set_stair_rgb(x,0,0,0)
		helpers.set_stair_rgb(x,0,0,255)
		time.sleep(.01)
		helpers.set_stair_rgb(x,0,0,0)

def calibrate_all():
	for x in range(1,17):
		calibrate(x)
	time.sleep(1)
	for x in range(1,17):
		calibrate2(17-x)

def all_white():
	for x in range(1,17):
		helpers.set_stair_rgb(x,255,255,255)

