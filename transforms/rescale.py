#Imports
from PIL import Image, ImageOps

class ReScale(object):

    def __init__(self, output_size):
        # output_size is the intended width of the image
        self.output_size = output_size;

    def __call__(self, image):
        # resizes the image
        ratio = 1.0 * image.size[1] / image.size[0];
        return image.resize((round(self.output_size), round(self.output_size * ratio)))


