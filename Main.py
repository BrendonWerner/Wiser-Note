import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty, ListProperty
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.storage.jsonstore import JsonStore
from kivy.base import runTouchApp
import requests
import json
Window.clearcolor = (1, 1, 1, 1)








    





class NewNote(Screen):
        

    

    def func_dce(self, instance):
        print(f"func_dce: Called from Button with text={instance.text}")



class SettingsScreen(Screen):

    def showtext(self):
        with open("test.txt","r") as f:
            return(f.read())

    def func_abc(self, instance):
        print(f"func_abc: Called from Button with text={instance.text}")

    def func_xyz(self, instance):
        print(f"func_xyz: Called from Button with text={instance.text}")

    



        

class ScreenManagement(ScreenManager):
    pass

class MenuScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):  
    def on_press(self):  
        pass







    class RootWidget(BoxLayout): 
  
        def btn_clk(self): 
            self.lbl.text = "You have been pressed"

class MyApp(App):

    def build(self):

        return ScreenManagement()

    def save(self, name, job):
        fob = open('test.txt', 'a')
        fob.write("Title: " + name + "\n"   )
        fob.write("Notes: " + job + "\n" + "\n" + "\n"  )   








if __name__ == '__main__':
    MyApp().run()
