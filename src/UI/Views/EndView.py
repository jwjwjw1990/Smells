from UI.Views.View import View

import os, sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.IN)

class EndView(View):  

    GPIO.output(21,0)
    GPIO.output(20,0)

    def render(self, app):
        self.create_buttons(app)