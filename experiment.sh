#!/bin/bash

for r in {1..150}
do
    echo $r
    LD_LIBRARY_PATH=/usr/local/lib CHURP/src/clock.exe -path .
    sleep 5
done
