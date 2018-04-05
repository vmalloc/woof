import click
from . import woof

@click.command()
@click.argument('message', nargs=-1)
def main(message):
    woof.notify(' '.join(message))
