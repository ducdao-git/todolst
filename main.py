from kivy.app import App

from libs.setting import theme_setting
from screens.upcoming_route import UpcomingRoute


class MyApp(App):
    color_plate = theme_setting("todolst")
    primary_color = color_plate['primary_color']
    primary_variant_color = color_plate['primary_variant_color']
    secondary_color = color_plate['secondary_color']
    text_color = color_plate['text_color']
    background_color = color_plate['background_color']
    good_color = color_plate['good_color']
    bad_color = color_plate['bad_color']

    def build(self):
        return UpcomingRoute()

    def on_stop(self):
        print("the program now closing")


if __name__ == '__main__':
    MyApp().run()
