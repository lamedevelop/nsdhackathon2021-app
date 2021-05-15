from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout

class Main(BoxLayout):
    pass

class Settings(BoxLayout):
    pass

class Messenger(BoxLayout):
    pass

class Registration(BoxLayout):
    pass

class Home(BoxLayout):
    open_call_box = False
    def animation_auth(self, self_widget, another_widget):
        if not self.open_call_box:
            Animation(
                disabled=False,
                opacity=1,
                d=0.6, t="in_out_quad"
                ).start(another_widget)
            Animation(
                disabled=True,
                opacity=0,
                size_hint_y=0,
                size_hint_x=0,
                d=0.6, t="in_out_quad"
                ).start(self_widget)
            self.open_call_box=True

class Main(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        return Builder.load_file('templates/index.kv')

    def go_to_registration(self, screen_manager: ScreenManager):
        screen_manager = screen_manager.parent.manager
        screen_manager.transition.direction = 'down'
        screen_manager.current = 'registration'

    def go_to_settings(self, screen_manager: ScreenManager):
        screen_manager = screen_manager.parent.manager
        screen_manager.transition.direction = 'left'
        screen_manager.current = 'settings'
        
    

if __name__ == '__main__':
    Main().run()