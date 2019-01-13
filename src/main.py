import sys
sys.path.insert(0, '/usr/local/lib/python3.5/dist-packages')

from Logic.Application import Application
from Controllers.SmellController import SmellController
import os

apppath = os.path.dirname(os.path.abspath(__file__))
#appresources = Resources(os.path.join(apppath, "resources"))

app = Application()
app.set_controller(SmellController)
app.display()


