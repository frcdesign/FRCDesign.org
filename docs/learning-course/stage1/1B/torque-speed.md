# 1B: Power Transmissions

## Torque and Speed

When designing power transmissions, there are two interlinked quantities that we are trying to modify: torque and speed. Torque refers to the rotational force applied to an object, while speed denotes how quickly that object rotates. In FRC, the unit used for speed is typically Rotations Per Minute (RPM). The units used for torque is typically Newton-Meters (Nm).

!!! Note "Torque and Speed"
    Speed and torque are inversely related in mechanical systems. This means that as one increases, the other decreases, and vice versa. For example, if speed is decreased by 4x, torque is increased by 4x. This is because of the principle of conservation of energy: the output energy is the same as the input energy (ignoring losses like friction), so if speed is reduced through mechanical means, torque must increase.

### Mechanical Advantage

Many mechanical systems use the principle of the conservation of energy to convert energy from one form to another to produce either larger forces or faster speeds. ***Mechanical advantage*** is the ratio of output force to input force in a system, whether it's a lever, screw, gears, or pulley, mechanical advantage is used to quantify how the force changes.

The ratio between the number of teeth of the input and output gear/sprocket/pulley system represents the mechanical advantage of that system. This is also called the ***gear ratio***, and is the key to understanding how to achieve a needed torque or speed from the specified torque and speed of a given motor.

Gear ratio is typically written in the form `n1:n2`. Since torque and speed are interlinked quantities, the ratio can be understood from the perspective of torque or speed. From the perspective of torque, `n1` is the output torque for `n2` input torque. From the perspective of speed, `n1` is the speed of the input for `n2` speed of the output. 

!!! Example
    A system has a gear ratio of 4:1. This means the output torque is 4x the input torque and that the output speed is 1/4 the input speed.

For a single stage transmission (only two transmission components), `n1` is the size of the driven component for `n2` size of the driving component.

### Ratio Applications

An arm mechanism needs very low RPM but a lot of torque to control efficiently, so a large *reduction* of speed might be used to increase torque. This depends on the weight and length of the arm, but can be 30:1 up to even 200:1. 

Shooter wheels or intake rollers often have little to no reduction, and in some cases may even need to go faster than the motor's free speed. In this case, an *upduction* can be be used to increase the speed, but the output torque gets lower as a consequence. Upductions typically don't get much higher than 1:2 due to the available motors already having a high speed, low torque output. A 1:2 upduction would double the speed and halve the torque of the input.

!!! Tip
    For situations that require higher speed and higher torque than what a single motor can provide, add more motors.

<br>