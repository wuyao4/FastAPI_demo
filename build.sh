#!/usr/bin/env bash
IMAGE_NAME=media-srv
FILENAME=Dockerfile
echo $IMAGE_NAME
echo "[Start building images]"
docker build -f $FILENAME . -t $IMAGE_NAME
#docker build --no-cache -f $FILENAME . -t $IMAGE_NAME
#docker build --cache-from ae7d6a794d5c -t $IMAGE_NAME .

echo "[Build a complete]"
#sleep 2
#echo "[Start pushing the mirror]"
#docker push $IMAGE_NAME
#echo "[Push to complete]"
