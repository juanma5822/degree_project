from temperature import get_temperature
from ufirebase import firebase_real_time_database
import time
import gc


def init(path, data):
    try:
        gc.collect()
        print('Chameleon Working!...')
        firebase_real_time_database(path, data)
        print('writing data ...')
        print('success!')
    except Exception as e:
        print('Cannot write data ==> FATAL ERROR:', e)
