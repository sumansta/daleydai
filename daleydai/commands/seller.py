import click

from daleydai.scraper import fetch_broker_data


@click.command()
@click.argument("id")
def seller(id: int):
    """
    Fetch sold shares by broker id
    """
    fetch_broker_data(id, isBuy=False)
