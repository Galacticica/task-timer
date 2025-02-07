'''
start.py
Reagan Zierke
2/6/25
This program creates a command for a user to start a new task to be tracked.
'''

from .task import Task, save_tasks, load_tasks
import click
from rich.console import Console

console = Console()

@click.command()
def create_new_task():
    '''Create a new task to track'''
    
    task_list = load_tasks()
    new_task = Task(click.prompt("Enter the name of the task"))
    task_list.append(new_task)
    save_tasks(task_list)
    console.print(f"[bold green]Task {new_task.name} created successfully![/bold green]")








