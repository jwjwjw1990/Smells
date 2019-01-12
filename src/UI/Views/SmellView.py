from src.UI.Views.View import View
from src.UI.Button import Button
from PIL import Image
import os, sys

class SmellView(View):

    button_values = [0, 6, 4, 3]
    end_values = [6, 3, 1, 4]
    positions = []
    red = [250, 100, 100]
    blue = [100, 100, 250]
    green = [100, 250, 100]
    orange = [250, 190, 100]
    yellow = [250, 250, 5]
    colors = [blue, red, green, orange]

    def create_button(self, app, key, i, pos, bg):
        but = Button(app, self, key, i, pos, self._images, bg)
        but.text = key
        self.add_child(key, but)

    def create_buttons(self, app):
        self.set_images()
        self.resize_images()
        for i in range(4):
            pos = self.get_position(i)
            bg = self.colors[i]
            self.create_button(app, self.button_values[i], i, pos, bg)

    def render(self, app):
        self.create_buttons(app)

    def update_button(self, index, value):
        self.button_values[index] = value
        if self.check_sneeze():
            print('sneezing')
        else:
            print('stop sneezing')
        self.check_end()

    def check_end(self):
        if self.button_values == self.end_values:
            print('end game')

    def check_sneeze(self):
        do_sneeze = False
        for im in self.button_values:
            if self._images[im].__contains__('fout'):
                do_sneeze = True
                break
        return do_sneeze


    def set_images(self):
        rootdir = os.path.dirname(os.getcwd()) + os.sep + 'resources\ButtonImages'
        tempimages = []
        for subdir, dirs, files in os.walk(rootdir):
            for file in files:
                filepath = subdir + os.sep + file
                if filepath.endswith('jpg'):
                    tempimages.append(filepath)
        self._images = tempimages

    def resize_images(self):
        for infile in self._images:
            # outfile = infile
            try:
                im = Image.open(infile)
                new_size = self.get_new_size(im.size)
                im = im.resize(new_size, Image.LANCZOS)
                im.save(infile, "JPEG")
            except IOError:
                print("cannot modify image for '%s'" % infile)

    def get_new_size(self, orig_size):
        max_size = 480, 275
        ratio = min(max_size[0] / orig_size[0], max_size[1] / orig_size[1])
        new_size = round(orig_size[0] * ratio), round(orig_size[1] * ratio)
        return new_size

    def get_position(self, index):
        return [index % 2, round((index - 0.5) / 2)]
