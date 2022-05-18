from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class Mywidget(GridLayout):
    pass

class FileChooserWindow(App):
    def build(self):
        return Mywidget()
