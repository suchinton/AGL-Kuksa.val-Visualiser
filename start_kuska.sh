#!/bin/sh
echo "# To run docker server #"
echo "sudo docker run -it --rm --net=host ghcr.io/eclipse/kuksa.val/databroker:master"
echo "# To run client #"
echo "kuksa-client --ip 127.0.0.1 --port 55555 --protocol grpc --insecure"

