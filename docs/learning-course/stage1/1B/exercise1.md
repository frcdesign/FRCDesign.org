

# 1B: Power Transmissions


## Practice Exercises
Time to practice! Start by **make a copy of the Stage 1B Exercises Document** through the button below, just like you did with the Stage 1A Exercises Document. Each exercise has a folder, a "reference" tab (a preview of what the final model should look like), and a tab or two for doing your exercise in. Solutions are also provided in the 1B Exercise Solutions Document to check your work afterwards.

<center markdown>[1B Exercises Document (COPY THIS)](https://cad.onshape.com/documents/b1706348cc4572441f336b65/w/8b05bae52d527bd02ea01221/e/a7b840fb60a71771dc88c5e4?renderMode=0&uiState=68d01c81cc1540ce7ec8a526 "1B Exercises Onshape Document"){:target="_blank" .md-button .md-button--primary }
[1B Exercise Solutions](https://cad.onshape.com/documents/5bdb5e55b32fce8eb3d75c54/w/ab9c87cf5aa3fe8f1c172e44/e/e5f7bf7a28d1dc27fbf197c0 "1B Exercise Solutions Onshape Document"){:target="_blank" .md-button .md-button--primary } </center>

## Exercise 1: Simple Gearbox 

In this exercise, you will be modeling and assembling a simple single stage gearbox. The goal of this exercise is to introduce how to model a very simple gear transmission. Additionally, you will learn how to use the the [`Shaft` Featurescript](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Julia's Featurescripts Onshape Document"){:target="_blank"}, `Replicate` tool, [MKCad parts library](../../course-setup/required-course-tools/part-library.md "Adding MKCAD Tutorial Page"){:target="_blank"}, and part configurations.

!!! Warning
    As this is the first exercise where MKCAD is being used, please be sure you have it added by following [the tutorial in course setup!](../../course-setup/required-course-tools/part-library.md "Adding MKCAD Tutorial Page"){:target="_blank"} MKCAD is a parts library for FRC used for inserting COTS components into assemblies.

!!! Note
    Exercise 1 adds hardware (bolts and nuts) to the CAD models. You can read more about hardware standards on the [Design Handbook](/design-handbook/structure/fasteners/ "Design Handbook Fasteners Page"){:target="_blank"} page.

### Layout Sketches

A layout sketch is a sketch that captures the geometry of a design without specifying the exact details. 
They are like the framing of a house—it defines the overall structure and relationships between key components, but doesn't include the finishing details like walls or paint. 
Keeping the key dimensions in a layout sketch makes it easy to adjust when needed. We will utilize layout sketches for almost all designs moving forward.

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
      <img src="/img/learning-course/stage1b/exercises/e1/e1s2.png" style="width:100%">
      <figcaption> 2. Add the outline of the motor, a ~65mm diameter circle, around the 12T gear that the motor is attached to. The layout sketch is now finished.  </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s3.png" style="width:100%">
      <figcaption> 3. Create a new sketch for the motor plate. Using the layout as the reference, draw a 1.125" hole for the bearing and a 22mm hole for the motor boss (the nub that sticks out from the motor). Note that depending on our manufacturing processes and tolerances, you may need to draw your bearing holes slightly larger or smaller than nominal (1.125"). </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s4.png" style="width:100%">
      <figcaption> 4. Add two mounting holes for the motor. A good practice to constrain the holes is to draw and dimension a <it>bolt circle</it>, then draw the holes for the bolts on the bolt circle. This constrains the distance of the holes from the center of the motor with a single dimension. The bolt circle for the motor we are using is 2". </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s5.png" style="width:100%">
      <figcaption>  5. Add the four bolt holes for connecting the two plates. Use a center rectangle to create the construction geometry so that only two dimensions are required to constrain the holes.    </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s6.png" style="width:100%">
      <figcaption> 6. Using centerpoint arcs, lines, and the sketch mirror tool, draw the outline for the plate around the holes and motor outline. The intelligent placement of the origin along the vertical line of symmetry allows you to use the right plane to mirror the plate outline. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s7.png" style="width:100%">
      <figcaption> 7. Extrude the motor plate to be 5mm thick. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s8.png" style="width:100%">
      <figcaption> 8. Use the <code>Spacer</code> Featurescript to add a round 10mm diameter, 16mm long spacer. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s9.png" style="width:100%">
      <figcaption> 9. Create the outer plate sketch on the face of the spacer. Use the <code>Use</code> sketch tool to project the holes and edges of the motor plate, but add a round cutout at the top using one of the <code>arc</code> tools. Note that the sketch can be mostly defined by using constraints such as <code>tangent</code>, <code>equal</code>, and <code>vertical</code>.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s10.webp" style="width:100%">
      <figcaption>10. Extrude the outer plate to be 5mm thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e1/e1s11.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>11. Use the <code>Shaft</code> Featurescript to model the output shaft. Follow the settings used. You can learn more about the shaft retention property on the Design Handbook page. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s12.webp" style="width:100%">
      <figcaption> 12. Finished part studio. Name the key sketches and parts. Set the material of the plate and spacers to 6061 Aluminum. The shaft has its material automatically determined from the <code>Shaft</code> Featurescript.</figcaption>
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

When putting together the assembly, you may need to use the "Lock Mate Inferences" functionality to properly mate the motor pinon. Watch the following video to learn how:

???+ Tip "Locking Mate Inferences when Mating Assemblies"
    To lock mate inferences when you see the one you want to select, hold the `Shift` key when mousing. This is particularly useful for mating the motor pinion gear.
    <center>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/shiftSelectEdited.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
    </center>
    <center>*Using Shift key to lock mate inferences while mating.*</center>

**Navigate to the "Exercise #1 Assembly" tab** in your copied document and **follow the instructions in the slides** to complete the exercise.

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
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e1/e1s13.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption> 1. Insert the part studio into the assembly and fix the gearbox plate. Group mate the two plates together and then mate the spacer to the motor plate. Then, use the <code>Replicate</code> tool to replicate the spacer and its associated mate onto the other spacer locations. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e1/e1s14.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption> 2. Assemble the bearings and shaft using parts from the MKCad App.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e1/e1s15.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption> 3. Assemble the motor and motor pinion gear using parts from the MKCad App. You will need to use mate inference locking to fasten the motor to the motor pinion: See the above drop down to learn how. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e1/e1s16.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption> 4. Assemble the shaft spacer and gear using parts from the MKCad App. Configurable parts will have a blue grid icon in the instance list. Notice how you were able to change the tooth count of the gear from 40T to 60T after mating it. Using configurable components like this makes your models more parametric since you can change the component without needing to re-insert and mate. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e1/e1s17.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption> 5. Assemble the shaft retention bolts using the MKCad app parts. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e1/e1s18.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption> 6. Assemble the motor bolts, gearbox bolts, and nuts using the Onshape Standard Content and MKCad app parts. When inserting Onshape Standard Content, you can use the snap mode to automatically add the mates when inserting or insert the component and then manually mate it. </figcaption>
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
    Make sure to have you and/or a more experienced member/mentor of the team [**review your CAD!**](../1A/focusing-on-improvement.md "Focusing on Improvement Page"){:target="_blank"} Your assembly should have 19 Instances and weigh approximately 1.04kg.


### Configurable Parts

In this exercise you made your first gearbox. In doing so, you also used part configurations - a powerful tool that allows for variations of the same part. The gears that you inserted from MKCad were configurable - you were able to easily change the tooth count of the gear without needing to inserting a new component. Try and use configurable parts when they are available to make your models more parametric.

<br>


