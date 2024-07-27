#!/bin/bash

if [ "$(docker ps -a -q -f name=ollama)" ]; 
then
    if [ "$(docker ps -aq -f status=running -f name=ollama)" ];
    then
        echo "Stopping the app..."
        #  xdotool key ctrl+q
        docker stop ollama
    fi
fi

echo "Prompt is closed in 5s..."
sleep 5s