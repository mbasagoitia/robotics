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

black_value = 302
white_high = 500
white_low = 350

"""I added in in a stop_distance variable because the sensors
sometimes read corners as "all black" due to the width of
the sensors. This is to prevent the robot from stopping
prematurely. In practice, I would adjust sensor width
or make the line thinner to better differentiate
corners from the finish line."""

stop_distance = 3
finished = False

radius = 0.0201
wheel_distance = 0.052

phildot = 0
phirdot = 0

total_distance = 0
orientation = 0

# Initial 90 degre rotation around z-axis
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

    if all(val < black_value for val in g) and total_distance >= stop_distance:
        # print("stopping")
        phildot = 0
        phirdot = 0
        finished = True

    else:
       # If at least one sensor reads white
        if g[0] > black_value or g[1] > black_value or g[2] > black_value:
            # Continue forward
            if g[0] > white_high and g[1] < white_low and g[2] > white_high:
                phildot, phirdot = MAX_SPEED, MAX_SPEED
            # Turn right
            elif g[2] < white_high:
                phildot, phirdot = 0.3 * MAX_SPEED, -0.1 * MAX_SPEED
            # Turn left
            elif g[0] < white_high:
                phildot, phirdot = -0.1 * MAX_SPEED, 0.3 * MAX_SPEED
            # Ambiguous reading, so continue forward slowly until further
            # measurements can be made
            else:
                phildot, phirdot = 0.3 * MAX_SPEED, 0.3 * MAX_SPEED

    if finished:
        leftMotor.setVelocity(0)
        rightMotor.setVelocity(0)

    else:
        leftMotor.setVelocity(phildot)
        rightMotor.setVelocity(phirdot)
   
   # Updating world position 
    xw = xw + np.cos(alpha) * deltaX
    yw = yw + np.sin(alpha) * deltaX
    alpha = alpha + omegaZ
    
    alpha_degrees = alpha * (180 / 3.14159)

    print(f"Position: x: {xw}, y: {yw}, Orientation: {alpha_degrees}°")
    print("Euclidean distance: ", np.sqrt(xw**2+yw**2), "m")
