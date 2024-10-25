from simple_reflex_agent import SimpleReflexAgent
from vc_enum import FloorStatus as Status

class SimpleReflexAgentState(SimpleReflexAgent):
    """
        Simple reflex agent with state for the vacuum cleaner world

        world - reference to the environment
        start - (x,y) coordinate pair to starting location
        state - model of previous cells (location,status)
    """

    def __init__(self,world,start):
        super().__init__(world,start)
        self.state = []

    #Actions
    def do_nothing(self):
        pass

    def step(self):
        """
        Simple reflex agent that stores each percept in a state model
        """
        self.state.append((self.location,self.world.percept(self.location)))

        if ((0,0),Status.CLEAN) in self.state and\
           ((0,1),Status.CLEAN) in self.state:
            self.do_nothing()
        elif self.world.percept(self.location) == Status.DIRTY:
            self.suck()
        elif self.location == (1,0):
            self.move_left()
        elif self.location == (0,0):
            self.move_right()

