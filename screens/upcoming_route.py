from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
# from kivy.core.window import Window
from kivy.config import Config

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '800')

Builder.load_file('upcoming_route.kv')


class UpcomingRoute(Widget):
    primary_color = [103 / 255, 58 / 255, 183 / 255, 1]
    primary_variant_color = [20 / 255, 4 / 255, 53 / 255, 1]
    secondary_color = [255 / 255, 191 / 255, 0, 1]

    pass


class MyApp(App):
    def build(self):
        # Window.clearcolor = (0, 1, 0, 1)
        return UpcomingRoute()


if __name__ == '__main__':
    MyApp().run()
