from .task import Task, task_list
import click

@click.group()
def view_tasks():
    '''View tasks'''
    pass

@view_tasks.command()
def view_all_tasks():
    '''View all tasks'''
    for task in task_list:
        click.echo(task)

@view_tasks.command()
def view_running_tasks():
    '''View running tasks'''
    for task in task_list:
        if task.status == "In Progress":
            click.echo(task)

@view_tasks.command()
def view_completed_tasks():
    '''View completed tasks'''
    for task in task_list:
        if task.status == "Complete":
            click.echo(task)

@view_tasks.command()
def end_task():
    '''End a task'''
    task_name = click.prompt("Enter the name of the task you would like to end")
    for task in task_list:
        if task.name == task_name:
            task.end_task()
            click.echo(f"Task {task.name} has been completed")
            return
    click.echo(f"Task {task_name} not found")

