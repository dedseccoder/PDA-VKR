#!/usr/bin/python3
#coding=utf-8

import os, sys, time
import Adafruit_DHT as dht
from datetime import datetime

sensor = 22
pin = 4

while True:
    humidity, temperature = dht.read_retry(sensor, pin)
    if (humidity is not None) and (temperature is not None):
        nowtime = datetime.strftime(datetime.now(), "%d.%m.%y %H:%M:%S")
        temperature = str(temperature)
        humidity = str(humidity)
        print(nowtime + "\t" + temperature + "°C\t" + humidity +"%")
        time.sleep(3)

