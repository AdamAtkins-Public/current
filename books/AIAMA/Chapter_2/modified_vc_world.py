from vc_enum import FloorStatus as Status
from agent_actions import Action
from agent import ReflexAgentState as Agent
import maps as Maps

class World():
    def __init__(self,map):
        self.map = map
        self.width = 0
        self.height = 0
        self.agent = None
        self.agent_x = 0
        self.agent_y = 0
        self.score = 0
        self.world = self.__build(map)

    def build(self,map):

        def map_symbol_conversion(symbol):
            status = None
            if symbol == "H":
                status = Status.OBSTACLE
            elif symbol == "X":
                status = Status.DIRTY
            elif symbol == "O":
                status = Status.CLEAN
            return status

        world = []
        self.width = len(map[0])
        self.height = len(map)

        for y in range(self.height):
            world.append([])
            for x in range(self.width):
                symbol = map[-(y+1)][x]
                if len(symbol) > 1:
                    symbol = symbol[0]
                    self.agent_x = x
                    self.agent_y = y

                world[y].append(map_symbol_conversion(symbol))

        return world

    def rebuild(self):
        self.score = 0
        self.world = self.__build(self.map)

    def add_agent(self,agent):
        self.agent = agent
        agent.update_location(self.agent_x,self.agent_y)

    def percept(self,x,y):
        return self.world[y][x]

    def performance_measure(self):
        score = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.world[y][x] == Status.CLEAN:
                    score += 1
        return score

    def is_move_action(self,action):
        return action is Action.LEFT or  \
               action is Action.RIGHT or \
               action is Action.UP or    \
               action is Action.DOWN

    def is_legal_move(self,action):
        legal = True
        if action == Action.LEFT:
            if self.world[self.agent_y][self.agent_x-1] == Status.OBSTACLE:
                legal = False
        if action == Action.RIGHT:
            if self.world[self.agent_y][self.agent_x+1] == Status.OBSTACLE:
                legal = False
        if action == Action.UP:
            if self.world[self.agent_y+1][self.agent_x] == Status.OBSTACLE:
                legal = False
        if action == Action.DOWN:
            if self.world[self.agent_y-1][self.agent_x] == Status.OBSTACLE:
                legal = False
        return legal

    def step(self):

        action = self.agent.program(self.percept(self.agent_x,self.agent_y))

        if action == Action.SUCK:
            self.world[self.agent_y][self.agent_x] = Status.CLEAN
        elif self.is_move_action(action):
            self.score -= 1

            if self.is_legal_move(action):
                if action == Action.LEFT:
                    self.agent_x -= 1
                elif action == Action.RIGHT:
                    self.agent_x += 1
                elif action == Action.UP:
                    self.agent_y += 1
                else:
                    self.agent_y -= 1

                self.agent.update_location(self.agent_x,self.agent_y)
        else: #No op
            pass
        self.score += self.performance_measure()

    __build = build

class WorldBump(World):
    def __init__(self,map):
        super().__init__(map)

    def step(self):

        action = self.agent.program(self.percept(self.agent_x,self.agent_y))
        if action == Action.SUCK:
            self.world[self.agent_y][self.agent_x] = Status.CLEAN
        elif self.is_move_action(action):
            self.score -= 1

            if self.is_legal_move(action):
                if action == Action.LEFT:
                    self.agent_x -= 1
                elif action == Action.RIGHT:
                    self.agent_x += 1
                elif action == Action.UP:
                    self.agent_y += 1
                else:
                    self.agent_y -= 1
            else:
                self.agent.set_bump(True)
        else:
            pass
        self.score += self.performance_measure()

