import urllib3
import logging
import os
import json
from pathlib import Path

user_agent = {'user-agent': 'inery-automation'}

http = urllib3.PoolManager(10, headers=user_agent)

def check_update():
    r = http.request("GET", "https://api.github.com/repos/briliant1/inery-automation/releases/latest")
    dat = r.data.decode("utf-8")
    data = json.loads(dat)

    version_tag = data['tag_name']

    current_version = open(f"{Path(__file__).parent}/version", "r")
    v = current_version.readline()

    if v != version_tag:
        logging.info(f"NEW UPDATE FOUND!")
        logging.info(f"DOWNLOADING {version_tag}")
        manual_update()
        logging.info(f"MENU UPDATED TO {version_tag}")
        logging.info(f"TOLONG RERUN ineryMenu.py nya")
    else:
        logging.info(f"NO NEW UPDATE")

def manual_update():
    os.system(f"rm -rf {Path(__file__).parent}; cd; git clone https://github.com/briliant1/inery-automation.git; chmod +x ./inery-automation/command.sh; chmod +x ./inery-automation/ineryMenu.py;")