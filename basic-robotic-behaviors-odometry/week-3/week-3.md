# Reactive Behaviors and State Machines

## Collision Avoidance

Low-level reactive primitive that stays with robot even as high-level controls are implemented. Lowest level of safety.

## Compound Behaviors

Using a combination of light and distance sensors, you can program a robot to turn towards the light, adjust wheel speed, avoid obstacles, etc. This can be done by simpling adding up their output. However, a more sophisticated way of moving the robot would be to use finite state machines and treating different states of the robot with different behaviors.

## Finite State Machines

Whereas some robots (tortoises) can be controlled by connecting sensors directly to actuators, such as in light-following, AKA phototaxis (purely reactive; no computation) and don't even require a computer (purely reactive behavior), many times we want to control the state of the machine and perform computation.

Set of finite states (initial state, follow light, avoid obstacles) and state transition functions (obstacle detected, no obstacle in sight). This can be implemented with if/else or switch statements and defining state transitions, or possibly by using a counter to stay in a certain state for several seconds, etc.

For example, the robot can estimate its progress by monitoring whether its light sensor is constantly increasing; if not, switch states.

Another behavior may be to monitor whether the robot has actually made progress towards its goal in a given amount of time, and switching states if not.

FSMs can be hard to maintain and complex, and can thus be grouped into clusters and super states to deal with information that needs to be processed at different times. This creates a hierarchical FSM/statechart. High-level FSMs may consist of several FSMs that serve a unique purpose, such as rounding sharp corners, further processing light sensors and dropping outliers/computing a running average, etc.

In practice, HFSMs are implemented in distinct processes that run independently and asynchronously. They can communicate using an inter-process communication (IPC) framework such as XMLRPC or REST, which are socket-based networking protocols that allow exchanging eXtended Markup Language (XML) or JavaScript Object Notation (JSON) data structures between two processes on the same or different computers using a networking interface. 

In an FSM, the maximum number of state transitions relative to number of states N is N*N