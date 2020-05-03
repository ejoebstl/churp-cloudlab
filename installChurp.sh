#!/bin/bash

# Base dependencies
sudo apt-get install gmp-dev flex bison git go

wget https://crypto.stanford.edu/pbc/files/pbc-0.5.14.tar.gz
tar xvzf pbc-0.5.14.tar.gz
cd pbc-0.5.14
./configure
make
sudo make install
cd ..
rm pbc-0.5.14.tar.gz
rm -rf pbc-0.5.14

# CHURP
git clone git@github.com:CHURPTeam/CHURP.git

cd CHURP/src/

make all

cd ../../
