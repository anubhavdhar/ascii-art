#Imports
from PIL import Image, ImageOps

# converts to gray scale
class GrayScale(object):
            
    def __call__(self, image):
        return image.convert("L");


