from kivy.app import App

from libs.get_data import get_theme_palette
from screens.upcoming_route import UpcomingRoute


class MyApp(App):
    theme_palette = get_theme_palette("dark")

    def build(self):
        return UpcomingRoute()

    def on_stop(self):
        print("the program now closing")


if __name__ == '__main__':
    MyApp().run()
