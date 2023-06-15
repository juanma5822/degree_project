from connection import do_connect
#from test_request import test_request
from temperature import get_temperature
from dht1122 import get_humidity
from ufirebase import firebase_real_time_database
from post_data import init
from post_to_dynamo import do_post
import time
import gc
gc.collect()
do_connect()

while (True):
    gc.collect()
    do_post()
    time.sleep(5)
    gc.collect()
