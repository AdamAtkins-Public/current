
# Hierarchy

The intended purpose of this set of functions is to demonstrate how one might create a datastructure to maintain a hierarchical relationship that is present in a dataset.

## The Hierarchical Relationship

A relation on a set *V* is a relation from *V* to *V*

<img src="https://render.githubusercontent.com/render/math?math=\forall x,y \in V, x \to y \Leftrightarrow x R y \Leftrightarrow (x,y) \in R">

The Hierarchical Relationship is a direct connection between a superior and subordinate.

A hierachical relationship can be thought of as a directed acyclic graph.

Constraints:
	- No value can be superior to itself (acyclic)
<img src="https://render.githubusercontent.com/render/math?math=\forall (x,y) \in R, x \neq y">
### Sources
*Discrete Mathematics with Applications*, 4th Edition, pages 446
	For relation on a set.
