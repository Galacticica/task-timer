import datetime

class Task():

    def __init__(self, name, start_time = datetime.datetime.now(), status = "In Progress"):
        self.name = name
        self.start_time = start_time
        self.status = status

    def __str__(self):
        return f"{self.name} started at {self.start_time} and is {self.status}"
    
    def __repr__(self):
        return f"{self.name} started at {self.start_time} and is {self.status}"
    
    def end_task(self):
        self.end_time = datetime.datetime.now()
        self.status = "Complete"
        self.time_taken = self.end_time - self.start_time

task_list = []