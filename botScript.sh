#!/bin/bash

echo "Starting bot..."

ut=0

while true
do
    # Update uptime
    ut+=1

    # Get page as txt file and trim page
    wget https://www.luc.devroye.org/251.html -0 raw.txt

    cat raw.txt | grep '' > trim.txt

    # Run Python checker
    python3 checker.py

    rm *.txt

    # Waiting between wget calls helps prevent requests from being blocked
    sleep 3600
done

echo -e "Bot finished. Up time: $ut cycles"