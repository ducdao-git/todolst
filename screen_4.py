import datetime

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

"""
screen_4.py

Functions used by WindowFour in screens_setups.py can be found here.
"""


class Row(BoxLayout):
    def __init__(self, id, **kwargs):
        super().__init__(**kwargs)
        self.id = id


class WindowFour(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

        self.data = \
            [{'id': 1, 'subject': 'cs230 hw1', 'time': '2021-03-11 23:59',
              'priority': 'none',
              'completed_time': datetime.datetime(2021, 3, 1, 10, 30)},
             {'id': 2, 'subject': 'cs230 hw2', 'time': '2021-03-12 23:59',
              'priority': 'none',
              'completed_time': datetime.datetime(2021, 3, 2, 10, 30)},
             {'id': 3, 'subject': 'cs230 hw3', 'time': '2021-03-13 23:59',
              'priority': 'none',
              'completed_time': datetime.datetime(2021, 3, 3, 10, 30)},
             {'id': 4, 'subject': 'cs230 hw4', 'time': '2021-03-14 23:59',
              'priority': 'none',
              'completed_time': datetime.datetime(2021, 3, 4, 10, 30)},
             {'id': 5, 'subject': 'cs230 hw5', 'time': '2021-03-15 23:59',
              'priority': 'none',
              'completed_time': datetime.datetime(2021, 3, 5, 10, 30)},
             {'id': 6, 'subject': 'cs230 hw6', 'time': '2021-03-16 23:59',
              'priority': 'none',
              'completed_time': datetime.datetime(2021, 3, 6, 10, 30)},
             {'id': 7, 'subject': 'cs230 hw7', 'time': '2021-03-17 23:59',
              'priority': 'none',
              'completed_time': datetime.datetime(2021, 3, 7, 10, 30)},
             {'id': 8, 'subject': 'cs230 hw8', 'time': '2021-03-18 23:59',
              'priority': 'none',
              'completed_time': datetime.datetime(2021, 3, 8, 10, 30)},
             {'id': 9, 'subject': 'cs230 hw9', 'time': '2021-03-19 23:59',
              'priority': 'none',
              'completed_time': datetime.datetime(2021, 3, 9, 10, 30)}
             ]

    def on_enter(self, *args):
        self.populate_tasks(self.data)

    def on_leave(self):
        self.ids.completed_tasks.clear_widgets()

    def remove_tasks_completed_more_than_24_hours_ago(self):
        ids_to_remove = []
        current_time = datetime.datetime.today()
        for task in self.data:
            time_difference = current_time - task['completed_time']
            if time_difference.days > 1:
                ids_to_remove.append(task['id'])
        self.data = [task for task in self.data
                     if task['id'] not in ids_to_remove]
        print(self.data)

    def populate_tasks(self):
        self.remove_tasks_completed_more_than_24_hours_ago()

        def remove_row(*args):
            pressed_button = args[0]
            for task in self.data:
                if task['id'] == pressed_button.parent.id:
                    self.data.remove(task)
                    break
            self.ids.completed_tasks.remove_widget(pressed_button.parent)

        for i in self.data:
            row = Row(i['id'])

            row.ids.task_label.text = f'Subject: {i["subject"]}\nTime:{i["time"]}'
            row.ids.remove_button.bind(on_release=remove_row)

            self.ids.completed_tasks.add_widget(row)
