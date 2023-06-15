import urequests, random
from temperature import get_temperature
from dht1122 import get_humidity

def do_post():
    letters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWQYZ"
    id =  "".join(random.choice(letters) for _ in range(len(letters)))
    print('ID CREATED ==>',id)
    url  = 'https://hv0bo12fnk.execute-api.us-east-1.amazonaws.com/api/post_logs'
    temperature = str(get_temperature())
    humidity = str(get_humidity())
    payload = {"id": id,"table_name":"chameleon_logs","temperature": temperature, "humidity": humidity}
    try:
        request = urequests.post(url, json=payload)
        print(request.text)
    except Exception as e:
        print("Fatal error  =>>:  " , e,"  ",request.status_code)
        
    return temperature, humidity
        
        
