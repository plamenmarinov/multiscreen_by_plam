from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class AppWindow(ScreenManager):
    pass


class FirstScreen(Screen):
    def next(self):
        self.manager.current = "second"
        self.manager.transition.direction = "left"


class SecondScreen(Screen):
    def next(self):
        self.manager.current = "third"
        self.manager.transition.direction = "left"

    def prev(self):
        self.manager.current = "first"
        self.manager.transition.direction = "right"


class ThirdScreen(Screen):
    def prev(self):
        self.manager.current = "second"
        self.manager.transition.direction = "right"


kv = Builder.load_file('multiscreen.kv')


class MultiScreenApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    app = MultiScreenApp()
    app.title = "Multiscreen application"
    app.run()
