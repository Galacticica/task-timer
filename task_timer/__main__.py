import click
from .task import Task
import datetime
import time

@click.group()
def main():
    '''This is a click group'''
    
@main.command()
def hello():
    """Hello command"""
    click.echo("Testing 1 2 3")

@main.command()
def time_test():
    """Time test"""
    click.echo(datetime.datetime.now())
    start = datetime.datetime.now()
    time.sleep(2)
    click.echo(datetime.datetime.now())
    end = datetime.datetime.now()
    click.echo(end - start)


# "App" for starting new tasks
# "App" for viewing running tasks and ending tasks
# "App" for viewing all tasks
# To exit out of current menu have a command here that runs the main function again


