#Imports

from PIL import Image, ImageOps

class ReScale(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''

        # Write your code here
        self.output_size = output_size;

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''

        # Write your code here
        temp_im = image
        temp_im.thumbnail((self.output_size, self.output_size))
        return temp_im
        

# Image.open('../../../sample_imgs/flip.png');
# image_resclaed = RescaleImage("0.25x")
# image_resclaed(image).save('re_skel.png')