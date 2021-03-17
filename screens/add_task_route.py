from datetime import datetime
from kivy.uix.screenmanager import Screen


# def _datetime_validation(datetime_str):
#     """
#     check validation of datetime
#     :pram datetime_str: string representation of a datetime
#     :return: True if datetime is valid, else False
#     """
#     datetime_str = datetime_str.split()
#     # if datetime_str


# Custom Exception used to catch errors in create_task().
class InvalidTimeError(Exception):
    pass


class AddTaskRoute(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.largest_id = app.user_data['largest_id']

    # def create_task(self):
    #     """
    #     turns the task information the user inputs into a dictionary
    #     that can be transferred back and displayed on UpcomingRoute.
    #
    #     :return: The task in dictionary form, task_as_dict
    #     """
    #     if self.ids.body.text == "":
    #         error = 'Make sure the Body field is provided.'
    #         raise InvalidTimeError(error)
    #
    #     task_as_dict = {
    #         "id": self.largest_id,
    #         "body": self.ids.body.text,
    #         "time": self.ids.time.text,
    #         "priority": self.ids.priority.active,
    #         "status": 0
    #     }
    #
    #     return task_as_dict
    #
    # def _set_due_time(self):
    #     input_time = self.ids.time.text
    #     curr_time = datetime.now()
    #
    #     if not len(input_time):
    #         return curr_time.strftime("%Y-%m-%d %H:%M")
    #     else:
    #         _datetime_validation(input_time)
