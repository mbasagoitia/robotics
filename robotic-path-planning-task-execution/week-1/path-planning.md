# Path Planning

Problems with feedback control:

- Different behaviors cancel each other out (obstacles vs waypoints)
- Resulting routes are not necessarily the shortest
- Time of arrival is unknown

## Multi-layer Architecture

- High-level planning on graph with optimality and coarse ETA
- Waypoint generation using different levels of local information
- Low-level implementation

We will use directed graphs (the direction of an edge matters). Can be encoded as a python dictionary with nodes as keys and nodes with incoming edges from the current node as a list of values. The path is a sequence of nodess.

Dual graphs: all the edges are nodes and all the nodes are edges; the path is a list of edges.

## Shortest Path Problem

Edge weights may represent distance, time energy, number of turns, etc. All potential paths must be explored.

Two options to explore the graph:

## Graph Traversal

**Breadth-first Search (BFS)**

FIFO: Go to a node and explore its neighbors before going deeper into the graph. Represented by queue data structure. 

- pop(0) removes and returns the first element in the list

**Depth-first Search (BFS)**

LIFO: Go deeper into the graph until you reach a leaf then return up to previously unvisited nodes. Represented by stack data structure.

- pop() removes and returns the last element in the list

To find shortest path, we add two data structures to either BFS or DFS:

- "distances" to keep track of all distances from any node to the start node; set all to infinity (except the start node, which is 0) an
- "previous" to keep track of previous nodes; every key is a node and value is the node used to go there using the shortest distance

While traversing, compute new distance by taking all distances to current node and adding 1. If the new distance is smaller than the previous distance, store new distance and update previous node.

However, this algorithm doesn't work with weighted graphs!

## Dijkstra's Algorithm

Uses a heap to visit nodes with low-cost edges first. Heapify the queue and store a tuple of node and cost

## From Grids to Graph

Can dynamically generate the graph structure from a grid map using tuples as indices on a grid.

## A* Search Algorithm

Like Dijkstra's, but with an added heuristic on the heap to expand toward the goal. Heuristic needs to underestimate for completeness. Good heuristics: Manhattan, Euclidean distance. Can be achieved by adding an estimate of the cost to the goal at every step.

Useful commands in webots:

- plt.imshow(map)
- plt.ion()

- plt.plot(goal[1], goal[0], 'y*')

- plt.show()
- plt.pause(0.000001)