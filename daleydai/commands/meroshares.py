import click
import json

from daleydai.constants import CONFIG_FILE

from daleydai.utils import add_mero_shares


@click.command()
def show():

    with open(CONFIG_FILE, "r+") as file:
        data = file.readline()

    data_dict = json.loads(data)
    print(data_dict)


@click.command()
@click.argument("stock")
def add(stock: str):
    add_mero_shares(stock)


@click.command()
@click.argument("stock")
def remove(stock: str):
    print(stock)
