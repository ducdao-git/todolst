from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox

from kivy.graphics import Color, Rectangle
from kivy.metrics import dp

from math import ceil
import calendar

from libs.get_data import get_user_data, get_next7dates

tree_structure = Builder.load_file('upcoming_route.kv')


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


# don't use as the layout look more complex if add - keep for future use
# class TaskDividerLabel(Label):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#
#         with self.canvas.before:
#             Color(1, 0, 0, 1)
#             self.rect = Rectangle()
#
#         self.bind(pos=self.update_rect, size=self.update_rect)
#
#     def update_rect(self, *args):
#         self.rect.pos = (self.pos[0] + dp(16), self.pos[1])
#         self.rect.size = (self.size[0] - dp(16), self.size[1])


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
    def __init__(self, root, task_id, **kwargs):
        super().__init__(**kwargs)

        # bind try to give 2 pos arg to lambda -- checkbox (address, value)
        self.bind(
            active=lambda cb_address, cb_value: root.completed_task(task_id,
                                                                    cb_address))


class TaskView(BoxLayout):
    def __init__(self, root, task, due_date=None, **kwargs):
        super().__init__(**kwargs)
        self.id = 'task_view_0'
        checkbox = TaskCheckBox(root, task['id'])
        self.add_widget(checkbox)

        if due_date is None:
            due_time = task['time']
        else:
            due_time = due_date + ' ' + task['time']

        self.add_widget(
            TaskButton(subject=task['subject'], due_time=due_time,
                       size_hint=(5, None)))

        # taskview_id = str(task['id'])
        self.bind(minimum_height=self.setter('height'))
        # self.bind(id=self.setter('id'))


class UpcomingRoute(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_data = get_user_data()
        self.upcoming_tasks = self.user_data['upcoming']
        self.theme_palette = self.user_data['theme_palette']
        Clock.schedule_once(self.build, 1)

    def build(self, *args):
        self.display_overdue_tasks()
        self.display_on_time_tasks()
        return tree_structure

    def display_date_title(self, date_str_rep):
        self.ids.upcoming_tasks_list_view.add_widget(
            DateButton(text=date_str_rep))
        self.ids.upcoming_tasks_list_view.add_widget(
            DateDividerLabel())

    def display_overdue_tasks(self):
        overdue_tasks = self.upcoming_tasks['overdue']
        self.display_date_title(date_str_rep='Overdue')

        for date in overdue_tasks:
            for task in overdue_tasks[date]:
                self.ids.upcoming_tasks_list_view.add_widget(
                    TaskView(self, task, due_date=date.strftime("%b %d")))

    def display_on_time_tasks(self):
        on_time_tasks = self.upcoming_tasks['on_time']
        due_date = on_time_tasks.keys()
        next_7_dates = get_next7dates()

        for date in next_7_dates:
            display_date = calendar.day_name[date.weekday()][
                           :3] + ' ' + date.strftime("%b %d")
            self.display_date_title(date_str_rep=display_date)

            if date in due_date:
                for task in on_time_tasks[date]:
                    self.ids.upcoming_tasks_list_view.add_widget(
                        TaskView(self, task))

    def completed_task(self, task_id, cb_address):
        # print('checkpoint')
        for status in self.upcoming_tasks:
            for date in self.upcoming_tasks[status]:
                date_tasks = self.upcoming_tasks[status][date]
                for i in range(len(date_tasks)):
                    if date_tasks[i]['id'] == task_id:
                        del date_tasks[i]

                        if len(date_tasks) == 0:
                            del self.upcoming_tasks[status][date]

                        break

                else:  # if no break then continue the loop
                    continue

                break

            else:  # if inner for loop break then all outer will
                continue

            break
        print(self.upcoming_tasks)

        self.ids.upcoming_tasks_list_view.do_layout()
