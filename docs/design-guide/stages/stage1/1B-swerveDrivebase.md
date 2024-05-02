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

# 1B: Swerve Drivebase Project

<span class="left">[< 1A: Sketching & Part Design](1A-onshapeFundamentals.md)</span> <span class="right">[1C: Gearbox Projects >](1C-gearboxes.md)</span>
<br>

For your first project, we’ll be making a swerve drivebase using COTS parts. It is important to learn how to design a swerve drivebase since it is now the most commonly used competitive drivetrain in FRC, and everything you design goes on top of it. In this project we will go step-by-step as we introduce new concepts. 

This guide is still useful to go through even if you already know how to make one with self-taught skills, as it will introduce both a good top-down design workflow that will be iterated upon for all future projects and many concepts that aren't common outside of FRC (such as using featurescripts to speed up the workflow).

## Project Overview

A swerve drivebase is composed of four "swerve modules". Each module has a 2 motors, 1 for powering the wheel and one for steering it. This allows it to move in any direction independent of rotation (strafe). In this project, we'll be using [SDS MK4i modules](https://www.swervedrivespecialties.com/products/mk4i-swerve-module), but there are other options depending on packaging limitations.

<center><img src="\img\design-guide\stage1b\Assembly_1.webp"></center>

!!! Note
    The use of unsimplified models is deliberate; we will use simplified models starting in stage 2B.


Notice how the structure is made out of aluminum box tubing. You’ll find that this is the most common “structural” part. You can think of this like the wooden beams for a house. It is most commonly found in 2 inch by 1 inch, 1 inch by 1 inch, and 2 inch by 2 inch sizes. It is also found in 1/8 inch and 1/16 inch thicknesses. 

For the rest of the tutorial, box tubing will be referred to by their shorthand name (based on their size), such as 2x1, 1x1, and 2x2.

!!! Note
    You can buy the simple extrusions at most metal suppliers, but [WCP](https://wcproducts.com/collections/systems-structure/products/punched-tubing), [TTB](https://www.thethriftybot.com/products/thrifty-box-extrusion), and [REV](https://www.revrobotics.com/MAXTube/) all sell box tubing with hole patterns for easier design and assembly.


## Part Studio

### Side Layout Sketch

To start, we will be making a sketch on the right plane. This will be representing the right side of our robot and help us determine the length of the drive train. Name the sketch “Robot Layout".

<center><img src="\img\design-guide\stage1b\1a-Swerve 1.webp"></center>

Make a center point rectangle and do a vertical constraint on the center point of the rectangle to the origin point (the black and white circle). Make the rectangle 2 inches high. This rectangle represents the box tube that you saw above. Then dimension the rectangle 1.75 inches above the origin. 

Now we have a drivetrain side of unknown length, that is 2 inches wide and 1.75 inches above the ground

<center><img src="\img\design-guide\stage1b\1a-Swerve 2.webp"></center>

Let’s define the length of the drivetrain. We can do this by dimensioning the rectangle to a set size, we’ll do 26.

<center><img src="\img\design-guide\stage1b\1a-Swerve 3.webp"></center>

This means that our drivebase is 26 inches long.

To make things a bit easier, let’s also draw our wheels. Make a 3 inch rectangle that is constrained horizontally to the origin (the wheel raises the drivetrain by 1.75 inches). We can then mirror the wheel to the other side by make a mirror line by drawing a line in the center and using the sketch mirror tool.

<center><img src="\img\design-guide\stage1b\1a-Swerve 4.webp"></center>

Now, let’s make the whole thing construction (drag-select all the geometry created and press ```q```). We’ll be using this as a reference to define the length and width of the square drivetrain. If we need to change the chassis dimensions, we can go back to “Robot Layout” and change it.

<center><img src="\img\design-guide\stage1b\1a-Swerve 5.webp"></center>

Now confirm the sketch by hitting the green checkmark in the sketch dialogue box.


### Modeling the Box Tubes

Now we’ll be modeling the drivetrain tubes using a top layout sketch. We’ll be ending with something that looks like this:

<center><img src="\img\design-guide\stage1b\Tubes.webp"></center>

!!! Note
    Notice how all the tubes of the drivetrain are designed in a single part studio.

The top layout sketch should be made at the bottom of where we want the tubes to be instead of at the ground. Instead of using a plane, we can create the sketch directly on a point on the side layout sketch, so the bottom of the tubes is driven by the side layout sketch without an extra plane.

Open the sketch dialogue to create a new sketch and click the circle symbol (select mate connector) next to the "sketch plane" selection box. Select a point on the bottom of the tube in the side layout sketch and a sketch will be created there. 

<center><img src="\img\design-guide\stage1b\mate_connector_sketch.webp"></center>

!!! Tip
    If the sketch is facing the wrong way, try selecting the point again and make sure the colored axis are pointing the right direction (blue up).

Press the “Top” button on the view cube to get a top view (or press ```n``` to rotate normal to the sketch plane). The next steps include sketching out the “top” of the drivetrain tubes. 

Start a center point rectangle on the origin, hover over the point at the top of the dotted line (making a horizontal constraint between it and the top of the rectangle), then moving the side out and clicking to finish the rectangle. 

<center><img src="\img\design-guide\stage1b\horiConstraint.webp"></center>

If you remember previously, that point was the edge of your drivetrain which you in the side layout sketch. See how the left side of the rectangle is already 26 inches? We want to make this a square, so let’s use the equal constraint (e key) between the top of the square and the left side of the square. This should make both sides equal to each other, and the whole sketch should be black.

<center><img src="\img\design-guide\stage1b\definedSketch.webp"></center>

Use the offset tool and offset the square inwards by 1 inch; this will define the side of your drive rails.

<center><img src="\img\design-guide\stage1b\offset.webp"></center>

Taking a look at the swerve drivetrain again, we can see there’s a cutout in each of the corners. We should define this in our sketch. From the edge of the corner, the gap is 4.25 inches long. 

<center><img src="\img\design-guide\stage1b\1a-Swerve 11.webp"></center>

Draw two lines, one horizontally constrained and one vertically constrained, and dimension them 4.25in away from the corner as shown.

<center><img src="\img\design-guide\stage1b\cornerCutout.webp"></center>

To apply this to all corners, circular pattern the two lines you created, changing the number of instances to four. It should look like this:

<center><img src="\img\design-guide\stage1b\1a-Swerve 13.webp"></center>

Confirming the sketch should show the chassis as shown, with some blue lines. Why is that? 

If you click on one of the points on the blue unconstrained lines, you can drag them around. This also reveals the center of rotation of the circular pattern (the blue dot).

<center><img src="\img\design-guide\stage1b\1a-Swerve 15.webp"></center>

Constrain the center of rotation to the origin by dragging it to the origin. Your sketch should look like this:

<center><img src="\img\design-guide\stage1b\1a-Swerve 16.webp"></center>

If we take the top view of a drivetrain, you can see how it looks similar. Removing the modules also shows the gaps we modeled.

<center>![Untitled](\img\design-guide\stage1b\1a-Swerve 17.webp){width=45% height=45%} ![Untitled](\img\design-guide\stage1b\1a-Swerve 18.webp){width=45% height=45%}</center>

Let’s now sketch out the middle cross beam. We’ll make this out of 2x2 aluminum since 2x2 is stronger than 2x1. Let’s make it 2 inches wide, and 2 inches away from the center (origin).

<center><img src="\img\design-guide\stage1b\1a-Swerve 19.webp"></center>

Rename the sketch to “Drivetrain Top” and confirm it with the green checkmark.

Now, lets create the tubes. Click the extrude individual featurescript. 

!!! Tip
    The "extrude individual" featurescript allows us to make multiple parts, one per sketch region, with a single extrude feature.

<center><img src="\img\design-guide\stage1b\1a-Swerve 20.webp"></center>

Click the top faces of the sketch and extrude them 2 inches up to make the tubes.

<center><img src="\img\design-guide\stage1b\1a-Swerve 21.webp"></center>

Now, use the "tube converter" featurescript and click on the four outer tubes.

!!! Tip
    The "tube converter" featurescript converts box tube-shaped extrudes into COTS box tube with a hole pattern. 

<center><img src="\img\design-guide\stage1b\1a-Swerve 22.webp"></center>

Set the thickness to 0.125in, as 0.125in thickness is “thick wall” tubing. 0.125in wall thickness tubes are strong and allow for a strong and rigid frame that is resistant to collisions. Set the 2 inch face style to “1 inch between holes”, and click the checkbox for center row. Confirm the tube converter feature. 

!!! Note
    As mentioned earlier, you can find this type of box tubing from various COTS vendors, which sell the pre-punched tubing for your convenience.

<details>
<summary>WCD Box Tubes</summary>
<center><img src="\img\design-guide\stage1b\1a-Swerve 23.webp"><figcaption>(Source: West Coast Products)</figcaption></center>
</details>



Let’s do another tube converter for the 2x2 tube, but change the thickness to 1/16in. The reason for this is because 1/16in 2x2 is plenty strong, and allows for weight savings down the line.

Once you are done, change the appearance of all of your tubes to a color of your choosing. I’ll be using dark gray. You can do this by going to the parts menu and clicking all 5 parts, then right clicking and selecting “edit appearance for 5 parts”.

<center><img src="\img\design-guide\stage1b\1a-Swerve 24.webp"></center>

<center><img src="\img\design-guide\stage1b\Tubes.webp"></center>

## Assembly

Now that we have the frame tubes, we need to insert them into the "assembly". You use part studios to design parts in reference to each other, and assemblies to define the position and motion of those parts and assemble the final product. Certain practices in the part studio can make assembly easier and faster; these are some of the best practices that are used in the guided projects and in the [best practices](../../../design-standards/index.md) section of the website.

### Origin Mate Connector
Something to note is that both assemblies and part studios have an origin. We will need to make sure that our parts are in the same place in both the origin and part studio. We can do this through an origin mate connector.

!!! Tip
    Make sure to show the origin in the feature list if it was hidden by hovering over the origin in the list and clicking the eye symbol.

Select the mate connector button on the top. 

<center><img src="\img\design-guide\stage1b\Mate-Connector.webp"></center>

Select the origin entity as the origin, then the owner entity as the 2x2 tube. The 2x2 tube will now have an mate connector at the origin.

<details>
<summary>Video Tutorial</summary>
  <center><iframe width="880" height="550" src="https://www.youtube.com/embed/4jTYh0Rn5cU" frameborder="0" allowfullscreen></iframe></center>
</details>


### Assembling
Now that you have finished your part studio, you can follow this video tutorial to do the rest of the assembly. Assemblies require a bit more explaining, which is why it's in video as opposed to text. 

<center><iframe width="880" height="550" src="https://www.youtube.com/embed/9cMRIJJGGeE" frameborder="0" allowfullscreen></iframe></center>

Make sure you sort the instances in your assembly into folders (i.e. tubes, swerve modules).

## Conclusion
You've completed a basic swerve drivebase, going over many concepts in the process. The CAD concepts include sketching parametrically, creating a sketch on a mate connector, using featurescripts, and the fast assembly workflow. The FRC concepts include box tube and swerve modules.

The most important concept is how you can start with a layout sketch or two and build the entire rest of the part studio on top of those, meaning the part studio and assembly could change if you only changed the dimensions in the side layout sketch. This is what a top-down workflow is, and it allows you to create an outline first and slowly go into more detail, referencing the outline as you go.

<center><img src="\img\design-guide\stage1b\Assembly_1.webp"></center>

Try changing the dimensions in the side layout sketch and seeing what happens to the part studio and assembly.

Next, you'll learn how to sketch and assemble power transmission components in a few gearboxes.

<br>
<center>1B: Drivebase</center> 
<span class="left">[< 1A: Sketching & Part Design](1A-onshapeFundamentals.md)</span> <span class="right">[1C: Gearbox Projects >](1C-gearboxes.md)</span>
<br>
<br>