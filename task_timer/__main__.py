'''
__main__.py
Reagan Zierke
2/6/25
This program creates the initialization for a task timer program.
'''

import click
import datetime
import time
from .task import Task, save_tasks, load_tasks
from .start import create_new_task
from .view import view_tasks, end_task


@click.group()
def main():
    '''Welcome to the task timer!'''

main.add_command(create_new_task)
main.add_command(view_tasks)
main.add_command(end_task)

task_list = load_tasks()




