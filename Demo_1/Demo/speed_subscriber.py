from kuksa_client.grpc import VSSClient

with VSSClient('127.0.0.1', 55555) as client:
    
    for updates in client.subscribe_current_values([
        'Vehicle.Speed',
    ]):
        speed = updates['Vehicle.Speed'].value
        print(f"Received updated speed: {speed}")
        #IsOpen = updates['Vehicle.Trunk.Body.Rear.IsOpen'].value
        #print(f"Received updated speed: {IsOpen}")
