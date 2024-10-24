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
World   Score
AOO      2000
AXO      2000
AOX      1999
AXX      1998
OOA      2000
XOA      1999
OXA      2000
XXA      1998

Average:1999.25

Solution: simple_reflex_agent.py, exercise_9.py