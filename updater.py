import urllib3
import logging
import os
import json
from pathlib import Path

http = urllib3.PoolManager()

def check_update():
    r = http.request("GET", "https://api.github.com/repos/briliant1/inery-automation/releases/latest")

    data = json.loads(r.data.decode("utf-8"))

    version_tag = data['tag_name']

    current_version = open("./version", "r")
    v = current_version.readline()

    if v != version_tag:
        manual_update()
        logging.info(f"MENU UPDATED TO {version_tag}")
    else:
        logging.info(f"NO NEW UPDATE")

def manual_update():
    inery_auto_path = Path(os.getcwd())
    os.system(f"rm -rf {inery_auto_path}; cd; git clone https://github.com/briliant1/inery-automation.git; chmod +x ./inery-automation/command.sh; chmod +x ./inery-automation/ineryMenu.py;")
