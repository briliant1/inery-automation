import os
import time
from pprint import pprint
from pick import pick
import logging
import coloredlogs
coloredlogs.install(fmt='[%(asctime)s] [%(levelname)-8s] [%(filename)s:%(lineno)d] %(message)s')
from pathlib import Path


exit = False
current_main_menu_index = None

current_path = Path(__file__)
innery_node_path = os.path.join(current_path.parent.parent, "innery-node")

def main_menu():
    global current_main_menu_index
    title = 'Pilih step mana yang mau kalian kerjakan'
    options = ["Install node part 1", "install node part 2", "Task 1", "Task 2", "Task 3", "Task 4", "Task 5", "Task 6", "Task 7", "Setup Node Config", "Exit"]
    option, index = pick(options, title)
    current_main_menu_index = index
    
def after_task(task_name):
    title = f"{task_name} Done! Please ke menu 'Setup Node'"
    after_task_option = ["Back To Main Menu", "Exit"]
    
    option, index = pick(after_task_option, title)
    

def install_master_node():
    logging.info("Cloning Inery Node")
    if not os.path.exists("./inery-node"):
        os.system(f"git clone https://github.com/inery-blockchain/inery-node {innery_node_path}")
        os.system(f"chmod +x {innery_node_path}/ine.py")
        os.system(f"{innery_node_path}/ine.py --export")
        os.system("cd; source .bashrc; cd -")
    else:
        logging.warning("INERY NODE FOLDER EXISTS!")
        
    title = "Done install Node, silahkan masukkan config kamu, atau kembali ke main menu"
    option = ["Setup Config", "Back To Main Menu", "Exit"]
    
    option, index = pick(option, title)
        

if __name__ == "__main__":
    main_menu()
    if current_main_menu_index == 0:
        install_master_node()
    if current_main_menu_index == 1:
        print("Installing node 2")
    if current_main_menu_index == 2:
        print("Task 1")
    if current_main_menu_index == 3:
        print("Task 2")
    if current_main_menu_index == 4:
        print("Task 3")
    if current_main_menu_index == 5:
        print("Task 4")
    if current_main_menu_index == 6:
        print("Task 5")
    if current_main_menu_index == 7:
        print("Task 6")
    if current_main_menu_index == 8:
        print("Task 7")
    if current_main_menu_index == 9:
        exit = True