from Controllers.Controller import Controller
from UI.Views.SmellView import SmellView
    
class SmellController(Controller):
    
    def __init__(self, application):
        super(SmellController, self).__init__(SmellView, application)
