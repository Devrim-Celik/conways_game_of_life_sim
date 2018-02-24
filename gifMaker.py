import os
import imageio

'''
Function: Creates Gif using Images

Usage: Provide
	- (a path and) a name for the gif (with .gif as datatype)
	- a path to folder, containing the images
	- number of frames per second
'''

def createGif(gif_name='./game_of_life.gif', image_path='./images', image_duration=0.10):

	image_list = []

	# argument with duration of each image in seconds
	kargs = { 'duration': image_duration }

	# save all image values in a list
	file_list = sorted([f for f in os.listdir(image_path) if f.endswith(".jpg") or f.endswith(".png")])
	for f in file_list:
		image_list.append(imageio.imread(os.path.join(image_path, f)))

	# create gif
	imageio.mimsave(os.path.join(image_path, gif_name), image_list, **kargs)

	# remove all images
	for f in file_list:
	    os.remove(os.path.join(image_path, f))

if __name__=='__main__':
	createGif()
