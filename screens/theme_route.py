from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from libs.get_data import get_theme_palette
# from main import MyApp

"""
screen_4.py

Functions used by WindowFour in screens_setups.py can be found here.
"""


class ThemeLayout(BoxLayout):
    def __init__(self, theme_name, theme_dict, **kwargs):
        super().__init__(**kwargs)
        self.primary_color_untouched = theme_dict['primary_color']
        self.primary_text_color_untouched = theme_dict['text_primary_color']
        self.secondary_color_untouched = theme_dict['secondary_color']
        self.secondary_text_color_untouched = theme_dict['text_secondary_color']
        self.theme_background_color = theme_dict['background_color']

        self.touched_color = (1, 0, 0, 1)
        self.ids.primary_color_label_button.background_color = self.primary_color_untouched
        self.ids.primary_color_label_button.text_color = self.primary_text_color_untouched
        self.ids.primary_color_label_button.text = theme_name
        self.ids.space_filling_label_button.background_color = self.theme_background_color

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.ids.primary_color_label_button.background_color = self.touched_color
            self.ids.space_filling_label_button.background_color = self.touched_color

    def on_touch_up(self, touch):
        self.ids.primary_color_label_button.background_color = self.primary_color_untouched
        self.ids.choice_checkbox.active = True
        self.ids.space_filling_label_button.background_color = self.theme_background_color


class ThemeRoute(Screen):
    def __init__(self, app, **kw):
        super().__init__(**kw)
        self.app = app
        self.normal_theme = get_theme_palette("todolst")
        self.dark_theme = get_theme_palette("dark")
        self.chosen_theme_checkbox = 0

    def add_theme_choice(self, theme_name, theme_dict):
        theme_choice = ThemeLayout(theme_name, theme_dict)
        self.ids.themes.add_widget(theme_choice)

    def on_pre_enter(self, *args):
        self.add_theme_choice('todolst', self.normal_theme)
        self.add_theme_choice('dark', self.dark_theme)

    def on_leave(self, *args):
        self.ids.themes.clear_widgets()
