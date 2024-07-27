#!/bin/bash

if [ "$(docker ps -a -q -f name=ollama)" ]; 
then
    if [ "$(docker ps -aq -f status=exited -f name=ollama)" ];
    then
        echo "Starting Ollama server..."
        docker start ollama
    fi
else
    echo "Running Ollama server..."
    docker run -d --gpus=all -v ./ollama:/root/.ollama -p 11434:11434 --name ollama ollama
fi

echo "Running $1..."
winpty docker exec -it ollama ollama run $1

echo "Prompt is closed in 5s..."
sleep 5s