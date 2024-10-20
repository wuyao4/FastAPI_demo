#!/bin/bash

# Overload the font cache
fc-cache

# Start the scheduler
#bash app/scripts/start_dramatiq.sh &
nohup bash app/scripts/start_dramatiq.sh > dramatiq.log 2>&1 &

# Start the service
python app/main.py
