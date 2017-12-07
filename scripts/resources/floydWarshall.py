"""
*************************************************
File: floydExample.py
Author: Luke Burks
Date: November 2017

Demonstrating a variation on the floyd warshall
algorithm

*************************************************
"""


import numpy as np;
import matplotlib.pyplot as plt;

def floyds(grid):
	'''
	Runs a version of the floyd warshall algorithm

	Inputs:
	#Grid: Occupancy grid. List of lists, or 2D numpy array, of 0's and 1's
	#pose: cops position, length 2 list [x,y]

	Outputs:
	#dist: Grid of distance, numpy array

	'''

	#find dimensions of grid
	sizeX = len(grid);
	sizeY = len(grid[0]);

	#initialize distance grid to infinity
	dist = np.ones(shape = (sizeX,sizeY,sizeX,sizeY))*np.Inf;
	nextPlace = np.ones(shape = (sizeX,sizeY,sizeX,sizeY))*np.Inf;

	#enforce that cells are zero distance from themselves
	for i in range(0,sizeX):
		for j in range(0,sizeY):
			dist[i,j,i,j] = 0;

	#set the distance of each cell to it's neighbors as 1
	#only cardinal directions, no diagonals for simplicity
	#makes sure occupied cells can't be accessed
	for i in range(0,sizeX):
		for j in range(0,sizeY):
			if(i>0 and grid[i-1][j] == 0):
				dist[i,j,i-1,j] = 1;
				nextPlace[i,j,i-1,j] = (i-1, j)
			if(i<sizeX-1 and grid[i+1][j] == 0):
				dist[i,j,i+1,j] = 1;
				nextPlace[i,j,i+1,j] = (i+1, j)
			if(j>0 and grid[i][j-1] == 0):
				dist[i,j,i,j-1] = 1;
				nextPlace[i,j,i,j-1] = (i, j-1)
			if(j<sizeY-1 and grid[i][j+1] == 0):
				dist[i,j,i,j+1] = 1;
				nextPlace[i,j,i,j+1] = (i, j+1)

	#Main loop, pretty ugly...
	#but a simple if statement at the core
	for kx in range(0,sizeX):
		for ky in range(0,sizeY):
			for ix in range(0,sizeX):
				for iy in range(0,sizeY):
					for jx in range(0,sizeX):
						for jy in range(0,sizeY):
							if(dist[ix,iy,jx,jy] > dist[ix,iy,kx,ky] + dist[kx,ky,jx,jy]):
								dist[ix,iy,jx,jy] = dist[ix,iy,kx,ky] + dist[kx,ky,jx,jy];
								nextPlace[ix, iy, jx, jy] = nextPlace[ix, iy, kx, ky]
		print(kx)

	return dist, nextPlace

def path(ux, uy, vx, vy, nextPlace):
	if nextPlace is None:
		return []
	path = [(ux, uy)]
	while u != v:
		u = nextPlace[ux, uy, vx, vy]
		path.append(u)
	return path

def displayMap(costs,pose=[0,3]):
	#lets see what the cost looks like for a position
	plt.imshow(costs[0,3]);
	plt.show();


def main():

	#A 5x5 grid with a wall near the top
	grid = [[0,0,0,0,0],[0,1,1,1,0],[0,0,0,1,0],[0,0,0,0,0],[0,0,0,0,0]]

	#The cops position
	pose = [0,3];

	costs = floyds(grid);
	displayMap(costs,pose);




if __name__ == '__main__':
	main()