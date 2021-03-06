#!/bin/bash

chmod +x *.sh

. ./setup.sh

if [[ "$MY_INDEX" -ne 0 ]]; then
    echo "Cannot start a bulletin with index not null."
    exit 0
fi

LD_LIBRARY_PATH=/usr/local/lib CHURP/src/bb.exe -c $NODE_COUNT -d $DEGREE -path $IP_PATH &
pid=$!

# Wait a bit (give all clients time to start)
echo "Waiting a bit before triggering clock"
sleep 600
echo "Triggering clock"

# Do something (in this case trigger clock signal)
LD_LIBRARY_PATH=/usr/local/lib CHURP/src/clock.exe -path $IP_PATH

# Wait until finish
wait $pid
