from Environment import Maze
from Agent import RandomAgent

start = [0,0]
finish = [5,5]
nrows = 6
ncols = 6
prob = 0.5

maze = Maze(start,finish,nrows,ncols,prob)
ag = RandomAgent(maze)

ag.act()

