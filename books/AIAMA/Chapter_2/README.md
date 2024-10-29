# Chapter 2

The chapter is the introduction to environment domain classification and agent architecture.

The source of the programming exercises can be found on pages 62-63.

"The following exercises all concern the implementation of environments and agents for the vacuum-cleaner world."

## 2.8 page 63

"Implement a performance-measuring environment simulator for the vacuum-cleaner world depicted in Figure 2.2 and specified on page 38. Your implementation should be modular so that the sensors, actuators, and environment characteristics (size, shape, dirt placement, etc.) can be changed easily."

* Vacuum-cleaner world
	* A simple 2d world containing cells that are either Clean or Dirty. The agent is a vacuum with the actions to move to an adjacent cell or Suck ( clean a dirty cell ).
* Performance measure
	* "The performance measure awards one point for each clean square at each time step, over a "lifetime" of 1000 time steps"
	* "The "geography" of the environment is known a priori (Figure 2.2) but the dirt distribution and the initial location of the agent are not. Clean squares stay clean and sucking cleans the current square. The Left and Right actions move the agent left and right except when this would take the agent outside the environment, in which case the agent remains where it is."
	* "The only available actions are Left, Right, and Suck."
	* "The agent correctly perceives its location and whether that location contains dirt."

Solution: vc_world.py

## 2.9 page 63

"Implement a simple reflex agent for the vacuum environment in Exercise 2.8. Run the environment with this agent for all possible initial dirt configurations and agent locations. Record the performance score for each configuration and the overall average score"

* Simple reflex agent
	* The world dimensions are 1x2 cells
	* With 2 possible statuses and 2 agent starting locations; the number of possible worlds is 2^3 

* Results

|World|Score|
|:----|----:|
|AOO|2000|
|AXO|2000|
|AOX|1999|
|AXX|1998|
|OOA|2000|
|XOA|1999|
|OXA|2000|
|XXA|1998|

Average:1999.25

Solution: simple_reflex_agent.py, exercise_9.py

## 2.10 page 63

"Consider a modified version of the vacuum environment in Exercise 2.8, in which the agent is penalized one point for each movement."

* a. "Can a simple reflex agent be perfectly rational for this environment? Explain."

No, the agent cannot be "perfectly" rational; for the agent to be "perfectly" rational there must be a guarantee that the action selected is to maximize the expected value of the performance measure. Since the agent is programmed to cover the environment, unnecessary movement occurs when the agent is moving back and forth between location A and location B.

* b. "What about a reflex agent with state? Design such an agent."

No, the agent must be programmed to cover the entire environment. Once the agent has determined that it has covered the entire environment, it can choose to remain at its current location. This reduces the unnecessary movement but is not "perfectly" rational since it may have made an unnecessary move.

Solution: simple_reflex_agent_state.py

* c. "How do your answers to **a** and **b** change if the agent's percepts give it the clean/dirty status of every square in the environment?"

For the agent without state: if the percept contains a dirty status, and the agent does not account for relative positioning, then the agent may never issue a move action if the dirty status is in a different location.

For the agent with state: the environment is fully observable from the percept, the agent has a complete model at the beginning of the process. The agent can be perfectly rational as this allows the agent to stop operation early without any unnecessary movement.

## 2.11 page 63

"Consider a modified version of the vacuum environment in Exercise 2.8, in which the geography of the environment - its extent, boundariesm and obstacles - is unknown, as is the initial dirt configuration. (The agent can go Up and Down as well as Left and Right.)"

* a. "Can a simple reflex agent be perfectly rational for this environment? Explain."

No, the simple reflex agent must know the environment a priori for perfectly rational behavior. The agent will eventually encounter a state in which it does not have an associated response.

* b "Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments."

Yes, a simple reflex agent with a randomized agent function can have higher performance because it can operate in any environment.

Environments:
		The following are some layouts of the vacuum cleaner world. They will be displayed in markdown tables with the following symbols: H, X, O, A; 
			where:
				A - Agent's starting location
				H - Wall or Obstacle
				X - Dirty status
				O - Clean status


	* Trivial 3x3

||||
|:---|:---|:---|
|H|H|H|
|H|XA|H|
|H|H|H|

	* Flooded Basement 5x5

||||||
|:---|:---|:---|:---|:---|
|H|H|H|H|H|
|H|X|X|X|H|
|H|X|XA|X|H|
|H|X|X|X|H|
|H|H|H|H|H|

	* L-Living Room 9x9

||||||||||
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|H|H|H|H|H|H|H|H|H|
|H|X|O|X|X|O|O|X|H|
|H|X|O|X|X|X|X|O|H|
|H|X|O|O|O|X|X|X|H|
|H|O|O|X|O|O|X|O|H|
|H|H|X|H|H|X|O|X|H|
|H|H|X|H|H|O|X|O|H|
|H|H|X|H|H|O|X|OA|H|
|H|H|H|H|H|H|H|H|H|

	* Dirty Closet 11x11

||||||||||||
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
|H|H|H|H|H|H|H|H|H|H|H|
|H|O|O|O|O|O|O|O|O|O|H|
|H|O|H|H|H|X|H|H|H|O|H|
|H|O|H|X|X|X|X|X|H|O|H|
|H|O|H|X|X|X|X|X|H|O|H|
|H|O|H|X|X|X|X|X|H|O|H|
|H|O|H|H|H|H|H|H|H|O|H|
|H|O|O|O|O|O|O|O|O|O|H|
|H|O|O|O|O|OA|O|O|O|O|H|
|H|O|O|O|O|O|O|O|O|O|H|
|H|H|H|H|H|H|H|H|H|H|H|


The following are the minimum, maximum, and average scores for a simple reflex agent with a randomized program. The scores are gathered over 100 trials in each of the environments displayed above.

Results

Map Name: Trivial
Min Score: 269
Max Score: 361
Average Score: 325.59

Map Name: Flooded_Basement
Min Score: 7158
Max Score: 8038
Average Score: 7655.37

Map Name: Living_Room
Min Score: 25780
Max Score: 33644
Average Score: 30238.0

Map Name: Dirty_Closet
Min Score: 45304
Max Score: 55687
Average Score: 47253.6

Solution: exercise_11.py, modified_vc_world.py, agent.py, maps.py

* c. "Can you design an environment in which your randomized agent will perform poorly? Show your results."

The results are listed in **b**. The agent can perform poorly in: large environments with many dirty cells (ex. Living Room) and environments with long-narrow corridors (ex. Dirty Closet); but if it is lucky to navigate the areas, it has a chance to perform well. The agent will perform move actions that penalize the score when no further moves are necessary in smaller environments (ex. Trivial)

* d. "Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?"

A reflex agent with state can outperform a simple reflex agent without state. The state allows for opportunities to rationally issue a No Op action, which improves performance by reducing the movement penalty.  Without the use of search algorithms, my attempt at a rational simple reflex agent (agent.py: ReflexAgentState()) fails to cover the entire area of some environments. With A* and some DFS, an agent can be expected to rationally cover the entire environment.


Results

Map Name: Trivial

Min Score: 996
Max Score: 996
Average Score: 996.0

Map Name: Flooded_Basement
Min Score: 8816
Max Score: 8816
Average Score: 8816.0

Map Name: Living_Room
Min Score: 30427
Max Score: 30427
Average Score: 30427.0

Map Name: Dirty_Closet
Min Score: 45852
Max Score: 45852
Average Score: 45852.0

Solution: exercise_11.py, modified_vc_world.py, agent.py, maps.py

## 2.12 page 63

"Repeat Exercise 2.11 for the case in which the location sensor is replaced with "bump" sensor that detects the agent's attempts to move into an obstacle or to cross boundaries of the environment. Suppose the bump sensor stops working, how should the agent behave?'"

If the bump sensor stops working, the agent should either revert to a randomized program or issue no op. Since it is not possible for the agent to determine whether the sensor is working or not, because it cannot track its location, the agent cannot rationally change its program.

* a. "Can a simple reflex agent be perfectly rational for this environment? Explain."

An agent without location tracking will not be able to determine the environment layout. Since knowledge of the dimensions of the environment are essential to expect perfect scores, the agent cannot be expected to be perfectly rational.

* b. "Can a simple reflex agent with a randomized agent function outperform a simple reflex agent? Design such an agent and measure its performance on several environments."

A randomized agent function does not make use of the bump sensor as it determines its action at random. The same agent and expected results are in common with Excersise 2.11.b.

* c. "Can you design an environment in which your randomized agent will perform poorly? Show your results."

The results are in common with Exercise 2.11.c.

* d. "Can a reflex agent with state outperform a simple reflex agent? Design such an agent and measure its performance on several environments. Can you design a rational agent of this type?"

I modified the agent design from 2.11.d by mapping its state interpretation to the bump sensor. The modifications resulted in a performance loss for the environment set.

Results:

Map Name: Trivial
Min Score: 989
Max Score: 989
Average Score: 989.0

Map Name: Flooded_Basement
Min Score: 7897
Max Score: 7897
Average Score: 7897.0

Map Name: Living_Room
Min Score: 30499
Max Score: 30499
Average Score: 30499.0

Map Name: Dirty_Closet
Min Score: 45000
Max Score: 45000
Average Score: 45000.0

Solution: exercise_12.py, modified_vc_world.py, agent.py
