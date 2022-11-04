import os

from pprint import pprint
from pick import pick
import logging
import coloredlogs
coloredlogs.install(fmt='[%(asctime)s] [%(levelname)-8s] [%(filename)s:%(lineno)d] %(message)s')

title = 'Pilih step mana yang mau kalian kerjakan'
options = ["Install node part 1", "install node part 2", "Task 1", "Task 2", "Task 3", "Task 4", "Task 5", "Task 6", "Task 7"]



def install_master_node():
    logging.info("Cloning Inery Node")
    os.system("git clone https://github.com/inery-blockchain/inery-node")
    os.system("cd inery-node")
    os.system("cd inery.setup")
    os.system("chmod +x ./ine.py")
    os.system("./ine.py --export")
    os.system("cd; source .bashrc; cd -")

while True:
    option, index = pick(options, title)
    if index == 0:
        install_master_node()
    if index == 1:
        print("Installing node 2")
    if index == 2:
        print("Task 1")
    if index == 3:
        print("Task 2")
    if index == 4:
        print("Task 3")
    if index == 5:
        print("Task 4")
    if index == 6:
        print("Task 5")
    if index == 7:
        print("Task 6")
    if index == 8:
        print("Task 7")
