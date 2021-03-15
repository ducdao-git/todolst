from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.graphics import Color, Rectangle
from kivy.metrics import dp

from math import ceil
from datetime import datetime
import calendar

from libs.get_data import get_user_data, get_next7dates

Builder.load_file('upcoming_route.kv')


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

    def __init__(self, subject, due_date, **kwargs):
        super().__init__(**kwargs)
        self.text = f'{subject}\n[size={int(dp(16))}][color=228135]' + \
                    f'{due_date}[/color][/size]'

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


class TaskDividerLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            Color(1, 0, 0, 1)
            self.rect = Rectangle()

        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = (self.pos[0] + dp(16), self.pos[1])
        self.rect.size = (self.size[0] - dp(16), self.size[1])


class TaskView(BoxLayout):
    def __init__(self, subject, due_date, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(CheckBox(size_hint=(1, 1), color=[1, 0, 0, 1]))
        self.add_widget(TaskButton(subject, due_date, size_hint=(5, None)))

        self.bind(minimum_height=self.setter('height'))


class UpcomingRoute(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_data = get_user_data()
        self.upcoming_tasks = self.user_data['upcoming']
        self.theme_palette = self.user_data['theme_palette']

        self.display_overdue_tasks(
            overdue_tasks=self.upcoming_tasks['overdue'])
        self.display_on_time_tasks(
            on_time_tasks=self.upcoming_tasks['on_time'])

    def display_overdue_tasks(self, overdue_tasks):
        self.ids.upcoming_tasks_list_view.add_widget(
            DateButton(text='Overdue'))
        self.ids.upcoming_tasks_list_view.add_widget(
            DateDividerLabel())

        for date in overdue_tasks:
            for task in overdue_tasks[date]:
                self.ids.upcoming_tasks_list_view.add_widget(
                    TaskView(subject=task['subject'],
                             due_date=str(date) + ' ' + task['time']))
                # self.ids.upcoming_tasks_list_view.add_widget(
                #     TaskDividerLabel())

    def display_on_time_tasks(self, on_time_tasks):
        count = 0
        for date in on_time_tasks:
            next_7_dates = get_next7dates()
            if date > next_7_dates[-1]:
                break

            # while date > next_7_dates[count]:
            #     missing_date = next_7_dates[count]
            #     display_date = calendar.day_name[missing_date.weekday()][
            #                    :3] + ' ' + missing_date.strftime("%b %d")
            #     self.ids.upcoming_tasks_list_view.add_widget(
            #         DateButton(text=str(display_date)))
            #     self.ids.upcoming_tasks_list_view.add_widget(
            #         DateDividerLabel())
            #     count += 1

            display_date = calendar.day_name[date.weekday()][
                           :3] + ' ' + date.strftime("%b %d")
            self.ids.upcoming_tasks_list_view.add_widget(
                DateButton(text=str(display_date)))
            self.ids.upcoming_tasks_list_view.add_widget(
                DateDividerLabel())

            for task in on_time_tasks[date]:
                self.ids.upcoming_tasks_list_view.add_widget(
                    TaskView(subject=task['subject'],
                             due_date=str(date) + ' ' + task['time']))
                # self.ids.upcoming_tasks_list_view.add_widget(
                #     TaskDividerLabel())
