#!/usr/bin/python3
import accounts
import os
import time
from pick import pick
import logging
import coloredlogs
from pathlib import Path
import json
from screenutils import list_screens, Screen
from task_logger import TaskLogger, Task
import updater

coloredlogs.install(fmt='[%(asctime)s] [%(levelname)-8s] [%(filename)s:%(lineno)d] %(message)s')


updater.check_update()

version = open(os.path.join(Path(__file__).parent, "version"), "r")
current_version = version.readline()

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
    
    menu_wallet = f"Wallet Menu"
    menu_wallet_create_wallet = f"Create New Wallet"
    menu_wallet_unlock = "Unlock Wallet"

    menu_check_node = "Check Node"

    menu_task_one = f"Task 1 | {TaskLogger().get_log_status(Task.TASK_ONE)} {TaskLogger().get_log_date(Task.TASK_ONE)}"
    menu_task_two = f"Task 2 | {TaskLogger().get_log_status(Task.TASK_TWO)} {TaskLogger().get_log_date(Task.TASK_TWO)}"
    menu_task_three = f"Task 3 (NOT READY) | {TaskLogger().get_log_status(Task.TASK_TRHEE)} {TaskLogger().get_log_date(Task.TASK_TRHEE)}"
    menu_task_four = f"Task 4 (NOT READY) | {TaskLogger().get_log_status(Task.TASK_FOUR)} {TaskLogger().get_log_date(Task.TASK_FOUR)}"
    menu_task_five = f"Task 5 (NOT READY) | {TaskLogger().get_log_status(Task.TASK_FIVE)} {TaskLogger().get_log_date(Task.TASK_FIVE)}"
    menu_task_six = f"Task 6 (NOT READY) | {TaskLogger().get_log_status(Task.TASK_SIX)} {TaskLogger().get_log_date(Task.TASK_SIX)}"
    menu_task_seven = f"Task 7 (NOT READY) | {TaskLogger().get_log_status(Task.TASK_SEVEN)} {TaskLogger().get_log_date(Task.TASK_SEVEN)}"
    menu_check_update = f"Check Update"

    title = f"""================={current_version}====================
MAIN MENU:
===========================================

MASTER NODE MENU : Menu buat setup node dan setup node config
Wallet Menu      : Create, Unlock Wallet
Task 1 - 7       : Buat jalankan task 1 -7 ( 1 - 7 Masih WIP BELUM FINAL )

==========================================="""
    options = [menu_master_menu, menu_wallet, menu_check_node, menu_task_one, menu_task_two, menu_task_three, menu_task_four, menu_task_five, menu_task_six, menu_task_seven,menu_check_update, "Exit"]
    option, index = pick(options, title, indicator="➤")
    
    if option == menu_master_menu:
        master_title = f"""================={current_version}====================
MASTER NODE MENU:
===========================================

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

    if option == menu_wallet:
        options = [menu_wallet_create_wallet, menu_wallet_unlock, "Back to Main Menu"]

        option, index = pick(options, title, indicator="➤")

        if option == menu_wallet_create_wallet:
            create_wallet()
        if option == menu_wallet_unlock:
            unlock_wallet()

    if option == menu_check_node:
        os.system("screen -R master")
    if option == menu_task_one:
        task_one()
    if option == menu_task_two:
        task_two()
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
    if option == menu_check_update:
        updater.manual_update()
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

def create_wallet():
    log("Masukkan detail wallet")
    print(current_path.parent.parent)
    nama_wallet = input("Nama wallet yang di mau:")
    os.system(f"cline wallet create -n {nama_wallet} -f $HOME/wallet.txt")
    logging.info(f"Import {config_file().get_master_account_name} private key ke wallet {nama_wallet}")
    os.system(f"cline wallet import --private-key {config_file().get_master_private_key} -n {nama_wallet}")
    

def unlock_wallet():
    get_wallet_password = open(os.path.join(current_path.parent.parent, "wallet.txt"), "r")
    wallet_password = get_wallet_password.readline()
    log("Masukkan detail wallet")
    log(f"Pastikan password wallet ada di path ini `{current_path.parent.parent}/wallet.txt`")
    nama_wallet = input("Nama wallet:")
    os.system(f'echo "{wallet_password}" | cline wallet unlock -n {nama_wallet}')
    logging.info(f"WALLET {nama_wallet} unlocked!")

def task_one():
    logging.critical("PASTIKAN SUDAH CLAIM 50.000 INR DI DASHBOARD!")
    os.system(f"cline system regproducer {config_file().get_master_account_name} {config_file().get_master_pubblic_key} 0.0.0.0:9010")
    os.system(f"cline system makeprod approve {config_file().get_master_account_name} {config_file().get_master_account_name}")
    TaskLogger().set_task_done(Task.TASK_ONE)

def task_two():
    logging.info("UNLOCKING WALLET")
    unlock_wallet()
    os.system("cline get code inery.token -c token.wasm -a token.abi --wasm")
    os.system(f"cline set code -j {config_file().get_master_account_name} token.wasm")
    os.system(f"cline set abi {config_file().get_master_account_name} token.abi")
    log("CREATE NEW TOKEN!")
    token_symbol = input("Masukkan 3 digit token symbol, `contoh: INDRO` :")
    token_supply = input("Masukkan supply token, `contoh: 50000.0000` :")
    token_memo = input("Masukkan token description/memo :")
    total_token_to_send = input("Berapa token yang mau di kirim ( per akun ) `contoh: 1.0000`:")
    transfer_message = input("Message buat transfer token :")

    accs = accounts.get_node_accounts(10)

    logging.info("CREATING NEW TOKEN")
    data = os.system(f'''cline push action inery.token create '["{config_file().get_master_account_name}", "{token_supply} {token_symbol}"], "{token_memo}"' -p {config_file().get_master_account_name}''')
    logging.warning(data)
    logging.info("ISSUEING NEW TOKEN")
    os.system(f'''cline push action inery.token issue '["{config_file().get_master_account_name}", "{token_supply} {token_symbol}", "{token_memo}"]' -p {config_file().get_master_account_name}''')
    logging.info("SENDING TOKEN!")
    os.system(f'''cline push action inery.token transfer '["{config_file().get_master_account_name}", "inery", "{total_token_to_send} {token_symbol}", "{transfer_message}"]' -p {config_file().get_master_account_name}''')

    for acc in accs:
        os.system(f'''cline push action inery.token transfer '["{config_file().get_master_account_name}", "{acc}", "{total_token_to_send} {token_symbol}", "{transfer_message}"]' -p {config_file().get_master_account_name}''')
        time.sleep(3)

if __name__ == "__main__":
    main_menu()