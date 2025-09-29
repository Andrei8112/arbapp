from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window

class ArbApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        label = Label(text="Приложение сигналов", font_size=28, color=(0, 1, 0, 1))
        button = Button(text="Получить сигнал", font_size=24, size_hint=(1, 0.2))

        layout.add_widget(label)
        layout.add_widget(button)
        return layout

if __name__ == "__main__":
    ArbApp().run()
