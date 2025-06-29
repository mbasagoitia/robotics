# Collision Checking and Randomized Algorithms

## Sampling-Based Planning

Limitations of grid-based planning:

- Breadth-first search still requires a lot of exploration
- Problematic in higher dimensions

Instead of discretizing the configuration space into a grid, we sample from continuous coordinates.

Only need function to generate possible (random) neighbor

Very fast exploration of large configuration space

## Rapidly-Exploring Random Trees

- Randomly grow tree until goal is found
- Use A* to find shortest path
- Optimize resulting trajectory

Basic algorithm:

Input:

- Configuration space C
- Start node qStart and end node qGoal
- The maximal number of vertices in the RRT K
- The incremental distance with which to build the tree deltaQ

Output:

- RRT graph G

Steps:

- Initialize graph with qStart
- Sample random point qRand
- Find nearest point to qRand (qNear)
- Move from qNear in direction of qRand by deltaQ
- Compute potential new node qNew
- If edge between qNear and qNew is collision-free, add edge and qNew to the graph
- If qNew is less than deltaQ from qGoal, add edge from qNew to qGoal and quit
- Otherwise, repeat process until K nodes

Bias search toward goal:

- Set qRand = qGoal with probability p (such as 10% or 15% of the time)
- Bias exploration toward goal

## Improvements to RRT

RRT*: 

- Instead of adding an edge to qNear, we add an edge to the node closest to the start
- Search a d-ball around qNear
- Every edge in the graph points toward start
- RRT has a couple of other improvements, including graph alterations during search that follows

C-FOREST: Speed up and parallelize

- Further refinements can be limited to a d-ellipse that is given by the current path length
- Can also be used to parallelize the algorithm (multi-core)

## Collision-Checking

Need to check every point along a potential edge

- On a grid-map: Bresenham's line algorithm; also exists in multiple dimensions
- In continuous space: linearly interpolate vectors

For complex objects, often this is handled by computer graphics engine with built-in collision checking

- Export UniversalRoboDescriptorFile from Solidworks/Webots
- Pairwise testing of all robot parts with all obstacles nearby