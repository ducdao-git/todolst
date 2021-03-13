from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '800')

Builder.load_file('upcoming_route.kv')


class UpcomingRoute(Widget):
    pass
