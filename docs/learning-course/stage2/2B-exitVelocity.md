# 2B: Basic Shooter

## Exit Velocity

### Surface Speed

The exit velocity of the game piece is primarily controlled by the surface speed of the flywheel. Surface speed is determined by the wheel's rotations per minute (RPM) and its diameter. Increasing the diameter is often more efficient because it achieves the same surface speed with a lower RPM. A common choice is a 4-inch diameter wheel. Among all variables, RPM and, optionally, shot angle are the only controllable factors in software.

For flywheel shooters, two CIM-class brushless motors are commonly used. 

### Inertia

When shooting a single game piece at a time, common choices for flywheel wheels include stealth wheels, Colsons, and solid roller wheels. These options store enough energy for a consistent shot while being durable. Avoid using compliant or treaded wheels, as they tend to expand or fail at high speeds, leading to inconsistent performance.

Each time a game piece is launched, the flywheel loses energy and slows down as the game piece accelerates to match the wheel's speed. When shooting multiple game pieces, this can result in delays between shots. Adding mass to the flywheel increases its [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia "MOI Wikipedia Page"){:target="_blank"}, which reduces the time between shots by minimizing the energy loss per shot. The tradeoff is a longer spin-up time to reach the target speed initially.

<figure>
<img align="left" src="\img\learning-course\stage2-shooter\2056.gif" width="40%"><img align="right" src="\img\learning-course\stage2-shooter\118.gif" width="40%">
<figcaption> Team 2056 and 118 shooting quickly by utilizing a high moment of inertia shooter wheel. </figcaption>
</figure>

Acceleration and recovery times can be improved by properly gearing down your motors or adding additional motors.

### Reference Design

In the reference design, two Kraken X60 motors are employed, though any brushless CIM-class motor will suffice. 

<figure>
<img src="/img/learning-course/stage2-shooter/motorsAndFlywheels.webp" width="60%">
<figcaption>Two Krakens driving the shooter wheels, flywheels, and a belt transferring power to the hood wheels.
</figure>


### Flywheel Calculator

A useful tool for determining the optimal gear ratio is the [ReCalc Flywheel Calculator](https://www.reca.lc/flywheel "ReCalc Flywheel Calculator"){:target="_blank"}. This tool calculates spin-up time, recovery time, and estimated projectile speed based on input parameters. You can adjust the target shooter RPM, gear ratio, and flywheel mass to optimize performance, while ensuring the projectile speed remains above 12 m/s for this game. For this shooter design, [the calculations](https://www.reca.lc/flywheel?currentLimit=%7B%22s%22%3A40%2C%22u%22%3A%22A%22%7D&efficiency=90&flywheelMomentOfInertia=%7B%22s%22%3A24.688%2C%22u%22%3A%22in2%2Albs%22%7D&flywheelRadius=%7B%22s%22%3A4%2C%22u%22%3A%22in%22%7D&flywheelRatio=%7B%22magnitude%22%3A1%2C%22ratioType%22%3A%22Reduction%22%7D&flywheelWeight=%7B%22s%22%3A3.086%2C%22u%22%3A%22lbs%22%7D&motor=%7B%22quantity%22%3A2%2C%22name%22%3A%22Kraken%20X60%2A%22%7D&motorRatio=%7B%22magnitude%22%3A1.33333%2C%22ratioType%22%3A%22Reduction%22%7D&projectileRadius=%7B%22s%22%3A2%2C%22u%22%3A%22in%22%7D&projectileWeight=%7B%22s%22%3A5%2C%22u%22%3A%22oz%22%7D&shooterMomentOfInertia=%7B%22s%22%3A16.056%2C%22u%22%3A%22in2%2Albs%22%7D&shooterRadius=%7B%22s%22%3A4%2C%22u%22%3A%22in%22%7D&shooterTargetSpeed=%7B%22s%22%3A3000%2C%22u%22%3A%22rpm%22%7D&shooterWeight=%7B%22s%22%3A2.007%2C%22u%22%3A%22lbs%22%7D&useCustomFlywheelMoi=0&useCustomShooterMoi=0 "ReCalc Calculations for Example ShooteR"){:target="_blank"} were performed with ReCalc, leading to the selection of a 4:3 reduction for the 4-inch shooter wheels and two 4-inch brass flywheels.

!!! Note
    Reductions or upductions should be done with belts due to their high efficiency and low maintenance. Use pulleys larger than 24 teeth on the flywheel and ensure high tooth engagement to maximize energy transfer and prevent belt skipping.

