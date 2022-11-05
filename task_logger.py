import os, json
from datetime import datetime
from pathlib import Path
from enum import Enum

class Task(Enum):
    INSTALL_NODE = "INSTALL_NODE"
    INSTALL_NODE_B = "INSTALL_NODE_B"
    SETUP_CONFIG = "SETUP_CONFIG"
    TASK_ONE = "TASK_ONE"
    TASK_TWO = "TASK_TWO"
    TASK_TRHEE = "TASK_THREE"
    TASK_FOUR = "TASK_FOUR"
    TASK_FIVE = "TASK_FIVE"
    TASK_SIX = "TASK_SIX"
    TASK_SEVEN = "TASK_SEVEN"


class TaskLogger:
    def __init__(self) -> None:
        self.outer_path = Path(__file__).parent.parent
        self.config_path = os.path.join(self.outer_path, "task_log.json")

    @property
    def load_logger(self):
        if not os.path.exists(self.config_path):
            with open(self.config_path, "w") as fs:
                json.dump({},fs,indent=4)

        with open(self.config_path, "r") as fs:
            data = json.load(fs)

        return data

    def set_task_done(self, task: Task):
        data = self.load_logger

        if task.value not in data:
            data[task.value] = {"STATUS": "", "DATE": ""}

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data[task.value]["STATUS"] = "✅"
        data[task.value]["DATE"] =  current_time

        with open(self.config_path, "w") as fs:
            json.dump(data, fs, indent=4)


    def get_log_status(self, task: Task):
        data = self.load_logger

        if task.value not in data:
            data[task.value] = {"STATUS": "❌", "DATE": "NONE"}

        return data[task.value]['STATUS']

    def get_log_date(self, task: Task):
        data = self.load_logger

        if task.value not in data:
            data[task.value] = {"STATUS": "❌", "DATE": "NONE"}

        return data[task.value]['DATE']

    def get_status(self, task: Task):
        stat = self.get_log_status(task)
        date = self.get_log_date(task)

        if "NONE" in date:
            return f"{stat}"
        else:
            return f"{stat} last update : {date}"