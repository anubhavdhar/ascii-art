####### REQUIRED IMPORTS FOR TRANSFORMS #######

from transforms import GrayScale, ReScale
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




# Define the function you want to call when the filebrowser button is clicked.
def fileClick(clicked_file):

	####### CODE REQUIRED (START) #######
	# This function should pop-up a dialog for the user to select an input image file.
	# Once the image is selected by the user, it should automatically get the corresponding outputs from the segmentor.
	# Hint: Call the segmentor from here, then compute the output images from using the `plot_visualization` function and save it as an image.
	# Once the output is computed it should be shown automatically based on choice the dropdown button is at.
	# To have a better clarity, please check out the sample video.

	#creating file dialog
	file_type_options = (('All files', '*.*'), ('jpg files', '*.jpg'), ('png files', '*.png'))
	file_path = filedialog.askopenfilename(title = 'Open the image file', initialdir = './pictures', filetypes = file_type_options)
	e.insert(0, file_path)

	#opening the image
	im = pilimg.open(file_path)
	im.save('original_image.png')
	#calling the segmentor

	####### CODE REQUIRED (END) #######

# will process the output when clicked.
def process():


	####### CODE REQUIRED (START) #######
	# Should show the corresponding segmentation or bounding boxes over the input image wrt the choice provided.
	# Note: this function will just show the output, which should have been already computed in the `fileClick` function above.
	# Note: also you should handle the case if the user clicks on the `Process` button without selecting any image file.
	'''
	try:
		# if some file is previously chosen
		global picture1
		picture1 = PhotoImage(file='./original_image.png')
		img1 = Label(root, image = picture1)
		global picture2
		#decide based on the dropdown menu selection
		picture2 = PhotoImage(file="final_image.png")
		img2 = Label(root, image = picture2)
		img1.grid(row = 2, column = 0, columnspan = 2)
		img2.grid(row = 2, column = 2, columnspan = 2)
	except:
		# if no file is chosen previously
		print("Please choose a file!")
		return
	'''

	im = pilimg.open('original_image.png')
	if clicked_file.get() == "Normal":
		im.save('working_image.png')
	else:
		image_grayscaled = GrayScale()
		im_g = image_grayscaled(im)
		im_g.save('working_image.png')

	im = pilimg.open('working_image.png')
	sz = 200
	if clicked_size.get() != "Select Width":
		sz = int(clicked_size.get());

	image_rescaled = ReScale(sz)
	image_rescaled(im).save('final_image.png')


	global picture2
	#decide based on the dropdown menu selection
	picture2 = PhotoImage(file="./final_image.png")
	img2 = Label(root, image = picture2)
	img2.grid(row = 1, column = 0, columnspan = 4)


	####### CODE REQUIRED (END) #######

# `main` function definition starts from here.
if __name__ == '__main__':

	####### CODE REQUIRED (START) ####### (2 lines)
	# Instantiate the root window.
	# Provide a title to the root window.
	root = Tk();
	root.title("Picture to Ascii converter | Python GUI | Anubhav Dhar")
	####### CODE REQUIRED (END) #######

	# Setting up the segmentor model.
	# annotation_file = './data/annotations.jsonl'
	# transforms = []

	# Instantiate the segmentor model.
	# segmentor = InstanceSegmentationModel()
	# Instantiate the dataset.
	# dataset = Dataset(annotation_file, transforms=transforms)

	
	# Declare the options.
	options_file = ["Grayscale", "Normal"]
	clicked_file = StringVar()
	clicked_file.set(options_file[0])	

	options_size = ["Select Width", "20", "50", "80", "100", "150", "200"]
	clicked_size = StringVar()
	clicked_size.set(options_size[0])

	e = Entry(root, width=70)
	e.grid(row=0, column=0)

	####### CODE REQUIRED (START) #######
	# Declare the file browsing button
	
	select_file_button = Button(root, text = "Select file", command = partial(fileClick, clicked_file))
	select_file_button.grid(row = 0, column = 1)

	####### CODE REQUIRED (END) #######

	####### CODE REQUIRED (START) #######
	# Declare the drop-down button

	drop_down_button_file = OptionMenu(root, clicked_file, *options_file)
	drop_down_button_file.grid(row = 0, column = 2)

	drop_down_button_size = OptionMenu(root, clicked_size, *options_size)
	drop_down_button_size.grid(row = 0, column = 3)


	####### CODE REQUIRED (END) #######

	# This is a `Process` button, check out the sample video to know about its functionality

	myButton = Button(root, text = "Process", command = partial(process))
	myButton.grid(row = 0, column = 4)

	
	####### CODE REQUIRED (START) ####### (1 line)
	# Execute with mainloop()
	root.mainloop();

	####### CODE REQUIRED (END) #######