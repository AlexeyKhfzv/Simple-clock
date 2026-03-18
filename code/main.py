import os
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
        h = dt.now().hour
        self.labelh = Label(
            text=f"0{h}" if h < 10 else str(h),
            color = (0,0,0,1),
            font_size = 50
        )
        m = dt.now().minute
        self.labelm = Label(
            text=f"0{m}" if m < 10 else str(m),
            color = (0,0,0,1),
            font_size = 50
        )
        s = dt.now().second
        self.labels = Label(
            text=f"0{s}" if s < 10 else str(s),
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
        h = dt.now().hour
        self.labelh.text = f"0{h}" if h < 10 else str(h)
        m = dt.now().minute
        self.labelm.text = f"0{m}" if m < 10 else str(m)
        s = dt.now().second
        self.labels.text = f"0{s}" if s < 10 else str(s)
    
    def on_start(self):
        os.system("wmctrl -r :ACTIVE: -b add,above")


clock = ClockExample()
clock.title = "Clock"
clock.run()
