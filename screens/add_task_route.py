"""
screen_2.py -- Created by Kyle Rossi

Functions used by WindowTwo in screens_setups.py can be found here.
"""

from kivy.uix.screenmanager import Screen


# Custom Exception used to catch errors in create_task().
class PostError(Exception):
    pass


class AddTaskRoute(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.largest_id = app.user_data['largest_id']
