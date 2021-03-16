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
            Color(1, 0, 0, 1)
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

    def __init__(self, subject, due_time, **kwargs):
        super().__init__(**kwargs)
        self.text = f'{subject}\n[size={int(dp(16))}][color=228135]' + \
                    f'{due_time}[/color][/size]'

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
        self.bind(active=lambda *args: parent.complete_task(task_id))


class TaskView(BoxLayout):
    def __init__(self, root, task, due_date=None, **kwargs):
        super().__init__(**kwargs)
        self.id = 'task_view_0'
        checkbox = TaskCheckBox(self, task['id'])
        self.add_widget(checkbox)
        self.root = root

        if due_date is None:
            due_time = task['time']
        else:
            due_time = due_date + ' ' + task['time']

        self.add_widget(
            TaskButton(subject=task['subject'], due_time=due_time,
                       size_hint=(5, None)))

        self.bind(minimum_height=self.setter('height'))

    def complete_task(self, task_id):
        Clock.schedule_once(lambda *args: self.remove_taskview(task_id), 0.2)

    def remove_taskview(self, task_id):
        self.root.completed_task(task_id, taskview_ref=self)
