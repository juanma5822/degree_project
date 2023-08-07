from max6675 import MAX6675
from machine import Pin
import time
from ufirebase import  firebase_real_time_database

def get_temperature():
    max = MAX6675()
    temp = max.readCelsius()
    print(max.readCelsius())
    firebase_real_time_database("Estado/temperature", temp)
    return  temp
