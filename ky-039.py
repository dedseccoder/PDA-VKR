#!/usr/bin/python3
#coding=utf-8

import time
import serial
from datetime import datetime

ser = serial.Serial('/dev/ttyS0', 9600, timeout=5)

while True:
	input_str = ser.readline()
	nowtime = datetime.strftime(datetime.now(), "%d.%m.%y %H:%M:%S")
	pulse = input_str.decode("utf-8").strip() 
	print(nowtime + '\t' + pulse)

