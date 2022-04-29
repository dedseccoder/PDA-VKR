#!/usr/bin/python3
#coding=utf-8

import RPi.GPIO as GPIO

input = 14
output = 15

# to use GPIO number not the pin physical number
GPIO.setmode(GPIO.BCM)

#or to use the physical pin numbers (1-40) instead of GPIO number
#GPIO.setmode(GPIO.BOARD)

# setting up pins as I/O
GPIO.setup(input, GPIO.IN) #sets GPIO as INPUT
GPIO.setup(output, GPIO.OUT) #sets GPIO as OUTPUT

# to assign pin input value to a variable
 input_value = GPIO.input(input)

# output to GPIO4
 GPIO.output(4, True)
