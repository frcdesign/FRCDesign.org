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

Shooters are used in FRC games when you need to score in high places, and are not allowed to physically reach to the scoring position. A flywheel is the most common method of scoring as seen below. 

Most shooting games involve launching a ball, but the fundamentals between ball shooters and shooters for non-spherical objects (discs or rings) remain roughly the same.

<br>
<figure><img align="left"  src="\img\learning-course\stage2-shooter\2910shooter.gif" width="47%" style="border:5px solid #ADADAD"><img align="right"  src="\img\learning-course\stage2-shooter\1690shooter.gif" width="42%" style="border:5px solid #ADADAD"></figure>
<center><figcaption>FRC Team 2910 and's 1690's 2021 Robot Launching Game Pieces</figcaption></center>
<br>

The most common way to launch game pieces is with flywheel shooters. Other methods such as catapults or punchers tend be more challenging to execute with the required accuracy/fire rate. They also have different fundamentals compared to flywheel shooters.

<br>
<figure><img align="left"  src="/img/mechanism-examples/shooter/citrus-shooter.webp" width="47%"><img align="right" src="/img/learning-course/stage2-shooter/1678-2024-shooter.webp" width="47%"></figure>
<center><figcaption>1678's 2022 and 2024 Flywheel Shooters. The 2022 shooter launched 9.5" diameter inflated balls and the 2024 shooter launched 14" diameter foam rings.</figcaption></center>
<br>

[This video](https://youtu.be/QZKDnRvLhrA) is a good slow-motion look at how a ball gets propelled out of a shooter.

Other mechanism examples and deep dives for shooters can be found on the [ball shooters page](/mechanism-examples/shooter/). The design handbook page will have a deep dive, but has not been started yet. 


## Project

You will be designing a flywheel shooter to launch a Power Cell, a 7 inch diameter foam ball, from the 2020/2021 Infinite Recharge game. Watch the [2020 Game Animation](https://www.youtube.com/watch?v=gmiYWTmFRVE), [Team 1690 2020 Robot Reveal](https://www.youtube.com/watch?v=7EPv0gfnSEw) and [2021 Chezy Champs Finals 2](https://www.youtube.com/watch?v=kBWlbf5j5SI) for an understanding of the game tasks. Refer to the [game manual](https://firstfrc.blob.core.windows.net/frc2020/Manual/2020FRCGameSeasonManual.pdf) and [field layout drawings](https://firstfrc.blob.core.windows.net/frc2020/PlayingField/LayoutandMarkingDiagram.pdf) for field elements and the [AndyMark website](https://www.andymark.com/products/7-in-diameter-foam-ball) for power cell specifications.

The shooter will be designed to shoot the Power Cells into the high goal from just behind the white "Initiation Line."

<center><img src="\img\learning-course\stage2-shooter\Shooter Assembly.webp" style="width:60%"></center>
<center><figcaption>Finished shooter assembly.</figcaption></center>

The reference shooter is provided below. Note that the reference shooter is not designed for the 2020 game. 

<center>[Shooter Example]((https://cad.onshape.com/documents/8f093edaad44b5702e92ddd9/w/fefbb7a7af099fc237c1513a/e/84d7075719d34c35b3be9410)){ .md-button .md-button--primary }</center>

### Engineering Concepts & Decisions

The following sections cover the basic shooter concepts, as well as the reasons for specific implementations in the example. We cover these concepts lightly so you can design your shooter and understand the basic ideas behind shooters, but the design handbook covers the "why" and in depth concepts if you are interested.


??? Concept "Trajectory"
    ## Trajectory 
    For a ball shooter, the trajectory is determined by the exit angle and exit velocity of the game piece. (How hard you launch and where you point)

    Rigidity impacts the consistency of the trajectory which makes your shooter less accurate. (Think about if your shooter wobbled how your shot would behave)

    <br>
    <figure>
    <img src="/img/learning-course/stage2-shooter/shot-trajectory.gif" style="width:80%; border:5px solid #ADADAD">
    </figure>
    <br>

    For 2020, you can use the initiation line (big white line) on the field to estimate where to shoot from and the angle, and the scoring size allows for enough forgiveness if you aren't in the exact spot when scoring. You can use a calculator to estimate your shot distance. 
    
    Play with [this](https://www.desmos.com/calculator/euvciqv3tr) 2020 trajectory calculator and observe how changes in your angle and speed impact your shot. Can you try to find one angle and speed that lets you score the easiest without being in the exact spot? 
    !!! Calculator
        <center><iframe src="https://www.desmos.com/calculator/5fil8alfmd?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe></center>

??? Concept "Rigidity"
    ## Rigidity
    Rigidity is important for every mechanism you design. For shooters it is vital to shoot at the same place every time. Think about what would happen if the shooter wobbled as you drove and shot. 

    This shooter uses two plates of 1/4" polycarbonate for the sides. 1/4 inch thick Polycarbonate is used as it is easy to machine, cheap, and rigid enough for shooters once you add supports. 

    In the example, the plates are mounted to the bottom drive rails and support beams. The plates are kept apart from each other on both sides by standoffs, which double up a camera mount and ball guide. In this way, the shooter is rigid.

    <figure>
    <img src="/img/learning-course/stage2-shooter/shooterfront.webp" width="60%">
    <figcaption>1x1 structure with the gussets helping support the polycaronbate plates.
    </figure>    


??? Concept "Exit Velocity"
    ### Surface Speed

    The exit velocity is primarily impacted/controlled by the surface speed. 

    The rotations per minute and the diameter of wheel impacts the surface speed. Increasing the diameter is often more efficient due to requiring a lower rotations per minute for the same surface speed. A common "go to" choice is 4 inches in diameter. That being said, out of all the variables, your RPM and optionally shot angle are the only controllable variables in software.

    Common motor choices for flywheel shooters are two CIM class brushless motors. The example uses two Kraken X60 motors, but any brushless cim class motor will work fine. A third motor can be used to power the flywheel and make the rest of the design more forgiving if wanted. 

    <figure>
    <img src="/img/learning-course/stage2-shooter/motorsAndFlywheels.webp" width="60%">
    <figcaption>Two Krakens driving the shooter wheels, flywheels, and a belt transferring power to the hood wheels.
    </figure>

    ### Inertia

    If shooting a single game piece at a time, common choices include stealth wheels, colsons, and solid roller wheels. These wheels store enough energy for your shot while being hard enough to be consistent. Do not use compliant wheels or treaded wheels as they will explode/be inconsistent.
     
    Every time you launch a game piece, the flywheel loses energy and slows down as the game piece accelerates to the speed of the wheel. When shooting multiple game pieces, this can lead to waiting between shots. Adding mass to the flywheel increases the [moment of inertia (wikipedia)](https://en.wikipedia.org/wiki/Moment_of_inertia), which lowers the time between shots by reducing the percentage of energy lost per shot. The primary tradeoff is that it will take longer to initially accelerate to your target speed. 

    <figure>
    <img align="left" src="\img\learning-course\stage2-shooter\2056.gif" width="40%"><img align="right" src="\img\learning-course\stage2-shooter\118.gif" width="40%">
    <figcaption> Team 2056 and 118 shooting quickly through a high moment of inertia. </figcaption>
    </figure>

    Acceleration time and recovery time can also be reduced by gearing down your motors properly, or adding additional motors. 

    A fantastic tool to help you decide your gear ratio is [https://www.reca.lc/flywheel](https://www.reca.lc/flywheel). Given a set of information, it calculates spin-up time, recovery time, and estimated projectile speed. You can mess with the target shooter rpm, ratio, and mass of your flywheel shooter to try to optimize the spin-up time and recovery time, while keeping the projectile speed above around 12 m/s (for this game). For this shooter, [these calculations](https://www.reca.lc/flywheel?currentLimit=%7B%22s%22%3A40%2C%22u%22%3A%22A%22%7D&efficiency=90&flywheelMomentOfInertia=%7B%22s%22%3A24.688%2C%22u%22%3A%22in2%2Albs%22%7D&flywheelRadius=%7B%22s%22%3A4%2C%22u%22%3A%22in%22%7D&flywheelRatio=%7B%22magnitude%22%3A1%2C%22ratioType%22%3A%22Reduction%22%7D&flywheelWeight=%7B%22s%22%3A3.086%2C%22u%22%3A%22lbs%22%7D&motor=%7B%22quantity%22%3A2%2C%22name%22%3A%22Kraken%20X60%2A%22%7D&motorRatio=%7B%22magnitude%22%3A1.33333%2C%22ratioType%22%3A%22Reduction%22%7D&projectileRadius=%7B%22s%22%3A2%2C%22u%22%3A%22in%22%7D&projectileWeight=%7B%22s%22%3A5%2C%22u%22%3A%22oz%22%7D&shooterMomentOfInertia=%7B%22s%22%3A16.056%2C%22u%22%3A%22in2%2Albs%22%7D&shooterRadius=%7B%22s%22%3A4%2C%22u%22%3A%22in%22%7D&shooterTargetSpeed=%7B%22s%22%3A3000%2C%22u%22%3A%22rpm%22%7D&shooterWeight=%7B%22s%22%3A2.007%2C%22u%22%3A%22lbs%22%7D&useCustomFlywheelMoi=0&useCustomShooterMoi=0) were done and a 4:3 reduction was decided upon for the 4 inch shooter wheels and two 4 inch brass flywheels. 

    !!! Note
        Reductions or upductions should be done with belts for their high efficiency and low maintenance. It's important to try to use pulleys larger than 24 teeth and keep the tooth engagement of the pulleys high to maximize energy transfer without skipping.

??? Concept "Wrap and Compression (Energy Transfer)"
    ### Compression
    The purpose of compression is to transfer energy into the game piece from the flywheel. The squishier the game piece, the more compression is required in order to get efficient energy transfer. Too little compression and the game piece slips, meaning energy isn't put into the ball. At the same time, too much compression leads to dragging on the rollers, which adds additional friction and inefficiency. It is important to find a balance through prototyping. For games with extremely hard game pieces such as 2017, compression is done through a foam backing instead.
    ### Wrap
    Wrap impacts the duration that the game piece stays in contact with the flywheel. The longer time the game piece remains in contact with the shooter, the more energy can be transferred consistently. For the associated physics concept see [Impulse (Wikipedia)](https://en.wikipedia.org/wiki/Impulse_(physics)).

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

    ### Feeder

        A wheel or set of belts is frequently used to feed game pieces into the flywheel. The setup depends on the game and how you approach it feeding, but in 2020 you want to have both sides of your feeder powered due to the power cell being sticky. In the example, a single compliant wheel is used to feed the game pieces into the shooter. (Note: A feeder/Indexing section may be added to stage 2 in the future. The design handbook will have the concepts earlier)

??? Concept "Spin Control and Additional Energy (Back Rollers)"

    For spherical gamepieces, back rollers may be used for two different applications. Reducing spin and adding extra energy.

    ### Spin
    Due to one side of the shooter being static, spherical game pieces have spin when shot with a single flywheel. In 2022, too much spin was detrimental since it led to bounce out of the game piece. Backrollers help reduce the amount of spin by spinning opposite of the spin direction while not being a source of friction. Spin also allows for a more stable shot, so in 2022 you didn't want to remove all of it, while in 2017 it was useful to have due to the steep arc trajectory. 
    
    ### Additional Energy Transfer Through Back Rollers
    Friction causes some of the energy spent on accelerating the ball into spinning the ball. As a result, this reduces the translational energy (how fast it shoots). Lowering the friction on the backing helped, but back rollers were a better solution. 

    <figure><center><iframe width="560" height="315" src="https://www.youtube.com/embed/1b8spBWIAT4?si=daEZUNFTRv_rsYMn" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe><figcaption> This high speed shooter video uses PTFE tape to lower the friction on the hood backing to reduce some of the spin. This led to a higher exit velocity by 2 miles per hour. </figcaption></center></figure>
    
    Back rollers allow for three different ways to increase the energy transfer:

    1. It reduces the amount of spin which turns into translational energy (shoots faster)
    2. It reduces the amount of drag as both sides are powered, which means you can have more compression (which leads to more energy transfer)
    3. There are more rollers that are transferring energy to the game piece in general. 

    Contact time rules still apply to back rollers. Since you can't have the game piece naturally wrap around the back rollers, you will need multiple back rollers to have the best effect. 

    Another small note is that the direction of the back rollers are opposite of the shooter, so you will need to swap the direction with gears when belting them together. It is better to belt them together since you only need to control 1 variable in code instead of two. 


     <figure>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/QZKDnRvLhrA?si=9ZoKnbHI4jayoux0&amp;start=5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <figcaption>See how the ball spins as it travels along the shooter path. Although there are back rollers, there is still some spin </figcaption>
     </figure>
        


??? Concept "Friction & Efficiency"

    Friction reduces efficiency by converting energy into heat and adding unnecessary load to the motor. Excessive friction can prevent the flywheel from reaching speed, causing shot inconsistencies, and may overheat or damage the motors.

    **To minimize friction:**

    Belt Tension: Slightly reduce belt tension by shortening the center-to-center distance (0.01-0.02") to improve efficiency.

    Spacers: Use spacers between components on shafts and bearings. Components should not contact the outer race of the bearing to avoid friction.
    <figure>
        <img src="/img/learning-course/stage2-shooter/hexspacers.webp" width="60%">
        <figcaption>A COTS 1/2 hex delrin spacer which is used to reduce friction and constrain the object.
    </figure>
    
    Shaft Constrain: Don't over-constrain shafts by using more than 2 fixed bearing points to hold a shaft; small misalignments can cause massive friction with the bearings.
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
        

    Bent Shafts: Bent shafts reduce efficiency. Prevent bending by avoiding excessive cantilevering and ensuring proper alignment of bearings. Keep pulleys close to bearings

    Tolerance Stackup: Minimize tolerance stackup, which occurs when multiple parts connect and introduce friction. Improve precision in fabrication or reduce the number of connections. Generally its best to keep belt runs on the same plate. In this design, a single manufactured plate for bearing holes and center-to-center distances helps reduce tolerance stackup.

    Large Wheels: Larger shooter wheels mean lower RPMs are necessary for the same surface speed, which reduces the amount of friction throughout the system. Additionally, gearing your motors down and running them at at not max speeds is better for the motor.

    Emergencies: If necessary, throw another motor at your shooter. This is the easiest way to deal with your problems in case you have slightly too much friction and needs something that works without too much work. 

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
