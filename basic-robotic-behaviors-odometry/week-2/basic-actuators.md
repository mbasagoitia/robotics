# Basic Actuators

Common actuators in robotics, especially rolling robots

Types:

- Stepper
- DC
- Brushless DC
- Servo

Most motors rotate at high RPM and are paired with reduction gears to lower speed and increase torque. Often combined with rotary encoders for position tracking.

## AC vs DC Motors

Electric motors convert electric energy --> kinetic energy using electromagnetism.
Ampère’s Law + coil winding --> strong magnetic field.

### AC Motors

- Use alternating current (AC); current direction changes (e.g., 60 Hz).
- Magnetic field naturally alternates, creating motion.
- Speed tied to frequency of AC.
- Basic design: rotor (spinning coil) inside stator (permanent magnets).
- Used in heavy machinery due to fixed speed.
- No brushes --> relatively efficient and durable.

### DC Motors

- Use direct current (DC); current direction is constant.
- A commutator and brushes swap polarity as the motor turns to maintain rotation.
- Speed is proportional to voltage.
- Torque is limited by current.
- Widely used in robotics.

Downsides: brush friction, wear-and-tear, lower efficiency.

## Stepper Motors

- Rotate in precise steps (e.g., 3.6° per step --> 100 steps per revolution).
- Use toothed stator and rotor, with coils that pull the rotor into alignment.
- Controlled by microcontrollers or stepper driver ICs.
- No encoders needed --> position is tracked by counting steps.
- Useful for precision movement, e.g., small robots, grippers.

Tradeoffs: bulkier and more expensive than DC motors.

## Brushless DC Motors (BLDC)

- Similar in principle to stepper motors but built for high-speed rotation.
- No brushes --> higher efficiency, less maintenance.
- Use sensors (Hall effect, encoders, or back-EMF detection) to monitor rotor position.
- Require fast power electronics to switch currents at high RPMs.
- Very compact and powerful --> ideal for drones, electric vehicles, portable robots.
- Performance enhanced by rare earth magnets like neodymium.

## Servo Motors

- Combine DC motor + gearbox + encoder + controller into one unit.
- Classic application: RC cars, airplane flaps, etc.
- Basic servo: input angle signal --> motor holds that angle.
- Digital servos: can control angle, speed, torque, and read temperature, position, etc.
- Usually not suitable for drivetrain due to gear reduction, but great for arms, hands, grippers.
- Linear servo motors: rotate a spindle to produce linear (sliding) motion.

## Motor Controllers

Convert digital control signals --> precise voltages and currents. Use transistors to amplify signals,

- Capacitors and coils for smoothing
- Diodes to handle reverse voltages
Must manage:
    - Voltage (U)
    - Current (I)
    - Power (P = U × I)

- Power losses due to resistance (P = I²R) --> generates heat.
- Heat dissipation becomes a key challenge.
- Passive: through the robot’s metal chassis
- Active: using fans or other cooling mechanisms

# Other Types of Actuators

## Hydraulic and Pneumatic Actuators

- Used in linear actuators, often for legged robots.
- Can be electric, hydraulic, or pneumatic.
- Common in heavy machinery, bipedal, and quadrupedal robots.
- Hydraulic Actuators
- Typically piston-based.
- Known for high force output --> exceed electric motors.
- Much larger than electric motors (tens of cm vs. mm scale).

### Components

- Tank filled with pressurized liquid (using gas as a buffer).
- Compressor pump (usually powered by a DC motor).
- Solenoid valves: one to release liquid into the actuator, one to let liquid escape.
- Compressor re-pressurizes the system after actuation.

Force output depends on:

- Tank pressure and size
- Tube diameter
- Valve size

Lower operational range than electric motors (less adaptable in speed/force). Low bandwidth --> less reactive than electric motors. Not ideal for human-populated environments due to slower reaction time. Difficult to control and expensive to maintain.

**Pneumatic Actuators**

Operate using compressed air instead of liquid.

Require:

- Compressor
- Air tank
- Valves for flow control

Air is highly compressible --> poor for high-force applications. Lightweight and available in small sizes (e.g., mm-scale solenoid valves).
Suitable for:

- Small, intricate mechanisms (e.g., robotic fish, robotic hands)
- Soft actuators with custom bending or torsional designs
- Soft Actuators

Made of flexible rubber with internal air cavities.

Use materials that:

- Are stiff in one direction (pulling)
- Flexible in another (bending)

Direct airflow to produce controlled bending or twisting.
Not balloons --> change in volume is considered a failure mode.

Goal: All air energy --> motion, not inflation.

## Other Specialty Actuators

- Shape-Memory Alloys (SMA)
- Electroactive Polymers (EAP)
- Piezo-elements

Allow for extreme miniaturization.

Downsides:

- Poor energy-to-force ratios
- Difficult to control
