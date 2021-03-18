import click

from daleydai.scraper import fetch_broker_data


@click.command()
@click.option("--id", default=58, help="Enter seller broker ID")
def seller(id):
    """
    Fetch sold shares by broker id
    """
    fetch_broker_data(id, isBuy=False)