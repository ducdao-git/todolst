from libs.get_data import add_item_to_dict
from datetime import datetime


def get_curr_date_time():
    curr_time_str = datetime.today().strftime('%Y-%m-%d %H:%M')
    return datetime.strptime(curr_time_str, '%Y-%m-%d %H:%M')


class ProcessTaskHandler:
    def __init__(self, app, _to, task, _date=None):
        self.upcoming_tasks = app.user_data['upcoming']
        self.completed_tasks = app.user_data['completed']

        self.task = task
        self._date = _date

        if _to == 'upcoming':
            self.add_upcoming_task()
        elif _to == 'completed':
            self.add_completed_task()
        elif _to == 'update_completed':
            self.update_completed_task()
        else:
            raise ValueError()

    def add_upcoming_task(self):
        if "completed_time" in self.task.keys():
            del self.task["completed_time"]

        date, time = self.task["time"].split()
        date = datetime.strptime(date, '%Y-%m-%d').date()

        task_due_time = datetime.strptime(self.task["time"], '%Y-%m-%d %H:%M')
        self.task["time"] = time

        if task_due_time <= get_curr_date_time():
            add_item_to_dict(self.upcoming_tasks['overdue'], date, self.task)
        else:
            add_item_to_dict(self.upcoming_tasks['on_time'], date, self.task)

    def add_completed_task(self):
        self.task["completed_time"] = get_curr_date_time()
        self.task["time"] = self._date + ' ' + self.task["time"]

        self.completed_tasks.append(self.task)
        # print('\n' + '-' * 90 + 'to completed: ', self.completed_tasks,
        #       '\n\n')

    def update_completed_task(self):
        completed_tasks_len = len(self.completed_tasks)
        curr_time = get_curr_date_time()

        for i in range(completed_tasks_len):
            time_diff = curr_time - self.completed_tasks[i]['completed_time']

            if time_diff.days > 1:
                del self.completed_tasks[i]
