import os

from pprint import pprint
from pick import pick

title = 'Pilih step mana yang mau kalian kerjakan'
options = ["Install node part 1", "install node part 2", "Task 1", "Task 2", "Task 3", "Task 4", "Task 5", "Task 6", "Task 7"]

option, index = pick(options, title)

def install_master_node():
    pass


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
