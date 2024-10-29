from agent_actions import Action
from vc_enum import FloorStatus as Status
import random

class Agent():
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y

    def program(self,percept):
        return Action.NOOP

    def update_location(self,x,y):
        self.x = x
        self.y = y

class RandomizedReflexAgent(Agent):
    def __init__(self,world,x,y):
        super().__init__(world,x,y)

    def program(self,percept):
        return random.choice(list(Action))

class RandomizedReflexAgentBump(RandomizedReflexAgent):
    def __init__(self,world,x,y):
        super().__init__(world,x,y)
    
    def set_bump(self,boolean):
        pass


class ReflexAgentState(Agent):
    def __init__(self,world,x,y):
        super().__init__(world,x,y)
        self.state = []
        self.action_priority = [Action.RIGHT,
                                Action.DOWN,
                                Action.LEFT,
                                Action.UP]
        self.primary_action = 0
        self.secondary_action = 1
        self.rotated = 0

    def rotate_action_priority(self,clockwise=True):
        if clockwise:
            self.primary_action = (self.primary_action + 1) % 4
            self.secondary_action = (self.secondary_action + 1) % 4
            self.rotated += 1
        else:
            self.primary_action = (self.primary_action - 1) % 4
            self.secondary_action = (self.secondary_action - 1) % 4
            self.rotated = 0

    def program(self,percept):
        if percept == Status.DIRTY:
            action = Action.SUCK
        elif self.rotated > 8:
            action = Action.NOOP
        elif ((self.x,self.y), self.action_priority[self.primary_action])\
            not in self.state:
            action = self.action_priority[self.primary_action]
            if not self.rotated == 0:
                self.rotate_action_priority(False)
        elif ((self.x,self.y), self.action_priority[self.secondary_action])\
            not in self.state:
            action = self.action_priority[self.secondary_action]
        else:
            self.rotate_action_priority()
            action = self.program(percept)

        self.state.append(((self.x,self.y),action))
        return action

class ReflexAgentStateBump(ReflexAgentState):
    def __init__(self,world,x,y):
        super().__init__(world,x,y)
        self.bump = False

    def set_bump(self,boolean):
        self.bump = boolean

    def program(self,percept):
        action = Action.NOOP
        if percept == Status.DIRTY:
            action = Action.SUCK
        elif self.rotated > 8:
            action = Action.NOOP
        elif not self.bump:
            action = self.action_priority[self.primary_action]
            if not self.rotated == 0:
                self.rotate_action_priority(False)
        elif self.bump:
            if self.state[-1] == self.action_priority[self.primary_action]:
                action = self.action_priority[self.secondary_action]
                self.set_bump(False)
            elif self.state[-1] == self.action_priority[self.secondary_action]:
                self.rotate_action_priority()
                action = self.action_priority[self.secondary_action]
                self.set_bump(False)
                
        self.state.append(action)
        return action

