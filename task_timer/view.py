from .task import Task, save_tasks, load_tasks
import click
import pickle



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
        click.echo("Invalid status")
        return
    

def view_all_tasks():
    '''View all tasks'''
    task_list = load_tasks()
    for task in task_list:
        click.echo(task)


def view_running_tasks():
    '''View running tasks'''
    task_list = load_tasks()
    for task in task_list:
        if task.status == "In Progress":
            click.echo(task)


def view_completed_tasks():
    '''View completed tasks'''
    task_list = load_tasks()
    for task in task_list:
        if task.status == "Complete":
            click.echo(task)

@click.command()
def end_task():
    '''End a task'''
    task_name = click.prompt("Enter the name of the task you would like to end")
    task_list = load_tasks()
    for task in task_list:
        if task.name == task_name:
            task.end_task()
            click.echo(f"Task {task.name} has been completed")
            save_tasks(task_list)
            return
    click.echo(f"Task {task_name} not found")

