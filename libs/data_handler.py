class ProcessTaskHandler:
    def __init__(self, app, _to, task):
        self.user_data = app.user_data
        self.task = task

        if _to == 'upcoming':
            self.add_upcoming_task()
        elif _to == 'completed':
            self.add_completed_task()
        else:
            raise ValueError()

    def add_upcoming_task(self):
        print(self.task)

    def add_completed_task(self):
        print(self.task)
