"""
screen_1.py

Functions used by WindowOne in screens_setups.py can be found here.
"""


def update_remaining_tasks(self, remaining_tasks):
    """
    Function written by Kyle Rossi. Updates the view_of_remaining_tasks
    Label on WindowOne to show any new tasks that the user added. This
    function is called as the user transitions from WindowTwo to
    WindowOne, so view_of_remaining_tasks will be updated when the
    user goes back to WindowOne.

    :param self: screens_setup.WindowOne.read_tasks_from_json
    :param remaining_tasks: A list of dictionaries of tasks
    :return: None
    """
    self.ids.view_of_remaining_tasks.text = ""
    screen1_text = ""

    for index in range(len(remaining_tasks)):
        screen1_text += 'Task: ' + remaining_tasks[index]['body'] + '\n'
        screen1_text += 'Time: ' + remaining_tasks[index]['time'] + '\n'

        if remaining_tasks[index]['priority']:
            screen1_text += 'Priority level is: HIGH' + '\n' + '\n'
        else:
            screen1_text += 'Priority level is: LOW' + '\n' + '\n'

    self.ids.view_of_remaining_tasks.text = screen1_text
