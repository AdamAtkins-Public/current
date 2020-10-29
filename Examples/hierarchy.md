
# Hierarchy

The intended purpose of this set of functions is to demonstrate how one might create a datastructure to maintain a hierarchical relationship that is present in a dataset.

## The Hierarchical Relationship

A relation on a set *V* is a relation from *V* to *V*

<img src="https://render.githubusercontent.com/render/math?math=\forall x,y \in V, x \to y \Leftrightarrow x R y \Leftrightarrow (x,y) \in R">

The Hierarchical Relationship is a direct connection between a *Superior* and a *Subordinate*.

The Hierarchical Relationship is *Irreflexive* and *Antisymmetric*, thus has an *Asymmetric* property.

A hierachical relationship can be thought of as a directed acyclic graph. 

**Constraints:**

 No value can be directly superior to itself (irreflexive/acyclic)
	<img src="https://render.githubusercontent.com/render/math?math=\forall (x,y) \in R, x \neq y">

 No value can be indirectly superior to itself (asymmetric/acyclic)
	<img src="https://render.githubusercontent.com/render/math?math=\forall \{(x,u),...,(u,y)\} \subseteq R, x \neq y">

### Sources
*Discrete Mathematics with Applications*, 4th Edition, pages 446
	For relation on a set.
