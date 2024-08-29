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

In FRC, games where you need to launch the game piece rather than directly placing it into the goal are very common. In these games, a "high goal" worth more points and significantly above the height limit of the robot is often paired with a "low goal" worth less points but within the height limit of the robot. The low goal offers a more accessible and reliable scoring method for many teams. Due to the nature of the game, it is sometimes required at higher levels of play. However, the ability to score in the high goal increases the likelihood of success without relying on alliance partners.

In recent years, this type of game can be seen in 2014, 2016, 2017, 2020, 2022, and 2024. Most shooting games involve launching a ball, but the fundamentals between ball shooters and shooters for non-spherical objects remain roughly the same.

<br>
<figure><img align="left"  src="\img\learning-course\stage2-shooter\2910shooter.gif" width="47%" style="border:5px solid #ADADAD"><img align="right"  src="\img\learning-course\stage2-shooter\1690shooter.gif" width="42%" style="border:5px solid #ADADAD"></figure>
<center><figcaption>FRC Team 2910 and's 1690's 2021 Robot Launching Game Pieces</figcaption></center>
<br>

The most common way to launch game pieces is with flywheel shooters. Other methods, such as catapults and punchers, are also effective but often more challenging to execute with the required accuracy.

<br>
<figure><img align="left"  src="/img/mechanism-examples/shooter/citrus-shooter.webp" width="47%"><img align="right" src="/img/learning-course/stage2-shooter/1678-2024-shooter.webp" width="47%"></figure>
<center><figcaption>1678's 2022 and 2024 Flywheel Shooters. The 2022 shooter launched 9.5" diameter inflated balls and the 2024 shooter launched 14" diameter foam rings.</figcaption></center>
<br>

[This video](https://youtu.be/QZKDnRvLhrA) is a good slow-motion look at how a ball gets propelled out of a shooter.

Other mechanism examples and deep dives for shooters can be found on the [ball shooters page](/mechanism-examples/shooter/). The mechanism fundamentals page is yet to be made but will also be a helpful resource.


## Project

In this stage, you will be designing a shooter to launch the Power Cell, a 7 inch diameter foam ball, from the 2020/2021 Infinite Recharge game. Watch the [2020 Game Animation](https://www.youtube.com/watch?v=gmiYWTmFRVE), [Team 1690 2020 Robot Reveal](https://www.youtube.com/watch?v=7EPv0gfnSEw) and [2021 Chezy Champs Finals 2](https://www.youtube.com/watch?v=kBWlbf5j5SI) for an understanding of the game tasks. Refer to the [game manual](https://firstfrc.blob.core.windows.net/frc2020/Manual/2020FRCGameSeasonManual.pdf) and [field layout drawings](https://firstfrc.blob.core.windows.net/frc2020/PlayingField/LayoutandMarkingDiagram.pdf) for field elements and the [AndyMark website](https://www.andymark.com/products/7-in-diameter-foam-ball) for power cell specifications.

The shooter will be designed to shoot the Power Cells into the high goal from just behind the white "Initiation Line."

<center><img src="\img\learning-course\stage2-shooter\Shooter Assembly.webp" style="width:60%"></center>
<center><figcaption>Finished shooter assembly.</figcaption></center>

The reference shooter is provided in [**this document**](https://cad.onshape.com/documents/8f093edaad44b5702e92ddd9/w/fefbb7a7af099fc237c1513a/e/84d7075719d34c35b3be9410). Model a copy of it in your own document. The mechanism design concepts, decisions made for this design, and a basic guide are all provided below.


### Engineering Concepts & Decisions

The following sections cover the design rationale for the shooter mechanism you will be copying. This integrates practical design principles with CAD skills for a more complete understanding of mechanism design.

### Goal

Every time a game piece is launched, energy is lost from the flywheel, taking time to spin back to full speed. You can optimize various design concepts to reduce the energy required to launch a game piece at your target speed and rate. 

??? Concept "Rigidity"

    Just like most mechanisms you will design for a robot, rigidity is extremely important. For shooters, high speeds from the flywheel could cause shaking and shot inconsistencies if the shooter construction isn't rigid enough. 

    This shooter uses two plates of 1/4" polycarbonate for the sides (both for bearing support and extra rigidity). Polycarbonate is used as it is easy to machine, rigid enough for shooters with some support, and cheap to acquire in large sizes. Alternatives include 1/8 aluminum and 1/4 pocketed aluminum (although expensive).

    Bottom cross rails and vertical tube supports are used to create the frame. The plates are kept apart from each other on both sides by standoffs (the ramp supports and the camera support). Spacers on a shaft with shaft retention can also help maintain the distance between the plates. In this way, the position of each part of the shooter is heavily constrained and kept rigid.

??? Concept "Trajectory"
    
    For a flywheel shooter, the ball trajectory is determined by the speed of the game piece and the exit angle. Game piece speed can be adjusted for a small adjustment range, but varying the exit angle is more difficult. For this design, the exit angle is fixed. 

    <br>
    <figure>
    <img src="/img/learning-course/stage2-shooter/shot-trajectory.gif" style="width:80%; border:5px solid #ADADAD">
    </figure>
    <br>

    In most games, you can determine a single spot to shoot from every time then estimate your shot angle using a sketch of the field in relation to the shooter or a community made calculator. Further adjustments should be made by having a way to manually adjust the fixed angle after constructing the shooter. 

    For 2020, you can use the white line on the field to estimate where to shoot from and the angle, and the scoring size allows for enough forgiveness if you aren't in the exact spot when scoring. 
    
    Play with [this](https://www.desmos.com/calculator/euvciqv3tr) trajectory calculator and observe how changes in your angle and speed impact your shot. 
    !!! Calculator
        <center><iframe src="https://www.desmos.com/calculator/5fil8alfmd?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe></center>

??? Concept "Surface Speed, Inertia, Motors, and Ratios"

    Surface speed determines how fast the game piece is launched. This is determined by 

    The moment of inertia of the flywheel system is important for maintaining consistent speeds throughout contact with a gamepiece or multiple gamepieces. It refers to the flywheel's resistance to changes in rotational motion; while adding more mass can take more time to spin up, it decreases the recovery time (the amount of time to reach a target speed immediately following a shot). A balance must be achieved between the moment of inertia and spin-up time (independent of desired wheel speed).
    <figure>
        <img align="left" src="\img\learning-course\stage2-shooter\2056.gif" width="40%"><img align="right" src="\img\learning-course\stage2-shooter\118.gif" width="40%">
        <figcaption> Team 2056 and 118 shooting quickly through a high moment of inertia. </figcaption>
    </figure>

    The preferred choice for motors is typically two CIM class brushless motors, which balance torque, speed, and thermal efficiency without needing excessive gearing. The combined torque of your shooter motors is important to maximize to keep spin-up and recovery times low, which is why we're using 2 Kraken X60 motors; however, these could be swapped to any CIM class brushless motor with similar results. Just make sure to account for RPM differences properly.

    <figure>
        <img src="/img/learning-course/stage2-shooter/motorsAndFlywheels.webp" width="60%">
        <figcaption>Two Krakens driving the shooter wheels, flywheels, and a belt transferring power to the hood wheels.
    </figure>

    A good gear ratio should allow us to spin up to speed quickly while allowing it to hit the maximum speed needed for a the distance you want to shoot from. The ratio needed is also heavily impacted by the diameter of the wheels; a larger wheel needs less rpm than a smaller wheel. For instance, a 2-inch wheel at 3000 RPM matches a 4-inch wheel at 1500 RPM in effective speed.

    A fantastic tool to help you decide your gear ratio is [https://www.reca.lc/flywheel](https://www.reca.lc/flywheel). Given a set of information, it calculates spin-up time, recovery time, and estimated projectile speed. You can mess with the target shooter rpm, ratio, and flywheel mass (the flywheels they refer to are the brass wheels added to increase the moment of inertia of the system) to try to optimize the spin-up time and recovery time, while keeping the projectile speed above around 12 m/s (for this game). For this shooter, [these calculations](https://www.reca.lc/flywheel?currentLimit=%7B%22s%22%3A40%2C%22u%22%3A%22A%22%7D&efficiency=90&flywheelMomentOfInertia=%7B%22s%22%3A24.688%2C%22u%22%3A%22in2%2Albs%22%7D&flywheelRadius=%7B%22s%22%3A4%2C%22u%22%3A%22in%22%7D&flywheelRatio=%7B%22magnitude%22%3A1%2C%22ratioType%22%3A%22Reduction%22%7D&flywheelWeight=%7B%22s%22%3A3.086%2C%22u%22%3A%22lbs%22%7D&motor=%7B%22quantity%22%3A2%2C%22name%22%3A%22Kraken%20X60%2A%22%7D&motorRatio=%7B%22magnitude%22%3A1.33333%2C%22ratioType%22%3A%22Reduction%22%7D&projectileRadius=%7B%22s%22%3A2%2C%22u%22%3A%22in%22%7D&projectileWeight=%7B%22s%22%3A5%2C%22u%22%3A%22oz%22%7D&shooterMomentOfInertia=%7B%22s%22%3A16.056%2C%22u%22%3A%22in2%2Albs%22%7D&shooterRadius=%7B%22s%22%3A4%2C%22u%22%3A%22in%22%7D&shooterTargetSpeed=%7B%22s%22%3A3000%2C%22u%22%3A%22rpm%22%7D&shooterWeight=%7B%22s%22%3A2.007%2C%22u%22%3A%22lbs%22%7D&useCustomFlywheelMoi=0&useCustomShooterMoi=0) were done and a 4:3 reduction was decided upon for the 4 inch shooter wheels and two 4 inch brass flywheels. 

    !!! Note
        Reductions or upductions are usually done with belts as they can maintain high speeds without maintenance and you can perform the ratio across a distance easily with the ratio between the pulleys. It's important to try to use pulleys larger than 24 teeth and keep the tooth engagement of the pulleys high to maximize energy transfer without wear (this is especially important to consider when using a double-sided belt run).

??? Concept "Wrap and Compression (Energy Transfer)"

    Contact time, compression, and shooter wheel material are all important factors for how much energy is transferred from the shooter wheels to the game piece. You may have high shooter wheel speeds, but without contact time, compression, grip, and the energy to transfer (moment of inertia), the game piece won't be able to speed up enough before it leaves the shooter. 

    Wrap is the distance for which the game piece remains in contact with the spinning wheel. A longer contact time allows more energy transfer from the wheel to the game piece. Of course, this requires there to be a good amount of inertia to keep the speed of the flywheel from dipping too much. When you design for contact time, you may find that a larger diameter wheel often allows for a longer contact time with the game piece. As a result, it is prioritized to have a large diameter wheel with a long contact distance

    Compression is a delicate balance; compress it too little and the energy transfer will be bad, but compress it too much and it will introduce unnecessary friction and lose efficiency. Compression usually needs to be prototyped depending on the game piece. For most feeder mechanisms, you can introduce compliance in the mechanism to increase grip and contact time (i.e. using [compliance wheels](https://www.andymark.com/products/4-in-compliant-wheels-options)), but you don't want to use squishy wheels for shooter wheels as they will expand and can even explode when spun faster, making shots inconsistent. 

    ??? Video "Not Enough Compression/Contact Time/Grip"
        <figure>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/5OoCSAgqm3s?si=ougTDRU_EV1QIwa3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
        </figure>
        <figcaption>This is what it may look like if you do not have enough compression. See how loud the shooter is compared to how far the shot actually goes (Warning: Loud Audio / Swearing)</figcaption>

    ??? Video "Good Contact Time and Compression"
        <figure>
        <iframe width="320" height="560" src="https://www.youtube.com/embed/9DEJG6eoeaQ" frameborder="0" allowfullscreen></iframe>
        </figure>
        <figcaption>This is what it looks like if you have good contact time and compression with the exact same robot. (Warning: Loud Audio)</figcaption>

    In short, you want to avoid complaint wheels as their profile makes them expand at a high RPM. Treaded wheels face similar problems due to wearing out causing inconsistent contact and diameter. 

    [Stealth wheels](https://www.andymark.com/products/stealth-wheels-options), Solid roller wheels, ([WCP Solid Roller Wheels](https://wcproducts.com/products/solid-roller-wheels)), and Colson wheels are chosen commonly because of their lack of compression and soft grippy silicone surface. These are all good options for shooter wheels to prototype in a build season. 

    The example design uses 4 inch diameter roller wheels. The diameter allows for enough contact time while being small enough to reasonably package. This is combined with a compression of about half an inch to transfer a good amount of energy to the power cells when they are launched.

??? Concept "Spin/Additional Energy Transfer (Back Rollers)"

    For spherical gamepieces, backrollers may be used for two different applications. Reducing spin and adding extra energy.

    ### Spin
    Due to one side of the shooter being static, spherical game pieces have spin when shot with a single flywheel. In 2022, too much spin was detrimental since it led to bounce out of the game piece. Backrollers help reduce the amount of spin by spinning opposite of the spin direction while not being a source of friction. You don't need to eliminate all of it, just enough for the application.

    In games with disc-shaped game pieces such as 2013 or 2024, adding spin is required for a stable shot.
    
    ### Additional Energy Transfer
    In the case that you cannot transfer enough energy to the game piece from your main flywheel, additional rollers add additional energy transfer, which may allow for even longer distances if necessary. This was used in 2020 due to it being difficult to transfer enough energy into the powercell. Additional motors can also be used. 
    
    The example uses backspin rollers to show how you can execute it into your design, typically involving a long belt + gears to reverse the direction. As the wheels are only 2 inches thick, some spin still remains.

     <figure>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/QZKDnRvLhrA?si=9ZoKnbHI4jayoux0&amp;start=5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <figcaption>See how the ball spins as it travels along the shooter path. Although there are back rollers, there is still some spin </figcaption>
     </figure>
        


??? Concept "Friction & Efficiency (in the flywheel system)"

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

    Tolerance Stackup: Minimize tolerance stackup, which occurs when multiple parts connect and introduce friction. Improve precision in fabrication or reduce the number of connections. In this design, a single manufactured plate for bearing holes and center-to-center distances helps reduce tolerance stackup.

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
