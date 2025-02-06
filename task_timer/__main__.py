import click
import datetime
import time
from .task import Task
from .start import create_new_task
from .view import view_tasks


@click.group()
def main():
    '''This is a click group'''

main.add_command(create_new_task)
main.add_command(view_tasks)


# To exit out of current menu have a command here that runs the main function again


