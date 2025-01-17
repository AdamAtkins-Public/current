﻿from agent_actions import Action
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

class TimedAgent(Agent):
    """
        Agent made to run in exercise_13.py
    """
    def __init__(self,world,x,y,steps):
        super().__init__(world,x,y)
        self.move_vertically = False
        self.start = (x,y)
        self.end = (4,1)
        self.wait_steps = steps
        self.timer = 0
        self.horizontal = Action.RIGHT
        self.vertical = Action.DOWN
        self.state = [(self.start,Action.NOOP)]

    def switch_horz(self):
        self.horizontal = Action.LEFT                       \
                          if self.horizontal == Action.RIGHT\
                          else Action.RIGHT

    def switch_vert(self):
        self.vertical = Action.UP                           \
                        if self.vertical == Action.DOWN     \
                        else Action.DOWN

    def set_timer(self):
        self.timer = self.wait_steps

    def program(self,percept):

        current_position = (self.x,self.y)
        action = Action.NOOP

        #Cycle maitenance
        if(current_position == self.start or                \
           current_position == self.end) and                \
           current_position != self.state[-1][0]:
            self.set_timer()
            self.switch_vert()


        if self.timer > 0:
            self.timer -= 1
            action = Action.NOOP
        elif percept == Status.DIRTY:
            action = Action.SUCK
        elif self.move_vertically:
            self.move_vertically = False
            self.switch_horz()
            action = self.vertical
        else:
            action = self.horizontal
            if action == Action.RIGHT                       \
            and current_position[0]+1 == 4:
                self.move_vertically = True
            if action == Action.LEFT                        \
            and current_position[0]-1 == 1:
                self.move_vertically = True

        self.state.append(((current_position),action))
        return action
