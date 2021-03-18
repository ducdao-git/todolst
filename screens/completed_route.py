import datetime

from kivy.uix.screenmanager import Screen
from libs.custom_kv_widget import TaskView

"""
screen_4.py

Functions used by WindowFour in screens_setups.py can be found here.
"""


class CompletedRoute(Screen):
    def __init__(self, app, **kw):
        super().__init__(**kw)
        self.app = app
        self.completed_tasks = self.app.user_data['completed']

    def on_enter(self, *args):
        self.populate_tasks()

    def on_leave(self):
        self.ids.completed_tasks.clear_widgets()

    def remove_tasks_completed_more_than_24_hours_ago(self):
        ids_to_remove = []
        current_time = datetime.datetime.today()
        for task in self.completed_tasks:
            time_difference = current_time - task['completed_time']
            if time_difference.days > 1:
                ids_to_remove.append(task['id'])
        self.completed_tasks = [task for task in self.completed_tasks
                                if task['id'] not in ids_to_remove]

    def remove_task(self, task_id, task_view):
        task_to_remove = {}
        for task in self.completed_tasks:
            if task['id'] == task_id:
                task_to_remove = task
                self.completed_tasks.remove(task)
                break
        self.ids.completed_tasks.remove_widget(task_view)
        self.app.process_task_handler('completed', task_to_remove)

    def populate_tasks(self):
        self.remove_tasks_completed_more_than_24_hours_ago()
        for i in self.completed_tasks:
            row = TaskView(self, i)
            self.ids.completed_tasks.add_widget(row)
