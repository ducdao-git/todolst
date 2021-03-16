from kivy.app import App
from kivy.config import Config
from kivy.lang.builder import Builder

from libs.get_data import get_user_data
from screens.upcoming_route import UpcomingRoute

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '800')

Builder.load_file('libs/custom_kv_widget.kv')
Builder.load_file('upcoming_route.kv')


class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_data = get_user_data()
        self.theme_palette = self.user_data['theme_palette']

    def build(self):
        return UpcomingRoute()

    def on_stop(self):
        print("the program now closing")


if __name__ == '__main__':
    MyApp().run()
