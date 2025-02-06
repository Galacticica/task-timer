import click
import datetime
import time
from .task import Task, task_list
from .start import create_new_task
from .view import view_tasks, end_task


@click.group()
def main():
    '''This is a click group'''

main.add_command(create_new_task)
main.add_command(view_tasks)
main.add_command(end_task)


# To exit out of current menu have a command here that runs the main function again


