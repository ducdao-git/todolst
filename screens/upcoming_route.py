from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

import calendar

from libs.get_data import get_next7dates
from libs.custom_kv_widget import DateButton, DateDividerLabel, TaskView


class UpcomingRoute(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app

        # obj python pass by ref -> edit app data within class
        self.upcoming_tasks = app.user_data['upcoming']

        Clock.schedule_once(self.build, 0)

    def build(self, *args):
        self.display_overdue_tasks()
        self.display_on_time_tasks()

    def display_overdue_tasks(self):
        overdue_tasks = self.upcoming_tasks['overdue']
        self.display_date_title(date_str_rep='Overdue')

        for date in overdue_tasks:
            for task in overdue_tasks[date]:
                self.ids.upcoming_scrollview.add_widget(
                    TaskView(self, task, due_date=date.strftime("%b %d"),
                             overdue=True))

    def display_on_time_tasks(self):
        on_time_tasks = self.upcoming_tasks['on_time']
        due_date = on_time_tasks.keys()
        next_7_dates = get_next7dates()

        for date in next_7_dates:
            display_date = calendar.day_name[date.weekday()][
                           :3] + ' ' + date.strftime("%b %d")
            self.display_date_title(date_str_rep=display_date)

            if date in due_date:
                for task in on_time_tasks[date]:
                    self.ids.upcoming_scrollview.add_widget(
                        TaskView(self, task))

    def display_date_title(self, date_str_rep):
        self.ids.upcoming_scrollview.add_widget(
            DateButton(text=date_str_rep))
        self.ids.upcoming_scrollview.add_widget(
            DateDividerLabel())

    def completed_task(self, task_id, taskview_ref):
        # move task from upcoming to completed by id
        for status in self.upcoming_tasks:
            for date in self.upcoming_tasks[status]:
                date_tasks = self.upcoming_tasks[status][date]
                for i in range(len(date_tasks)):
                    if date_tasks[i]['id'] == task_id:
                        self.app.process_task_handler('completed',
                                                      date_tasks[i])
                        del date_tasks[i]

                        if len(date_tasks) == 0:
                            del self.upcoming_tasks[status][date]

                        break

                else:  # if no break then continue the loop
                    continue

                break

            else:  # if inner for loop break then all outer will
                continue

            break

        # remove task from screen
        self.ids.upcoming_scrollview.remove_widget(taskview_ref)
