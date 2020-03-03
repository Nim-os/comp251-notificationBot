#!/bin/bash

echo "Starting bot..."

ut=0

while true
do
    # Update uptime
    ut+=1

    # Get page as txt file
    wget luc.devroye.org/251.html -O raw.txt

    # Run Python checker
    python3 checker.py

    rm raw.txt

    # Waiting between wget calls helps prevent requests from being blocked
    echo "Sleeping..."
    sleep 7200
done

echo -e "Bot ended. Up time: $ut cycles"