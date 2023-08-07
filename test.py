import network
from machine import Pin
import machine
import time
from time import sleep
import utime
import urequests
import json
import gc
import dht

#from connection import do_connect



red = network.WLAN(network.STA_IF)
red.active(True)
red.connect("MERCHAN ROMERO","3147819989")
print("connection succesfull...")

ventilador = Pin(2,Pin.OUT)
d = dht.DHT11(machine.Pin(5))

#sendor_humidity = Pin(10, Pin.IN)
class MAX6675():
    def __init__(self, so_pin=13, cs_pin=15, sck_pin=14):
        self.cs = Pin(cs_pin, Pin.OUT)
        self.so = Pin(so_pin, Pin.IN)
        self.sck = Pin(sck_pin, Pin.OUT)
        self.cs.on()
        self.so.off()
        self.sck.off()

        self.last_read_time = utime.ticks_ms()

    def readFahrenheit(self):
        return  self.readCelsius() * 9.0 / 5.0 + 32

    def readCelsius(self):
        data = self.__read_data()
        volts = sum([b * (1 << i) for i, b in enumerate(reversed(data))])
        #print(volts)

        return volts * 0.25

    def __read_data(self):
        # CS down, read bytes then cs up
        self.cs.off()
        utime.sleep_us(10)
        data = self.__read_word() # (self.__read_byte() << 8) | self.__read_byte()
        self.cs.on()

        #print(data)
        #print(data[1:-3])

        if data[-3] == 1:
            raise NoThermocoupleAttached()

        return data[1:-3]

    def __read_word(self):
        return [self.__read_bit() for _ in range(16)]


    def __read_bit(self):
        self.sck.off()
        utime.sleep_us(10)
        bit = self.so.value()
        self.sck.on()
        utime.sleep_us(10)
        return bit

def firebase_real_time_database(path, data):
    print('init firebase function')
    location = path
    project_id = "estado-73a8e"
    temp = data
    data = json.dumps(temp)
    url = f"https://{project_id}.firebaseio.com/{location}.json"
    try:
        gc.collect()
        print('init request to firebase...')
        request = urequests.post(url, data=data)
        print("data pushed =>", request.status_code)
        request.close()
        print('closing connection')

    except Exception as e:
        print('cannot upload data ==>', e)
        request = urequests.put(url,data=data)
        request.close()


def firebase_get_data(path):
    location = path
    project_id = "estado-73a8e"
    url = f"https://{project_id}.firebaseio.com/{location}.json"
    try:
        gc.collect()
        request = urequests.get(url)
        data = request.json()
        request.close()
        return data

    except Exception as e:
        print('cannot read data ==>', e)
        #request = urequests.put(url,data=data)
        request.close()



def get_temperature():
    max = MAX6675()
    print(max.readCelsius())
    sleep(2)
    return max.readCelsius()

def get_humidity():
    try:
        d.measure()
        temp_celsius = d.temperature()
        humidity = d.humidity()
        print("Temperature:", temp_celsius, "°C")
        print("Humidity:", humidity, "%")
        firebase_real_time_database("Estado/humidity",humidity)
    except Exception as e:
        print("Error:", e)
    sleep(2)  # Delay before the next reading


while True:
    hum = get_humidity()
    temp=get_temperature()
    firebase_real_time_database(path="Estado/temperature",data= temp)
    dic_temp= firebase_get_data("Estado/test")
    temp_setup = dic_temp["temperature"]
    print("The temperature configured is: " + str(temp_setup))

    if temp > temp_setup:
        ventilador.off()
    else:
        ventilador.on()

