import os
import sys
import json

from daleydai import console

from daleydai.constants import CONFIG_DIR, CONFIG_FILE, STOCKS_LIST_FILE


def create_required_files():
    console.print("[blue]Creating config files")
    if not os.path.exists(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)

    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "w+"):
            pass

    if not os.path.exists(STOCKS_LIST_FILE):
        with open(STOCKS_LIST_FILE, "w+"):
            pass


def add_mero_shares(stock: str):
    with open(CONFIG_FILE, "r+") as file:
        data = file.readline()

        if not data:
            value = {stock: 11}
            json.dump(value, file)
            sys.exit()

        data_dict = json.loads(data)

        if stock not in data_dict:
            data_dict[stock] = 11

        file.seek(0)
        json.dump(data_dict, file)
