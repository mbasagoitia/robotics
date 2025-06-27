# Differential Kinematics and Control

In differential kinematics, we are looking at the relationships of derivatives:

- x: distance
- x': speed/velocity

x' = r * phi l'/2 + r * phi r'/2
w' = (r * phi r' - r * phi l') / d

Where:

x' = speed of the robot
w' = rotational speex
r = wheel radius
phi' = derivative of wheel orientation of each wheel (left and right)

If we rearrange the above equations to solve for phi, we see that this is similar to the equations used to minimize the error of the robot's distance and angle from the target.

## Minimizing Error

Finding the minimum of an error function involves walking along its gradient/derivative. This approach is very similar to feedback control!

Minimizing the error function of the robot:

- Control input to the robot are x' (forward speed of robot) and phiR' (rotational speed of robot)
- Our error components are provided in polar coordinates
- Directly applicable to robot controller
- Solving for wheel speeds (inverse kinematics)
- Compare with intuitive result

- phiL' = (2p * 2rho - p1 alpha d) / 2r
- phiR' = (2p * 2rho + p1 alpha d) / 2r

## Proportional Control

- The larger the error, the bigger the movement
- Controller gets very slow as we approach
- Overshooting is highly undesirable
- Steady-state error due to "dead band" effect; control signal too weak to get the robot moving

## PID Control

Control signal is made up of

- Proportional to error
- Integral of previous errors
- Derivative of error

In practice you add up the last N error terms to prevent wind-up

P term helps decrease steady state error

Proportional to the change of error (D term) increases speed of convergence

Jacobian matrix can be used for gradient descent; uses partial derivatives

## Summary

- Non-holonomic systems require looking at their velocities, not actuator positions
- This is known as differential kinematics
- Velocities can be used in a feedback control scheme akin to iteratively minimizing an error function using gradient descent
- PID controllers provide additional tools to create stable controllers with faster convergence
- The general form of differential kinematics is the velocity Jacobian, which provides the gradient in multi-dimensional feedback controllers (up to six degrees of freedom)
- This also works for multi-link arms