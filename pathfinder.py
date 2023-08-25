###############################
# Baptiste PICARD 			  #
# picard.baptiste@laposte.net #
# Starting the 02/25/2020     #
# Pathfinder A* from scratch  #
#							  #
###############################

# Imports
import time 
from grid import Grid 

if __name__ == "__main__" :
	old = time.time()
	print("Let's start a new project")
	my_Grid = Grid("My Grid", 5, 5, 5)
	my_Grid.showTK()
	print("It takes {} seconds to reach the end of the A* pathfinder code.".format(time.time()-old))