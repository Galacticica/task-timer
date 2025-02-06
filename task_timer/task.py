import datetime
import pickle
import os

class Task():

    def __init__(self, name, start_time = datetime.datetime.now(), status = "In Progress"):
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
        self.end_time = datetime.datetime.now()
        self.status = "Complete"
        self.time_taken = self.end_time - self.start_time

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