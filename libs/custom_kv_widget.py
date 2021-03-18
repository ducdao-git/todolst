from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox

from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp

from math import ceil


class DateDividerLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(rgba=self.color)
            self.rect = Rectangle()

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class DateButton(Button):
    """
    custom button use for display date title
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = f'[b][size={int(dp(19))}]' + \
                    ' ' * 4 + f'{self.text}[/size][/b]'

        # before bind / call update on pos & size, they have default value
        #   in python but get auto calculated in kivy
        # bind function pass left side argument to right side function
        self.bind(size=self.update_text_size)

    def update_text_size(self, *args):
        self.text_size = self.width, None


class TaskButton(Button):
    """
    custom button use for display task info
    """

    def __init__(self, subject, due_time, overdue=False, **kwargs):
        super().__init__(**kwargs)
        if overdue:
            duetime_color = self.bad_color
            duetime_icon = self.overdue_icon

        else:
            duetime_color = self.good_color
            duetime_icon = self.ontime_icon

        due_time = f'[size=14sp]{duetime_icon}  {due_time}[/size]'
        self.text = f'{subject}\n' + \
                    f'[color={duetime_color}]{due_time}[/color]'

        self.bind(size=self.update_text_size)
        self.bind(texture_size=self.update_height)

    def update_text_size(self, *args):
        self.text_size = self.width, None

    def update_height(self, *args):
        if self.texture_size[1] < dp(24):
            self.height = dp(32)
        elif not self.texture_size[1] % dp(8) == 0:
            self.height = dp(8) * ceil(self.texture_size[1] / dp(8)) + dp(12)
        else:
            self.height = self.texture_size[1] + dp(12)


class TaskCheckBox(CheckBox):
    def __init__(self, parent, task_id, **kwargs):
        super().__init__(**kwargs)

        # active return 2 pos arg to lambda -- checkbox address, checkbox value
        self.bind(active=lambda *args: parent.remove_task(task_id))


class TaskView(BoxLayout):
    def __init__(self, root, task, due_date=None, overdue=False,
                 checkbox_active=False, **kwargs):
        super().__init__(**kwargs)
        # self.id = 'task_view_0'
        checkbox = TaskCheckBox(self, task['id'], active=checkbox_active)
        self.add_widget(checkbox)
        self.root = root

        if due_date is None:
            due_time = task['time']
        else:
            due_time = due_date + ' ' + task['time']

        self.add_widget(
            TaskButton(subject=task['subject'], due_time=due_time,
                       overdue=overdue, size_hint=(5, None)))

        self.bind(minimum_height=self.setter('height'))

    def remove_task(self, task_id):
        Clock.schedule_once(lambda *args: self.remove_taskview(task_id), 0.3)

    def remove_taskview(self, task_id):
        if self.root.name == 'upcoming_route':
            self.root.completed_task(task_id, taskview_ref=self)
        elif self.root.name == 'completed_route':
            self.root.remove_task(task_id, self)
