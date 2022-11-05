#!/bin/bash
sudo apt-get update && sudo apt install git && sudo apt install screen
yes | sudo apt-get install make
yes | sudo apt-get install bzip2
yes | sudo apt-get install automake
yes | sudo apt-get install libbz2-dev
yes | sudo apt-get install libssl-dev
yes | sudo apt-get install doxygen
yes | sudo apt-get install graphviz
yes | sudo apt-get install libgmp3-dev
yes | sudo apt-get install autotools-dev
yes | sudo apt-get install libicu-dev
yes | sudo apt-get install python2.7
yes | sudo apt-get install python2.7-dev
yes | sudo apt-get install python3
yes | sudo apt-get install python3-dev
yes | sudo apt-get install python3-pip
yes | sudo apt-get install autoconf
yes | sudo apt-get install libtool
yes | sudo apt-get install curl
yes | sudo apt-get install zlib1g-dev
yes | sudo apt-get install sudo
yes | sudo apt-get install ruby
yes | sudo apt-get install libusb-1.0-0-dev
yes | sudo apt-get install libcurl4-gnutls-dev
yes | sudo apt-get install pkg-config
yes | sudo apt-get install patch
yes | sudo apt-get install llvm-7-dev
yes | sudo apt-get install clang-7
yes | sudo apt-get install vim-common
yes | sudo apt-get install jq
yes | sudo apt-get install libncurses5
sudo ufw allow 22
sudo ufw allow 8888
sudo ufw allow 9010
yes | sudo ufw enable
pip install pick
pip install coloredlogs
pip install screenutils
chmod +x ./inery-automation/ineryMenu.py
echo -e "\nPATH=$PATH:$PWD/inery-automation:$PWD/inery-node/inery/bin" >> ~/.profile
ineryMenu.py