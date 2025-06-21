# Trajectory Following

In mobile robotics, trajectory following is the task of controlling a robot to move along a predetermined path consisting of multiple waypoints. The trajectory is essentially a sequence of coordinates that define the path that the robot should follow. The robot needs to move from one waypoint to the next until it has reached the final destination.

## Using Waypoints to Compute Errors

rho: hypotenuse of triangle which represents the distance between the robot's current orientation and desired orientation

rho = sqrt((xg - xr)^2 + (yg - yr)^2)

alpha: angle that the robot must turn to reach desired orientation

alpha = arctan2(yg - yr, xg - xr) - theta r <-- theta r = current robot orientation

theta e (error in heading) = theta g + theta r

arctan2 discontinuity: as soon as alpha exceeds 180 degrees, subtract 360 to put it back into the range of -180 to 180, and if it falls below -180 degrees, add 360 degrees

## Implementing the Controller

Turn error into wheel speed

For a right turn, since alpha is already negative:

- left wheel = -p1 * alpha + p2 * rho
- right wheel = p1 * alpha + p2 * rho

Additional term for theta e, or switch to heading adjustment once rho is below a certain length

## Summary

Going from waypoint to waypoint is a key ability for any robot (arm or mobile) to implement a desired trajectory

Waypoint navigation is a 2 step process:

1. Computing the error between current and desired pose
2. Turning the error into a control signal