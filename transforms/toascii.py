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


# outputs ascii art with both black and white intended backgrounds
def ToAsciiFiner(image, output_file_b, output_file_w):
	
	"                         "
	"........................."
	":::::::::::::::::::::::::"
	";;;;;;;;;;;;;;;;;;;;;;;;;"
	"ccccccccccccccccccccccccc"
	"CCCCCCCCCCCCCCCCCCCCCCCCC"
	"3333333333333333333333333"
	"0000000000000000000000000"
	"8888888888888888888888888"
	"#########################"
	
	original_img = np.copy(np.transpose(image, (0, 1)))

	for i in range(original_img.shape[0]):
		for j in range(original_img.shape[1]):
			if original_img[i][j] <= 25:
				output_file_w.write('##')
				output_file_b.write('  ')
			elif original_img[i][j] <= 50:
				output_file_w.write('88')
				output_file_b.write('..')
			elif original_img[i][j] <= 76:
				output_file_w.write('00')
				output_file_b.write('::')
			elif original_img[i][j] <= 101:
				output_file_w.write('33')
				output_file_b.write(';;')
			elif original_img[i][j] <= 127:
				output_file_w.write('CC')
				output_file_b.write('cc')
			elif original_img[i][j] <= 152:
				output_file_w.write('cc')
				output_file_b.write('CC')
			elif original_img[i][j] <= 178:
				output_file_w.write(';;')
				output_file_b.write('33')
			elif original_img[i][j] <= 203:
				output_file_w.write('::')
				output_file_b.write('00')
			elif original_img[i][j] < 229:
				output_file_w.write('..')
				output_file_b.write('88')
			else:
				output_file_w.write('  ')
				output_file_b.write('##')
		
		output_file_b.write('\n')
		output_file_w.write('\n')

	# returning the dimension
	return (original_img.shape[0], original_img.shape[1] * 2);
