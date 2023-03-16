from kuksa_client.grpc import VSSClient

with VSSClient('127.0.0.1', 55555) as client:
    
    for updates in client.subscribe_current_values([
            'Vehicle.Speed',
            'Vehicle.Trunk.isOpen',
        ]):
        speed = updates['Vehicle.Speed'].value
        print(f"Received updated speed: {speed}")
        Trunk_is_Open = updates['Vehicle.Trunk.isOpen'].value
        print(f"Trunk is open: {Trunk_is_Open}")
