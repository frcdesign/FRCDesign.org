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
* {box-sizing:border-box}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Hide the images by default */
.mySlides {
  display: none;
}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.6);
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 0.25s;
}

@keyframes fade {
  from {opacity: .4}
  to {opacity: 1}
}
</style>

# 1B: Design Methodology

<span class="left">[< 1A: Onshape Fundamentals](1A-onshapeFundamentals.md)</span> <span class="right">[1C: Gearbox Projects >](1C-gearboxes.md)</span>
<br>

## Project Overview

So far, you've worked on modeling FRC components in isolation. In Stage 1B, you'll dive right into robot design. In this project, you will be designing a swerve drivebase using COTS swerve modules. You will be introduced to a design workflow that will be applied to all future projects. Even if you've already CADed a drivetrain the past, this guide serves as an excellent introduction to the **top-down master sketch** design methodology.

To begin, you'll be modeling a swerve drivebase. Then, you'll create a top level robot assembly and insert a pre modeled mechanism (1678's 2023 scoring mechanism).

<center><img src="\img\design-guide\stage1b\FullAssy.png" style="width:100%"></center>
<center>*Final robot assembly.*</center>


As with previous exercises, the finished project is available for reference [here](https://cad.onshape.com/documents/6c6044229091a87cf359270b/w/ed9648f0c04c639a2561615a/e/67a7ed0c6038787281325a51). If you need help, please feel free to ask on the Discord!

## Master Sketch Methodology
When designing a model in CAD, there are two high level strategies that can be employed: top-down and bottom-up. Top-down design employs high level, low detail sketches to dictate the design, and then refining details and components within that framework. Conversely, bottom-up design involves creating individual components or parts separately and then assembling them to form the final product. 

Top-down design offers a holistic approach, allowing for better system integration, consistency, and is more parametric. Bottom-up design offers flexibility and independence in designing individual parts. In FRC robot design, top-down approach is favored as system integration is often the most challenging aspect. Top-down ensures that the robot architecture dictates part design.

To achieve this, a ***master sketch*** is utilized. A master sketch is a series of sketches that capture the major dimensions of each mechanism, field element interactions, and robot size constraints. Then, the master sketch(es) are inserted into each mechanism's part studio and the individual components are then modeled around the imported layout sketch. More information on master sketches can be found on the [Master Sketch Best Practices](/best-practices/mastersketch-setup/) page.

<center><img src="\img\design-guide\stage1b\exampleMasterSketch.webp" style="width:60%"></center>
<center>*Example of robot master sketches. Each mechanism has a number of layout sketches that capture the important details.*</center>

## Swerve Drivebase
A drivebase is the mobile platform on which all our other mechanisms are designed around and attached to. With the advent of COTS swerve, designing a swerve drivebase has been made significantly easier and has become the most commonly used competitive drivetrain in FRC. 

A swerve drivebase is composed of four *swerve modules*. Each module has 2 motors: 1 for spinning the wheel and one for steering it. This enables the robot to translate in any direction independent of the rotation of the robot. There are many other COTS options available, each with their own advantages and tradeoffs. In this project, we'll be using [SDS MK4i modules](https://www.swervedrivespecialties.com/products/mk4i-swerve-module). You can learn more about drivetrains on the [Design Fundamentals](/design-fundamentals/mechanisms/drivebase/) page.

<center><img src="\img\design-guide\stage1b\SwerveBase\DriveAssy.png" style="width:100%"></center>
<center>*Stage 1B swerve drivebase project.*</center>

As was introduced in Stage 1A, robot structures are typically constructed out of aluminum box tubing. The drivebase is no exception to this. Most teams will opt to design their box tubing with a standard 0.5" spacing pattern of 0.196" diameter holes. This enables modularity and allows for easy integration of many COTS components like gussets.

Box tubing extrusions can be purchased at most metal suppliers, but many FRC vendors including [WCP](https://wcproducts.com/collections/systems-structure/products/punched-tubing), [TTB](https://www.thethriftybot.com/products/thrifty-box-extrusion), [REV](https://www.revrobotics.com/MAXTube/) sell box tubing with pre-cut hole patterns which can significantly reduce manufacturing time and equipment requirements.

### Drivetrain Master Sketches
To begin, you will be creating a layout sketch of the drivetrain. This will dictate the size and position of the drive tubes. The layout will be drawn from the side and top view of the drivetrain. For your swerve drivebase, you will make it 26"x26".

Start by creating a part studio called `Master Sketch`. Then, use the `Origin Cube` Featurescript to create an origin cube. **You should start every part studio with an origin cube to set a reference for the origin of the robot.** The origin of the robot is typically defined as the center of the drivebase on ground level. You can learn more about origins and the origin cube in [Assembly Best Practices](/best-practices/assembly-setup#origin-cube-method).


<center>**Drivetrain Layout Sketch Slides**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtFinalLayout.webp" style="width:100%">
      <figcaption>0. The final layout sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/originCube.webp" style="width:100%">
      <figcaption>1. Start by inserting the origin cube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtSideLayout1.webp" style="width:100%">
      <figcaption>2. Draw the side profile of the drivetrain on the Right Plane. We place the tube 1.75" from the ground, which is the offset from the ground to the bottom of the tube for the MK4i modules.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtSideLayout2.webp" style="width:100%">
      <figcaption>3. Draw the wheel clearance box, which represents the area that the wheel takes up. For the MK4i modules, the box is 4.625" wide. The side layout of the drivebase is now finished.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtTopLayout1.gif" style="width:100%">
      <figcaption>4. Create the top layout sketch by using the bottom mate connector on the vertical line of the side layout. Utilizing auto-generated mate connectors for sketch planes is a very useful tool to have. Press the “Top” button on the view cube to get a top view.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtTopLayout2.gif" style="width:100%">
      <figcaption>5. Sketch the top outline of the drive base. Make the rectangle a square and set the side length equal to the length of the side layout tube. This ensures that the size of the top layout always matches the side layout, which makes the design parametric. Notice that the sketch is fully defined despite having no sketch dimensions.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtTopLayout3.webp" style="width:100%">
      <figcaption>6. To sketch the tubes, draw a square 1" smaller than the previous square. This will represent the four 2"x1" tubes that make up the outer frame. Then, draw the top profile of the 2"x2" tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtTopLayout4.webp" style="width:100%">
      <figcaption>7. Next, we need to make the cutouts on the drivetube for the swerve modules. Start by drawing two lines, each offset by 4.25" from the edge. This is the required offset for MK4i modules. Other modules will differ.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtTopLayout5.gif" style="width:100%">
      <figcaption>8. To apply the cutout for all four tubes, we use the <code>Circular Pattern</code> sketch tool to copy the lines to all four corners. For a  <code>Circular Pattern</code> we first define the number of instances and then the axis of rotation.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtFinalLayout.webp" style="width:100%">
      <figcaption>9. Finally, name your sketches and organize them into folders in the feature tree. Your sketches should all be fully defined.</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1,0)" style="background-color: #000; color: #fff;">&#10094;</a>
  <a class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</a>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

As previously explained, this method of top-down modeling is extremely powerful as it enables you to capture the most important dimensions all in one place. However, you should be careful to not over-detail master sketches. More information on master sketches can be found on the [Master Sketch Best Practices](/best-practices/mastersketch-setup/) page.

In this part, you were also introduced to the `Derived` feature. This feature is extremely powerful and can be used to import parts from one part studio into another to enable a references for modeling. However, you must be careful to not overuse this function as it can significantly slow down your part studios.

### Deriving Layout Sketches and Part Modeling

Now that you have created the layout sketch, you can begin modeling the individual parts. The critical dimensions of the parts, such as the length of the tubes, will be driven by the layout sketch. This way, the tubes will automatically update with any changes in the size of the drivebase in the layout sketch.

Start by creating a new folder tab called `Drivetrain`. Then, create a new part studio called `Drivetrain` within the folder.

<center>**Drivetrain Part Modeling**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts0.webp" style="width:100%">
      <figcaption>0. The part studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts1.webp" style="width:100%">
      <figcaption>1. Start by inserting the origin cube. Then, use the <code>Derived</code> tool to insert the layout sketches you previously drew from the Master Sketch part studio. This feature will automatically update if changes are made to the layout sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts2.webp" style="width:100%">
      <figcaption>2. Use the <code>Extrude Individual</code> and <code>Tube Converter</code> Featurescripts to model the tubes. The 2"x1" tubes should be 1/8" wall for strength, while the 2"x2" tube can be 1/16" wall.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts3.webp" style="width:100%">
      <figcaption>3. Start with one corner of the bellypan. The corner is cut out to create room for the swerve module. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts4.gif" style="width:100%">
      <figcaption>4. Use the <code>Fillet</code> sketch tool to add a 1" radius sketch fillet on the two internal corners of the cutout. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts5.gif" style="width:100%">
      <figcaption>5. Next, use the <code>Circular Pattern </code> sketch tool to pattern the other three corners. Extrude the bellypan to be 1/8" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts6.webp" style="width:100%">
      <figcaption>6. Use the <code> Fillet All Edges</code> Featurescript to add a 0.25" radius fillet to the remaining edges on the bellypan by selecting the bottom face of the bellypan.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts7.webp" style="width:100%">
      <figcaption>7. Add the seed instances of the holes for the bellypan.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts8.gif" style="width:100%">
      <figcaption>8. Next, use the <code>Linear Pattern</code> sketch tool to pattern the holes along the edge.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts9.gif" style="width:100%">
      <figcaption>9. Use the <code>Circular Pattern</code> sketch tool to pattern the holes about the origin onto all four edges.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts10.gif" style="width:100%">
      <figcaption>10. Use the <code>Linear Pattern</code> sketch tool to pattern the holes for the 2"x2" tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts11.webp" style="width:100%">
      <figcaption>11. Clean up the sketch by moving the dimensions so that they are all visible. A clean sketch is important for readability of the CAD so that it is easily editable in the future.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtParts0.webp" style="width:100%">
      <figcaption>12. Finally, name your sketches and organize them into a folder in the feature tree. Additionally, set the material of the bellypan to Aluminum 6061 and name your parts.</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1,1)" style="background-color: #000; color: #fff;">&#10094;</a>
  <a class="next" onclick="plusSlides(1,1)" style="background-color: #000; color: #fff;">&#10095;</a>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

At this point, you should be feeling more and more comfortable with Onshape modeling and using Featurescripts. Always make sure to clean up your feature tree while working to keep it organized and easy to use. You can learn about feature tree organization on the [Feature Tree Best Practices](/best-practices/feature-tree-setup/) page.


### Assembly

Now that the part studio is finished, you can create the drivetrain assembly. Create a new assembly tab called `Drivetrain Assembly` in the `Drivetrain` folder you made previously. 

Previously, in Stage 1A when you created assemblies one of the parts in the group mate was fixed in place. However, this is not considered a good practice as it is not parametric. This is where the origin cube comes in: the origin cube has a mate connector placed at the origin of the part studio. After inserting and grouping all of the parts, you can fasten the origin cube to the origin of the assembly. This aligns the part studio origin and assembly origin.

<center>**Drivetrain Assembly**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtAssy0.webp" style="width:100%">
      <figcaption>0. The assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtAssy1.gif" style="width:100%">
      <figcaption>1. Insert the parts into the assembly, <code>Group</code> them, then fasten the origin cube to the origin of the assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/design-guide/stage1b/SwerveBase/dtAssy2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Insert the MK4i module from the MKCad app into the assembly and mate it into place. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtAssy3.gif" style="width:100%">
      <figcaption>3. Use the <code>Circular Pattern</code> assembly tool to finish assembling the modules. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/design-guide/stage1b/SwerveBase/dtAssy4.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Insert a 3/16" rivet from the MKCad app into the assembly and mate it. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtAssy5.gif" style="width:100%">
      <figcaption>5. Use the <code>Replicate </code> assembly tool to replicate the rivet and rivet mate onto all matching geometry on the bottom face of the bellypan</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtAssy0.webp" style="width:100%">
      <figcaption>6. The assembly.</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1,2)" style="background-color: #000; color: #fff;">&#10094;</a>
  <a class="next" onclick="plusSlides(1,2)" style="background-color: #000; color: #fff;">&#10095;</a>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

The `Replicate` tool, which was introduced in Stage 1B exercise 5, is a very powerful tool for duplicating parts in assemblies. `Replicate` works by creating a copy of the selected parts, and duplicates the selected mate onto the selected geometry. Note that the selected geometry must exactly match the origin mate geometry, eg: the hole diameter must be the same for replicate to copy a rivet. In your assembly, you use the select the face for replicate to apply to. What this does is identify all geometry that matches the original mate and then copy the selected components and mate to those matching locations on the selected face. If you want to replicate onto only specific holes, you can change the drop-down menu to "Match Individual Edges".

<details>
<summary>Match Individual Edges for Replicate</summary>
<center>
  <video width="1920" controls>
    <source src="/img/design-guide/stage1b/replicateExample.mp4" type="video/mp4">
  </video>
</center>
<center> Using "Match Individual Edges" allows us to select specific holes to replicate to instead of every hole on the face of the gusset. </center>
</details>

#### Adding More Components

When you model more parts in the part studio, you can insert them into the assembly in a similar to fashion to before. Hit insert and immediately click on the green checkmark. Then, edit the initial `Group` you made and add the part to the group. By doing this, you ensure that added parts will always stay in the same place it was modeled in the part studio.

Let's add a gusset to connect the 2"x2" tube to the 2"x1" tube.

<center>**Adding a Gusset**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtAdd0.webp" style="width:100%">
      <figcaption>0. Finished drivetrain assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtAdd1.webp" style="width:100%">
      <figcaption>1. Add the gusset for the crosstube with the <code>Gusset</code> Featurescript.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtAdd2.gif" style="width:100%">
      <figcaption>2. Insert the gusset into the assembly and add it to the <code>Group</code>.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtAdd3.webp" style="width:100%">
      <figcaption>3. Copy the gusset and mate it to the other side. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtAdd4.gif" style="width:100%">
      <figcaption>4. Edit the replicate feature to add rivets to the gusset. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/SwerveBase/dtAdd0.webp" style="width:100%">
      <figcaption>4. Finished drivetrain assembly.</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1,3)" style="background-color: #000; color: #fff;">&#10094;</a>
  <a class="next" onclick="plusSlides(1,3)" style="background-color: #000; color: #fff;">&#10095;</a>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>


Make sure you sort the instances in your assembly into folders (i.e. frame, swerve modules) and name any patterns and replicates used. This will help you locate components in the assembly later down the line.

More details about best practices for Onshape assemblies are included on the [Assembly Best Practices Page](/best-practices/assembly-setup/).

It should be noted that while modeling every detail of the robot hardware (bolts, rivets, nuts) is beneficial for purchasing and real life assembly purposes, it isn't strictly necessary. Time is a precious resource, especially during build season, so you should spend it on what will give you the biggest return.

## Top Level Robot Assembly
Now that you have a drivebase, you can create a *top level robot assembly*. The top level robot assembly is the highest in the [assembly hierarchy](/best-practices/document-setup/). Organizing the assemblies in this way keeps thing organized from both a CAD assembly and real life assembly standpoint. 

Create an assembly tab above the `Master Sketch` part studio and name it `Top Level Robot Assembly`. Here, you will bring in the drivebase and the scoring mechanism from [1678's 2023 robot](https://www.thebluealliance.com/team/1678/2023).

Copy [this link](https://cad.onshape.com/documents/28a750426de8e2bc17d5b900/w/8e79c6217ae2ce07ff57d900/e/a4d266d03289620078d13a80) to access the scoring mechanism.

<center>**Top Level Robot Assembly**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/TopLevel/topL0.webp" style="width:100%">
      <figcaption>0. Finished top level robot assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/design-guide/stage1b/TopLevel/topL1.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>1. Insert the drivetrain assembly and fasten the origin cube to the assembly origin. You may need to unhide the origin cube to mate it.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/design-guide/stage1b/TopLevel/topL2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Insert the 1678 2023 scoring assembly by pasting the scoring mechanism link into the `Insert` menu textbox. Then, fasten its origin cube to the assembly origin. You may need to hide the drivetrain's origin cube to access the origin of the assembly for mating.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/TopLevel/topL0.webp" style="width:100%">
      <figcaption>3. Finished top level assembly. </figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1,4)" style="background-color: #000; color: #fff;">&#10094;</a>
  <a class="next" onclick="plusSlides(1,4)" style="background-color: #000; color: #fff;">&#10095;</a>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

And that's all there is to the top level robot assembly! The use of the origin cube makes it very easy to mate together. In later stages you will explore how to create flexible assemblies (arms, elevators, etc) with the origin cube. If you are interested, you can get a sneak peek [here](/best-practices/assembly-setup/#utilizing-origin-cube-for-flexible-assemblies).

Congratulations on completing Stage 1B! Remember, practice is essential – the more CAD models you create, the more proficient and efficient you'll become. Using keyboard shortcuts can significantly accelerate your CAD workflow. Be attentive to best practices to avoid developing any bad habits. Keep up the good work!

At this point, you've learned and had some practice on modeling individual components and creating a top-down design. Starting in Stage 1C, we'll introduce some mechanical design topics including power transmission. This is the final step before being able to design a full mechanism!

<br>
<center>1B: Design Methodology</center> 
<span class="left">[< 1A: Onshape Fundamentals](1A-onshapeFundamentals.md)</span> <span class="right">[1C: Gearbox Projects >](1C-gearboxes.md)</span>
<br>
<br>

<!-- ------------------DO NOT TOUCH ANYTHING BELOW HERE------------------ -->

<script>
// Initialize slide index for each slideshow
let slideIndices = [];

let slideshows = document.getElementsByClassName("slideshow-container");
  for (let no = 0; no < slideshows.length; no++) {
    slideIndices[no] = 1;
    let dotsContainer = slideshows[no].getElementsByClassName("dotsContainer")[0];
    let slides = slideshows[no].getElementsByClassName("mySlides");
    for (let i = 0; i < slides.length; i++) {
      let dot = document.createElement("span");
      dot.className = "dot";
      dot.onclick = function() { currentSlide(i+1, no); };
      dotsContainer.appendChild(dot);
    }
    showSlides(1, no);
  }

// Next/previous controls
function plusSlides(n, no) {
  showSlides(slideIndices[no] += n, no);
}

// Thumbnail image controls
function currentSlide(n, no) {
  showSlides(slideIndices[no] = n, no);
}

function showSlides(n, no) {
  let i;
  let x = document.getElementsByClassName("slideshow-container")[no].getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("slideshow-container")[no].getElementsByClassName("dot");
  if (n > x.length) {slideIndices[no] = 1}    
  if (n < 1) {slideIndices[no] = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  x[slideIndices[no]-1].style.display = "block";  
  dots[slideIndices[no]-1].className += " active";
}

</script>