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