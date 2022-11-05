#!/usr/bin/python3

import os
import time
from pick import pick
import logging
import coloredlogs
from pathlib import Path
import json
from screenutils import list_screens, Screen
from task_logger import TaskLogger, Task

coloredlogs.install(fmt='[%(asctime)s] [%(levelname)-8s] [%(filename)s:%(lineno)d] %(message)s')


exit = False
current_main_menu_index = None

current_path = Path(__file__)
innery_node_path = os.path.join(os.getcwd(), "inery-node")
config_path = os.path.join(innery_node_path, "inery.setup", "tools", "config.json")

class config_file:

    @property
    def load_config(self):
        with open(config_path, "r") as conf:
            data = json.load(conf)

        return data

    @property
    def get_master_account_name(self):
        return self.load_config['MASTER_ACCOUNT']['NAME']

    @property
    def get_master_pubblic_key(self):
        return self.load_config['MASTER_ACCOUNT']['PUBLIC_KEY']

    @property
    def get_master_private_key(self):
        return self.load_config['MASTER_ACCOUNT']['PRIVATE_KEY']

    @property
    def get_master_peer_address(self):
        return self.load_config['MASTER_ACCOUNT']['PEER_ADDRESS']

    @property
    def get_genesis_peer_address(self):
        return self.load_config['GENESIS_ACCOUNT']['PEER_ADDRESS']

def log(message):
	print("==================================================")
	print(message.center(50, ' '))
	print("==================================================")

def main_menu():
    global current_main_menu_index

    menu_master_menu = "Master Node Menu"
    menu_install_node    = f"Install Node      | {TaskLogger().get_log_status(Task.INSTALL_NODE)} {TaskLogger().get_log_date(Task.INSTALL_NODE)}"
    menu_install_node_pb = f"Install Part 1B   | {TaskLogger().get_log_status(Task.INSTALL_NODE)} {TaskLogger().get_log_date(Task.INSTALL_NODE)}"
    menu_setup_config    = f"Setup Config      | {TaskLogger().get_log_status(Task.SETUP_CONFIG)} {TaskLogger().get_log_date(Task.SETUP_CONFIG)}"

    menu_check_node = "Check Node"

    menu_task_one = f"Task 1 | {TaskLogger().get_log_status(Task.TASK_ONE)} {TaskLogger().get_log_date(Task.TASK_ONE)}"
    menu_task_two = f"Task 2 | {TaskLogger().get_log_status(Task.TASK_TWO)} {TaskLogger().get_log_date(Task.TASK_TWO)}"
    menu_task_three = f"Task 3 | {TaskLogger().get_log_status(Task.TASK_TRHEE)} {TaskLogger().get_log_date(Task.TASK_TRHEE)}"
    menu_task_four = f"Task 4 | {TaskLogger().get_log_status(Task.TASK_FOUR)} {TaskLogger().get_log_date(Task.TASK_FOUR)}"
    menu_task_five = f"Task 5 | {TaskLogger().get_log_status(Task.TASK_FIVE)} {TaskLogger().get_log_date(Task.TASK_FIVE)}"
    menu_task_six = f"Task 6 | {TaskLogger().get_log_status(Task.TASK_SIX)} {TaskLogger().get_log_date(Task.TASK_SIX)}"
    menu_task_seven = f"Task 7 | {TaskLogger().get_log_status(Task.TASK_SEVEN)} {TaskLogger().get_log_date(Task.TASK_SEVEN)}"

    title = """===========================================
MAIN MENU:
===========================================

MASTER NODE MENU : Menu buat setup node dan setup node config
Task 1 - 7       : Buat jalankan task 1 -7 ( 1 - 7 Masih WIP BELUM FINAL )

==========================================="""
    options = [menu_master_menu, menu_check_node, menu_task_one, menu_task_two, menu_task_three, menu_task_four, menu_task_five, menu_task_six, menu_task_seven, "Exit"]
    option, index = pick(options, title, indicator="➤")
    
    if option == menu_master_menu:
        master_title = """===========================================
MASTER NODE MENU:

Install Node       : Download Inery Node + Setup Config + Start Node Sync
Install Part 1B    : jalankan kalau misalkan udah setup config duluan
Back to Main Menu  : Balik ke menu utama
==========================================="""

        master_opt = [menu_install_node, menu_install_node_pb, menu_setup_config, "Back to Main Menu"]
        master_node_opt, master_node_ind = pick(master_opt, master_title, indicator="➤")

        if master_node_opt == menu_install_node:
            install_master_node()
        if master_node_opt == menu_install_node_pb:
            install_master_node_two()
        if master_node_opt == menu_setup_config:
            setup_config()
        if master_node_opt == "Back to Main Menu":
            main_menu()

    if option == menu_check_node:
        os.system("screen -R maste")
    if option == menu_task_one:
        print("Task 1")
    if option == menu_task_two:
        print("Task 2")
    if option == menu_task_three:
        print("Task 3")
    if option == menu_task_four:
        print("Task 4")
    if option == menu_task_five:
        print("Task 5")
    if option == menu_task_six:
        print("Task 6")
    if option == menu_task_seven:
        print("Task 6")
    if option == "Exit":
        logging.info("EXIT!")
    

def setup_config():
    logging.info("CONFIG SETUP")
    log("CONFIG SETUP")
    account_name = input("insert accountName: ")
    public_key = input("insert publicKey: ")
    private_key = input("insert privateKey: ")
    your_ip = input("insert your IP: ")

    with open(config_path,"r") as jsFile:
        data = json.load(jsFile)

    data['MASTER_ACCOUNT']['NAME'] = account_name
    data['MASTER_ACCOUNT']['PUBLIC_KEY'] = public_key
    data['MASTER_ACCOUNT']['PRIVATE_KEY'] = private_key
    data['MASTER_ACCOUNT']['PEER_ADDRESS'] = f"{your_ip}:9010"

    with open(config_path, "w") as jsFile:
        json.dump(data, jsFile, indent=4)

    logging.info("NODE SYNCING")
    log("NODE START SYNC PILIH MENU CHECK NODE BUAT CHECK STATUSNYA")
    TaskLogger().set_task_done(Task.SETUP_CONFIG)
    install_master_node_two()
    

def install_master_node_two():
    inery_setup_path = os.path.join(innery_node_path, "inery.setup")
    os.system(f"cd {inery_setup_path}")
    logging.info("STARTING MASTER NODE")
    s = Screen("master", True)
    s.send_commands(f"cd {inery_setup_path}")
    s.send_commands(f"./ine.py --master")
    TaskLogger().set_task_done(Task.INSTALL_NODE_B)
    main_menu()

def install_master_node():
    logging.info("CLONING INERY NODE GIT")
    log("CLONING INERY NODE GIT")
    if not os.path.exists(innery_node_path):
        logging.info(os.getcwd())
        logging.info(innery_node_path)
        os.system(f"git clone https://github.com/inery-blockchain/inery-node {innery_node_path}")
        os.system(f"chmod +x {innery_node_path}/inery.setup/ine.py")

        TaskLogger().set_task_done(Task.INSTALL_NODE)
        
    else:
        logging.warning("INERY NODE FOLDER EXISTS!")

    
    setup_config()

if __name__ == "__main__":
    main_menu()