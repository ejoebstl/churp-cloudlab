#!/bin/bash

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

if [ -z "${NODE_COUNT}" ]; then
    echo "NODE_COUNT variable needs to be defined."
    exit 1
fi

if [ -z "${DEGREE}" ]; then
    echo "DEGREE variable needs to be defined."
    exit 1
fi

if [ ! -d "metadata" ]; then
  mkdir metadata
fi

export IP_PATH=$(pwd)

if [ -d "ip_list" ]; then
  rm ip_list
fi

echo $NODES | sed "s/;/\n/g" | sed "s/$/:${PORT}/" > ip_list