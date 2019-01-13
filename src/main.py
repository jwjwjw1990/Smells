from Logic.Application import Application
from Controllers.SmellController import SmellController
import os, sys
apppath = os.path.dirname(os.path.abspath(__file__))
#appresources = Resources(os.path.join(apppath, "resources"))

app = Application()
app.set_controller(SmellController)
app.display()


