#!/bin/bash

echo "Starting bot..."

ut=0

while true
do
    # Update uptime
    ut+=1

    # Get page as txt file
    wget -q luc.devroye.org/251.html

    # Run Python checker
    python3 checker.py

    rm 251.html

    # Waiting between wget calls helps prevent requests from being blocked
    echo "Sleeping..."
    sleep 7200
done

echo -e "Bot terminated. Up time: $ut cycles"