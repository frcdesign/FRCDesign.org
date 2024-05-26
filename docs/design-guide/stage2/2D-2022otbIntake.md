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

# 2D: 2022 Over-the-Bumper Intake

<span class="left">[< 2C: Deadaxle Pivot](2C-deadaxlePivot.md)</span> <span class="right">[2E: 2023 Pasta Roller Intake >](2E-2023pastaRollerIntake.md)</span>
<br>

## Over-the-Bumper Intakes
A common style of intake for gamepieces in FRC (depending on extension rules) is an "over-the-bumper" intake (OTB for short). These bring the gamepiece from the floor against and then over the bumper into another subsystem. They were used commonly in 2019, 2020, 2022, 2023, and 2024, and other past games. 

The two types of OTB intakes are "slapdown" which consists of a single set of arms with rollers which slap down and back up again, and four-bar linkages, which allow the intake to stow more horizontally instead of vertically. Four-bar linkages are gone over in [stage 2F](2F-fourbarLinkage.md). The intake designed in this stage will be a slapdown intake for 2022.
<br>
<figure><img align="left"  src="/img/cad-examples/intake/slapdown/4414style.webp" width="50%"><img align="right" src="/img/cad-examples/intake/4bar/1678.webp" width="40%"></figure>
<br>

[This video](https://www.youtube.com/watch?v=pSQX5c7G8yg) is a great example of a slapdown intake in 2022, on Madtown 1323's robot.

Other mechanism examples and deep dives for OTB intakes can be found on the [slapdown intakes page](../../mechanism-examples/intake/slapdown/index.md) and [4-bar intakes page](../../mechanism-examples/intake/4bar/index.md). The mechanism fundamentals page is yet to be made.

## Project
Reference [**this document**](https://cad.onshape.com/documents/17302d787e092ce11015f7ee/w/f7cf5c02c7655f0328a3a74a/e/f1456325e0175c4c081008c2?renderMode=0&uiState=6652c72b09aa2845d67f627f) to copy the 2022 OTB intake in it in your own document. 

<center><img src="/img/design-guide/stage2d/intakeTopLevel.webp" width="70%"></center>

This OTB intake has 3 total rollers, but only 2 of them are on the pivoting arm portion. The final one inside the frame perimeter is going to be on a separate plate. This can keep the pivot for the intake arms lower.

Steps are provided below for convenience.

### Master Sketch

   1. Sketch the side of your drivetrain and bumper profile
   2. Sketch the path of the ball over the bumper
   3. Sketch roller or wheel positions needed to get the game piece to move that way. The distance between rollers should be adjusted using the [WCP Belt Calculator](https://wcproducts.com/pages/calculator-belt). "Extra center" should be set as -0.02 for ease of assembly and efficiency.
   4.  Use a sketch circular pattern to represent the stowed position of your intake rollers and define where you want the pivot to be

<center><img src="/img/design-guide/stage2d/masterSketch.webp" width="70%"></center>

### Part Studio

1. CAD the front of your reference drivetrain or derive the tubes and modules from the another swerve drivebase you designed (e.g. from 2A). Make these a composite part. This is only for referencing.
2. CAD the superstructure tube (mirror and add the mirror to the drivetrain composite for referencing). Use the assembly mirror featurescript to add mate connectors to the tube for easy assembly.
3. Derive and transform the nut strips for referencing
4. Design the plates based off of your master sketch
5. Create the shafts using the shaft featurescript
6. Create the intake arm and spacer to attach a sprocket to it
7. Create two mate connectors on the pivot point in the master sketch, one owned by the main plate and one owned by the intake arm plate. This is for creating motion in the top level assembly.
8. Use your chosen belt/chain generator featurescripts to create the belts and chain
9. Name and give materials and appearances to all your parts

<center><img src="/img/design-guide/stage2d/intakePartStudio.webp" width="70%"></center>

### Assembly
Because this subsystem contains a static part and a moving part, we want to separate them into rigid (no movement) assemblies, then combine them at the top level. This makes load times significantly less.

Create an assembly for the static parts, insert the parts from the part studio with the green checkmark, and group them together. Fasten the assembly to the origin by right clicking one of the parts and clicking "Add mate connector to instance origin" and fastening that mate connector to the origin of the assembly. Add the rest of the parts from the part studio, MKCAD, and standard content that don't move with the intake arms.

<center><img src="/img/design-guide/stage2d/staticAssembly.webp" width="70%"></center>

Create an assembly for the intake arms and do the same thing as above to complete the assembly and make it rigid.

<center><img src="/img/design-guide/stage2d/intakeArms.webp" width="70%"></center>

Now create a top level assembly and insert the static assembly (fasten to the origin) and intake arm assembly. Create a revolute mate between the mates you created in the part studio earlier and add a limit to it. This completes the slapdown intake assembly.

<center><img src="/img/design-guide/stage2d/intakeTopLevel.webp" width="70%"></center>

<br>
<center>2D: OTB Intake</center> 
<span class="left">[< 2C: Deadaxle Pivot](2C-deadaxlePivot.md)</span> <span class="right">[2E: 2023 Pasta Roller Intake >](2E-2023pastaRollerIntake.md)</span>
<br>
<br>