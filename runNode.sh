#!/bin/bash

./setup.sh

if [[ "$MY_INDEX" -eq 0 ]]; then
    echo "Cannot start a node with index 0. Index 0 must be the bulletin."
    exit 0
fi

./node.exe -l $MY_INDEX -c $NODE_COUNT -d $DEGREE -path $IP_PATH &