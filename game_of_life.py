import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.misc

THRESH = 0.35
SIZE = 256

def start_cell(size):

	# initial cell
	cell = np.random.rand(size,size)

	# set zeros and ones (after casting boolean to it)
	cell = (cell < THRESH).astype(int)

	return cell

def update_cell(old_cell, size):

	new_cell = np.copy(old_cell)

	# iterate through every cell
	for row in range(size):
		for col in range(size):

			# calculate sum of the cell
			cell_sum = 0

			for x in [-1,0,1]:
				for y in [-1,0,1]:

					new_x = row+x
					new_y = col+y

					if not(new_x<0) and not(new_y<0) and (new_x<size) and (new_y<size):
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




def gol():
	# create initial cell state and save it
	cell = start_cell(SIZE)
	#scipy.misc.imsave('/pictures/pic'+str(0)+'.png', cell)
	plt.figure()
	plt.imsave('pictures/pic'+str(0)+'.png', cell)
	# let the game begin ...
	for i in range(400,500):
		print(i)
		cell = update_cell(cell, SIZE)
		plt.figure()
		plt.imsave('pictures/pic'+str(i)+'.png', cell)
		#scipy.misc.imsave('/pictures/pic'+str(i)+'.png', cell)


if __name__=='__main__':
	gol()