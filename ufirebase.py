import urequests
import json
import time
import machine
import gc

def firebase_real_time_database(path, data):
    print('init firebase function')
    location = path
    project_id = "estado-73a8e"
    temp = data
    data = json.dumps(temp)
    print(data)
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
    # Print the response status code to check if the request was successful


    
    