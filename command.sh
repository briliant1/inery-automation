#!/bin/sh
pwd 
sudo apt-get update && sudo apt install git && sudo apt install screen
sudo apt-get install -y make bzip2 automake libbz2-dev libssl-dev doxygen graphviz libgmp3-dev \
autotools-dev libicu-dev python2.7 python2.7-dev python3 python3-dev python3-pip\
autoconf libtool curl zlib1g-dev sudo ruby libusb-1.0-0-dev \
libcurl4-gnutls-dev pkg-config patch llvm-7-dev clang-7 vim-common jq libncurses5 \
sudo ufw allow 22
sudo ufw allow 8888
sudo ufw allow 9010
yes | sudo ufw enable
pip install pick
pip install coloredlogs
pip install screenutils
chmod +x ./inery-automation/ineryMenu.py
export PATH=$PATH:./inery-automation
ineryMenu.py