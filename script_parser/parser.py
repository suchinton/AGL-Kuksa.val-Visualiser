from kuksa_client.grpc import VSSClient
from kuksa_client.grpc import Datapoint

import re
import time


def send_update(param,val):
    # try:
        with VSSClient('127.0.0.1', 55555) as client:
            client.set_current_values({
                param: Datapoint(val),
            })
        print(f"Feeding data to client, {param} : {val}")
    #except:
    #    print("Kuska client not configured properly")


script = open('demo_script','r')
content = script.readlines()
print("starting in 2 seconds ...")
time.sleep(2)
for line in content:
    
    if(re.search('set',line)):
        line = line.replace("set(","").replace(")","").replace("\n","")
        updates = line.split(',')
        if(updates[1].isdigit()):
            updates[1] = int(updates[1])
        send_update(updates[0],updates[1])
        print(updates)

    if(re.search('sleep',line)):
        line = line.replace("sleep(","").replace(")","").replace("\n","")
        updates = re.findall('(\d+)',line)
        time.sleep(int(updates[0]))

print("Finished.")


