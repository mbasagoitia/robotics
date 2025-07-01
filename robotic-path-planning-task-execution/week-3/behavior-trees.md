# Behavior Trees

# RRT for Arbitrary Kinematics

- Motion model is computed from geometric description (URDF)
- Robot moves in joint space, bullet computes Cartesian pose and checks for collisions
- In practice, need:

- Inverse kinematics to sample toward goal (need equations to tell you the joing angles that would correspond to the desired position)
- Inverse differential kinematics to sample in vicinity of current location

## Behavior Trees

Behavior trees are a software engineering tool that provide additional abstractions (beyond states in finite state machines) and graphical symbols that help structure the behavior and a reduction to simple behaviors that can either succeed or fail.

- Actual implementation is in the leaves

## Sequence nodes (-->)

- Used to group leaves
- A leaf can "succeed" or "fail." A sequence keeps going until a node fails
- If any of its leaves fail, the sequence fails, otherwise it yields success
- Sequence nodes execute children (leaves) from left to right until the first one fails

## Selector Nodes (?)

- Executes leaves from left to right until the first one succeeds
- Can also be used to try different things in decreasing priority

## Adding States

Simply insert a child into the sequence and it will automatically take care of executing the necessary actions

Currently, every leaf executes until it completes; but we may need concurrency

## Real-Time Execution Model

- Introduce new state RUNNING, which represents the state until "succeed" is reached
- Return to last RUNNING state after each tick (such as 32ms)
- We can now implement real-time reactive behaviors and parallelize behavior trees

## Parallel BTs

- Execute tasks in parallel, all children are executed at the same time, such as sequences for scanning the scene and implementing the behavior
- Succeeds if all succeed, one succeed, at least n succeed

## Decorators

- Influence execution flow
    - Repeat (diamond)
    - SUCCESSisFAILURE
    - FAILUREisSUCCESS
    - RUNNINGisSUCCESS
    - etc.

## Blackboards

- Shared memory/global variables
- Controlled read and write access
- Library dependent

All of this can be implemented using the pyTrees library

## Summary

- Behavior trees are a class of abstractions that facilitate the definition of complex behaviors
- Contain sequences, selectors, and parallel nodes
- No universal definition, library dependent features and execution model
- Reduction to SUCCESS, FAILURE, and RUNNING makes composing and debugging easy