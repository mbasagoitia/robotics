"""basic_epuck_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, LightSensor

robot = Robot()

timestep = int(robot.getBasicTimeStep())

motor_left = robot.getDevice('left wheel motor')
motor_right = robot.getDevice('right wheel motor')

ds_names = ["ds0", "ds1", "ds2", "ds3", "ds4", "ds5", "ds6", "ds7"]
distance_sensors = []

for i in range(8):
    distance_sensors.append(robot.getDevice(ls_names[i]))
    distance_sensors[i].enable(timestep)

motor_left.setPosition(float('inf'))
motor_right.setPosition(float('inf'))

while robot.step(timestep) != -1:
    distance_values = []
    for i in range(8):
        distance_values.append(distance_sensors[i].getValue())
    print(distance_values)
    motor_left.setVelocity(3.14)
    motor_right.setVelocity(3.14)
    pass

