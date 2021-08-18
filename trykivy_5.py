# программа с двумя экранами
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.animation import Animation
from kivy.clock import Clock

from random import random 

# Экран (объект класса Screen) - это виджет типа "макет" (Screen - наследник класса RelativeLayout).
# ScreenManager - это особый виджет, который делает видимым один из прописанных в нём экранов.

class FirstScr(Screen):
    def __init__(self, name='первый'):
        super().__init__(name=name) # имя экрана должно передаваться конструктору класса Screen
        btn = Button(text="Переключиться на другой экран")
        btn.on_press = self.next
        self.add_widget(btn) # экран - это виджет, на котором могут создаваться все другие (потомки)

    def next(self):
        self.manager.transition.direction = 'up' # объект класса Screen имеет свойство manager 
                                                   # - это ссылка на родителя
        self.manager.current = 'второй'

def todo(dt):
    print("прошло",dt,"секунд")
    if random() > 0.9:
        print("тебе не повезло конец")
        return False
    return 1

class SecondScr(Screen):
    def __init__(self, name='второй'):
        super().__init__(name=name)
        btn = Button(text="Вернись, вернись!")
        btn.on_press = self.next
        self.add_widget(btn)
        Clock.schedule_interval(todo,5)
        self.popup = Popup(auto_dismiss=False,size_hint=(None,None),
                                                    size=(100,100))
        self.animpopup = Animation(size=(300,300),duration=10)
        self.exitb = Button()
        self.popup.add_widget(self.exitb)
        self.exitb.on_press = self.exitpopup

    def exitpopup(self):
        self.popup.dismiss()

    def next(self):
        #self.manager.transition.direction = 'right'
        #self.manager.current = 'первый'
        self.popup.open()
        self.animpopup.start(self.popup)


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(FirstScr())
        sm.add_widget(SecondScr())
        # будет показан FirstScr, потому что он добавлен первым. Это можно поменять вот так:
        # sm.current = 'second'
        return sm

app = MyApp()
app.run()