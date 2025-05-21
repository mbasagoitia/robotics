WHEEL_RADIUS = 0.0205 meters

Electric motors rely on a combination of permanent magnets and coils in which a magnetic field is induced by electric current. What are possible ways to generate a change in the electric field that actually makes the motor turn?


The motor can be operated by "alternating current" (AC), which limits the rotational speed to the frequency of the current. 

Correct
This is correct. As this makes it very difficult to change speed, this approach is only used in heavy machinery. 

Provided with a sensor to estimate the position of the coil, one can use fast power electronics to switch the polarity of the current just in time. 

Correct
Yes. This is known as a "brushless DC motor".

Thinking about what you just learned about the DC motor and the stepper motor, what could be the drawback of a stepper motor? 

Stepper motors require multiple strong coils, making the stepper motor much bulkier as a DC motor.

Correct
Yes. Being bulkier is not their only drawback, however, they are usually also much more expensive than a DC motor. 

The robot always avoids the obstacle by turning right? How could we bias the robot to avoid obstacles by turning to the left? Don't just guess, but try your solution in Webots! Please select all correct answers.


phil=3.14-1.1*d[0]-d[1]-d[2]    
phir=3.14-d[7]-d[6]-d[5]

Correct
Yes, increasing the influence of the right sensor d[0], will make the left wheel brake even stronger, leading to a left turn. 


phil=3.14-0.9*d[0]-d[1]-d[2]
phir=3.14-d[7]-d[6]-d[5]


phil=3.14-d[0]-d[1]-d[2]
phir=3.14-0.9*d[7]-d[6]-d[5]

Correct
Yes. Diminishing the influence of the left sensor d[7] will make the right wheel go faster, the robot turns left. 

Changing the height of the light source had profound impact on the robot's behavior. How could you achieve a similar effect? 


Changing the orientation of the light sensors to look upward.


Making the light source even stronger.


Reducing the strength of the light even more.

Correct
Yes. Changing the orientation of the light sensors will strongly affect the observed behavior and in this case let the robot operate with a light source that is mounted higher up. 

Imagine you want to add a "Finished" state that makes the robot stop once the light is reached. Which of the following is not needed. 


The implementation of the "FINISH" state in which the wheel speeds are set to zero. 


A state transition from the "AVOID" state to the "FINISH" state ***


A state transition from the "FOLLOW" state to the "FINISH" state


A sensor event to detect when the light is reached

What information is needed to define the orientation of an object in space?


A three-axis coordinate system


6 numbers


Three translations and three rotations

Correct
Yes, specifying a three axis coordinate system is the only way to fully define a robot's orientation. There are many ways to do this and many only require four values. 

You are given a coordinate system consisting of the vectors 
(
1
,
0
,
0
)
T
(1,0,0) 
T
 left parenthesis, 1, comma, 0, comma, 0, right parenthesis, start superscript, T, end superscript and 
(
0
,
1
,
0
)
T
(0,1,0) 
T
 left parenthesis, 0, comma, 1, comma, 0, right parenthesis, start superscript, T, end superscript. The coordinate system follows the right hand rule, what is the "z" component of the third vector 
(
x
,
y
,
z
)
T
(x,y,z) 
T
 left parenthesis, x, comma, y, comma, z, right parenthesis, start superscript, T, end superscript?

1
Correct
Yes, the third vector must be orthogonal to the other two and all three vectors need to be normal vectors. 

A robot can only move forward and backwards as well as strafe left and right. How many degrees of freedom does it have? 


2


1


4

Correct
Yes, the robot is able to move along two orthogonal axes of a coordinate system. Back-and-forth and left-and-right refer to the same degree of freedom (the same coordinate axes) and therefore are only two degrees of freedom. 

Do additional motors always add degrees of freedom?


Yes, as a rule of thumb, every motor adds a degree of freedom


No, it depends on their exact configuration. 

Correct
Yes. Adding six motors behind each other will not add any degrees of freedom; worse, a robot could only turn by skidding (like a tank). The analog situation for a manipulator arm would be a motor that simply drives the same axis as another one. 

A Swedish wheel can move forward by rotating around its x-axis and sideways by rotating around its y-axis. 


Yes, the Swedish wheel has rollers, whose axes are perpendicular to the forward direction of the wheel. 


No, the rollers of the Swedish wheel are mounted at a 45 degree angle to the forward direction of the wheel. **

Correct