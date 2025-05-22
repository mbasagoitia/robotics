"""line_following controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

leftMotor = robot.getDevice("left wheel motor")
rightMotor = robot.getDevice("right wheel motor")

MAX_SPEED = 6.28

gs = []

for i in range(3):
    gs.append(robot.getDevice("gs" + str(i)))
    gs[-1].enable(timestep)

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.
    g = []
    
    for gsensor in gs:
        g.append(gsensor.getValue())
    
    print(g)
    
    if (g[0] > 500 and g[1] < 350 and g[2] > 500:
        phildot, phirdot = MAX_SPEED, MAX_SPEED
    elif (g[2] < 550)
        phildot, phirdot = 0.25 * MAX_SPEED, -0.1 * MAX_SPEED
    elif (g[0] < 550)
        phildot, phirdot = -0.1 * MAX_SPEED, 0.25 * MAX_SPEED
    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    leftMotor.setVelocity(phildot)
    rightMotor.setVelocity(phirdot)
    pass

# Enter here exit cleanup code.
