from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen

"""
screen_4.py

Functions used by WindowFour in screens_setups.py can be found here.
"""


class Row(BoxLayout):
    def remove(self):
        self.parent.remove_widget(self)


class WindowFour(Screen):
    data = [{"subject": "Potato 1", "time": "Time 1"},
            {"subject": "Potato 2", "time": "Time 1"},
            {"subject": "Potato 3", "time": "Time 1"},
            {"subject": "Potato 4", "time": "Time 1"},
            {"subject": "Potato 5", "time": "Time 1"},
            {"subject": "Potato 6", "time": "Time 1"},
            {"subject": "Potato 7", "time": "Time 1"},
            {"subject": "Potato 8", "time": "Time 1"},
            {"subject": "Potato 9", "time": "Time 1"},
            {"subject": "Potato 10", "time": "Time 1"},
            {"subject": "Potato 11", "time": "Time 1"},
            {"subject": "Potato 12", "time": "Time 1"},
            {"subject": "Potato 13", "time": "Time 1"}]

    def on_enter(self, *args):
        self.populate_tasks(self.data)

    def populate_tasks(self, data):
        for i in data:
            row = Row()

            row.ids.task_label.text = f'Subject: {i["subject"]}\nTime:{i["time"]}'

            self.ids.completed_tasks.add_widget(row)
