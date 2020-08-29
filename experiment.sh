#!/bin/bash

for r in {1..50}
do
    echo $r
    LD_LIBRARY_PATH=/usr/local/lib CHURP/src/clock.exe -path .
    sleep 30
done
