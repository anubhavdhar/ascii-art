#Imports

import numpy as np
from PIL import Image, ImageFont, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import matplotlib.image as pltim
import scipy.misc


# outputs ascii art with both black and white intended backgrounds
def ToAscii(image, output_file_b, output_file_w):

	original_img = np.copy(np.transpose(image, (0, 1)))

	for i in range(original_img.shape[0]):
		for j in range(original_img.shape[1]):
			if original_img[i][j] < 85:
				output_file_w.write('##')
				output_file_b.write('  ')
			elif original_img[i][j] < 170:
				output_file_w.write('++')
				output_file_b.write('++')
			else:
				output_file_w.write('  ')
				output_file_b.write('##')
		
		output_file_b.write('\n')
		output_file_w.write('\n')

	# returning the dimension
	return (original_img.shape[0], original_img.shape[1] * 2);
