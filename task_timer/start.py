from .task import Task, save_tasks, load_tasks
import click
import pickle

@click.command()
def create_new_task():
    '''Create a new task to track'''
    task_list = load_tasks()
    new_task = Task(click.prompt("Enter the name of the task"))
    task_list.append(new_task)
    save_tasks(task_list)
    click.echo(f"Task {new_task.name} has been created")






