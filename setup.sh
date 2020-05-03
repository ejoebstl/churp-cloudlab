#!/bin/bash

echo "Building Churp..."

## You dont need this when running on docker.
./installChurp.sh

echo "Churp installed."

if [ -z "${NODES}" ]; then
    echo "NODES variable needs to be defined."
    exit 1
fi

if [ -z "${PORT}" ]; then
    echo "PORT variable needs to be defined."
    exit 1
fi

if [ -z "${MY_INDEX}" ]; then
    echo "MY_INDEX variable needs to be defined."
    exit 1
fi

if [ -z "${DEGREE}" ]; then
    echo "DEGREE variable needs to be defined."
    exit 1
fi

if [ ! -d "metadata" ]; then
  mkdir metadata
fi

if [ -d "ip_list" ]; then
  rm ip_list
fi

echo $NODES | sed "s/,/\n/g" | sed "s/$/:${PORT}/" > ip_list

export IP_PATH=$(pwd)
IP_LENGTH=$(wc -l < ip_list)
# Bulletin does not count as node.
export NODE_COUNT=`expr $IP_LENGTH - 1`

echo "Running with Environment:"
echo "NODE_COUNT=${NODE_COUNT}"
echo "IP_PATH=${IP_PATH}"
echo "DEGREE=${DEGREE}"
echo "MY_INDEX=${MY_INDEX}"