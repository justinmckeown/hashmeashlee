import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooser

#from plyer import filechooser
import diectorydive as dd
import kivyfilechooser as fc


class MyLayout(GridLayout):

    #Initialize infinitre keywords
    def __init__(self, **kwargs):
        #call constructor
        super(MyLayout, self).__init__(**kwargs)

        #set direction of boxlayout
        
        #Set columns
        self.cols = 4
        self.rows = 4
        self.row_force_default=True
        self.row_default_height=40
        self.padding =100

        #add widgets
        self.add_widget(Label(text="File Path: ", size_hint_x=None, width=100))
        
        self.filepath = TextInput(multiline=False, size_hint_x=None, width=300)
        self.add_widget(self.filepath)

        #submit button
        self.submit = Button(text="Submit", size_hint_x=None, width=200)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    

    def press(self, instance):
        #file_path = self.filepath.text
        #print(f'Hello. Is this the correct path: {file_path}')
        #path = filechooser.open_file(title="Pick a CSV file..", 
        #                    filters=[("Comma-separated Values", "*.csv")])
        #print(path)
        pass
       

   
    


class HashsterApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    HashsterApp().run()