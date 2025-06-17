# Range Finders and Homogeneous Transforms

**Laser scanners**: historically a mechanical device (now also available as a solid state laser); results in an array of ranges and angles (angles often implicit; must compute yourself).

## Polar Coordinates

The range r is the hypotenuse of a triangle

The angle phi is the angle of the triangle

Convert to Cartesian coordinates using:

- x = r cos(phi)
- y = r sin(phi)

## Homogeneous Transforms

Instead of AQ = ABR * BQ + AP, we can express the transformation as a single matrix multiplication.

When we read laser data, we get an array of 360 values, a ray r and a corresponding angle a for each one.

1. Read laser data
2. Convert to robot coordinate system
3. Convert to world coordinate system

We multiply the x and y values of the laser data (column vectors) with the 3x3 transformation matrix

## 3D Range Finders

Also exist in 3D AKA "depth camera"

Two ways of encoding the second angle: spherical and cylindrical projection

Many different technologies: laser, time-of-flight, stereo, etc.

Pointcloud: x, y, z coordinates of each point

## Summary

- 2D and 3D range data is critical for navigation
- Range information can be turned into a point cloud
- Homogeneous transforms simplify notation and implementation
- Large variety of range sensors are available