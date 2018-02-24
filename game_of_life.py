import sys
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})

from gifMaker import createGif

#=====#=====#=====#=====#=====#=====#======#=====#=====#=====#=====#=====#=====#

def start_cell(img_size, inital_prob):
	# initial cell
	cell = np.random.rand(img_size, img_size)
	# set zeros and ones (after casting boolean to it)
	cell = (cell < inital_prob).astype(int)
	return cell

#=====#=====#=====#=====#=====#=====#======#=====#=====#=====#=====#=====#=====#

def update_cell(old_cell, img_size):
	new_cell = np.copy(old_cell)

	# iterate through every cell
	for row in range(img_size):
		for col in range(img_size):
			# calculate sum of the cell
			cell_sum = 0
			for x in [-1,0,1]:
				for y in [-1,0,1]:
					new_x = row+x
					new_y = col+y
					if not(new_x<0) and not(new_y<0) and (new_x<img_size) and (new_y<img_size):
						cell_sum += old_cell[new_x, new_y]

			# rule1: living cell and less than 2 neighbours --> dead
			if (old_cell[row, col]==1) and (cell_sum<2):
				new_cell[row, col] = 0
			# rule2: living cell and 2 or 3 neighbours --> live
			elif (old_cell[row, col]==1) and (cell_sum<4):
				new_cell[row, col] = 1
			# rule3: living cell with more than 3 neighbours --> dead
			elif (old_cell[row, col]==1):
				new_cell[row, col] = 0
			# rule4: dead cell with exactly 3 neighbours --> live
			elif (old_cell[row, col]==0) and (cell_sum==3):
				new_cell[row, col] = 1
			# any other cell (only dead ones, with more/less than 3 neighbours) --> dead
			else:
				new_cell[row, col] = 0

	return new_cell

#=====#=====#=====#=====#=====#=====#======#=====#=====#=====#=====#=====#=====#

def CGoL(img_size = 512, inital_prob = .6):
	"""
	Arguments:
		img_size		Image Size will we (img_size x img_size)
		inital_prob		With which probability will a
							state be active at the start

	Returns:
		state_list		List of all States
	"""
	state_list = []

	# create initial cell state and save it
	cell = start_cell(img_size, inital_prob)

	# let the game begin ...
	for i in range(400,650):
		state_list.append(cell)
		plt.figure()
		plt.imsave('images/img'+str(i)+'.png', cell, cmap="Greys_r")
		# clear matplotlib cache, since it tends to overflow and slow down
		plt.cla()
		plt.clf()
		# print progress
		cell = update_cell(cell, img_size)
		progress(int(100*(i-400)/(250-1)))

	return state_list

#=====#=====#=====#=====#=====#=====#======#=====#=====#=====#=====#=====#=====#

def progress(pg):
    if (pg != 100):
        sys.stdout.write('\r[*] Generation Progress: [{0}] {1}%'.format('#'*int(pg/2), pg))

    else:
        sys.stdout.write('\r[+] Generation Progress: [{0}] {1}%\n'.format('#'*(int(pg/2)-2), pg))

sys.stdout.flush()

#=====#=====#=====#=====#=====#=====#======#=====#=====#=====#=====#=====#=====#

if __name__=='__main__':
	_ = CGoL()
	#createGif()
