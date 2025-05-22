# Coordinate Systems, Degrees of Freedom, and Forward Kinematics

## Degrees of Freedom

In this context, "degrees" refers to the extent of motion that you can do.

6 degrees of freedom:

Three axes in a coordinate system (translations) that something can move along:

- Forward/back
- Sideways
- Down/up

Three rotations around these axes:

- Pitch: airplane nose up/down
- Roll: turning left or right
- Yaw: turning around its center

These six numbers fully characterize the state of the plane (or other object)

To determine the complete pose of an object in space, we need to provide an entire coordinate system rooted at the center of the object

The **right hand rule** shows the relationship between the axes:

- Thumb along x-axis
- Index along y-axis
- Middle along z-axis

When holding your thumb up, the direction of your fingers curling around your hand indicates the positive direction of rotation.

Webots uses axis-angle or quaternion (four values) notation. We only need 4 values to express rotations because the vectors are orthonormal (normal and orthogonal); the third value is given by the other two.

Degrees of Freedom can be used to talk about position in Cartesian vs actuator space. Certain robots may only have the ability to travel/rotate/be controlled in certain directions (actuator space), meaning fewer degrees of freedom, or in more than six degrees (redundancy). Redundancy allows us to reach the same pose/orientation with different actuator configurations.

Also, as for the E-puck robot, it can only drive forward/back (actuator space) and rotate around z-axis, which is two degrees of freedom; but it can be anywhere in the xy plane in cartesian space and rotate around z, meaning three degrees of freedom in cartesian space.

**Degrees of freedom of wheels**

- Standard: can turn and pivot on a point (2 degrees of freedom)
- Caster wheel: can turn, pivot, and pivot on the top where it is mounted (3 degrees of freedom)
- Swedish wheel: diagonally-mounted rollers (3 degrees of freedom)
- Spherical wheel: similar to caster wheel, can be actuated

All wheels can ADD degrees of freedom OR constraints

**Degrees of freedom of manipulators**

Every motor/link usually adds a degree of freedom

**Kinematics of the E-Puck**

In differential-wheeled robots such as the e-puck, the change in the displacement of the robot (the center point) is given by:

### Translation along x-axis

delta x = r * phi1 / 2 + r * phi2 / 2

where:

- delta x = displacement
- r = wheel radius
- phi1 and phi2 are the angles at which the left and right wheels are turned, where 2pi radians is 1 full rotation

### Rotation around z-axis

To solve for the angle w itself, we can use

wd = r phi right - r phi left

where: angle of rotation times diameter (distance between the two wheels) equals arc length. Remember that a left turn (positive forward speed of right wheel) contributes to a positive move along the axis and vice versa. So the two terms cancel out when the two wheels are moving at the same speed (no angle of rotation)

We cannot derive any equations for the y-axis translation because the robot does not have the proper wheels to move along its y-axis. The same holds for rotation around the x and y-axes and translation along the z-axis.

## Static vs Dynamic Stability

A **statically stable** mechanism will not fall even when not actuated. A **dynamically stable** robot instead requires constant actuation to prevent it from falling.