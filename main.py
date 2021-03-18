import kivysome

from kivy.app import App
from kivy.config import Config
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager

from libs.get_data import get_user_data
from libs.data_handler import ProcessTaskHandler
from screens.upcoming_route import UpcomingRoute
from screens.add_task_route import AddTaskRoute

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '800')
# Config.set('graphics', 'width', '450')
# Config.set('graphics', 'height', '900')

kivysome.enable("https://kit.fontawesome.com/4adb19bb6e.js",
                group=kivysome.FontGroup.SOLID, font_folder="assets/fonts")

Builder.load_file('libs/custom_kv_widget.kv')
Builder.load_file('screens/upcoming_route.kv')
Builder.load_file('screens/add_task_route.kv')
# Builder.load_file('merge-repo/add_task_route2.kv')


class MyApp(App):
    user_data = get_user_data()
    theme_palette = user_data['theme_palette']
    route_manager = ScreenManager()

    def process_task_handler(self, _to, task):
        ProcessTaskHandler(app=self, _to=_to, task=task)

    def build(self):
        self.route_manager.add_widget(UpcomingRoute(app=self))
        self.route_manager.add_widget(AddTaskRoute(app=self))
        # self.route_manager.add_widget(CompletedRoute(app=self))
        return self.route_manager

    def on_stop(self):
        print(self.user_data)
        print("the program now closing")


if __name__ == '__main__':
    MyApp().run()
