from kuksa_client.grpc import VSSClient
from kuksa_client.grpc import Datapoint 

import time

with VSSClient('172.0.0.1', 55555) as client:
    for speed in range(0,100):
        client.set_current_values({
        'Vehicle.Powertrain.CombustionEngine.MaxPower': Datapoint(speed),
        })
        print(f"Feeding Vehicle.Powertrain.CombustionEngine.MaxPower to {speed}")
        time.sleep(1)
    print("hi")
print("Finished.")
