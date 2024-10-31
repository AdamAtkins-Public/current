from modified_vc_world import WorldRandom as World
from agent import TimedAgent as Agent
import maps as Maps

if __name__ == "__main__":

    scores = []
    steps = 1000
    trials = 1000

    for trial in range(trials):
        world = World(Maps.Clean())
        agent = Agent(world,world.agent_x,world.agent_y,0)
        world.add_agent(agent)
        for step in range(steps):
            world.step()
        scores.append(world.score)

    print("Average score over 1000 trials: {}"\
         .format(sum([score for score in scores])/trials))
