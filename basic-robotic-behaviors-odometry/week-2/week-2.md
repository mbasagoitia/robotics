# Sensors and Actuators

Everday sensors:

- Proximity sensors
- 3D sensors
- Camera
- Ultrasonic
- Radar
- PIR (passive infrared)

# Sensors

## Classes of Sensors

An **accelerometer** is very cheap and small, measures acceleration, integrates for speed and distance, and whose applications include: 

- Telling the pose of an object from the direction of gravity
- Telling when robot hits an object

F = kx = ma <- this means that my knowing the mass, spring constant, and displacement, we can work out what the acceleration is

**Gyroscopes**:

- Measure orientation
- Are expensive and infeasible to minimize
- Rate gyroscopes measure rotational speed
- Are implemented using MEMS vibration devices, measure Coriolis force on two proof masses vibrating in plane
- Applications:
    - Correct heading

**Wheel/Joint Encoder**: used to tell the orientation/direciton of a wheel or a robotic arm

## Classes of Measurements

**Distance from light intensity**: emit some light of a known frequency, such as infrared, and measuring how much comes back

- Emitter/receiver pair
- Nonlinear
- Depends on surface color
- Confuses emissions from other sensors
- Requires a lot of energy

**Distance from Structure**: projecting a known pattern and observing the deformity/bending; used to reconstruct 3D information

**Distance from Sound**

- Emitter/receiver pair
- Algorithm
    - Emit ping/chirp
    - Measure time until it returns
    - Calculate distance based on speed of sound
- Requires large objects
- Quality of result depends on object size

**Distance from Phase Shift**: emitting a laser ray to measure objects based on phase shift. Expensive and don't work well in rain.

## Classifying Sensors

- Type of information (distance, acceleration, velocity)
- Physical principle (measuring sound, phase shift, displacement, etc.)
- Absolute vs derivative
- Amount of information (bandwidth/frequency at which measurements are delivered)
- Low and high reading (dynamic range)
- Accuracy and precision
- Resolution (minimum difference between values)

## Summary of Sensors

- Sensors do not serve specific applications and no sensor solves a problem completely
- Many sensors observe the same phenomenon using different physical principles
- Different sensors have different tradeoffs qualified in their different precision, accuracy, bandwidth, dynamic range, and resolution
- There are smart ways to extract the desired information from a set of sensors and fuse them (sensor fusion)

# Actuation

- Locomotion: moving oneself
    - Enacting a force on/utilizing a force within the environment
    - Rolling, walking, running, jumping, sliding, flying, etc.

- Manipulation: moving others
    - Enacting forces on objects

Choosing the right form of locomotion: Most common robotics environments are engineered to be wheel-friendly. Rolling is far more efficient for flat surfaces. No examples of wheel structures in nature.

## Actuators

- Electric motors (turns)
    - (brushless) DC
        - High RPM, low torque
        - Usually paired with gear reduction to add force at the expense of RPM
        - Encoder to determine position/amount of rotation
    - Stepper
        - Fixed amount of rotation using electromagnets

- Linear actuators
    - Electric
    - Pneumatic
    - Hydraulic
    - Many specialty actuators

Key motor innovation:

**Direct Drive**

- Brushless (less friction/wear)
- Sold w/o packaging, perfect for integration
- Hollow shaft
- High torque density
- Does not require gears

Coils create large reverse voltage spike when current stops; remedied with a flyback diode

Key motor innovation: 

**Harmonic Drive**

- Used for gear reduction
- Very high ratios, e.g. 1:50
- Requires little space
- Very efficient
- Not back-drivable

Sensors and actuators are noisy and have fundamental limitations.