from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager


class Main(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Gray'
        return Builder.load_file('templates/index.kv')

if __name__ == '__main__':
    Main().run()