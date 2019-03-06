import tkinter
from guizero import PushButton


class Button(PushButton):

    def __init__(self, app, parent, idx, i, pos, images, bg):
        self._id = idx
        self._index = i
        self._app = app
        self._parent = parent
        self._images = images
        super(Button, self).__init__(app, command=self.press, grid=pos)
        self.image = self._images[0]
        self.resize(960, 1040)
        self.bg = bg
        self.update()

    def press(self):
        self._id = (self._id + 1) % 23
        self.update()

    def update(self):
        # self.text = self._id
        self.image = self._images[self._id]
        self.resize(314, 234) # 506, 294
        self._parent.update_button(self._index, self._id)


    def get_id(self):
        return self._id
