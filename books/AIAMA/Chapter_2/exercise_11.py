from modified_vc_world import World
from agent import RandomizedReflexAgent as RandomAgent
from agent import ReflexAgentState as StateAgent
import maps as Maps

def main(Agent,steps,trials):
    
    maps = [Maps.Trivial,
            Maps.Flooded_Basement,
            Maps.Living_Room,
            Maps.Dirty_Closet]
    
    max_steps = steps
    max_trials = trials

    for map in maps:

        min_score = 9999999
        max_score = 0
        scores = []

        world = World(map())

        for trial in range(max_trials):
            agent = Agent(world,world.agent_x,world.agent_y)
            world.add_agent(agent)
            for step in range(max_steps):
                world.step()
            score = world.score
            if score < min_score: min_score = score
            if score > max_score: max_score = score
            scores.append(score)
            world.rebuild()

        print("Map Name: {}\nMin Score: {}\nMax Score: {}\nAverage Score: {}\n"\
              .format(map.__name__,min_score.__str__(),max_score.__str__(),\
              (sum([score for score in scores])/len(scores)).__str__())
              )

if __name__ == "__main__":

    #Exercise 2.11.b
    print("Randomized Agent:\n")
    main(RandomAgent,1000,100)

    #Exercise 2.11.d
    print("Agent with state:\n")
    main(StateAgent,1000,100)
