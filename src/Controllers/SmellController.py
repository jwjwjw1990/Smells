from Controllers.Controller import Controller
from UI.Views.SmellView import SmellView
# from pip.gpiozero import LED

class SmellController(Controller):

    sneeze_active = False
    correct_answer = False

    # output_sneeze = LED(1)

    def __init__(self, application):

        super(SmellController, self).__init__(SmellView, application)

    def is_sneeze_active(self):
        return self.sneeze_active

    def set_sneeze(self, value):
        self.sneeze_active = value

    def check_sneeze(self):
        print('running')
        # self.output_sneeze = self.sneeze_active
