from exercise_11 import main as main
from modified_vc_world import WorldBump as World
from agent import RandomizedReflexAgentBump as RandomAgent
from agent import ReflexAgentStateBump as StateAgent
import maps as Maps

if __name__ == "__main__":

    #Exercise 2.12.b
    print("Randomized Agent:\n")
    main(World,RandomAgent,1000,100)

    #Exercise 2.12.d
    print("Agent with state:\n")
    main(World,StateAgent,1000,100)

