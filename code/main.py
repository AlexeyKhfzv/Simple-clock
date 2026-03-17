from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
from datetime import datetime as dt
Window.clearcolor = (1,1,1,1)
Window.size = (210, 80)

class ClockExample(App):
    def build(self):
        self.labelh = Label(
            text=str(dt.now().hour),
            color = (0,0,0,1),
            font_size = 50
        )
        self.labelm = Label(
            text=str(dt.now().minute),
            color = (0,0,0,1),
            font_size = 50
        )
        self.labels = Label(
            text=str(dt.now().second),
            color = (80,80,80,1),
            font_size = 50
        )
        
        # Schedule 'update_label' to run every 1.0 seconds
        Clock.schedule_interval(self.update_label, 1.0)
        
        box = BoxLayout()
        box.add_widget(self.labelh)
        box.add_widget(self.labelm)
        box.add_widget(self.labels)

        return box

    def update_label(self, dtime):
        self.labelh.text = str(dt.now().hour)
        self.labelm.text = str(dt.now().minute)
        self.labels.text = str(dt.now().second)

clock = ClockExample()
clock.title = "Clock"
clock.run()