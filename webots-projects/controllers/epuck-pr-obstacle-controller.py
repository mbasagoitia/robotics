"""basic_epuck_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, LightSensor

robot = Robot()

timestep = int(robot.getBasicTimeStep())

motor_left = robot.getDevice('left wheel motor')
motor_right = robot.getDevice('right wheel motor')

ls_names = ["ls0", "ls1", "ls2", "ls3", "ls4", "ls5", "ls6", "ls7"]
light_sensors = []

for i in range(8):
    light_sensors.append(robot.getDevice(ls_names[i]))
    light_sensors[i].enable(timestep)

motor_left.setPosition(float('inf'))
motor_right.setPosition(float('inf'))

while robot.step(timestep) != -1:
    light_values = []
    for i in range(8):
        light_values.append(light_sensors[i].getValue())
    print(light_values)
    motor_left.setVelocity(light_values[7]/1000)
    motor_right.setVelocity(light_values[0]/1000)
    pass

