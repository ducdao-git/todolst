from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

"""
screen_4.py

Functions used by WindowFour in screens_setups.py can be found here.
"""


def populate_tasks(root_screen, data):
    for i in data:
        row = BoxLayout()
        row_button = Button()
        row_label = Label()
        row.add_widget(row_button)
        row.add_widget(row_label)

        row_label.text = f'Subject: {i["subject"]}\nTime:{i["time"]}'
        row_button.text = "Press"
        row_button.size_hint_x = 10
        row_label.size_hint_x = 100
        row_button.height = 10

        root_screen.ids.completed_tasks.add_widget(row)
