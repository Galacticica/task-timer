from .task import Task, task_list
import click

@click.command()
def create_new_task():
    '''Create a new task to track'''
    new_task = Task(click.prompt("Enter the name of the task"))
    task_list.append(new_task)
    click.echo(f"Task {new_task.name} has been created")
    





