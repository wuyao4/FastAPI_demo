#!/bin/bash

# Limit the number of workers
# dramatiq utils.actors.dramatiq_task -p $SPIDER_PROCESS_NUM -t $SPIDER_PROCESS_NUM

# Default
# dramatiq utils.actors.dramatiq_task

delay=1
while true; do
  dramatiq app.utils.actors.dramatiq_task -p 1 -t 1
  if [ $? -eq 3 ]; then
    echo "Connection error encountered on startup. Retrying in $delay second(s)..."
    sleep $delay
    delay=$((delay * 2))
  else
    exit $?
  fi
done

