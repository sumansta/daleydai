import click

from daleydai.commands import buyer, seller


@click.group()
def cli():
    """
    karod bata road....
    """
    pass


cli.add_command(buyer)
cli.add_command(seller)
