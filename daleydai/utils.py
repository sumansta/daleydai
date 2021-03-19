import os
import json

from daleydai.constants import CONFIG_DIR, CONFIG_FILE


def add_mero_shares(stock: str):
    if not os.path.exists(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)

    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w+"):
            pass

    with open(CONFIG_FILE, "r+") as file:
        data = file.readline()

        if not data:
            value = {stock: 11}
            json.dump(value, file)

        data_dict = json.loads(data)

        if stock not in data_dict:
            data_dict[stock] = 11

        file.seek(0)
        json.dump(data_dict, file)
