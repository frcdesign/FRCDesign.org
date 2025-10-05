

# 1B: Power Transmissions


## Practice Exercises
Time to practice! Start by **make a copy of the Stage 1B Exercises Document** through the button below, just like you did with the Stage 1A Exercises Document. Each exercise has a folder, a "reference" tab (a preview of what the final model should look like), and a tab or two for doing your exercise in. Solutions are also provided in the 1B Exercise Solutions Document to check your work afterwards.

<center markdown>[1B Exercises Document (COPY THIS)](https://cad.onshape.com/documents/ce41613fac38db8c00e65020/w/a65651477167d5e36fe871c0/e/755940e52d82bddfdf7be61e "1B Exercises Onshape Document"){:target="_blank" .md-button .md-button--primary }
[1B Exercise Solutions](https://cad.onshape.com/documents/c6a8ec29479a2578841fb9f2/w/85094b3baa15a05c873920c9/e/47efe87a05a8318bffd60957 "1B Exercise Solutions Onshape Document"){:target="_blank" .md-button .md-button--primary } </center>

## Exercise 1: Simple Gearbox 

In this exercise, you will be modeling and assembling a simple single stage gearbox. The goal of this exercise is to introduce how to model a very simple gear transmission. Additionally, you will learn how to use the the [`Robot Shaft` and `Robot Spacer` Featurescripts](https://cad.onshape.com/documents/9cffa92db8b62219498f89af/v/0d2ae9a0b843b03bdb63724f/e/99672d1e329b38e647d90146 "Alex's Featurescripts Onshape Document"){:target="_blank"} and the `Replicate` tool. You will also use the [FRCDesignLib part library](../../course-setup/required-course-tools/part-library.md "Adding FRCDesignApp Tutorial Page"){:target="_blank"} for components other than fasteners, such as gears and motors.

!!! Note
    Exercise 1 adds hardware (bolts and nuts) to the CAD models. You can read more about hardware standards on the [Design Handbook](/design-handbook/structure/fasteners/ "Design Handbook Fasteners Page"){:target="_blank"} page.

### Layout Sketches

A layout sketch is a sketch that captures the geometry of a design without specifying the exact details. 
They are like the framing of a house—it defines the overall structure and relationships between key components, but doesn't include the finishing details like walls or paint. 
Keeping the key dimensions in a layout sketch makes it easy to adjust when needed. We will utilize layout sketches for almost all designs moving forward.

!!! Tip "Motor"
    The motor used in this exercise is a CIM-class motor called a Falcon 500. While discontinued for purchase, many teams still own some and they use the same 2" mounting hole pattern that most other FRC motors use, as discussed on the [Motors page](motors.md).

### Part Studio Instructions
**Navigate to the "Exercise #1 Part Studio" tab** in your copied document and **follow the instructions in the slides** to complete the part studio.


<!-- <center>**Exercise 1 Instruction Slides**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s12.webp" style="width:100%">
      <figcaption>0. Finished Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s1.webp" style="width:100%">
      <figcaption> 1. Begin by creating the layout sketch for the gearbox. Draw the pitch circles for the 60T and 12T gears. Set the pitch circles tangent to constrain the center-to-center distance between the gears. Constrain the centers of the two gears to be vertical.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s2.webp" style="width:100%">
      <figcaption> 2. Add the outline of the motor, a 2.5" diameter circle, around the 12T gear that the motor is attached to. The layout sketch is now finished.  </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s3.webp" style="width:100%">
      <figcaption> 3. Create a new sketch for the motor plate. Using the layout as the reference, draw a 1.125" hole for the bearing and a 1.25" hole for the motor boss (the nub that sticks out from the motor). Note that depending on your manufacturing processes and tolerances, you may need to draw your bearing holes slightly larger or smaller than nominal (1.125"). </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s4.webp" style="width:100%">
      <figcaption> 4. Add two mounting holes for the motor on a 2" bolt circle. When using only two mounting holes, an alternative to using a circular pattern is to draw and dimension a 2" <it>construction circle</it>, then draw the holes for the bolts on the circle. Make sure to constrain the angle of the holes as well; we used a horizontal constraint.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s5.webp" style="width:100%">
      <figcaption>  5. Add the four bolt holes for connecting the two plates. Use a center rectangle to create the construction geometry so that only two dimensions are required to constrain the holes.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s6.webp" style="width:100%">
      <figcaption> 6. Using centerpoint arcs, lines, and the sketch mirror tool, draw the outline for the plate around the holes and motor outline. The intelligent placement of the origin along the vertical line of symmetry allows you to use the right plane to mirror the plate outline. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s7.webp" style="width:100%">
      <figcaption> 7. Extrude the motor plate to be 1/4" thick. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s8.webp" style="width:100%">
      <figcaption> 8. Use the <code>Robot Spacer</code> Featurescript to add a round 3/8" diameter, 5/8" long spacer. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s9.webp" style="width:100%">
      <figcaption> 9. Create the outer plate sketch on the face of the spacer. Use the <code>Use</code> sketch tool to project the holes and edges of the motor plate, but add a round cutout at the top using one of the <code>arc</code> tools. Note that the sketch can be mostly defined by using constraints such as <code>tangent</code>, <code>equal</code>, and <code>vertical</code>.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s10.webp" style="width:100%">
      <figcaption>10. Extrude the outer plate to be 1/4" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/RDXcECn8uSI?rel=0" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption>11. Use the <code>Robot Shaft</code> Featurescript to model the output shaft. Follow the settings used.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s12.webp" style="width:100%">
      <figcaption> 12. Finished part studio. Name the key sketches and features. Set the name, material (6061 Aluminum), and appearance of the plates and spacer by right clicking the parts in the part list. The shaft has its material automatically determined from the <code>Robot Shaft</code> Featurescript.</figcaption>
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

### Assembly Instructions

When putting together the assembly, **you may have some difficulty mating the motor pinion gear** to the motor shaft. 

You can **lock the visible mate connectors on a face by holding the `Shift` key before going to press on a mate connector** that isn't physically on the face. Watch the video below for a tutorial.

<figure>
  <iframe src="https://www.youtube.com/embed/zI8wBHeTfdc?rel=0" width="768" height="432" frameborder="0" allowfullscreen></iframe>
  <figcaption>Using the Shift key to lock mate inferences while mating</figcaption>
</figure>


**Now navigate to the "Exercise #1 Assembly" tab** in your copied document and **follow the instructions in the slides** to complete the exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/kChIFuuLahU?rel=0" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption> 1. Insert the part studio into the assembly and fix the gearbox plate. Group mate the two plates together and then mate the spacer to the motor plate. Then, use the <code>Replicate</code> tool to replicate the spacer and its associated mate onto the other spacer locations. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/gKP-n5eKmjE?rel=0" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption> 2. Assemble the bearings and shaft using parts from FRCDesignLib.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/ZJCs0ms3I8A?rel=0" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption> 3. Assemble the motor and motor pinion gear using parts from FRCDesignLib. You will need to use mate inference locking to fasten the motor to the motor pinion: See the above drop down to learn how. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/mMP-kkl6AuY?rel=0" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption> 4. Assemble the shaft spacer and gear using parts from FRCDesignLib. Configurable parts will have a blue grid icon in the instance list. Notice how you were able to change the tooth count of the gear from 40T to 60T after mating it. Using configurable components like this makes your models more parametric since you can change the component without needing to re-insert and mate. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/SytVbO_-BrM?rel=0" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption> 5. Insert the shaft retention bolts from FRCDesignLib. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
       <iframe src="https://www.youtube.com/embed/D4OWWMYYwWM?rel=0" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption> 6. Add the motor bolts, gearbox bolts, and nuts using FRCDesignLib parts.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s0.webp" style="width:100%">
      <figcaption>7. Finished assembly. Make sure to sort your parts into folders and name your replicate features. </figcaption>
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

!!! Success "Verification"
    Make sure to have you and/or a more experienced member/mentor of your team [**review your CAD!**](../1A/focusing-on-improvement.md "Focusing on Improvement Page"){:target="_blank"} Your assembly should have 19 Instances and weigh approximately 2.3 lbs.


### Configurable Parts

In this exercise you made your first gearbox. In doing so, you also used part configurations - a powerful tool that allows for variations of the same part. The gears that you inserted from FRCDesignLib were configurable - you were able to easily change the tooth count of the gear without needing to inserting a new component. Try and use configurable parts when they are available to make your models more parametric.

<br>


