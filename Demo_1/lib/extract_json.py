from kuksa_client.grpc import VSSClient
from kuksa_client.grpc import Datapoint

data  = VSSClient.get_server_info()
print(data)