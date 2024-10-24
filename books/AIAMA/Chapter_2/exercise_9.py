from vc_world import World as World
from simple_reflex_agent import SimpleReflexAgent as Agent
import math

def generate_configurations(height,width):
    """
    generates list of possible vacuum cleaner starting configurations

    returns list of tuples [(world,agent)]

    world - [height,width,distribution,shape]
    agent - (x,y)
    """
    configurations = []

    def gen(height,width):
        """
        permutation of indices
        """
        domain = height*width
        possible_worlds = int(math.pow(domain,2))
        index_sets = []
        for world in range(possible_worlds):
            index_set = []
            for index in range(domain):
                if ((world >> index)&1) == 1:
                    index_set.append(index)
            index_sets.append(index_set)
        return index_sets

    locations = []
    for y in range(height):
        for x in range(width):
            locations.append((x,y))

    #All possible worlds
    world_configurations = []
    for index_set in gen(height,width):
        configuration = []
        for index in index_set:
            configuration.append(locations[index])
        world_configurations.append((height,width,configuration,[]))

    #Agent start location
    for location in locations:
        for world in world_configurations:
            configurations.append((world,location))

    return configurations

def report_performance(configuration,score):
    """
    creates a string representation of the world configuration and performance score

    This is a specific function for 2.9, not intended to be used elsewhere

    X - dirty cell
    O - clean cell
    A - represents agent start location; far-left if cell 1, far-right if cell 2

    Example:
        AXO - represents agent starting in cell 1; cell 1 is dirty; cell 2 is clean
    """
    world, agent = configuration[0][2], configuration[1]
    
    if len(world) == 1:
        world_string = "XO" if world[0][0] == 0 else "OX"
    elif len(world) > 1:
        world_string = "XX"
    else:
        world_string = "OO"

    world_string = "A" + world_string \
        if agent[0] == 0 else         \
        world_string + "A"

    return "{:<5}\t{:>5}".format(world_string,score.__str__())


if __name__ == '__main__':
    """
    Exercise 2.9:

    For each possible configuration of the simple vacuum cleaner world:

        Determine the agent's performance score for the configuration

    Determine the overall average score
    """

    height, width = 1, 2
    time_steps = 1000
    scores = []
    report = []

    for config in generate_configurations(height, width):
        world = World(config[0][0],config[0][1],config[0][2],[])
        agent = Agent(world,config[1])
        score = 0
        for step in range(time_steps):
            agent.step()
            score += world.performance_measure()
        scores.append(score)
        report.append(report_performance(config,score))

    #Report
    print("World\tScore")
    for line in report:
        print(line)
    print("\nAverage:{}".format(sum(score for score in scores)/len(scores)))
   