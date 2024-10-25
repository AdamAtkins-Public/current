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
