# Mapping

Range data is usually provided in polar coordinates (distance r and angle theta for each laser ray).

To convert to robot coordinate system, x = r cos(theta) and y = r sin(theta); these x and y coordinates give you a point cloud, which also exists in 3D.

Homogeneous transforms allow you to create a 4x4 matrix that contains the 3x3 rotation matrix and 3x1 translation vector

To get the point cloud in world coordinates, we multiply this transformation matrix with the 3x360 matrix vector of angles and readings.

With this data, we can perform mapping for uses such as:

- Navigation
- Localization

## Grid Map

All world data is stored in a grid, creating a constant memory requirement. Transforms continuous world coordinates into discrete map coordinates using some discretizing function.

Laser data (ranges and angles) -> transformation point cloud -> discretization -> NxN map (where N is the width of the map)

Write down x/y extrema/bounds/corners of the world data and i/j discrete map values for the same locations and derive a function to map these points to a discrete display.

This representation is not efficient to store in a computer, so we use a **K-D Tree** to store grid-based data where K is the dimension (in this case 4, known as a **4D/QuadTree**).

Splits the arena in 4 ways--4 big squares, further subdivides squares as needed.

- Store points in a list associated with each quadrant of the map
- Limit the number of points each quadrant can store
- As more measurements come in, if the number of points exceeds this number, subdivide the quadrant and store points in the new quadrant(s)
- Can define a number of resolution layers and discard further points that fall into each bin

Benefits of QuadTrees:

- Save a lot of memory
- Accessing the data is easier
    - Accessing/retrieval all M occupied pixels is O(M) time because empty areas are skipped
    - Checking if x/y coordinate is occupied: traverse up to maximum depth of tree (O(1))

## Topological Maps

- All points of interest have GPS coordinates
- Intersections and streets are nodes and edges of a graph
- Often stored in a dictrionary as a collection of nodes, each with a list of each neighbor that can be accessed from it and the edge cost/weight
- Can use shortest path algorithms on graphs

Can convert between grid-maps and graphs and vice versa

## Mapping and Localization

- You cannot map without good localization
- Odometry is quite bad
- GPS (location) and compass (orientation) sensors help
- In the real world, this problem is known as simultaneous localization and mapping
