#!/bin/bash

./setup.sh

if [[ "$MY_INDEX" -ne 0 ]]; then
    echo "Cannot start a bulletin with index not null."
    exit 0
fi

./bb.exe -c $NODE_COUNT -d $DEGREE -path $IP_PATH &
./clock.exe -path $IP_PATH