
import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class BoxApp(App):
    def build(self):
        bl = BoxLayout(padding=[15, 480, 15, 5])
        bl.add_widget(Button(text="Теория"))
        bl.add_widget(Button(text="Тесты"))
        bl.add_widget(Button(text="Поиск по фото"))
        return bl

class MainApp(App):
    def build(self):
        button = Button(text='Hello from Kivy',
                        size_hint=(.5, .5),
                        pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=self.on_press_button)

        return button

    def on_press_button(self, instance):
        print('Вы нажали на кнопку!')

class MyApp(App):

    def build(self):
        return Label(text='Hello world')


if __name__ == '__main__':
    app = BoxApp()
    app.run()
