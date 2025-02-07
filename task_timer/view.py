'''
view.py
Reagan Zierke
2/6/25
This program allows the user to view tasks and end tasks.
'''

from .task import save_tasks, load_tasks
import click
from rich.console import Console
from rich.table import Table

console = Console()



@click.command()
@click.option("--status", default="all", help="Filter tasks by status")
def view_tasks(status):
    '''View tasks'''

    if status == "all":
        view_all_tasks()
    elif status == "running":
        view_running_tasks()
    elif status == "completed":
        view_completed_tasks()
    else:
        console.print("Invalid status")
        return
    

def view_all_tasks():
    '''Loads the tasks and creates a table of all the tasks regardless of status'''

    task_list = load_tasks()
    console.print(create_table(task_list))  


def view_running_tasks():
    '''Loads the tasks and creates a table of all the tasks that are in progress'''

    task_list = load_tasks()
    in_progress_tasks = []

    for task in task_list:
        if task.status == "[bold red]In Progress[/bold red]":
            in_progress_tasks.append(task)
    console.print(create_table(in_progress_tasks))


def view_completed_tasks():
    '''Loads the tasks and creates a table of all the tasks that are complete'''

    task_list = load_tasks()
    complete_tasks = []

    for task in task_list:
        if task.status == "[bold green]Complete[/bold green]":
            complete_tasks.append(task)
    console.print(create_table(complete_tasks))

@click.command()
def end_task():
    '''End a task'''

    task_name = click.prompt("Enter the name of the task you would like to end")
    task_list = load_tasks()

    # Find the task in the list and end it
    for task in task_list:
        if task.name == task_name:
            task.end_task()
            console.print(f"[bold green]Task {task.name} has been completed[/bold green]")
            save_tasks(task_list)
            return
    console.print(f"[bold red]Task {task_name} not found[/bold red]")

def create_table(task_list):
    '''Create a table of tasks'''

    table = Table(title="Task List")
    table.add_column("Name", style="bold")
    table.add_column("Start Time", style="magenta")
    table.add_column("Status", style="green")
    table.add_column("End Time", style="yellow")
    table.add_column("Time Taken", style="blue")

    for task in task_list:
        table.add_row(task.name, str(task.start_time), task.status, str(task.end_time), str(task.time_taken))
    return table