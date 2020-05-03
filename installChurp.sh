#!/bin/bash

# Base dependencies
sudo apt-get update
sudo apt-get install -y libgmp-dev flex bison

# Install GO. We need at lest version 1.14
curl -LO https://get.golang.org/$(uname)/go_installer && chmod +x go_installer && sudo ./go_installer && rm go_installer

# Install pbc dependency
wget https://crypto.stanford.edu/pbc/files/pbc-0.5.14.tar.gz
tar xvzf pbc-0.5.14.tar.gz
cd pbc-0.5.14
./configure
make
sudo make install
cd ..

# CHURP
git clone https://github.com/CHURPTeam/CHURP.git

cd CHURP/src/

# Need to run make as root because permissions are somehow messed up.
sudo bash -c "source ~/.bash_profile && make"

cd ../../
