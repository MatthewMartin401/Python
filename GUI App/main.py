# Writing GUI App

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window


# GUI
class WritingScreen(GridLayout):
    def __init__(self, **kwargs):
        super(WritingScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text = "user name"))

class WritingApp():

    def build(self):
        return WritingScreen
# Machine Learning


# Main Loop

Window.size(400, 800)
if __name__ == "__main__":
    WritingApp().run()