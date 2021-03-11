"""
screens_setup.py

Functionality for all screens are implemented here from their respective
files (i.e. WindowOne uses functions from screen_1.py). Be sure to install
a virtual environment with Kivy before using.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

from screen_1 import update_remaining_tasks
from screen_2 import PostError, create_task

# Lists of arrays of dictionaries that contain task entries.
remaining_tasks = []
completed_tasks = []

# Default largest id for remaining_tasks.
largest_id = 0


class WindowOne(Screen):
    def read_tasks_from_json(self):
        update_remaining_tasks(self, remaining_tasks)


class WindowTwo(Screen):
    def add_task_to_json(self):
        global largest_id
        current_largest_id = largest_id

        try:
            new_task = create_task(self, current_largest_id)
        except PostError as e:
            error_text = str(e)

            content = BoxLayout(orientation='vertical')
            message_label = Label(text=error_text)
            dismiss_button = Button(text='OK')

            content.add_widget(message_label)
            content.add_widget(dismiss_button)

            popup = Popup(title='Error', content=content, size_hint=(0.5, 0.25))
            dismiss_button.bind(on_press=popup.dismiss)
            popup.open()
        else:
            remaining_tasks.append(new_task)
            largest_id += 1

            window_1_access = self.manager.get_screen('window_one')
            window_1_access.read_tasks_from_json()


class WindowThree(Screen):
    pass


class WindowFour(Screen):
    pass


class WindowManager(ScreenManager):
    pass


screens_kv = Builder.load_file('screens.kv')


class ScreensApp(App):
    def build(self):
        return screens_kv


if __name__ == '__main__':
    ScreensApp().run()
