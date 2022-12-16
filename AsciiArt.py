####### REQUIRED IMPORTS FOR TRANSFORMS #######

from transforms import GrayScale, ReScale, ToAscii
from PIL import Image, ImageFont, ImageDraw, ImageFont, ImageOps
import matplotlib.pyplot as plt
import matplotlib.image as pltim
import scipy.misc
import numpy as np
from tkinter import *
from functools import partial
from tkinter import filedialog
import PIL.Image as pilimg
import os
import webbrowser


# Function for the filebrowser button
def fileClick():

	#creating file dialog
	file_type_options = (('All files', '*.*'), ('jpg files', '*.jpg'), ('png files', '*.png'))
	file_path = filedialog.askopenfilename(title = 'Open the image file', initialdir = './pictures', filetypes = file_type_options)
	e.insert(0, file_path)

	#saving the image
	im = pilimg.open(file_path)
	im.save('./temp_images/original_image.png')



# Will process the output when clicked.
def process(clicked_size, output_text):


	try:
		# if some file is previously chosen	
		im = pilimg.open('./temp_images/original_image.png')
	except:
		# if no file is chosen previously
		print("Select a File")
		return
	

	#grayscaling
	image_grayscaled = GrayScale()
	im_g = image_grayscaled(im)

	#resizing
	sz = 100
	if clicked_size.get() != "Select Width":
		sz = int(clicked_size.get());
	image_rescaled = ReScale(sz / 2)
	im_r = image_rescaled(im_g)


	#creating ascii outputs of both white and black background
	output_file_b = open("output_file_black_bg.txt","w")
	output_file_w = open("output_file_white_bg.txt","w")
	dimensions = ToAscii(im_r, output_file_b, output_file_w);
	output_file_b.close()
	output_file_w.close()

	#displying the black background picture on the GUI
	output_file = open("output_file_black_bg.txt","r")
	output_text.grid_remove()
	img_str = output_file.read()
	scroll_bar = Scrollbar(root, orient = 'vertical')
	scroll_bar.grid(row = 1, column = 4)
	
	#Adusting font size to fit in the dimension
	if dimensions[0] * 480 > dimensions[1] * 1000:
		WIDTH = 1000
		output_text = Text(root, bg = 'black', fg = 'white', height = dimensions[0], width = dimensions[1], font = ("Monospace", str(round(WIDTH / dimensions[0]))));
		output_text.insert(END, img_str)
	else:
		HIEGHT = 480
		output_text = Text(root, bg = 'black', fg = 'white', height = dimensions[0], width = dimensions[1], font = ("Monospace", str(round(HIEGHT/ dimensions[1]))));
		output_text.insert(END, img_str)


	# Positioning the output
	output_text.grid(row = 1, column = 0, columnspan = 4)
	output_file.close()

	# Changing the 'Process' Button to 'Exit Program' Button
	ExitButton = Button(root, text = "Exit Program", command = partial(exit))
	ExitButton.grid(row = 0, column = 3)




# Main function starts
if __name__ == '__main__':

	# Creating the root tkinter GUI
	root = Tk();
	root.title("Picture to Ascii converter | Python GUI | Anubhav Dhar")

	# widget for output
	output_text = Text(root)

	# options for widths
	options_size = ["Select Width", "20", "50", "80", "100", "150", "170", "200", "300", "350"]
	clicked_size = StringVar()
	clicked_size.set(options_size[0])

	# file dialogue entry
	e = Entry(root, width=70)
	e.grid(row=0, column=0)
	
	# select file button
	select_file_button = Button(root, text = "Browse file", command = partial(fileClick))
	select_file_button.grid(row = 0, column = 1)

	# drop down button for choosing width
	drop_down_button_size = OptionMenu(root, clicked_size, *options_size)
	drop_down_button_size.grid(row = 0, column = 2)

	# 'Process' Button
	myButton = Button(root, text = "Process", command = partial(process, clicked_size, output_text))
	myButton.grid(row = 0, column = 3)

	# start the GUI
	root.mainloop();

	# removing temporary files
	if os.path.exists('./temp_images/original_image.png'):
		os.remove('./temp_images/original_image.png')