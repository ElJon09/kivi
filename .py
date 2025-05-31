from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

# class MiprimeraApp(App):
#     def build(self):
#         layout = BoxLayout(orientation ='vertical')
#         self.etiqueta = Label(text='¡Hola, soy una etiqueta!')
#         boton = Button(text='Hello World', size_hint=(None, None), size=(200, 100))
#         boton.bind(on_press = self.boton_presionado)
#         layout.add_widget(self.etiqueta)
#         layout.add_widget(boton)
#         return layout
        
#     def boton_presionado(self, etiqueta):
#         self.etiqueta.text = "¡Texto cambiado!"

class FirstScr(Screen):
    def __init__(self, name='first'):
        super().__init__(name=name)
        btn = Button(text='Hello World')
        self.add_widget(btn)
        btn.on_press = self.next

    def next(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'second'

class SecondScr(Screen):
    def __init__(self, name='second'):
        super().__init__(name=name)
        btn = Button(text='Hello World')
        btn.on_press = self.next
        self.add_widget(btn)

    def next(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'first'

class MiprimeraApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        return sm

myApp = MiprimeraApp()
myApp.run()