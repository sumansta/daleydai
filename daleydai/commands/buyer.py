import click

from daleydai.scraper import fetch_broker_data


@click.command()
@click.option("--id", default=58, help="Enter buyer broker ID")
def buyer(id):
    """
    Fetch bought shares by broker id
    """
    fetch_broker_data(id, isBuy=True)