#Importaciones de Kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.layout import Layout
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen

# Importaciones de nuestros modulos
from instuccions import app_info, app_inst, app_inst2, toma_de_pulasaciones, app_inst3

class FirstScreen(Screen):
    def __init__(self, name='instructions'):
        super().__init__(name=name)
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text= app_info)
        self.label2 = Label(text=app_inst)
        self.label3 = Label(text=app_inst2)
        self.form_name = TextInput(hint_text='')
        self.form_age = TextInput(hint_text='Ingrese su edad')
        self.btn_star = Button(text='Comenzar Test')
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.label2)
        self.layout.add_widget(self.label3)
        self.layout.add_widget(self.form_name)
        self.layout.add_widget(self.form_age)
        self.layout.add_widget(self.btn_star)
        self.add_widget(self.layout)
        self.btn_star.on_press = self.next

    def next(self):
        self.manager.username = self.form_name.text
        self.manager.current = 'test'

    def on_enter(self):
        self.username.text = getattr(self.manager, 'username')
        self.ruffier_index.text = ruffier_index()
        self.ruffier_efficiency.text = ruffier_efficiency()
        self.ruffier_advice.text = ruffier_advice()
        
class SecondScreen(Screen):
    def __init__(self, name='test'):
        super().__init__(name=name)
        self.label_pulse = Label(text=toma_de_pulasaciones)
        self.input_pulse = TextInput(hint_text='Ingrese sus pulsaciones')
        self.btn_next = Button(text='Siguiente')
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.label_pulse)
        self.layout.add_widget(self.input_pulse)
        self.layout.add_widget(self.btn_next)
        self.add_widget(self.layout)
        self.btn_next.on_press = self.next

    def next(self):
        self.manager.pulse = self.input_pulse.text
        self.manager.current = 'third'

class ThirdScreen(Screen):
    def __init__(self, name='third'):
        super().__init__(name=name)
        self.inst3 = Label(text="Realiza 30 sentadillas en 1 minuto")
        self.btn_next = Button(text='Siguiente')
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.inst3)
        self.layout.add_widget(self.btn_next)
        self.add_widget(self.layout)
        self.btn_next.on_press = self.next

    def next(self):
        self.manager.current = 'fourth'

class FourthScreen(Screen):
    def __init__(self, name='fourth'):
        super().__init__(name=name)
        self.inst3 = Label(text=app_inst3)
        self.result1 = TextInput(hint_text='Ingrese sus resultados')
        self.result2 = TextInput(hint_text='Ingrese sus resultados despues del descanso')
        self.btn_next = Button(text='Finalizar Test')
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.inst3)
        self.layout.add_widget(self.result1)
        self.layout.add_widget(self.result2)
        self.layout.add_widget(self.btn_next)
        self.add_widget(self.layout)
        self.btn_next.on_press = self.next

    def next(self):
        self.manager.result1 = self.result1.text
        self.manager.result2 = self.result2.text
        self.manager.current = 'fifth'

class FifthScreen(Screen):
    def __init__(self, name='fifth'):
        super().__init__(name=name)
        self.username = Label(text = self.manager.username)
        self.rufller_index = Label(text=10)
        self.ruffler_efficiency = Label(text="Por calcular")
        self.ruffler_advice = Label(text="Por definir")
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.username)
        self.layout.add_widget(self.rufller_index)
        self.layout.add_widget(self.ruffler_efficiency)
        self.layout.add_widget(self.ruffler_advice)
        self.add_widget(self.layout)

class HeartCheckerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='instructions'))
        sm.add_widget(SecondScreen(name='test'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(FourthScreen(name='fourth'))
        sm.add_widget(FifthScreen(name='fifth'))
        return sm
    
app = HeartCheckerApp()
app.run()