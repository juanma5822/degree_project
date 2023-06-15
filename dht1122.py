from dht import DHT11
from machine import Pin
from time import sleep

def get_humidity():
    sensorDHT = DHT11 (Pin(5))
    sleep (1)
    sensorDHT.measure ()
    temp=sensorDHT.temperature ()
    hum=sensorDHT.humidity()

    print ("T={:02f} ºC, H={:02f} %".format (temp,hum))
        
    return hum