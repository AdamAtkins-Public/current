import os
import random
from vc_enum import FloorStatus as Status

class World:
    """ This is an implemenation of the 2d vacuum cleaner world located on page 38 """

    def __init__(self,height,width,distribution,shape):
        """
           vacuum cleaner world generator

           height - y-axis 
           width - x-axis
           distribution - list of coordinate pairs or -1 for random distribution
           shape - list of coordinate pairs containing obstacles or empty list for none
        """
        self.height = int(height)
        self.width = int(width)
        self.distribution = distribution
        self.shape = shape
        self.world = self.__build()

    def build(self):
        """
            generates world from values set by __init__
            
            returns a 2d list of enum FloorStatus
        """
        randomize = self.distribution == -1
        shape = not self.shape
        world = []

        for x in range(self.width):
            world.append([])
            for y in range(self.height):
                # hand wavy 50/50
                world[x].append(Status(round(random.random()))) \
                if randomize else \
                world[x].append(Status.CLEAN)

        if not randomize:
            for (x,y) in self.distribution:
                world[x][y] = Status.DIRTY

        if not shape:
            for (x,y) in self.shape:
                world[x][y] = Status.OBSTACLE

        return world

    def percept(self,cell):
        """
            percept available to vacuum cleaner agent sensor

            cell - (x,y) coordinate pair

            returns the percept (FloorStatus) of requested location
        """
        return self.world[cell[0]][cell[1]]

    def update_cell(self,cell,status):
        """
            consequence of vacuum cleaner agent actuator

            cell - (x,y) coordinate pair
            status - enum FloorStatus.Name
        """
        self.world[cell[0]][cell[1]] = status

    def performance_measure(self):
        """
            returns current score of the environment's state
        """
        score = 0
        for x in range(self.width):
            for y in range(self.height):
                if self.world[x][y] == Status.CLEAN:
                    score += 1
        return score

    __build = build

#TEST
if __name__ == '__main__':

    def print_world(world):
        for y in range(world.height-1,-1,-1):
            line = ""
            for x in range(world.width):
                line += " (x:{},y:{}):".format(x,y) + (world.percept((x,y)).name)
            print(line)

    h, w = 3, 4
    
    #randomize
    world = World(h,w,[],[])
    print_world(world)

    #defined layout and performance_measure
    world = World(h,w,[(2,2)],[(0,0),(0,2),(3,0),(3,2)])
    print_world(world)
    print(world.performance_measure())
    print(world.percept((2,2)))
    print(world.percept((0,0)))
