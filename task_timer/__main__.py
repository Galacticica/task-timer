import click
from .task import initdb, dropdb, hi

@click.group()
def cli():
    """Main command group"""

cli.add_command(initdb)
cli.add_command(dropdb)
cli.add_command(hi)

@cli.command()
def main():
    """Main click"""
    click.echo("Hello")

@cli.command()
def hello():
    """Hello command"""
    click.echo("Testing 1 2 3")
