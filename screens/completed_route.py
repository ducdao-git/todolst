from kivy.uix.screenmanager import Screen
from libs.custom_kv_widget import TaskView


class CompletedRoute(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.completed_tasks = self.app.user_data['completed']

    def on_pre_enter(self, *args):
        self.populate_tasks()

    def on_leave(self):
        self.ids.completed_tasks.clear_widgets()

    def remove_tasks_completed_more_than_24_hours_ago(self):
        self.app.process_task_handler('update_completed', '')

    def remove_task(self, task_id, task_view):
        for task in self.completed_tasks:

            if task['id'] == task_id:
                self.app.process_task_handler('upcoming', task)
                self.completed_tasks.remove(task)
                break

        self.ids.completed_tasks.remove_widget(task_view)

    def populate_tasks(self):
        print('\n before', self.completed_tasks)
        self.remove_tasks_completed_more_than_24_hours_ago()
        print('\n after', self.completed_tasks)

        for task in self.completed_tasks:
            row = TaskView(self, task, checkbox_active=True)
            self.ids.completed_tasks.add_widget(row)
