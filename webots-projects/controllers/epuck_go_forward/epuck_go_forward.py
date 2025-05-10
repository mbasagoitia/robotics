from controller import Robot, Motor

TIME_STEP = 64
SPEED = 6.28  # rad/s
WHEEL_RADIUS = 0.0205  # in meters

robot = Robot()

# Motors
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(SPEED)
rightMotor.setVelocity(SPEED)

# Encoders
leftEncoder = robot.getDevice('left wheel sensor')
rightEncoder = robot.getDevice('right wheel sensor')
leftEncoder.enable(TIME_STEP)
rightEncoder.enable(TIME_STEP)

# Timing
startTime = robot.getTime()
done = False

while robot.step(TIME_STEP) != -1:
    elapsed = robot.getTime() - startTime

    if not done and elapsed >= 3.0:
        # Stop motors at exactly 3 seconds
        leftMotor.setVelocity(0)
        rightMotor.setVelocity(0)

        # Read encoder values
        leftRotation = leftEncoder.getValue()
        rightRotation = rightEncoder.getValue()
        avgRotation = (leftRotation + rightRotation) / 2

        # Convert to linear distance
        distance_m = avgRotation * WHEEL_RADIUS
        distance_cm = distance_m * 100

        print(f"Elapsed time: {elapsed:.2f} s")
        print(f"Left rotation: {leftRotation:.2f} rad")
        print(f"Right rotation: {rightRotation:.2f} rad")
        print(f"Distance traveled: {distance_cm:.2f} cm")

        done = True  # Only print once

