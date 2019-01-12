from src.Logic.Application import Application
from src.Controllers.SmellController import SmellController
import os
apppath = os.path.dirname(os.path.abspath(__file__))
#appresources = Resources(os.path.join(apppath, "resources"))

app = Application()
app.set_controller(SmellController)
app.display()
