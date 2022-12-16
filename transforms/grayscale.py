#Imports

from PIL import Image, ImageOps

class GrayScale(object):
    '''
        Flips the image.
    '''
            
    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)
        '''

        # Write your code here
        
        return image.convert("L");



# image = Image.open('../../../sample_imgs/flip.png');
# imagefliped = FlipImage('horizontal')
# imagefliped(image).save('filip.png')