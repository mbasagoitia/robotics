"""basic_epuck_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
motor_left = robot.getDevice('left wheel motor')
motor_right = robot.getDevice('right wheel motor')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)
motor_left.setPosition(float('inf'))
motor_right.setPosition(float('inf'))
# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    motor_left.setVelocity(5)
    motor_right.setVelocity(10)
    pass

# Enter here exit cleanup code.
