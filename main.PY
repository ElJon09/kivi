#Importaciones de Kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

# Importaciones de nuestros modulos
from instuccions import app_info, app_inst, app_inst2

class FirstScreen(Screen):
    def __init__(self, name='instructions'):
        super().__init__(name=name)
        layout = BoxLayout(orientation='vertical')
        label = Label(text= app_info)
        label2 = Label(text=app_inst)
        label3 = Label(text=app_inst2)
        form_name = TextInput(hint_text='Ingrese su nombre')
        form_age = TextInput(hint_text='Ingrese su edad')
        btn_star = Button(text='Comenzar Test')
        layout.add_widget(label)
        layout.add_widget(label2)
        layout.add_widget(label3)
        layout.add_widget(form_name)
        layout.add_widget(form_age)
        layout.add_widget(btn_star)
        self.add_widget(layout)

class HeartCheckerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='instructions'))
        #sm.add_widget(SecondScreen(name='test'))
        return sm
    
app = HeartCheckerApp()
app.run()