#!/usr/bin/python3

import sys
sys.path.insert(0, '/usr/local/lib/python3.5/dist-packages')
from Logic.Application import Application
from Controllers.SmellController import SmellController
import tkinter
import os

#apppath = os.path.abspath('__file__')
apppath = os.path.dirname(os.path.abspath('__file__'))
print (apppath)
#appresources = Resources(os.path.join(apppath, "resources"))

app = Application()
app.set_controller(SmellController)
app.display()


