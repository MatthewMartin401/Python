# Writing GUI App

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

#import shelves


# GUI
class MakeAccount(GridLayout):
    def __init__(self, **kwargs):
        super(MakeAccount, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        self.add_widget(Label(text = "UserName"))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)
        self.add_widget(Label(text = "Password"))
        self.password = TextInput(password = True, multipline = False)
        self.add_widget(self.password)


class LogScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LogScreen, self).__init__(**kwargs)
        '''
        self.cols = 2
        self.rows = 3
        self.add_widget(Label(text = "user name"))
        self.username = TextInput(multiline = False)
        self.add_widget(self.username)
        self.add_widget(Label(text = "Password"))
        self.password = TextInput(password = True, multiline = False)
        self.add_widget(self.password)
        self.btn1 = Button(text = "Create Account")
        self.btn1.bind(on_press = self.createAccount)
        self.add_widget(self.NewAccount)
        self.add_widget(Button(text = "Sign in", bind = self.createAccount))
        '''
        
    def createAccount():
        Acc_create = MakeAccount
        return Acc_create



class WritingApp(App):
    
    def build(self):
        #return Label(text = "Hello World")
        return LogScreen()


# Machine Learning


# Main Loop

#Window.size(400, 800)
if __name__ == "__main__":
    WritingApp().run()