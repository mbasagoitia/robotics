# Coordinate Transforms and Odometry

Each point representing a 3D pose relative to a coordinate system centered at a robot's center of gravity is a linear combination of basis vectors multiplied by some coefficients. Often represented as a **rotation matrix** which may simply be the identity matrix.

p = Rc

where:

- p = pose
- R = rotation matrix
- c = coefficients

A rotation matrix has 9 values, but only 4 are needed to represent orientation because a third vector is orthogonal and all of them have length 1.

The rotation matrix consists of the basis vectors of one coordinate system expressed in the target coordinate system; used to transform motions in one coordinate system into the other. These matrices can be constructed element-by-element and it always works!

## Kinematics Equations for Differential Wheeled Robots

- delta x = r * phil + r * phir
    - Translation along x-axis

- omega z = (r * phir - r * phil) / d
    - Rotation along z-axis


## Holonomy

Systems in which closed loops in joint space result in closed loops in Cartesian space are **holonomic**, such as robot arms and robot sliding on a track

If that is not the case, they are **non-holonomic**, such as most wheeled platforms

## Coordinate Transforms

If the z-axis of the world coordinate system is aligned with the z-axis of the robot system, the rotation matrix is given by:

pose in world system = 

[cos a      -sin a    0]
[sin a      cos a     0]
[0          0         0]

times 

pose in robot system ([x, y, z])

where a is the angle of the robot coordinate system relative to the world coordinate system

The simpler way to do this is to take the dot product, where xr (robot) dot product xw (world) = cos a |xr| |xw|

For the E-puck robot, we can express the change in the robot's position relative to the world coordinate system (it can only describe change in its own x and rotation in z) by the following:

xw = xw + np.cos(alpha) * deltaX

yw = yw + np.sin(alpha) * deltaX

alpha = alpha + omegaZ

We get the angle of the robot's coordinate system relative to the world's coordinate system by updating alpha, which is directly related to the rotation around the z-axis