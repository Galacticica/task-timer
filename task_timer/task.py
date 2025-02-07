'''
task.py
Reagan Zierke
2/6/25
This program creates a task class to store and manage information about the tasks
such as start time, end time, and status.
'''
import datetime
import pickle
import os
import datetime

class Task():

    def __init__(self, name, start_time = datetime.datetime.now(), status = "[bold red]In Progress[/bold red]"):
        self.name = name
        self.start_time = start_time
        self.status = status
        self.end_time = None
        self.time_taken = None

    def __str__(self):
        return f"{self.name} started at {self.start_time} and is {self.status}"
    
    def __repr__(self):
        return f"{self.name} started at {self.start_time} and is {self.status}"
    
    def end_task(self):
        '''
        End the task and calculate the time taken
        '''

        self.end_time = datetime.datetime.now()
        self.status = "[bold green]Complete[/bold green]"
        self.time_taken = self.end_time - self.start_time

    @staticmethod
    def format_datetime(dt):
        """Format datetime as string."""

        if isinstance(dt, datetime.timedelta):  
            return str(dt)  
        return dt.strftime("%Y-%m-%d %H:%M:%S")

def load_tasks():
    """Load tasks from the pickle file."""

    if os.path.exists('tasks.pkl'):
        with open('tasks.pkl', "rb") as f:
            return pickle.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to the pickle file."""
    
    with open('tasks.pkl', "wb") as f:
        pickle.dump(tasks, f)