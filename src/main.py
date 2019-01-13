from Logic.Application import Application
from Controllers.SmellController import SmellController
import sys, os

sys.path.insert(0, '/usr/local/lib/python3.5/dist-packages')
apppath = os.path.dirname(os.path.abspath(__file__))
#appresources = Resources(os.path.join(apppath, "resources"))

app = Application()
app.set_controller(SmellController)
app.display()


