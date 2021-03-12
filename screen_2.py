"""
screen_2.py -- Created by Kyle Rossi

Functions used by WindowTwo in screens_setups.py can be found here.
"""

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

# Lists of arrays of dictionaries that contain task entries.
remaining_tasks = []

# Default largest id for remaining_tasks.
largest_id = 0


# Custom Exception used to catch errors in create_task().
class PostError(Exception):
    pass


def create_task(self):
    """
    Turns the task information the user inputs into a dictionary
    that can be transferred back and displayed on WindowOne.
    Includes error-checking that catches when the user enters
    nothing in the body or time TextInputs.

    :param self: screens_setup.WindowTwo.add_task
    :return: The task in dictionary form, task_as_dict
    """
    if self.ids.body.text == "":
        error = 'Make sure the Body field is provided.'
        raise PostError(error)
    if self.ids.time.text == "":
        error = 'Make sure the Time field is provided.'
        raise PostError(error)

    task_as_dict = {
        "id": largest_id,
        "body": self.ids.body.text,
        "time": self.ids.time.text,
        "priority": self.ids.priority.active,
        "status": 0
    }

    return task_as_dict


def add_task_to_json(self):
    global largest_id

    try:
        new_task = create_task(self)
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

        update_remaining_tasks(self)


def update_remaining_tasks(self):
    """
    Updates the view_of_remaining_tasks Label on WindowOne to show
    any new tasks that the user added. This function is called as the
    user transitions from WindowTwo to WindowOne, so view_of_remaining_tasks
    will be updated when the user goes back to WindowOne.

    :param self: screens_setup.WindowTwo.update_tasks
    :return: None
    """

    window_1_access = self.manager.get_screen('window_one')

    window_1_access.ids.view_of_remaining_tasks.text = ""
    screen1_text = ""

    for index in range(len(remaining_tasks)):
        screen1_text += 'Task: ' + remaining_tasks[index]['body'] + '\n'
        screen1_text += 'Time: ' + remaining_tasks[index]['time'] + '\n'

        if remaining_tasks[index]['priority']:
            screen1_text += 'Priority level is: HIGH' + '\n' + '\n'
        else:
            screen1_text += 'Priority level is: LOW' + '\n' + '\n'

    window_1_access.ids.view_of_remaining_tasks.text = screen1_text
