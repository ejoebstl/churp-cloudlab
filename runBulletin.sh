#!/bin/bash

chmod +x *.sh

. ./setup.sh

if [[ "$MY_INDEX" -ne 0 ]]; then
    echo "Cannot start a bulletin with index not null."
    exit 0
fi

CHURP/src/bb.exe -c $NODE_COUNT -d $DEGREE -path $IP_PATH &
pid=$!

# Wait a bit (give all clients time to start)
sleep 10

# Do something (in this case trigger clock signal)
LD_LIBRARY_PATH=/usr/local/lib CHURP/src/clock.exe -path $IP_PATH

# Wait until finish
wait $pid