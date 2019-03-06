from Controllers.Controller import Controller
from UI.Views.EndView import EndView
    
class EndController(Controller):
    
    def __init__(self, application):
        super(EndController, self).__init__(EndView, application)
