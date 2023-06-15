from max6675 import MAX6675
from machine import Pin
import time


def get_temperature():
    max = MAX6675()
    print(max.readCelsius())
    return max.readCelsius()