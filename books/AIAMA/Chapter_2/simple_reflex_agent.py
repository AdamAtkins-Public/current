import vc_world as World
from vc_enum import FloorStatus as Status

class SimpleReflexAgent():
    """
        Simple reflex agent for the vacuum cleaner world

        world - reference to the environment
        start - (x,y) coordinate pair to starting location
    """

    def __init__(self,world,start):
        self.world = world
        self.location = start

    #Actions
    def move_left(self):
        if not self.location[0] == 0:
            self.location = (self.location[0] - 1, self.location[1])

    def move_right(self):
        if not self.location[0] == 1:
            self.location = (self.location[0] + 1, self.location[1])

    def suck(self):
        self.world.update_cell(self.location,Status.CLEAN)

    def step(self):
        """
        policy function of the agent to be called at each time step
        """
        if self.world.percept(self.location) == Status.DIRTY:
            self.suck()
        elif self.location == (1,0):
            self.move_left()
        elif self.location == (0,0):
            self.move_right()
