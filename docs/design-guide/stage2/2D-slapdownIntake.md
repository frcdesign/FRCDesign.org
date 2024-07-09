# 2D: Slapdown Intake

## Over-the-Bumper Intakes
A common style of intake for gamepieces in FRC (depending on extension rules) is an "over-the-bumper" intake (OTB for short). These bring the gamepiece from the floor against and then over the bumper into another subsystem. They were used commonly in 2019, 2020, 2022, 2023, and 2024, and other past games. 

The two types of OTB intakes are "slapdown" which consists of a single set of arms with rollers which slap down and back up again, and four-bar linkages, which allow the intake to stow more horizontally instead of vertically. The intake designed in this stage will be a slapdown intake for 2022 (inspired by 4414 HighTide’s slapdown intake from 2023).
<br>
<figure><img align="left"  src="/img/mechanism-examples/intake/slapdown/4414style.webp" width="50%"><img align="right" src="/img/mechanism-examples/intake/4bar/1678.webp" width="40%"></figure>
<br>

[This video](https://www.youtube.com/watch?v=pSQX5c7G8yg) is a great example of a slapdown intake in 2022, on Madtown 1323's robot.

Other mechanism examples and deep dives for OTB intakes can be found on the [slapdown intakes page](../../mechanism-examples/intake/slapdown/index.md) and [4-bar intakes page](../../mechanism-examples/intake/4bar/index.md). The mechanism fundamentals page is yet to be made but will also be a helpful resource.

## Project
Reference [**this document**](https://cad.onshape.com/documents/17302d787e092ce11015f7ee/w/f7cf5c02c7655f0328a3a74a/e/f1456325e0175c4c081008c2?renderMode=0&uiState=6652c72b09aa2845d67f627f) to copy the 2022 OTB intake in your own document. 

<center><img src="/img/design-guide/stage2d/intakeTopLevel.webp" width="70%"></center>

### Concepts

**Intake Golden Rules**

There are many good resources out there for how to design good intakes. Torrance from Team 254 has provided [a list of golden rules for roller intakes](https://www.chiefdelphi.com/t/besiktas-rsports-9483-2023-off-season-build-blog/440340/15). This will also be slightly paraphrased/added to in the intake fundamentals page.


**General Design and Robustness**

The main structure uses 1/4" polycarbonate, 2x1 tubes, and nut strips to attach the plates directly to the frame. In this way, the structure would do an especially good job resisting impacts from the front. Because of the rigid nature in how the main plate is mounted, it can be polycarbonate, making it lighter and stronger than pocketed aluminum. The two secondary plates used to make sure all axles are supported on two points aren't connected with a very rigid structure and so work better as aluminum.

The intake is as wide as possible to decrease the precision and time needed by the driveteam or autonomous code to intake the game piece. The only aim is to get the game piece into the robot, then it can be centered or serialized inside frame perimeter, also minimizing the time that the intake is down.

**Pivot**

The pivot is powered by a single Kraken motor on a 2-stage MAXplanetary gearbox. The 4:1 stages in the MAXplanetary (16:1) and the 12:48 sprocket reduction make a total of 42:1 overall reduction for the pivot. You can assess whether you want this much reduction on your own mechanism by using an arm calculator, but around 30:1 to 42:1 should be good for most intakes.

The MAXplanetary uses a 1:1 belt/pulley to transfer rotation to a long cross-axle. All custom pulleys have pockets for COTS metal inserts to prevent them from stripping. There are sprockets on either end of this cross axle, with chain going up to sprockets attached to the arm. This setup is to ensure both sides of the intake are moved up and down equally so there's no weird twisting forces on the intake.

For reducing backlash in the system, the 1:1 belt/pulley is exact center-center distance, and the chains are tensioned with inline tensioners. Large sprockets on the output of the arms are good as well for more teeth engagement with the chain.

For controlling the intake position, no absolute encoder is needed. You can zero the position when it is stowed and against the hardstop or have it rest on the ground when the robot is turned on, and use the relative encoder to take it to a specific position down.


**Rollers and Roller Position**

The rollers are powered with a single Kraken motor with small reduction of 1.6:1; often, you want rollers to be spinning very fast, but still have enough torque to bring in game pieces without stalling the motor. Compression also matters a lot with this. You want to balance compression of a game piece so the intake can move it easily enough without needing too much extra torque from the motors. This is often why adding grippy material to the rollers instead of increasing compression is optimal.

There are 3 total rollers. Rollers often provide more consistent compression than wheels and are a great option for transporting game pieces. They are typically cheaper, lighter, and easier to put on a dead axle than wheels. Dead axles allow the intake arms to be connected by effectively long standoffs, making the assembly more rigid, while still allowing the rollers to spin on bearings. The dead axle rollers used in this project use polycarbonate tube and 3D-printed endcaps for the bearings and power transfer. The document can be found [here](https://cad.onshape.com/documents/b75886a5660c38eee7d50e47/w/58faeca16d5b2008a9485b5c/e/6274f59b451ed6222cd7523d).

Only 2 of the rollers are on the pivoting arm portion. The final one inside the frame perimeter is on a separate plate. This can keep the pivot for the intake arms lower, lowering the vertical height of the intake when stowed.

**Zombie Axles**

For transferring power to the rollers, because of the plates in the way and how small the pulleys are, it's necessary to transfer power through the axles (live axle). However, one of these axles is repurposed as a deadaxle by the sprockets attached to the intake arms. The sprockets are on bearings, and driven by chain, so they rotate independently from the axles used by the belts and pulleys. A setup like this, where power is transferred both through the axle and just on top of it for packaging purposes, is called a 'zombie axle'.



### Master Sketch

   1. Sketch the side of your drivetrain and bumper profile
   2. Sketch the path of the ball over the bumper
   3. Sketch roller or wheel positions needed to get the game piece to move that way. The distance between rollers should be adjusted using the [WCP Belt Calculator](https://wcproducts.com/pages/calculator-belt). "Extra center" should be set as -0.02 for ease of assembly and efficiency.
   4.  Use a sketch circular pattern to represent the stowed position of your intake rollers and define where you want the pivot to be

<center><img src="/img/design-guide/stage2d/masterSketch.webp" width="70%"></center>

### Part Studio

1. Insert the origin cube (use the featurescript)
2. CAD the front of your reference drivetrain or derive the tubes and modules from the another swerve drivebase you designed (e.g. from 2A). Make these a composite part. This is only for referencing.
3. CAD the superstructure tube (mirror and add the mirror to the drivetrain composite for referencing). Use the assembly mirror featurescript to add mate connectors to the tube for easy assembly.
4. Derive and transform the nut strips for referencing
5. Design the plates based off of your master sketch
6. Create the shafts using the shaft featurescript
7. Create the intake arm and spacer to attach a sprocket to it
8. Create a mate connector on the pivot point in the master sketch, owned by the origin cube. This is for creating motion in the top level assembly.
9. Use your chosen belt/chain generator featurescripts to create the belts and chain
10. Name and give materials and appearances to all your parts

<center><img src="/img/design-guide/stage2d/intakePartStudio.webp" width="70%"></center>

### Assembly
Because this subsystem contains a static part and a moving part, we want to separate them into rigid (no movement) assemblies, then combine them at the top level. This makes load times significantly less.

Create an assembly for the static parts, insert the parts from the part studio with the green checkmark, and group them together. Fasten the assembly to the origin by right clicking one of the parts and clicking "Add mate connector to instance origin" and fastening that mate connector to the origin of the assembly. Add the rest of the parts from the part studio, MKCAD, and standard content that don't move with the intake arms.

<center><img src="/img/design-guide/stage2d/staticAssembly.webp" width="70%"></center>

Create an assembly for the intake arms and do the same thing as above to complete the assembly and make it rigid.

<center><img src="/img/design-guide/stage2d/intakeArms.webp" width="70%"></center>

Now create a top level assembly and insert the static assembly (fasten to the origin) and intake arm assembly. Create a revolute mate between the mate connectors from the origin cubes in both assemblies and add a limit to it. This completes the slapdown intake assembly.

<center><img src="/img/design-guide/stage2d/intakeTopLevel.webp" width="70%"></center>

<br>