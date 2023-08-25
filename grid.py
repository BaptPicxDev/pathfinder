###############################
# Baptiste PICARD 			  #
# picard.baptiste@laposte.net #
# Starting the 02/25/2020     #
# Grid for pathfinders        #
#							  #
###############################

# import 
import random
import tkinter as tk


class Grid : 
	def __init__(self, name, rows, columns, walls) :
		self.name = name
		self.rows = rows
		self.columns = columns
		self.nb_walls = walls
		self.walls = random.sample([i for i in range(0, self.rows*self.columns, 1)], self.nb_walls)
		self.posBegin = (1,1)
		self.posEnd = (self.rows-2, self.columns-2)
		self.window = tk.Tk()
		self.canvas = tk.Canvas(self.window, bg="white", height=300, width=300)
		self.grid = self.createGrid()
		print("The {}*{} grid {} was created. It's composed by {} random walls.".format(self.rows, self.columns, self.name, self.nb_walls))

	def createGrid(self) :
		grid = []
		for row in range(self.rows) :
			grid_row = []
			for column in range(self.columns) :
				grid_row.append(' ')
			grid.append(grid_row)
		grid[self.posBegin[0]][self.posBegin[1]] = '1'
		grid[self.posEnd[0]][self.posEnd[1]] = '2'
		for i in range(len(grid)):
			print(i)
		return grid

	def show(self) :
		for grid_row in self.grid:
			print(grid_row)

	def showTK(self) :
		self.window.mainloop()
