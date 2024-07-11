# 2B: Basic Shooter

## Shooter Mechanisms

In FRC, games where you need to launch the game piece rather than directly placing it into the goal are very common. In these games, a "high goal" worth more points and significantly above the height limit of the robot is paired with a "low goal" worth less points but within the height limit of the robot. The low goal provides an easier and more reliable way of scoring for many teams, and through the nature of the game is sometimes even required at higher levels of gameplay, but the capability of scoring in the high goal will make it easier to succeed without depending on other teams in your alliance.

This type of game can be seen in 2014, 2016, 2017, 2020, 2022, and 2024. 2018 and 2023 saw some small usage of shooters as well, but were mostly accomplished with mechanisms like elevators instead. Most games have you launch balls, but the fundamentals between ball shooters and shooters for non-spherical objects remain roughly the same.

The most common way of launching a gamepiece is with a flywheel shooter, though other methods exist (catapults and punchers).

<br>
<figure><img align="left"  src="/img/mechanism-examples/shooter/citrus-shooter.webp" width="47%"><img align="right" src="/img/design-guide/stage2-shooter/1678-2024-shooter.webp" width="47%"></figure>
<center><figcaption>1678's 2022 and 2024 Flywheel Shooters</figcaption></center>
<br>

[This video](https://youtu.be/QZKDnRvLhrA) is a good slow-motion look at how a ball gets propelled out of a shooter.

Other mechanism examples and deep dives for shooters can be found on the [ball shooters page](). The mechanism fundamentals page is yet to be made but will also be a helpful resource.


## Project

Reference [**this document**](https://cad.onshape.com/documents/8f093edaad44b5702e92ddd9/w/fefbb7a7af099fc237c1513a/e/84d7075719d34c35b3be9410) to copy the 2020 basic shooter in your own document. 

<center><img src="\img\design-guide\stage2-shooter\Shooter Assembly.webp" style="width:60%"></center>

The gamepiece you are designing for is the power cell from 2020/2021 Infinite Recharge, a 7 inch diameter foam ball. Watch the [1690 2020 Robot Reveal](https://www.youtube.com/watch?v=7EPv0gfnSEw) and [2021 Chezy Champs Finals 2](https://www.youtube.com/watch?v=kBWlbf5j5SI) for an understanding of the game tasks. Refer to the [game manual](https://firstfrc.blob.core.windows.net/frc2020/Manual/2020FRCGameSeasonManual.pdf) and [field layout drawings](https://firstfrc.blob.core.windows.net/frc2020/PlayingField/LayoutandMarkingDiagram.pdf) for field elements and [the AndyMark website](https://www.andymark.com/products/7-in-diameter-foam-ball) for power cell specifications. Let's say you've decided to shoot from just behind the white "initiation line," aiming into the smaller back goal.


### Concepts

**General Design & Robustness**

How do you make a shooter robust?
Are there ways to save money while keeping it robust?
Are there any general design principles that are popular for shooters?


Shooter robustness goes a long way to making your shooter more efficent. A robust shooter is quiet, easier to control, and more consistent. As a result, robustness is a must. The idea is that it should so stiff to the point where it doesn’t wobble or move at all. 

A common way of doing this is two sets of ¼ aluminum plates that are parallel to each other. This is one of the most robust ways, but it also tends to be extremely expensive. Other options include using a box tube support for the shooter, while using ¼ polycarbonoate machined plates to hold the bearings. As a note, if you use ¼ polycarbonate, you may need additional large diameter standoffs to keep it stiff.


Explain what makes the design simple and robust, and how to maintain rigidity in a structure like this.

<br>


**Hood Angle and Trajectory** DONE

The hood angle of a flywheel shooter for balls, if the hood isn't adjustable, should always be dependent on the field element that is being shot into and the range you're shooting from. The angle in 2017 and 2022, since the balls had to be scored from above and from relatively close, could be a little shallower than in a game like 2020, where the goal was in front of the robot.

Though there are some calculations that can be made, they are complicated, and you can usually estimate an optimal angle pretty well by picking an average distance you're most likely to be shooting a lot from (from game analysis and game strategy) and creating an arc you like that makes it into the goal at a good angle, given that the gamepieces won't be moving fast enough to achieve a straight line. For this game, at a fixed angle of around 45 degrees, you can adjust the speed of the shot depending on the distance to make the trajectory of the shot go through the goal.

<br>


**Wheel Speed, Inertia, Motors, and Ratios** DONE

Wheel speed determines how fast the flywheel spins and directly affects the distance a power cell can be shot. Higher speeds increase range but require a longer time to spin up to speed. 

The moment of inertia of the flywheel system is important for maintaining consistent speeds throughout contact with a gamepiece or multiple gamepieces. It refers to the flywheel's resistance to changes in rotational motion; while adding more mass can take more time to spin up, it decreases the recovery time (the amount of time to reach a target speed immediately following a shot). A balance must be achieved between the moment of inertia and spin-up time (independent of desired wheel speed).

The preferred choice for motors is typically two CIM class brushless motors, which balance torque, speed, and thermal efficiency without needing excessive gearing. The combined torque of your shooter motors is important to maximize to keep spin-up and recovery times low, which is why we're using 2 Kraken X60 motors, the CIM-class brushless motors with the most stall torque today. In 2020, Falcon 500s would have been used instead, as the Kraken X60s were not out yet.

A good gear ratio should allow us to spin up to speed quickly while allowing it to hit the maximum speed needed for a the distance you want to shoot from. The ratio needed is also heavily impacted by the diameter of the wheels; a larger wheel needs less angular speed than a smaller wheel. For instance, a 2-inch wheel at 3000 RPM matches a 4-inch wheel at 1500 RPM in effective speed.

A fantastic tool to help you decide your gear ratio is [https://www.reca.lc/flywheel](https://www.reca.lc/flywheel). Given a set of information, it calculates spin-up time, recovery time, and estimated projectile speed. You can mess with the target shooter rpm, ratio, and flywheel mass (the flywheels they refer to are the brass wheels added to increase the moment of inertia of the system) to try to optimize the spin-up time and recovery time, while keeping the projectile speed above around 12 m/s (for this game). For this shooter, [these calculations](https://www.reca.lc/flywheel?currentLimit=%7B%22s%22%3A40%2C%22u%22%3A%22A%22%7D&efficiency=90&flywheelMomentOfInertia=%7B%22s%22%3A24.688%2C%22u%22%3A%22in2%2Albs%22%7D&flywheelRadius=%7B%22s%22%3A4%2C%22u%22%3A%22in%22%7D&flywheelRatio=%7B%22magnitude%22%3A1%2C%22ratioType%22%3A%22Reduction%22%7D&flywheelWeight=%7B%22s%22%3A3.086%2C%22u%22%3A%22lbs%22%7D&motor=%7B%22quantity%22%3A2%2C%22name%22%3A%22Kraken%20X60%2A%22%7D&motorRatio=%7B%22magnitude%22%3A1.33333%2C%22ratioType%22%3A%22Reduction%22%7D&projectileRadius=%7B%22s%22%3A2%2C%22u%22%3A%22in%22%7D&projectileWeight=%7B%22s%22%3A5%2C%22u%22%3A%22oz%22%7D&shooterMomentOfInertia=%7B%22s%22%3A16.056%2C%22u%22%3A%22in2%2Albs%22%7D&shooterRadius=%7B%22s%22%3A4%2C%22u%22%3A%22in%22%7D&shooterTargetSpeed=%7B%22s%22%3A3000%2C%22u%22%3A%22rpm%22%7D&shooterWeight=%7B%22s%22%3A2.007%2C%22u%22%3A%22lbs%22%7D&useCustomFlywheelMoi=0&useCustomShooterMoi=0) were done and a 4:3 reduction was decided upon for the 4 inch shooter wheels and two 4 inch brass flywheels. 

!!! Note
    Reductions or upductions are usually done with belts as they can maintain high speeds without maintenance and you can perform the ratio across a distance easily with the ratio between the pulleys. It's important to try to use pulleys larger than 24 teeth and keep the tooth engagement of the pulleys high to maximize energy transfer without wear (this is especially important to consider when using a double-sided belt run).

<br>


**Contact Time and Compression (Energy Transfer)** DONE

Contact time, compression, and shooter wheel material are all important factors for how much energy is transferred from the shooter wheels to the game piece. You may have high shooter wheel speeds, but without contact time, compression, grip, and the energy to transfer (moment of inertia), the game piece won't be able to speed up enough before it leaves the shooter. 

Contact time is the duration for which the game piece remains in contact with the spinning wheel. A longer contact time allows more energy transfer from the wheel to the game piece. Of course, this requires there to be a good amount of inertia to keep the speed of the flywheel from dipping too much. When you design for contact time, you may find that a larger diameter wheel often allows for a longer contact time with the game piece. As a result, it is prioritized to have a large diameter wheel with a long contact distance

Compression is a delicate balance; compress it too little and the energy transfer will be bad, but compress it too much and it will introduce unnecessary friction and lose efficiency. Compression usually needs to be prototyped depending on the game piece. For most feeder mechanisms, you can introduce compliance in the mechanism to increase grip and contact time (i.e. using [compliance wheels](https://www.andymark.com/products/4-in-compliant-wheels-options)), but you don't want to use squishy wheels for shooter wheels as they will expand and can even explode when spun faster, making shots inconsistent. 

Instead of adding compliance in the mechanism, prototype to find the best combination between compression and shooter wheel material. The grip of the shooter wheels, a result of the hardness rating in the case of silicone, can be maximized to maximize the energy transfer. The grippiest wheels are usually ones with soft silicone or a grippy texture (you can apply grip tape). Tread patterns may even help. 

[Stealth wheels](https://www.andymark.com/products/stealth-wheels-options), fairlane wheels (colloqiual term in FRC for wheels made of solid rubber with a small core for the axle) ([WCP Solid Roller Wheels](https://wcproducts.com/products/solid-roller-wheels)), and Colson wheels are chosen commonly because of their lack of compression and soft grippy silicone surface. These are all good options for shooter wheels to prototype in a build season. 

For this design, 4" Stealth wheels have been chosen because of their grip and large diameter (leading to good contact time). This is combined with a compression of about half an inch to transfer a good amount of energy to the power cells when they are launched.



<br>


**Spin**

Depending on the gamepiece and field element into which you're launching it, spin may be crucial. In games like 2013 and 2024 with disc-shaped game pieces, adding spin stabilizes the gamepiece through gyroscopic motion. You can add backspin or topspin to spherical objects to help it stay inside the goal, like in 2017, or you may want to mitigate spin or change spin depending on the distance from the goal, like in 2022, because backspin would cause the balls to bounce or roll out of the goal. Sometimes, the spin won't matter, such as in games like 2014 or 2020. 

According to initial prototyping for this hypothetical game, the spin of the ball isn't a factor in shot consistency or accuracy. This design uses flywheels only on the bottom to launch the ball, with the ball compressing and sliding against a bent sheet of polycarbonate. This setup naturally adds backspin due to the angular direction of the shooter wheels and the friction and compression between the ball, the wheels, and the polycarbonate. To counteract backspin, wheels driven in the opposite direction on the opposite side of the ball from the launching wheels could be added, a technique used in many shooters in 2022.

[Add Image]

<br>


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


<br>

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

<br>



### Master Sketch

1. Use the origin cube featurescript 
2. Sketch any field elements you intend to interact with. There's no hard alignment, but you intend to shoot into the back goal of the "Power Port," so you must sketch that from a side view using the game manual and field layout drawings for reference. Place it 135 inches away from the origin, as that places the center of your robot 15 inches away from the white "initiation line"

    <center><img src="/img/design-guide/stage2-shooter/Field Elements.webp" width="80%"></center>

3. Sketch a side view of your drivetrain + bumpers.
4. Sketch a rectangle with your frame perimeter and height limit. This becomes your bounding box on where to design.
5. Sketch your flywheel location, with the flywheels being 4in diameter.
6. Sketch another circle concentric with the flywheels, 0.5" smaller in radius. This is to compensate for the compression of the ball.
7. Sketch another circle, concentric with the other two circles, and make the outside of that circle 7 inches away from the outside of the 3" compression circle. This large circle is to denote the path of the ball and eventually the bent polycarb the ball slides against.
8. Sketch your hood wheels by adding two 2 inch circles tangent to the outside of the large circle. Dimension them from each other using a belt calculator.
9. To constrain your shot angle to the field element placement, since the hood is not adjustable, create a line between the 3" compression circle and the last hood wheel, create an arc from the center of that line to the center of the back goal of the Power Port, and make it normal to the first line you made in this step. Adjust the radius of the arc until you are happy with the arc. The arc itself can be adjustable in real life depending on how far away from the goal you are by adjusting the speed of the flywheels.

    <center><img src="/img/design-guide/stage2-shooter/Constrained Shot Angle.webp" width="80%"></center>

10. Decide where you want the motors for the flywheels to go and dimension them away from the flywheel center using a belt calculator.
11. Now decide how the shooter is being fed. This depends on the amount of space in the rest of the indexing system, but here we're using an S-shape feeder because the balls are being fed from the front and shot from the back. Sketch two concentric circles for the feeder wheels (green compliant wheels), 3" and 2" to account for the compression of the wheels, making the 2" circle concentric to the large ball path circle. Add a final large ball path circle concentric with your feeder wheels and make it tangent to the original 3" compression circle of the flywheels.
12. Sketch 7" circles representing the power cells to further demonstrate the ball path.

Now make sure all the geometry in the master sketch is fully constrained (black). Constrain any unconstrained geometry arbitrarily if you need to.

<center><img src="/img/design-guide/stage2-shooter/Finished Master Sketch.webp" width="70%"></center>


### Part Studio

!!! Tip
    If you make a copy of the document, you can use the rollback bar to view the part studio at each step of the process.

1. Model your reference drivetrain cross tubes that the shooter plates will mount onto and make them a closed composite part. These will be 8 inches apart to leave room for the ball to travel between the plates.
2. Model your main plate on the inside of the cross rails, sketching mounting hardware holes first, including standoffs to hold the bent polycarb following the edge of the large ball path circle concentric to the feeder wheels, then power transmission (motors, belt center-to-center lines, gear pitch circles), then finally the plate outline. Similar to sketching a large gearbox, isn't it? Make sure to extrude it and mirror it for parametric reference for other parts.
3. Model the additional 1x1 tube used to mount the front of the shooter to the drivetrain. This helps keep it rigid despite potential flywheel vibrations at high speeds.
4. Model the power transmission components using the contextless belts and shaft generator featurescripts. 
5. Most pulleys will be inserted in the assembly using MKCAD's configurable HTD pulley part (they can all be 3D-printed), but the Kraken x60 pinion pulley for the feeder wheels will use a SplineXS 3D-printed part adapter. Use MKCAD to derive the base pulley into the part studio, and derive the SplineXS 3dp adapter from [this document](https://cad.onshape.com/documents/1b85e3f2d6e09d4be8bb81ba/v/531d064ba727d665df487f4a/e/e64fbaae49bd0a01559aa66c?renderMode=0&uiState=668f43004852b8565ff6390e). Perform a boolean subtract operation on the pulley with the adapter to create the cutout, checking keep tools to keep the adapter part. Make sure they're transformed into the correct place on the main plate.
6. Model the polycarb backing with holes in it to attach it to the standoffs with zip ties.
7. Model the 3D-printed camera mount and camera mount spacers for the Limelight 3

<center><img src="/img/design-guide/stage2-shooter/Shooter Part Studio.webp" width="50%"></center>

### Assembly
Create an assembly, insert the parts and origin cube from the part studio (excluding the reference tubes) with the green checkmark, and group them together. Fasten the origin cube to the origin. Add the rest of the parts from the part studio, MKCAD, and standard content, using replicate and patterns when you can. Try to use [simplified motors](https://cad.onshape.com/documents/6df614f3562416a3f9d98607/w/4e6feba12e09e298d8220fdc/e/7c565c28856cdb62e8b20117).

<center><img src="\img\design-guide\stage2-shooter\Shooter Assembly.webp" style="width:60%"></center>

<br>