from libs.get_data import add_item_to_dict
from datetime import datetime


class ProcessTaskHandler:
    def __init__(self, app, _to, task):
        self.upcoming_tasks = app.user_data['upcoming']
        self.completed_tasks = app.user_data['completed']
        self.task = task

        if _to == 'upcoming':
            self.add_upcoming_task()
        elif _to == 'completed':
            self.add_completed_task()
        else:
            raise ValueError()

    def add_upcoming_task(self):
        if "completed_time" in self.task.keys():
            del self.task["completed_time"]

        date, time = self.task["time"].split()
        date = datetime.strptime(date, '%Y-%m-%d').date()
        self.task["time"] = time

        print(self.task)
        add_item_to_dict(self.upcoming_tasks['on_time'], date, self.task)

    def add_completed_task(self):
        print(self.task)
