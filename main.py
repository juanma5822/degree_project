from connection import do_connect
from temperature import get_temperature
from dht1122 import get_humidity
from ufirebase import firebase_real_time_database
from ufirebase import firebase_get_data
#from post_data import init
#from post_to_dynamo import do_post
import time
import gc
import machine

gc.collect()
do_connect()

fan = machine.Pin(2,machine.Pin.OUT)
light = machine.Pin(16,machine.Pin.OUT)
while True:
    gc.collect()
    temp = get_temperature()
    get_humidity()
    dic_temp = firebase_get_data("Estado/test")
    temp_setup = dic_temp["temperature"] 
    #do_post()
    print("The temperature configured is: " + str(temp_setup))

    if temp > temp_setup:
        fan.off()
        light.on()
    else:
        fan.on()
        light.off()
    time.sleep(2)
    gc.collect()
