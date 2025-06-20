# Probabilistic Mapping and Configuration Space

How can we create consistent and reliable maps? They are noisy due to localization and sensor error

Uncertainty comes from laser uncertainty--poor reflection, robot wobble, laser may hit ground

## Probabilistic Map

Each entry is the probability of a cell being occupied

Basic approach: 

- Increment cell by 1% whenever it is hit by the laser
- Decrememt by 1% when nothing is read in that cell
- Use thresholding to determine obstacles (such as 0.5 or above)

Now that we have an obstacle map, how can we use it for navigation?

Questions of interest:

- How can we deal with the extension of the robot when finding a shortest path to the white dot?

Solution: **configuration space**

Grow all obstaclesby the radius of the robot and turn the robot to a point

The robot is now represented by a point x and y

## Computing the Configuration Space (2D)

Blurring operation: 

- Grow by half the radius of the robot and threshold
- Robot becomes a single pixel
- If objects now touch, robot will not fit
- This only works if the robot is circular

## Computing 3D Configuration Space

- Robot is a rectangle instead of a disc
- Convolve with a rectangular kernel
- Check to see if robot can turn

- Can be computed for arbitrary angles (quadrants, octants, 360 degrees, etc.)
- Robot can move up and down a layer by turning
- Planning problem is now in 3D space

## The Convolution

"Shift two functions against each other and compute their product at this position"

Add up the products of the two functions at all positions 

2D convolution:

- Sweep "kernel" over an image, such as a Gaussian kernel

Edge detection kernels

## Bresenham's Line Algorithm

- Very fast, only integer operations
- Each octant (45 degree slice) uses specific equation
- No need to implement this, use any line-drawing algorithm

Lasers don't just provide measurements of obstacles; they also measure free space