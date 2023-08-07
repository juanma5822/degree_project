import  dht
import  machine
import  time
from ufirebase import firebase_real_time_database
# Create a DHT11 object
d = dht.DHT11(machine.Pin(5))  # GPIO5


def get_humidity():
    try:
        d.measure()
        #temp_celsius = d.temperature()
        humidity = d.humidity()
        print("Humidity:", humidity, "%")
        firebase_real_time_database("Estado/humidity", humidity)
    except Exception as e:
        print("Error:", e)
    time.sleep(2)  # Delay before the next reading

