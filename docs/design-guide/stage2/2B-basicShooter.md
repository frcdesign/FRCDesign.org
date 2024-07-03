<style>
.right{
    float:right;
}
.center{
    text-align:center;
}

.left{
    float:left;
}
</style>

# 2B: Basic Shooter

<span class="left">[< 2A: Full Detail Drivebase](2A-drivebaseFullDetail.md)</span> <span class="right">[2C: Deadaxle Pivot >](2C-deadaxlePivot.md)</span>
<br>

<<<<<<< Updated upstream
Work In Progress
=======
## Shooter Mechanisms

The type of games where you may need to launch the game piece instead of placing it directly into the goal is very common in FRC. The height limits are significantly lower than one of the scoring regions, necessitating a mechanism to launch the game piece to score it. These goals are typically defined as the “high goal”, and is often paired with another scoring region within height limits (generally called the "low goal") that may provide an easier and more reliable way of scoring for many teams. 

This type of game can be seen in 2014, 2016, 2017, 2020, 2022, and 2024. 2018 and 2023 saw some small usage of shooters as well, but were mostly accomplished with mechanisms like elevators instead. Most games have you launch balls, but the fundamentals between ball shooters and shooters for non-spherical objects remain roughly the same.

The most common way of launching a gamepiece is with a flywheel shooter, though other methods exist (catapults and punchers).

[IMAGES]

[This video](https://youtu.be/QZKDnRvLhrA) is a good slow-motion look at how a ball gets propelled out of a shooter.

Other mechanism examples and deep dives for shooters can be found on the [ball shooters page](). The mechanism fundamentals page is yet to be made but will also be a helpful resource.


## Project

Reference [**this document**](https://cad.onshape.com/documents/8f093edaad44b5702e92ddd9/w/fefbb7a7af099fc237c1513a/e/84d7075719d34c35b3be9410) to copy the basic shooter in your own document. 

[IMAGE]

The gamepiece you are designing for is a 6 inch rubber kickball like the one below.

<center><img src="\img\design-guide\stage2b\6inKickball.webp" style="width:30%"></center>

### Concepts

**Shooter Wheels**

The choice of wheel for launching the gamepiece is important, and usually prototyped to see the interaction between the wheels and gamepiece. The aspects to pay the most attention to is the hardness of the wheel surface and the grip between the wheel and gamepiece. The hardness can be a part of the grip, such as in the hardness rating of silicone, but can also be a factor in compression. Generally, since shooter wheels will be spun pretty fast for most games, you want to use wheels that can't be compressed, because they will expand depending on the angular speed and make shots inconsistent. 

The material of the wheel you choose should depend on prototyping, and should maximize grip without attaching to the gamepiece. [Stealth wheels](https://www.andymark.com/products/stealth-wheels-options) and fairlane wheels (colloqiual term in FRC for wheels made of solid rubber with a small core for the axle) ([WCP Solid Roller Wheels](https://wcproducts.com/products/solid-roller-wheels)) are chosen commonly, and used for this shooter, because of their lack of compression and soft grippy silicone surface. These are both good options for shooter wheels to prototype in a build season.


**Contact Time, Wheel Speed, & Compression**

These three factors massively impact how the game piece is launched, in addition, they all are heavily interconnected with each other.

In short:
Contact time is the distance that the game piece stays in contact with a spinning wheel.
Wheel Speed is how fast the wheel spins, in relation to the surface speed of the wheel.
Compression is how much the game piece is compressed when being launched. 
Generally speaking, a faster spinning wheel will lead to the game piece being shot farther. As a tradeoff, it will take more time to spin up to that target speed. An important factor to note is that the diameter of the wheel also impacts the speed of the shot. As a rule of thumb, a 2 inch wheel running at 3k rotations per minute will have the same effective speed as a 4-inch wheel running at 1.5k RPM. 

With that being said, another thing to keep in mind is contact time. Contact time directly relates to surface speed as the amount of time the game piece is in contact with the wheel, the more energy can be transferred to it. For example, you may need to run a flywheel at 8k RPM with a low contact time, while you might be able to run it at 3k with a longer contact time.

(show pictures)

When you design for contact time, you may find that a larger diameter wheel often allows for a longer contact time with the game piece. As a result, it is prioritized to have a large diameter wheel with a long contact distance, which allows you to spin at slower RPMs, allowing for faster acceleration.

Finally, compression. Compression plays a large factor into how efficient your shot is and how much energy is transferred into the game piece. If you have too little compression, the game piece might not take all the energy from the flywheel,≠= while too much might introduce unnecessary friction and lose efficiency. As a result, you may need to prototype to find a “perfect” compression number for your shooter or borrow values from other teams. 

In short, the squishier the game piece, the more compression you want to have, while the harder the game piece, the less compression you can have. 

**Inertia**

**Spin**

Why is spin important?
There’s multiple types of spin, but when you are launching a game piece, spin is important nonetheless. Depending on the game, you may want 0 spin, a lot of spin, or spin in a different direction (such as notes in 2024), for now, this design doesn’t implement anything that compensates for spin, as a result, the plain backing will result in a heavy backspin on the game piece.

How does it impact your shot?
In some games such as 2022, a heavy back spin may not be beneficial, leading the “bounce out”, in which the energy from the spin causes the ball to bounce out. In other games such as steamworks, the spin is beneficial, helping the game piece stay inside of the goal. 

For Disk shaped objects, spinning the object horizontally (like how you spin a frisbee), allows for a more stable flight path. There hasn’t been a game in which top spin is important, though it would be an interesting type of game. 

**Motor & Ratio Choice**

Why is motor choice important?
Why is ratio choice important?
How does it relate to surface speed?
Now, we need to power our flywheel shooter. This is done via motors. There are a lot of motors to choose from, in addition to gearing it to a certain speed, what do we choose? In short, the “go to” choice for a flywheel shooter is two CIM class brushless motors. Although we can choose smaller motors and gear them to speed, cim class motors allow us to only need a small amount of gearing, have plenty of torque and speed, and have the thermal mass necessary to not smoke.
Standardizing on this is a safe bet for success, and reduces any risks you may have with motor choice to near zero.
That being said, even though we chose motors, we still need to figure out a gear ratio. A good gear ratio should allow us to spin up to speed quickly, while hitting the minimum high speed we need in order to shoot.

This is heavily impacted by the surface speed concept we talked about in the previous section. If we have a larger wheel, we may need less gearing, or need to gear down as we have a higher surface speed. If our wheel is smaller, we may need to gear up to hit the target surface speed. In addition, factors such as wrap and compression may also impact this. 

You may be able to get a best guess estimate through calculators, but prototyping is your best bet. In general, the most you will need to gear your flywheels is either a 3:2 or a 2:3. 

An important thing to note is that tooth count is somewhat important, so it is generally good practice to have a minimum of 24 tooth pulleys.

(Insert example numbers from previous years for people to reference in terms of gearing.)
(example: 2022, 3600 RPM, 2 Falcon 500, 2:3 Ratio, 4 Inch wheel (i made these numbers up)) 


**Friction & Efficiency**

Friction & Efficiency
Why is friction and efficiency important?
How does it impact your shot speed and consistency?
What are some ways you can help fix this?
The last concept we’ll be talking about, but one of the most important concepts is friction and efficiency. This is how much friction is in your system powering your flywheel, and how efficient it is. Friction takes energy and turns it into heat. This is a problem, as we want all of the energy going into the flywheel. If we have too much friction, or its too inefficient, we may encounter issues where our flywheel wont go up to speed, and our motors burn out. As a result, we may have inconsistent shots, take a long time to go up to speed, or your motors may heat up.
We can fix this by focusing on reducing the amount of friction, there are a couple of different sources, but here are the major concepts:
Belts
For flywheels, you want to make sure you do a belt subtraction for efficiency. a -0.02 CC subtraction usually is enough, but you may need more depending on how much stackup you have.
Spacers
Spacers are important to reduce the friction between your pulleys and your bearings. Although bearings already reduce a large amount of friction, this is still important. You can see
Bent Shafts
Yes, you can bend shafts, and a small amount of bending will go a long way. In general, this comes from two different sources: Overly cantilevered shafts with tight belts, or misaligned plates. You want to try to keep your pulleys as close as you can to a bearing, and avoid layering too many plates. 
Tolerance Stackup
Similar to the bent shafts issue, but slightly different. Tolerance stackup commonly is caused by having too much going on that’s connected with each other. An example is too many belt runs that are all connected. For this shooter, we only have 1 belt run to a parralel plate, which reduces these issues.


**Indexing/Feeding**

Include storage of balls leading to the size of the shooter and indexing

Why is indexing important?
How does the type of game piece impact how you index the game piece?
Why is feeding important?
How is it different from indexing and how does it relate? 
Include storage of balls leading to the size of the shooter and indexing
Finally, we go to indexing. Indexing has many similar robustness/friction fundamentals as shooters, but indexer and feeding are important in their own way, allowing you to consistently feed the game piece into the shooter at a set speed.
The feeder feeds the game piece into the shooter, while the indexer “indexes” and organizes the game pieces to be fed one at a time consistently. This being said, your feeder and indexer can be the same thing (as shown by this example), or they can be separate. 
In games where there are multiple game pieces, your indexer is separate to organize the game pieces and have it organized to feed one at a time. In these situations your indexer may be geared slower in order to avoid the game pieces from hitting each other in the air. At the same time, you might have a separate feeder, which is both utilized to block the game peices from entering the shooter before the shooter goes to speed, while also is used to help accelerate the game piece before entering the shooter. This “pre” acceleration allows for a slightly more consistent shot.

**Hood Angle**

**General Design & Robustness**

How do you make a shooter robust?
Are there ways to save money while keeping it robust?
Are there any general design principles that are popular for shooters?


Shooter robustness goes a long way to making your shooter more efficent. A robust shooter is quiet, easier to control, and more consistent. As a result, robustness is a must. The idea is that it should so stiff to the point where it doesn’t wobble or move at all. 

A common way of doing this is two sets of ¼ aluminum plates that are parallel to each other. This is one of the most robust ways, but it also tends to be extremely expensive. Other options include using a box tube support for the shooter, while using ¼ polycarbonoate machined plates to hold the bearings. As a note, if you use ¼ polycarbonate, you may need additional large diameter standoffs to keep it stiff.


Explain what makes the design simple and robust, and how to maintain rigidity in a structure like this.

### Master Sketch
(NOTE TO DAVID: Remember, brief tips/steps for these sections, they should know how to do the actual CAD but it's nice to have a more general checklist of what to do. Be a bit more thorough in master sketches since the master sketches for each mechanism will need different things. Check the OTB intake page for an example.)

### Part Studio

### Assembly
>>>>>>> Stashed changes

<br>
<center>2B: Shooter</center> 
<span class="left">[< 2A: Full Detail Drivebase](2A-drivebaseFullDetail.md)</span> <span class="right">[2C: Deadaxle Pivot >](2C-deadaxlePivot.md)</span>
<br>
<br>