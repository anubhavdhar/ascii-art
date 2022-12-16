#Imports

import numpy as np
from PIL import Image, ImageFont, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import matplotlib.image as pltim
import scipy.misc


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


	return (original_img.shape[0], original_img.shape[1] * 2);
	# pltim.imsave(output, img)

	# Write the required arguments
	# The function should plot the predicted segmentation maps and the bounding boxes on the images and save them.
	# Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.