<style>

    details {
        font-size: 0.7rem !important;
    }    

    .left {
        float: left;
        width: 50%;
    }

    .right {
        float: right;
        width: 50%;
    }

</style>

# 2B: Basic Shooter

## Shooter Mechanisms

Shooters are used in FRC games when you need to score in high places but are not allowed to physically reach up to the scoring position. A flywheel is the most common method of scoring as illustrated below. 

While most shooting games involve launching a ball, the fundamentals between ball shooters and shooters for non-spherical objects (discs or rings) remain roughly the same.

<br>
<figure><img align="left"  src="\img\learning-course\stage2-shooter\2910shooter.gif" width="47%" style="border:5px solid #ADADAD"><img align="right"  src="\img\learning-course\stage2-shooter\1690shooter.gif" width="42%" style="border:5px solid #ADADAD"></figure>
<center><figcaption>FRC Team 2910 and's 1690's 2021 Robot Launching Game Pieces</figcaption></center>
<br>

The most common way to launch game pieces is with flywheel shooters. Other methods, such as catapults or punchers, tend be more challenging to execute with the required accuracy/fire rate and rely on different concepts than flywheel shooters.

<br>
<figure><img align="left"  src="/img/mechanism-examples/shooter/citrus-shooter.webp" width="47%"><img align="right" src="/img/learning-course/stage2-shooter/1678-2024-shooter.webp" width="47%"></figure>
<center><figcaption>1678's 2022 and 2024 Flywheel Shooters. The 2022 shooter launched 9.5" diameter inflated balls and the 2024 shooter launched 14" diameter foam rings.</figcaption></center>
<br>

[This video](https://youtu.be/QZKDnRvLhrA) is a good slow-motion look at how a ball gets propelled out of a shooter.

Other mechanism examples and deep dives for shooters can be found on the [ball shooters page](/mechanism-examples/shooter/). The design handbook page will have a deeper dive when the shooter design page is completed. 


## Project

You will be designing a flywheel shooter to launch a Power Cell, a 7 inch diameter foam ball, from the 2020/2021 Infinite Recharge game. Watch the [2020 Game Animation](https://www.youtube.com/watch?v=gmiYWTmFRVE), [Team 1690 2020 Robot Reveal](https://www.youtube.com/watch?v=7EPv0gfnSEw) and [2021 Chezy Champs Finals 2](https://www.youtube.com/watch?v=kBWlbf5j5SI) for an understanding of the game tasks. Refer to the [game manual](https://firstfrc.blob.core.windows.net/frc2020/Manual/2020FRCGameSeasonManual.pdf) and [field layout drawings](https://firstfrc.blob.core.windows.net/frc2020/PlayingField/LayoutandMarkingDiagram.pdf) for field elements and the [AndyMark website](https://www.andymark.com/products/7-in-diameter-foam-ball) for power cell specifications.

The shooter will be designed to shoot the Power Cells into the high goal from just behind the white "Initiation Line."

<center><img src="\img\learning-course\stage2-shooter\Shooter Assembly.webp" style="width:60%"></center>
<center><figcaption>Finished shooter assembly.</figcaption></center>

The reference shooter is provided below. Note that the reference shooter is not designed for the 2020 game. 

<center>[Shooter Example]((https://cad.onshape.com/documents/8f093edaad44b5702e92ddd9/w/fefbb7a7af099fc237c1513a/e/84d7075719d34c35b3be9410)){ .md-button .md-button--primary }</center>

### Engineering Concepts & Decisions

The following sections cover the basic shooter concepts, as well as the reasons for specific implementations in the example. We cover these concepts lightly so you can design your shooter and understand the basic ideas behind shooters. The design handbook covers the "why" if you would like to gain a deeper understanding.

??? Concept "Trajectory"
    In a ball shooter, the trajectory is primarily determined by the exit angle and exit velocity of the game piece, which translates to how hard you launch and where you point the shooter.

    Rigidity is crucial for maintaining trajectory consistency. Any wobbling or flexing in the shooter structure can negatively impact accuracy, as even slight movements can alter the exit angle or velocity, leading to unpredictable shot behavior.

    <figure>
    <img src="/img/learning-course/stage2-shooter/shot-trajectory.gif" style="width:60%; border:5px solid #ADADAD">
    </figure>

    For 2020, the initiation line on the field can serve as a reference point to estimate your shooting position and angle. The goal's scoring area is forgiving enough to accommodate slight variations in position, making precise alignment less critical. By using a shot distance calculator, you can estimate the optimal shooting parameters.
    
    Explore [this 2020 trajectory calculator](https://www.desmos.com/calculator/euvciqv3tr) to see how adjustments to angle and speed affect your shot. Can you identify a combination of angle and speed that allows for consistent scoring even with some positional variation?
    !!! Calculator
        <center><iframe src="https://www.desmos.com/calculator/5fil8alfmd?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe></center>

??? Concept "Rigidity"

    Rigidity is essential for every mechanism you design, and it is particularly critical for shooters to ensure consistent performance. If a shooter wobbles while driving or shooting, accuracy will be compromised, making it difficult to hit the target consistently.

    This shooter uses two 1/4" polycarbonate plates for the sides. The 1/4" thickness is chosen because polycarbonate is easy to machine, cost-effective, and rigid enough for shooters when properly supported. In the reference design, the plates are mounted to the bottom drive rails and reinforced with support beams. Standoffs, which also serve as a camera mount and ball guide, keep the plates spaced apart, ensuring the overall rigidity of the shooter.

    <figure>
    <img src="/img/learning-course/stage2-shooter/shooterfront.webp" width="60%">
    <figcaption>1x1 structure with the gussets helping support the polycaronbate plates.
    </figure>    


??? Concept "Exit Velocity"
    **Surface Speed**

    The exit velocity of the game piece is primarily controlled by the surface speed of the flywheel. Surface speed is determined by the wheel's rotations per minute (RPM) and its diameter. Increasing the diameter is often more efficient because it achieves the same surface speed with a lower RPM. A common choice is a 4-inch diameter wheel. Among all variables, RPM and, optionally, shot angle are the only controllable factors in software.

    For flywheel shooters, two CIM-class brushless motors are commonly used. In this example, two Kraken X60 motors are employed, though any brushless CIM-class motor will suffice. 

    <figure>
    <img src="/img/learning-course/stage2-shooter/motorsAndFlywheels.webp" width="60%">
    <figcaption>Two Krakens driving the shooter wheels, flywheels, and a belt transferring power to the hood wheels.
    </figure>

    **Inertia**

    When shooting a single game piece at a time, common choices for flywheel wheels include stealth wheels, Colsons, and solid roller wheels. These options store enough energy for a consistent shot while being durable. Avoid using compliant or treaded wheels, as they tend to expand or fail at high speeds, leading to inconsistent performance.

    Each time a game piece is launched, the flywheel loses energy and slows down as the game piece accelerates to match the wheel's speed. When shooting multiple game pieces, this can result in delays between shots. Adding mass to the flywheel increases its [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia "MOI Wikipedia Page"){:target="_blank"}, which reduces the time between shots by minimizing the energy loss per shot. The tradeoff is a longer spin-up time to reach the target speed initially.

    <figure>
    <img align="left" src="\img\learning-course\stage2-shooter\2056.gif" width="40%"><img align="right" src="\img\learning-course\stage2-shooter\118.gif" width="40%">
    <figcaption> Team 2056 and 118 shooting quickly through a high moment of inertia. </figcaption>
    </figure>

    Acceleration time and recovery time can also be reduced by gearing down your motors properly, or adding additional motors. 

    A fantastic tool to help you decide your gear ratio is [https://www.reca.lc/flywheel](https://www.reca.lc/flywheel). Given a set of information, it calculates spin-up time, recovery time, and estimated projectile speed. You can mess with the target shooter rpm, ratio, and mass of your flywheel shooter to try to optimize the spin-up time and recovery time, while keeping the projectile speed above around 12 m/s (for this game). For this shooter, [these calculations] were done and a 4:3 reduction was decided upon for the 4 inch shooter wheels and two 4 inch brass flywheels. 

    Acceleration and recovery times can be improved by properly gearing down your motors or adding additional motors.

    A useful tool for determining the optimal gear ratio is the [ReCalc Flywheel Calculator](https://www.reca.lc/flywheel "ReCalc Flywheel Calculator){:target="_blank"}. This tool calculates spin-up time, recovery time, and estimated projectile speed based on input parameters. You can adjust the target shooter RPM, gear ratio, and flywheel mass to optimize performance, while ensuring the projectile speed remains above 12 m/s for this game. For this shooter design, [the calculations](https://www.reca.lc/flywheel?currentLimit=%7B%22s%22%3A40%2C%22u%22%3A%22A%22%7D&efficiency=90&flywheelMomentOfInertia=%7B%22s%22%3A24.688%2C%22u%22%3A%22in2%2Albs%22%7D&flywheelRadius=%7B%22s%22%3A4%2C%22u%22%3A%22in%22%7D&flywheelRatio=%7B%22magnitude%22%3A1%2C%22ratioType%22%3A%22Reduction%22%7D&flywheelWeight=%7B%22s%22%3A3.086%2C%22u%22%3A%22lbs%22%7D&motor=%7B%22quantity%22%3A2%2C%22name%22%3A%22Kraken%20X60%2A%22%7D&motorRatio=%7B%22magnitude%22%3A1.33333%2C%22ratioType%22%3A%22Reduction%22%7D&projectileRadius=%7B%22s%22%3A2%2C%22u%22%3A%22in%22%7D&projectileWeight=%7B%22s%22%3A5%2C%22u%22%3A%22oz%22%7D&shooterMomentOfInertia=%7B%22s%22%3A16.056%2C%22u%22%3A%22in2%2Albs%22%7D&shooterRadius=%7B%22s%22%3A4%2C%22u%22%3A%22in%22%7D&shooterTargetSpeed=%7B%22s%22%3A3000%2C%22u%22%3A%22rpm%22%7D&shooterWeight=%7B%22s%22%3A2.007%2C%22u%22%3A%22lbs%22%7D&useCustomFlywheelMoi=0&useCustomShooterMoi=0 "ReCalc Calculations for Example ShooteR"){:target="_blank"} were performed with ReCalc, leading to the selection of a 4:3 reduction for the 4-inch shooter wheels and two 4-inch brass flywheels.

    !!! Note
        Reductions or upductions should be done with belts due to their high efficiency and low maintenance. Use pulleys larger than 24 teeth on the flywheel and ensure high tooth engagement to maximize energy transfer and prevent belt skipping.

??? Concept "Wrap and Compression (Energy Transfer)"
    **Compression**

    The purpose of compression is to efficiently transfer energy from the flywheel to the game piece. The softer the game piece, the more compression is needed for effective energy transfer. Insufficient compression causes slipping, resulting in poor energy transfer, while excessive compression increases power requirements and reduces efficiency. Prototyping is essential to find the right balance. For games with hard game pieces, like in 2017, compression can be also achieved using a foam backing.

    **Wrap**

    Wrap refers to the duration the game piece stays in contact with the flywheel. A longer wrap time allows for more consistent energy transfer. For the underlying physics, see [Impulse (Wikipedia)](https://en.wikipedia.org/wiki/Impulse_(physics) "Impulse Wikiepdia Page"){:target="_blank"}.

    ??? Video "Not Enough Compression/Contact Time"
        <figure>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/5OoCSAgqm3s?si=ougTDRU_EV1QIwa3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </figure>
        <figcaption>This is what it may look like if you do not have enough compression. See how loud the shooter is compared to how far the shot actually goes (Warning: Loud Audio / Swearing)</figcaption>

    ??? Video "Good Contact Time and Compression"
        <figure>
        <iframe width="320" height="560" src="https://www.youtube.com/embed/9DEJG6eoeaQ" frameborder="0" allowfullscreen></iframe>
        </figure>
        <figcaption>This is what it looks like if you have good contact time and compression with the exact same robot. (Warning: Loud Audio)</figcaption>

    [Stealth wheels](https://www.andymark.com/products/stealth-wheels-options), Solid roller wheels, ([WCP Solid Roller Wheels](https://wcproducts.com/products/solid-roller-wheels)), and Colson wheels are chosen commonly because of their lack of compression and soft grippy silicone surface. These are all good options for shooter wheels to prototype in a build season. 

    The example design uses 4 inch diameter roller wheels. The diameter allows for enough contact time while being small enough to reasonably package. 

    **Feeder**

    A wheel or set of belts is commonly used to feed game pieces into the flywheel. The design depends on the game and the specific feeding strategy. For instance, in the 2020 game, it is advantageous to power both sides of the feeder due to the sticky nature of the power cell. In the example, a single compliant wheel is employed to direct the game pieces into the shooter.
    <br>
    <figure><img align="left"  src="\img\learning-course\stage2-shooter\2910shooter.gif" width="47%" style="border:5px solid #ADADAD"><img align="right"  src="\img\learning-course\stage2-shooter\1690shooter.gif" width="42%" style="border:5px solid #ADADAD"></figure>
    <center><figcaption>Observe how the game pieces are fed into 2910's and 1690's robot.</figcaption></center>
    <br>
        

??? Concept "Spin Control and Additional Energy (Back Rollers)"

    **Spin**

    When using a single flywheel shooter, spherical game pieces can acquire spin due to the static nature of one side of the shooter. In 2022, excessive spin was problematic as it caused the game piece to bounce out of the goal. To address this, backrollers were introduced to counteract the spin by rotating in the opposite direction. While some spin can enhance shot stability—beneficial in games like 2017, where a steep arc trajectory was advantageous—it needed to be carefully managed in 2022 to avoid negatively impacting shot accuracy.

    <center>
    <video width="600" controls>
    <source src="\img\learning-course\stage2-shooter\bounceout.webm" type="video/webm">
    Your browser does not support the video tag.
    </video>
    <center> *Bounceout caused by too much spin. Credit: FRC Team 7492* </center>
    </center>

    **Additional Energy Transfer Through Back Rollers**
    
    Reducing friction helps transfer more energy into the shot by minimizing the energy lost to spinning the ball. This can be achieved by using low-friction materials on the hood or incorporating back rollers, which further decrease friction and improve shot efficiency.

    <figure><center><iframe width="560" height="315" src="https://www.youtube.com/embed/1b8spBWIAT4?si=daEZUNFTRv_rsYMn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe><figcaption> This high speed shooter video uses PTFE tape to lower the friction on the hood backing to reduce some of the spin. This led to a higher exit velocity by 2 miles per hour. </figcaption></center></figure>
    

    Back rollers increase energy transfer to the ball in three key ways:

    1. They reduce the amount of spin imparted to the game piece, converting more energy into forward motion and increasing shooting speed.
    2. They decrease drag by ensuring both sides are powered, allowing for greater compression and more effective energy transfer.
    3. They increase the number of contact points, improving overall energy transfer to the game piece.

    Back rollers should rotate in the opposite direction to the shooter. This can be achieved by adding additional motor(s) to the back rollers or by using gears and belts to link the main flywheel to the back rollers. Linking the two sides mechanically can simplify software control. By changing the speed of the back rollers, you can control the amount of spin imparted onto the game piece.

     <figure>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/QZKDnRvLhrA?si=9ZoKnbHI4jayoux0&amp;start=5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <figcaption>Observe how the ball spins as it travels along the shooter path. Despite the presence of back rollers, some spin is still evident. </figcaption>
     </figure>
        


??? Concept "Friction & Efficiency"

    Friction reduces efficiency by converting energy into heat and adding unnecessary load to the motor. Excessive friction can prevent the flywheel from reaching speed, causing shot inconsistencies, and may overheat or damage the motors.

    **To minimize friction:**

    **Belt Tension:** Slightly reduce belt tension by shortening the center-to-center distance (0.01-0.02") to improve efficiency.

    **Spacers:** Use spacers between components on shafts and bearings. Components should not contact the outer race of the bearing to avoid friction.
    <figure>
        <img src="/img/learning-course/stage2-shooter/hexspacers.webp" width="60%">
        <figcaption>A COTS 1/2 hex delrin spacer which is used to reduce friction and constrain the object.
    </figure>
    
    **Shaft Support:** Don't over-constrain shafts by using more than 2 fixed bearing points to hold a shaft; small misalignments can cause massive friction with the bearings.
    !!! Example
        <div class = "right">
            <center>
            <img src="/img/learning-course/stage2-shooter/overconstrained-shaft.webp" width="40%">
            <figcaption>Example of a shaft being overconstrained by having a fixed bearing in the middle of the shaft.</figcaption>
            </center>
        </div>
        <div class = "left">
            <center>
            <img src="/img/learning-course/stage2-shooter/proper-constraint.webp" width="40%">
            <figcaption>Example of a shaft being properly constrained with two fixed bearings.</figcaption>
            </center>
        </div>
        

    **Bent Shafts:** Bent shafts reduce efficiency. Prevent bending by avoiding excessive cantilevering and ensuring proper alignment of bearings. Keep pulleys close to bearings

    **Tolerance Stackup:** Minimize tolerance stackup, which occurs when multiple parts connect and introduce friction. Improve precision in fabrication or reduce the number of connections. Generally its best to keep belt runs on the same plate. In this design, a single manufactured plate for bearing holes and center-to-center distances helps reduce tolerance stackup.

    **Larger Wheels:** Larger shooter wheels mean lower RPMs are necessary for the same surface speed, which reduces the amount of friction throughout the system. Additionally, gearing your motors down and running them at at not max speeds is better for the motor.

    **Last Resort:** If necessary, throw another motor at your shooter. This is the easiest way to deal with your problems in case you have slightly too much friction and need something that works without too much effort. 

    !!! Note
        These tips for reducing friction can be applied to all power transmissions


### Master Sketch

1. Use the origin cube featurescript 
2. Sketch any field elements you intend to interact with. There's no hard alignment, but you intend to shoot into the back goal of the "Power Port," so you must sketch that from a side view using the game manual and field layout drawings for reference. Place it 135 inches away from the origin, as that places the center of your robot 15 inches away from the white "initiation line"

    <center><img src="/img/learning-course/stage2-shooter/Field Elements.webp" width="80%"></center>

3. Sketch a side view of your drivetrain + bumpers.
4. Sketch a rectangle with your frame perimeter and height limit. This becomes your bounding box on where to design.
5. Sketch your flywheel location, with the flywheels being 4in diameter.
6. Sketch another circle concentric with the flywheels, 0.5" smaller in radius. This is to compensate for the compression of the ball.
7. Sketch another circle, concentric with the other two circles, and make the outside of that circle 7 inches away from the outside of the 3" compression circle. This large circle is to denote the path of the ball and eventually the bent polycarb the ball slides against.
8. Sketch your hood wheels by adding two 2 inch circles tangent to the outside of the large circle. Dimension them from each other using a belt calculator.
9. To constrain your shot angle to the field element placement, since the hood is not adjustable, create a line between the 3" compression circle and the last hood wheel, create an arc from the center of that line to the center of the back goal of the Power Port, and make it normal to the first line you made in this step. Adjust the radius of the arc until you are happy with the arc. The arc itself can be adjustable in real life depending on how far away from the goal you are by adjusting the speed of the flywheels.

    <center><img src="/img/learning-course/stage2-shooter/Constrained Shot Angle.webp" width="80%"></center>

10. Decide where you want the motors for the flywheels to go and dimension them away from the flywheel center using a belt calculator.
11. Now decide how the shooter is being fed. This depends on the amount of space in the rest of the indexing system, but here we're using an S-shape feeder because the balls are being fed from the front and shot from the back. Sketch two concentric circles for the feeder wheels (green compliant wheels), 3" and 2" to account for the compression of the wheels, making the 2" circle concentric to the large ball path circle. Add a final large ball path circle concentric with your feeder wheels and make it tangent to the original 3" compression circle of the flywheels.
12. Sketch 7" circles representing the power cells to further demonstrate the ball path.

Now make sure all the geometry in the master sketch is fully constrained (black). Constrain any unconstrained geometry arbitrarily if you need to.

<center><img src="/img/learning-course/stage2-shooter/Finished Master Sketch.webp" width="70%"></center>


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

<center><img src="/img/learning-course/stage2-shooter/Shooter Part Studio.webp" width="50%"></center>

### Assembly
Create an assembly, insert the parts and origin cube from the part studio (excluding the reference tubes) with the green checkmark, and group them together. Fasten the origin cube to the origin. Add the rest of the parts from the part studio, MKCAD, and standard content, using replicate and patterns when you can. Try to use [simplified motors](https://cad.onshape.com/documents/6df614f3562416a3f9d98607/w/4e6feba12e09e298d8220fdc/e/7c565c28856cdb62e8b20117).

<center><img src="\img\learning-course\stage2-shooter\Shooter Assembly.webp" style="width:60%"></center>

<br>

## Summary

You've completed Stage 2B, and your first full mechanism! To summarize what you've learned in this stage:

- One way to make 2 parallel plates rigid
- All the factors that go into designing a flywheel shooter
- Tips to reduce friction and inefficiences in power transmissions
- Using a reference drivetrain to build a mechanism off of to reduce integration complexity
- How to create a master sketch for a flywheel shooter for balls
- Direction-changes in power transmissions
- Customizing a 3D-printed pulley
- Designing a custom limelight mount for a shooter
- How to model a whole mechanism!

While you've now modeled your first full mechanism, it is fully static in the context of the robot, with no moving parts. In the next stage, you'll learn the different concepts that go into designing a robust pivot and how to model one in Onshape, making sure to optimize load times.

<br>
