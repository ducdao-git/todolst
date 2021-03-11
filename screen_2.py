"""
screen_2.py

Functions used by WindowTwo in screens_setups.py can be found here.
"""


# Custom Exception used to catch errors in create_task().
class PostError(Exception):
    pass


def create_task(self, largest_id):
    """
    Function written by Kyle Rossi. Turns the information the
    user inputs into a dictionary that can be transferred back
    to WindowOne. Includes error-checking that catches when the
    user enters nothing in the body or time TextInputs.

    :param self: screens_setup.WindowTwo.add_task_to_json
    :param largest_id: The id assigned to the next task
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
