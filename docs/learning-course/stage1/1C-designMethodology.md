<style>
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
#slide1 {display:block}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 250px;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 3px 3px 3px 3px;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
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

# 1C: Design Methodology

## Introduction

So far, you've worked on CAD fundamentals through courses and FRC-relevant exercises, but haven't done anything within a larger context. In Stage 1C, you'll dive right into designing for a real robot. In this project, you will be designing a swerve drivebase while being introduced to a design workflow that will be applied to all future projects. 

1. Learn the basics of top-down design and mastersketching
2. Model a swerve drivebase using COTS swerve modules
3. Create a top-level assembly and insert a pre-modeled mechanism (1678's 2023 elevator and manipulator) 

Even if you've already CADed a drivetrain the past, this guide serves as an excellent introduction to the **top-down master sketch** design methodology.

<center><img src="\img\learning-course\stage1c\FullAssy.webp" style="width:100%"></center>
<center>*Swerve drivebase with pre-modeled mechanism*</center>


As with previous exercises, the finished project is available for reference. If you need help, please feel free to ask on the Discord!

<center>[1C Drivebase Reference](https://cad.onshape.com/documents/6c6044229091a87cf359270b/w/ed9648f0c04c639a2561615a/e/67a7ed0c6038787281325a51 "1C Drivebase Reference Onshape Document"){:target="_blank" .md-button .md-button--primary }</center>

## Master Sketch Methodology
When designing a model in CAD, there are two high level strategies that can be employed: top-down and bottom-up. Top-down design employs high level, low detail sketches to dictate the design, and then refining details and components within that framework. Conversely, bottom-up design involves creating individual components or parts separately and then assembling them to form the final product. 

Top-down design offers a holistic approach, allowing for better system integration, consistency, and is more parametric. Bottom-up design offers flexibility and independence in designing individual parts. In FRC robot design, top-down approach is favored as system integration is often the most challenging aspect. Top-down ensures that the robot architecture dictates part design.

To achieve this, a ***master sketch*** is utilized. A master sketch is a series of sketches that capture the major dimensions of each mechanism, field element interactions, and robot size constraints. Then, the master sketch(es) are inserted into each mechanism's part studio and the individual components are then modeled around the imported layout sketch. More information on master sketches can be found on the [Master Sketch Best Practices](/best-practices/mastersketch-setup/ "Master Sketch Best Practices Page"){:target="_blank"} page.

???+ Example "Example Master Layout Sketch"
    <center><img src="\img\learning-course\stage1c\exampleMasterSketch.webp" style="width:60%"></center>
    <center>*Example of robot master sketches. Each mechanism has a number of layout sketches that capture the important details.*</center>


### Origin Placement and Origin Cube
To fully utilize master sketch top-down design, we must choose a unified origin for all part studios. Utilizing the same origin as the master sketch across all part studios and assemblies is twofold:

1. The origin will always be a consistent central point you can reference. This helps keep things parametric too.
2. To unify the robot CAD and robot software origin point. By having the same origin in CAD and code, the robot can be seamlessly exported to [AdvantageScope](https://github.com/Mechanical-Advantage/AdvantageScope "AdvantageScope Repository"){:target="_blank"} and camera transformations more easily measured. 

!!! Note
    Although definitions may vary from team to team, the origin of an FRC robot is typically defined as ***the center of the drivebase, on floor level***.

To achieve this, we use the [`Origin Cube` Featurescript](https://cad.onshape.com/documents/321c197a842fc5f1a29e6621/w/fc3cdd5ca7edcd93e02f13cc/e/df3afdbec8d1356c2af15e4b?renderMode=0&uiState=6637caa6ccbcaa36badca03a "Origin Cube Featurescript Document"){:target="_blank"} which generates a transparent 2" cube at the origin and provides several useful constants and functions that have already been used in previous stage.

The Origin Cube will become very useful later on for assembly mating but for now all you need to remember is that **the Origin Cube should be the first feature in all part studios**. You can read more about the Origin Cube on the [assembly best practices page](../../best-practices/assembly-setup.md "Assembly Best Practices Page"){:target="_blank"}., 

## Swerve Drivebase
A drivebase is the mobile platform on which all our other mechanisms are designed around and attached to. With the advent of reliable COTS swerve, designing a swerve drivebase has been made significantly easier and has become the most commonly used competitive drivetrain in FRC. 

A swerve drivebase is composed of four *swerve modules*. Each module has two motors: one for spinning the wheel and one for steering it. This enables the robot to translate in any direction independent of the rotation of the robot. In this project, we'll be using [SDS MK4i modules](https://www.swervedrivespecialties.com/products/mk4i-swerve-module "SDS MK4i Product Page"){:target="_blank"}. There are many other COTS options available, each with their own advantages and tradeoffs. 

<!-- You can learn more about drivetrains on the [Design Handbook](/design-handbook/mechanisms/drivetrain/) page. -->

<center><img src="\img\learning-course\stage1c\SwerveBase\DriveAssy.webp" style="width:80%"></center>
<center>*Stage 1C swerve drivebase project.*</center>

As was introduced in Stage 1A, robot structures are typically constructed out of aluminum box tubing. The drivebase is no exception to this. Most teams will opt to design their box tubing with a standard 0.5" spacing pattern of 0.196" diameter holes. This enables modularity and allows for easy integration of many COTS components like gussets.

Box tubing extrusions can be purchased at most metal suppliers, but many FRC vendors including [WCP](https://wcproducts.com/collections/systems-structure/products/punched-tubing){:target="_blank"}, [TTB](https://www.thethriftybot.com/products/thrifty-box-extrusion){:target="_blank"}, and [REV](https://www.revrobotics.com/MAXTube/){:target="_blank"} sell box tubing with pre-cut hole patterns which can significantly reduce manufacturing time and equipment requirements.

### Drivetrain Master Sketches
To begin, you will be creating a layout sketch of the drivetrain. This will dictate the size and position of the drive tubes. The layout will be drawn from the side and top view of the drivetrain. For your swerve drivebase, you will make it 26"x26".

Start by **creating a new Onshape Document called `Stage 1C Robot`** and within it, **a new part studio called `Master Sketch`**. Then, use the `Origin Cube` Featurescript to create an origin cube. **Follow the instructions in the slides** to complete the master sketch.


<!-- <center>**Drivetrain Layout Sketch Slides**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtFinalLayout.webp" style="width:100%">
      <figcaption>0. The final layout sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/originCube.webp" style="width:100%">
      <figcaption>1. Start by inserting the origin cube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtSideLayout1.webp" style="width:100%">
      <figcaption>2. Draw the side profile of the drivetrain on the Right Plane. We place the tube 1.75" from the ground, which is the offset from the ground to the bottom of the tube for the MK4i modules.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtSideLayout2.webp" style="width:100%">
      <figcaption>3. Draw the wheel clearance box, which represents the area that the wheel takes up. For the MK4i modules, the box is 4.625" wide. The side layout of the drivebase is now finished.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtTopLayout1.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Create the top layout sketch by using the bottom mate connector on the vertical line of the side layout. Utilizing auto-generated mate connectors for sketch planes is a very useful tool to have. Press the “Top” button on the view cube to get a top view.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtTopLayout2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. Sketch the top outline of the drive base. Make the rectangle a square and set the side length equal to the length of the side layout tube. This ensures that the size of the top layout always matches the side layout, which makes the design parametric. Notice that the sketch is fully defined despite having no sketch dimensions.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtTopLayout3.webp" style="width:100%">
      <figcaption>6. To sketch the tubes, draw a square 1" smaller than the previous square. This will represent the four 2"x1" tubes that make up the outer frame. Then, draw the top profile of the 2"x2" tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtTopLayout4.webp" style="width:100%">
      <figcaption>7. Next, we need to make the cutouts on the drivetube for the swerve modules. Start by drawing two lines, each offset by 4.25" from the edge. This is the required offset for MK4i modules. Other modules will differ.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtTopLayout5.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>8. To apply the cutout for all four tubes, we use the <code>Circular Pattern</code> sketch tool to copy the lines to all four corners. For a  <code>Circular Pattern</code> we first define the number of instances and then the axis of rotation.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtFinalLayout.webp" style="width:100%">
      <figcaption>9. Finally, name your sketches and organize them into folders in the feature tree. Your sketches should all be fully defined.</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <button class="prev" onclick="plusSlides(-1,0)" style="background-color: #000; color: #fff;">&#10094;</button>
  <button class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</button>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

As previously explained, this method of top-down modeling is extremely powerful as it enables you to capture the most important dimensions all in one place. However, you should be careful to not over-detail master sketches. You will be practicing master sketches all throughout Stage 2, and use them in Stage 3 alongside multi-document practices to design a whole robot.

### Deriving Layout Sketches and Part Modeling

Now that you have created the layout sketch, you can begin modeling the individual parts. The critical dimensions of the parts, such as the length of the tubes, will be driven by the layout sketch. This way, the tubes will automatically update with any changes in the size of the drivebase in the layout sketch.

Start by **creating a new folder tab in your Document called `Drivetrain`**. Then, **create a new part studio called `Drivetrain`** within the `Drivetrain` folder. **Follow the instructions in the slides** to complete the part studio. Remember that the Origin Cube should be the first feature in your part studio.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtParts0.webp" style="width:100%">
      <figcaption>0. The part studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtParts1.webp" style="width:100%">
      <figcaption>1. Start by inserting the origin cube. Then, use the <code>Derived</code> tool to insert the layout sketches you previously drew from the Master Sketch part studio. This feature will automatically update if changes are made to the layout sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtParts2.webp" style="width:100%">
      <figcaption>2. Use the <code>Extrude Individual</code> and <code>Tube Converter</code> Featurescripts to model the tubes. The 2"x1" tubes should be 1/8" wall for strength, while the 2"x2" tube can be 1/16" wall.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtParts3.webp" style="width:100%">
      <figcaption>3. Start with one corner of the bellypan. The corner is cut out to create room for the swerve module. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtParts4.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Use the <code>Fillet</code> sketch tool to add a 1" radius sketch fillet on the two internal corners of the cutout. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtParts5.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. Next, use the <code>Circular Pattern </code> sketch tool to pattern the other three corners. Extrude the bellypan to be 1/8" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtParts6.webp" style="width:100%">
      <figcaption>6. Use the <code> Fillet All Edges</code> Featurescript to add a 0.25" radius fillet to the remaining edges on the bellypan by selecting the bottom face of the bellypan.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtParts7.webp" style="width:100%">
      <figcaption>7. Add the seed instances of the holes for the bellypan.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtParts8.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>8. Next, use the <code>Linear Pattern</code> sketch tool to pattern the holes along the edge.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtParts9.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>9. Use the <code>Circular Pattern</code> sketch tool to pattern the holes about the origin onto all four edges.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtParts10.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>10. Use the <code>Linear Pattern</code> sketch tool to pattern the holes for the 2"x2" tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtParts11.webp" style="width:100%">
      <figcaption>11. Clean up the sketch by moving the dimensions so that they are all visible. A clean sketch is important for readability of the CAD so that it is easily editable in the future.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtParts0.webp" style="width:100%">
      <figcaption>12. Finally, name your sketches and organize them into a folder in the feature tree. Additionally, set the material of the bellypan to Aluminum 6061 and name your parts.</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <button class="prev" onclick="plusSlides(-1,1)" style="background-color: #000; color: #fff;">&#10094;</button>
  <button class="next" onclick="plusSlides(1,1)" style="background-color: #000; color: #fff;">&#10095;</button>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

In this section, you were introduced to the `Derived` feature. This feature is extremely powerful and can be used to import parts from one part studio into another to enable references for modeling. However, you must be careful to not overuse this function as it can significantly slow down your part studios.

At this point, you should be feeling more and more comfortable with Onshape modeling and using Featurescripts. Always make sure to clean up your feature tree while working to keep it organized and easy to use. You can more learn about feature tree organization on the [Feature Tree Best Practices](/best-practices/feature-tree-setup/ "Feature Tree Best Practices Page"){:target="_blank"} page.

### Assembly

Now that the part studio is finished, you can create the drivetrain assembly. 

Previously, in Stage 1A when you created assemblies one of the parts in the group mate was fixed in place. However, this is not considered a good practice as it is not parametric. This is where the origin cube comes in: the origin cube has a mate connector placed at the origin of the part studio. After inserting and grouping all of the parts, you can fasten the origin cube to the origin of the assembly. This aligns the part studio origin and assembly origin.

Start by **creating a new assembly tab called `Drivetrain Assembly`** in the `Drivetrain` folder. **Follow the instructions in the slides** to complete the assembly.

<!-- <center>**Drivetrain Assembly**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtAssy0.webp" style="width:100%">
      <figcaption>0. The assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtAssy1.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>1. Insert the parts into the assembly, <code>Group</code> them, then fasten the origin cube to the origin of the assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtAssy2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Insert the MK4i module from the MKCad app into the assembly and mate it into place. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtAssy3.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>3. Use the <code>Circular Pattern</code> assembly tool to finish assembling the modules. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtAssy4.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Insert a 3/16" rivet from the MKCad app into the assembly and mate it. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtAssy5.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. Use the <code>Replicate </code> assembly tool to replicate the rivet and rivet mate onto all matching geometry on the bottom face of the bellypan</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtAssy0.webp" style="width:100%">
      <figcaption>6. The assembly.</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <button class="prev" onclick="plusSlides(-1,2)" style="background-color: #000; color: #fff;">&#10094;</button>
  <button class="next" onclick="plusSlides(1,2)" style="background-color: #000; color: #fff;">&#10095;</button>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

The `Replicate` tool is a very powerful tool for duplicating parts in assemblies. `Replicate` works by creating a copy of the selected parts, and duplicates the selected mate onto the selected geometry. Note that the selected geometry must exactly match the origin mate geometry, eg: the hole diameter must be the same for replicate to copy a rivet. In your assembly, you use the select the face for replicate to apply to. What this does is identify all geometry that matches the original mate and then copy the selected components and mate to those matching locations on the selected face. If you want to replicate onto only specific holes, you can change the drop-down menu to "Match Individual Edges".

??? Video "Match Individual Edges for Replicate"
    <video width="1920" controls>
      <source src="/img/learning-course/stage1c/replicateExample.webm" type="video/mp4">
    </video>

**Adding More Components**

When you model more parts in the part studio, you can insert them into the assembly in a similar to fashion to before. Hit insert and immediately click on the green checkmark. Then, edit the initial `Group` you made and add the part to the group. By doing this, you ensure that added parts will always stay in the same place it was modeled in the part studio.

Let's add a gusset to connect the 2"x2" tube to the 2"x1" tube.

Start by **navigating to the `Drivetrain` Part Studio** in the `Drivetrain` folder. **Follow the instructions in the slides** to add the gusset.

<!-- <center>**Adding a Gusset**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtAdd0.webp" style="width:100%">
      <figcaption>0. Finished drivetrain assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtAdd1.webp" style="width:100%">
      <figcaption>1. Add the gusset for the crosstube with the <code>Gusset</code> Featurescript.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtAdd2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Insert the gusset into the assembly and add it to the <code>Group</code>.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtAdd3.webp" style="width:100%">
      <figcaption>3. Copy the gusset and mate it to the other side. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtAdd4.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Edit the replicate feature to add rivets to the gusset. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtAdd0.webp" style="width:100%">
      <figcaption>4. Finished drivetrain assembly.</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <button class="prev" onclick="plusSlides(-1,3)" style="background-color: #000; color: #fff;">&#10094;</button>
  <button class="next" onclick="plusSlides(1,3)" style="background-color: #000; color: #fff;">&#10095;</button>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>


Make sure you sort the instances in your assembly into folders (i.e. frame, swerve modules) and name any patterns and replicates used. This will help you locate components in the assembly later down the line.

!!! success "Verification"
    If all is done correctly your assembly should weigh approximately 31.4lbs.

    Your tab manager should have the following tabs and folder:
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtTabManager.webp" style="width:100%">
    </figure>

It should be noted that while modeling every detail of the robot hardware (bolts, rivets, nuts) is beneficial for purchasing and real life assembly purposes, it isn't strictly necessary. Time is a precious resource, especially during build season, so you should spend it on what will give you the biggest return.

More details about best practices for Onshape assemblies are included on the [Assembly Best Practices Page](/best-practices/assembly-setup/ "Assembly Best Practices Page"){:target="_blank"}.

## Top Level Robot Assembly
Now that you have a drivebase, you can create a *top level robot assembly*. The top level robot assembly is the highest in the assembly hierarchy. Organizing the assemblies in this way keeps thing organized from both a CAD assembly and real life assembly standpoint. 

You will create a top level robot assembly to go with your drivebase. The mechanism you'll be adding is the scoring mechanism from [1678's 2023 robot](https://www.thebluealliance.com/team/1678/2023 "1678 2023 Blue Alliance Page"). The scoring mechanism CAD can be accessed from here:

<center>[1678 2023 Scoring Mechanism Document](https://cad.onshape.com/documents/28a750426de8e2bc17d5b900/w/8e79c6217ae2ce07ff57d900/e/a4d266d03289620078d13a80 "Team 1678 2023 Scoring Mechanism Onshape Document"){:target="_blank" .md-button .md-button--primary }</center>

Start by, **creating a new assembly tab above the `Master Sketch` part studio** and name it **`Top Level Robot Assembly`**. **Follow the instructions in the slides** to complete the top level robot assembly.

<!-- <center>**Top Level Robot Assembly**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/TopLevel/topL0.webp" style="width:100%">
      <figcaption>0. Finished top level robot assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/TopLevel/topL1.webm" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>1. Insert the drivetrain assembly and fasten the origin cube to the assembly origin. You may need to unhide the origin cube to mate it.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/TopLevel/topL2.webm" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Insert the 1678 2023 scoring assembly by pasting the scoring mechanism link into the <code>Insert</code> menu textbox. Then, fasten its origin cube to the assembly origin. You may need to hide the drivetrain's origin cube to access the origin of the assembly for mating.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/TopLevel/topL0.webp" style="width:100%">
      <figcaption>3. Finished top level assembly. </figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <button class="prev" onclick="plusSlides(-1,4)"style="background-color: #000; color: #fff;">&#10094;</button>
  <button class="next" onclick="plusSlides(1,4)" style="background-color: #000; color: #fff;">&#10095;</button>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

!!! success "Verification"
    Your tab manager should now looks like this:
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtTabManager2.webp" style="width:100%">
    </figure>

And that's all there is to the top level robot assembly! The use of the origin cube makes it very easy to mate together assemblies. In later stages you will explore how to create flexible assemblies (arms, elevators, etc) with the origin cube. If you are interested, you can get a sneak peek [here](/best-practices/assembly-setup/#utilizing-origin-cube-for-flexible-assemblies "Origin Cube Information Page"){:target="_blank"}.



<!-- TODO: CHANGE THIS TEXT -->

## Summary

Congratulations on completing Stage 1C! Keep up the good work!

Here is a quick summary of what you have achieved in 1C:

* Learned about top-down robot design methodology and master sketches
* Learned how to use the derive feature to drive part studios using master sketches
* Learned how to use the origin cube to mate together top level assemblies
* Learned how to model a simple swerve drivetrain

Remember, practice is essential – the more CAD models you create, the more proficient and efficient you'll become. Using keyboard shortcuts can significantly accelerate your CAD workflow. Be attentive to best practices to avoid developing any bad habits.

In Stage 2, you will begin to model robot mechanisms using all the skills you have learned in Stage 0 and Stage 1! Note that in stage 2, the learning course will become less step-by-step and more open ended, which will enable you to add your own input on designs based on your team's way of doing things. As always though, reference CAD models will be available.

Optionally, please fill out [this feedback form](https://forms.gle/J1QNvRkvpi7xyfuU8 "Learning Course Feedback Form"){:target="_blank"} about stages 0 and 1.

<br>

<!-- ------------------DO NOT TOUCH ANYTHING BELOW HERE------------------ -->

<script>

// Initialize slide index for each slideshow

let slideIndices = [0];

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

  currentSlide(1);

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