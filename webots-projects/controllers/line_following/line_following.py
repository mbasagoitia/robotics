"""Line-following controller """

from controller import Robot
import numpy as np

robot = Robot()
timestep = int(robot.getBasicTimeStep())

leftMotor = robot.getDevice("left wheel motor")
rightMotor = robot.getDevice("right wheel motor")
leftMotor.setPosition(float("inf"))
rightMotor.setPosition(float("inf"))

MAX_SPEED = 3.14

gs = []
for i in range(3):
    sensor = robot.getDevice("gs" + str(i))
    sensor.enable(timestep)
    gs.append(sensor)

BLACK_THRESHOLD = 302
HIGH_THRESHOLD = 500
LOW_THRESHOLD = 350
STOP_DISTANCE = 3.0

radius = 0.0201
wheel_distance = 0.052

phildot = 0
phirdot = 0

total_distance = 0
orientation = 0

finished = False
motors_locked = False

# Problem here? Robot starts 90 degrees (I think) from starting position)
# What is alpha and omegaZ....?
alpha = np.pi / 2
xw = 0
yw = 0

while robot.step(timestep) != -1:

    g = [sensor.getValue() for sensor in gs]
    # print(g)

    timestep_s = timestep / 1000
    deltaX = ((radius * phildot + radius * phirdot) / 2) * timestep_s
    total_distance += deltaX

    omegaZ = ((radius * phirdot - radius * phildot) / wheel_distance) * timestep_s
    orientation_degrees = omegaZ * (180 / 3.14159)
    orientation += orientation_degrees

    all_black = all(val < BLACK_THRESHOLD for val in g)

    if all_black and total_distance >= STOP_DISTANCE:
        # print("stopping")
        phildot = 0
        phirdot = 0
        finished = True

    elif not finished:
   
        if g[0] > BLACK_THRESHOLD or g[1] > BLACK_THRESHOLD or g[2] > BLACK_THRESHOLD:
            if g[0] > HIGH_THRESHOLD and g[1] < LOW_THRESHOLD and g[2] > HIGH_THRESHOLD:
                phildot, phirdot = MAX_SPEED, MAX_SPEED
            elif g[2] < HIGH_THRESHOLD:
                phildot, phirdot = 0.3 * MAX_SPEED, -0.1 * MAX_SPEED
            elif g[0] < HIGH_THRESHOLD:
                phildot, phirdot = -0.1 * MAX_SPEED, 0.3 * MAX_SPEED
            else:
                phildot, phirdot = 0.3 * MAX_SPEED, 0.3 * MAX_SPEED
        else:
            phildot, phirdot = 0, 0

    if finished and not motors_locked:
        leftMotor.setVelocity(0)
        rightMotor.setVelocity(0)
        leftMotor.setPosition(leftMotor.getTargetPosition())
        rightMotor.setPosition(rightMotor.getTargetPosition())
        motors_locked = True
    else:
        leftMotor.setVelocity(phildot)
        rightMotor.setVelocity(phirdot)
    
    # Wtf is alpha doing?
    xw = xw + np.cos(alpha) * deltaX

    yw = yw + np.sin(alpha) * deltaX
    # I think position is working fine, but not orientation
    alpha = alpha + omegaZ

    print(f"Position: {xw}, {yw}, Orientation: {orientation}°")
    print("Euclidean distance: ", np.sqrt(xw**2 + yw**2))
