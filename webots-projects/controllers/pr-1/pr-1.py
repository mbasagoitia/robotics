"""basic_epuck_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot, LightSensor
import math

robot = Robot()
timestep = int(robot.getBasicTimeStep())

motor_left = robot.getDevice('left wheel motor')
motor_right = robot.getDevice('right wheel motor')

ds_names = ["ps0", "ps1", "ps2", "ps3", "ps4", "ps5", "ps6", "ps7"]
distance_sensors = []

for i in range(8):
    distance_sensors.append(robot.getDevice(ds_names[i]))
    distance_sensors[i].enable(timestep)

motor_left.setPosition(float('inf'))
motor_right.setPosition(float('inf'))

left_velocity = 3.14
right_velocity = 3.14

state = "drive"

# To differentiate between the three drive states, I'm keeping track of if I have already avoided the obstacles      
o1_avoided = 0
o2_avoided = 0

while robot.step(timestep) != -1:

    distance_values = [distance_sensors[i].getValue() for i in range(8)]
    
    # Describes wheel velocities/behaviors during each state
    match state:
        case "drive":
            left_velocity = 6.28
            right_velocity = 6.28
        case "turn":
            left_velocity = -3.14
            right_velocity = 3.14
        case "rotate_cw":
            left_velocity = 3.14
            right_velocity = -3.14
        case "stop":
            left_velocity = 0
            right_velocity = 0 
            
    # Approaching first obstacle and switching to turn when close enough to object        
    if state == "drive" and not o1_avoided:
        # Front distance sensor values
        fs_1 = distance_values[0]
        fs_2 = distance_values[7]
        
        if fs_1 > 80 or fs_2 > 80:
            o1_avoided = 1
            state = "turn"
    
    # Turning until back sensors are roughly equal
    if state == "turn":
        # Back distance sensor values
        bs_1 = distance_values[3]
        bs_2 = distance_values[4]
        
        if bs_1 > 80 and bs_2 > 80 and math.floor(bs_1) - math.floor(bs_2) <= 3:
            state = "drive"
    
    # First obstacle has been avoided; driving until we reach second obstacle and switching to rotate clockwise state
    if state == "drive" and o1_avoided and not o2_avoided:
        fs_1 = distance_values[0]
        fs_2 = distance_values[7]
        
        if fs_1 > 80 or fs_2 > 80:
            state = "rotate_cw"
    
    # Rotate clockwise until left sensor is at maximum value
    if state == "rotate_cw":
        # Left distance sensor value
        ls = distance_values[5]
        # print(ls)
        if ls > 109:
            o2_avoided = 1
            state = "drive"
    
    # Both abstacles have been avoided; drive forward again until left sensor no longer senses the object
    if state == "drive" and o1_avoided and o2_avoided:
        ls = distance_values[5]
        
        if ls < 80:
            state = "stop"
        
    
    motor_left.setVelocity(left_velocity)
    motor_right.setVelocity(right_velocity)


