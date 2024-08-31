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


# 1A: Onshape Fundamentals

Welcome to Stage 1! Here, you'll engage in a series of Onshape exercises and projects designed to introduce and develop your CAD skills within an FRC context. 

In Stage 1A, there are 3 major sections: sketching and part design, multi-part part studios, and assemblies. Each section has a link to a learning course to learn the skills of each topic, then an exercise to help immediately apply those skills in an FRC context. 

!!! Tip
    Remember to take a look at the [website feature guide](../website-feature-guide.md "Website Feature Guide Page"){:target="_blank"} to gain an understanding of the different features used throughout the learning course!

### Learning Courses
[Onshape's Learning Center](https://learn.onshape.com/ "Onshape Learning Center"){:target="_blank"} provides free learning courses and articles covering everything from document navigation and sketching to advanced surface and sheet metal modeling. It's a valuable resource for both novice and seasoned users alike. We use a few selected courses to assist learning the fundamentals of doing CAD in Onshape, but the rest of the curriculum is project based.

The structure of the courses includes some short videos and practice models, expected time is 2-4 hours.

!!! Warning
    The Onshape learning courses are important as they will teach you the interface and form a basic foundation for CAD skills. Unless you have a significant amount of prior experience using Onshape, you should not skip the learning courses as the exercises assume that you have an understanding of CAD basics.


    
## Sketching and Part Design
Sketches and features are the building blocks you will use to create every 3D model in Onshape, so it's good to have a good grasp on the fundamentals.

**Complete the following Onshape Learning Courses:**

1. The [**Introduction to Sketching**](https://learn.onshape.com/courses/fundamentals-sketching "Introduction to Sketching Onshape Learning Course"){:target="_blank"} course runs you through different sketch tools, constraints, and a good sketch workflow.

2. The [**Part Design Using Part Studios**](https://learn.onshape.com/courses/fundamentals-part-design-using-part-studios "Part Design Using Part Studios Onshape Learning Course"){:target="_blank"} course runs you through creating different parts with a variety of features.

With a good understanding of both of these, you can create almost any part you want to. The following sections are all about integrating design intent into the process and learning how to design a whole project with multiple pieces.

!!! Tip
    For future reference without having to go through the learning center, [sketch basics](https://cad.onshape.com/help/Content/sketch_basics.htm?tocpath=Part%20Studios%7C_____15 "Sketch Basics Onshape Help Page"){:target="_blank"}, [sketch tools](https://cad.onshape.com/help/Content/sketch-tools.htm?TocPath=Part%20Studios%7CSketch%20Tools%7C_____0 "Sketch Tools Onshape Help Page"){:target="_blank"}, [feature basics](https://cad.onshape.com/help/Content/feature-basics.htm?tocpath=Part%20Studios%7C_____17 "Feature Basics Onshape Help Page"){:target="_blank"}, and [feature tools](https://cad.onshape.com/help/Content/featuretools.htm?TocPath=Part%20Studios%7CFeature%20Tools%7C_____0 "Feature Tools Onshape Help Page"){:target="_blank"} are all covered in text form in the help center. 

!!! Warning "<span style="font-size: 0.8rem !important;">**DO NOT MOVE PAST THIS POINT UNTIL YOU HAVE COMPLETED THE TWO LEARNING COURSES ABOVE**</span>"

<br>

### Practice Exercise Prerequisites
**Make a copy of the Stage 1A Exercises Document** through the button below. Each exercise has a folder, a "reference" tab (a preview of what the final model should look like), and a tab or two for doing your exercise in. Solutions are also provided in the 1A Exercise Solutions Document to check your work afterwards.

<center>
[1A Exercises Document](https://cad.onshape.com/documents/812b2974ed32b9c89e8f1e25/w/747e47444b6c685bd0bee334/e/58894354f0152cd6485fe45e?renderMode=0&uiState=663d81b7afce5246f0309e28 "1A Exercises Onshape Document"){:target="_blank"  .md-button .md-button--primary}
[1A Exercise Solutions Document](https://cad.onshape.com/documents/1bdaed8e23446ffe70a851a4/w/37cd1a4984497b01d74e4c41/e/fd6796321fb9611305e5ff7d?renderMode=0&uiState=663d81d5d060d67d3cd48855 "1A Exercise Solutions Onshape Document"){:target="_blank" .md-button .md-button--primary}
</center>

<br>


??? Tip "Tab Manager"
    You can navigate between the tabs by accessing the tab manager or from the bottom navigation bar. 
    <center>
      <video width="1920" controls>
        <source src="\img\learning-course\stage1a\1a-tabs.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
    <center> *Accessing the Tab Manager.* </center>

<br>

### Exercise #1: Simple Box Tube

**Box Tube Explanation**

In FRC, robot structures are typically constructed out of aluminum box tubing, similar to wood beams for a house. Aluminum box tubing is commonly found in 2"x1", 1"x1", and 2"x2" sizes with 1/8" (thickwall) or 1/16" (thinwall) wall thicknesses. Box tubing is typically referred to by its size, eg: 2x1, 1x1, and 2x2 (Spoken as "two-by-one", "one-by-one", and "two-by-two"). For the rest of the learning course, we will use this notation when referring to box tube.


??? Example "Box Tube Example"
    <center><img src="\img\learning-course\stage1a\tube.webp" width="45%"> </center>

<br>

**Instructions**

For this exercise, you will be modeling a simple 2x1 with some holes in it. For this exercise, do not use any Featurescripts. **Navigate to the "Exercise #1 Box Tube" tab** in your copied document and **follow the instructions in the slides** to complete your first exercise.

<br>

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure markdown="span">
      <img src="/img/learning-course/stage1a/exercises/e1/e1s6.webp" style="width:100%; data-description="0. The final part"">
      <figcaption>0. The final part.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e1/e1s1.webp" style="width:100%; data-description="1. Start by sketching a center rectangle on the top plane."">
      <figcaption>1. Start by sketching a center rectangle on the top plane. Notice that we put the origin of the part at the center of the tube so that we can leverage the default geometry later on. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e1/e1s2.webp" style="width:100%; data-description="2. Extrude the rectangle symmetrically, 2 inches tall."">
      <figcaption>2. Extrude the rectangle symmetrically, 2" tall.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e1/e1s3.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>3. Shell the block to turn it into a 1/16" wall tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e1/e1s4.webm" type="video/webm"> 
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Add the top holes. Set the centerpoint of the hole to be vertical with the midpoint of the bottom line, then Mirror the hole across, using the front plane as the mirror line. We are able to use the front plane to mirror since we intelligently placed the origin at the center of the tube in step 1. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e1/e1s5.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. Add the side holes. Create the layout for the side holes by creating a center point rectangle and turning it into construction geometry. Again, having the origin at the center of the tube lets us place the center of the pattern at the center of the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e1/e1s6.webp" style="width:100%; data-description="6. Name the key sketches and part. Set the material to be 6061 Aluminum."">
      <figcaption>6. Extrude the holes to cut all the way through the tube. Name the key sketches and part. Set the material to be 6061 Aluminum. </figcaption>
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

!!! note "Verification"
    If you did everything correctly your box tube should weigh about 0.351lbs

Notice how we utilized construction geometry to define the location of the holes on the 2" face of the tube. Using construction geometry to assist with sketching makes your parts more parametric and betters conveys design intent compared to manually specifying the location of each hole with dimensions.

!!! Note
    Some sketches and features have been renamed (i.e. "Tube Profile"). You can rename sketches and features by hovering over the name in the dialogue box and clicking the pencil icon, or right clicking a sketch or feature in the feature list and clicking "rename". 

Notice how we utilized construction geometry to define the location of the holes on the 2" face of the tube. Using construction geometry to assist with sketching makes your parts more parametric and betters conveys design intent compared to manually specifying the location of each hole with dimensions.

<br>

## Multi-Part Modeling

Onshape is a software focused on a *top-down design* workflow (explored more in [Stage 1C](1C-designMethodology.md "Learning Course Stage 1C Page"){:target="_blank"}) using multi-part part studios. It allows you to create several different related parts in the same tab, all referencing each other, making the part creation for something like a subsystem easy.

**Complete the following Onshape Learning Course:**

- The [**Multi-Part Part Studios**](https://learn.onshape.com/courses/fundamentals-multi-part-part-studios "Multi-Part Part Studios Onshape Learning Course"){:target="_blank"} course runs you through top-down design principles, sketching for multiple parts (master sketches), and some more practical skills for working with multiple parts in a part studio.

Check out [this page](../../best-practices/sub-document-setup.md "Sub-Document Best Practices Page"){:target="_blank"} to learn more about best practices for sub-documents. The following practice exercises will help you reinforce these concepts.

??? Example "Multi-Part Part Studio Example"
    Notice how there's one instance of each unique part within this part studio. The part studio also resembles the completed product, as the parts are modeled relative to each other.
    <center><img src="\img\learning-course\stage1a\1a-PartStudio.webp" width="55%"></center>
    <center> *Example of a part studio* </center>

!!! Warning "<span style="font-size: 0.8rem !important;">**DO NOT MOVE PAST THIS POINT UNTIL YOU HAVE COMPLETED THE LEARNING COURSE ABOVE**</span>"

<br>

### Exercise #2: Box Tube and Gusset Joint

**Gusset Explanation**

Aluminum box tubes are commonly connected together with 'gussets'. A gusset is a flat plate that, when attached to both tubes, helps create rigidity in the structure. 

??? Example "Gusset Example"
    <center><img src="\img\learning-course\stage1a\8033-000-2024C_8.png" width="45%"> </center>

<br>

**Instructions**

For this exercise, you will design two box tubes attached together with a gusset. This gusset will be created in the same part studio as the tubes that it is connecting!

You will utilize the `Extrude Individual` and `Tube Converter` Featurescripts for this exercise. **Do not use the `Gusset` Featurescript for this exercise.**

- The `Extrude individual` Featurescript enables you to extrude sketch regions without merging them. In this exercise, if you were to extrude the sketch of the tubes with the standard <code>Extrude</code> tool, only a single part would generate.

- The `Tube Converter` Featurescript condenses the steps of shelling, sketching and dimensioning holes, and extruding holes into a single, customizable feature to easily model tubes. 

???+ Warning "Creating New Parts"
    When extruding a sketch in a part studio, you can decide whether to `Add` to existing geometry, or to create `New` geometry. `New` creates a new body, whereas `Add` will merge the feature with existing parts. Make sure that when you extrude your gusset, you tell Onshape to create a new part.
    <center><img src="\img\learning-course\stage1a\1a-merge.png" width="20%"></center>
    <center> *The different options for extruding* </center>

**Navigate to the "Exercise #2 Gusset" tab** in your copied document and **follow the instructions in the slides** to complete the second exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure markdown="span">
      <img src="/img/learning-course/stage1a/exercises/e2/e2s11.webp" style="width:100%; data-description="0. The finished parts."">
      <figcaption>0. The finished parts.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e2/e2s1.webp" style="width:100%; data-description="1. Start by sketching the tubes on the right plane."">
      <figcaption>1. Start by sketching the tubes on the right plane. Positioning the origin horizontally in the center of the part studio enables mirroring the vertical tube from the left to the right using the front plane.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e2/e2s2.webp" style="width:100%; data-description="2. Use the `Extrude Individual` Featurescript to extrude the blocks."">
      <figcaption>2. Use the <code>Extrude Individual</code> Featurescript to extrude the blocks. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e2/e2s3.webp" style="width:100%; data-description="3. Use `Tube Converter` Featurescript to turn the blocks into 1/16 inch wall tubes with a 0.5 inch spacing pattern of 0.196 inch holes."">
      <figcaption>3. Use <code>Tube Converter</code> Featurescript to turn the blocks into 1/16" wall tubes with a 0.5" spacing pattern of 0.196" holes.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e2/e2s4.webp" style="width:100%; data-description="4. Draw a triangle with construction geometry for the gusset."">
      <figcaption>4. Draw a triangle with construction geometry for the gusset. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e2/e2s5.webp" style="width:100%; data-description="5. Dimension the triangle to be 0.5 inches away from the edges of the tube."">
      <figcaption>5. Dimension the triangle to be 0.5" away from the edges of the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e2/e2s6.webp" style="width:100%; data-description="6. Use the `Offset Entities` tool to offset the construction geometry 0.25 inches. This will be the outline of the gusset."">
      <figcaption>6. Use the <code>Offset Entities</code> tool to offset the construction geometry 0.25". This will be the outline of the gusset. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e2/e2s7.webp" style="width:100%; data-description="7. Use the `Sketch Fillet` tool to add a 0.25 inch fillet to the three corners of the gusset."">
      <figcaption>7. Use the <code>Sketch Fillet</code> tool to add a 0.25" fillet to the three corners of the gusset. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e2/e2s8.webp" style="width:100%; data-description="8. Delete the three points left over from the fillet."">
      <figcaption>8. Delete the three points left over from the fillet. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e2/e2s9.webp" style="width:100%; data-description="9. Use the `Use (Project/Convert)` tool to project the tube holes onto the gusset sketch."">
      <figcaption>9. Use the <code>Use (Project/Convert)</code> tool to project the tube holes onto the gusset sketch. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e2/e2s10.webp" style="width:100%; data-description="10. Extrude the gusset to be 1/8 inch thick. Select `New` as the extrude type to make the extrude a new part."">
      <figcaption>10. Extrude the gusset to be 1/8" thick. Select <code>New</code> as the extrude type to make the extrude a new part. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e2/e2s11.webp" style="width:100%; data-description="11. Name the key sketches and parts. Set the material to be 6061 Aluminum."">
      <figcaption>11. Name the key sketches and parts. Set the material to be 6061 Aluminum. </figcaption>
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

In this exercise, you can begin to see the power of Featurescripts. What would have been a number of sketches, extrudes, and shells to create the tubes is packaged into a single, easy to use custom feature. 

!!! note "Verification"
    If all is done correctly your parts should weigh a combined 0.27lbs

<br>

## Assemblies

Assemblies are where parts designed in the part studio get assembled together. This is where you truly define the position and motion of all the different parts of something. 

**Complete the following Onshape Learning Course:**

- The [Onshape Assemblies](https://learn.onshape.com/courses/fundamentals-onshape-assemblies "Onshape Assemblies Onshape Learning Course"){:target="_blank"} learning course introduces assemblies, mating parts together, and other useful assembly concepts.

As was introduced in the Onshape learning tutorials, when parts are inserted into an assembly, they free float. We can utilize a number of different assembly tools to constrain the motion of all the parts:

- **`Group`**: Restricts the relative motion between a group of parts
- **`Fix`**: Locks a part in place within the assembly (not recommended as it's not parametric)
- **`Mates`**: Tools to constrain the degrees of freedom between parts using "mate connectors." These connectors are automatically generated or manually created coordinate systems on parts. You can align the axes and apply offsets in any direction or rotation. Different mates constrain different degrees of freedom. Here are three commonly used mates:
    - `Fasten`: Prevents any movement between two mate connectors, such as a bolt in a hole
    - `Revolute`: Allows rotational movement about the z-axis between two mate connectors (e.g. an arm pivot)
    - `Slider`: Enables linear movement along the z-axis between two mate connectors (e.g. an elevator)

??? Example "Example of a Fasten Mate"
    <center>
      <video width="1920" controls>
        <source src="\img\learning-course\stage1a\1a-fasten.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
    </center>

The best practices for constraining an assembly, along with other assembly tools like replicate, pattern, and standard content, will be learned through projects and described in more detail in later stages. They are also outlined in the [assembly best practices](../../best-practices/assembly-setup.md "Assembly Best Practices Page"){:target="_blank"} page.

!!! Warning "<span style="font-size: 0.8rem !important;">**DO NOT MOVE PAST THIS POINT UNTIL YOU HAVE COMPLETED THE LEARNING COURSE ABOVE**</span>"

<br>

### Exercise #3: Box Tube Frame
For this exercise, you will create a simple frame and two gussets in the part studio, then create an assembly and mate together all the components.

You will utilize the `Extrude Individual`, `Tube Converter`, and `Gusset` Featurescripts for this exercise.

- The `Gusset` Featurescript is an easy way to create gussets by selecting the locations of the holes the gusset should attach to.

**Navigate to the "Exercise #3 Structure" part studio tab** in your copied document and **follow the instructions in the slides** to complete the second exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s10.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s1.webp" style="width:100%">
      <figcaption>1. Start by sketching the tubes on the right plane.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s2.webp" style="width:100%">
      <figcaption>2. Use the <code>Extrude Individual</code> Featurescript to extrude the blocks.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s3.webp" style="width:100%">
      <figcaption>3. Use <code>Tube Converter</code> Featurescript to turn the blocks into 1/16" wall tubes with a 0.5" spacing pattern of 0.196" holes.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s4.webp" style="width:100%">
      <figcaption>4. Use the <code>Gusset</code> tool to create the top gusset by selecting the holes on the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s5.webp" style="width:100%">
      <figcaption>5. Use the <code>Gusset</code> tool to create the bottom gusset by selecting the holes on the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s6.webp" style="width:100%">
      <figcaption>6. Name the key sketches and parts. The materials will have already been set to 6061 Aluminum from the Featurescripts.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e3/e3s7.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>7. Insert the parts into the assembly by directly clicking on the green checkmark. Then, <code>Group</code> all the parts together. Finally, <code>fix</code> the bottom tube in place. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e3/e3s8.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>8. Copy and paste the gussets four times. Then, use the <code>Fasten</code> mate to attach the gussets to the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e3/e3s9.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>9. Some gussets may need to have their <code>Fasten</code> mate reoriented in order to properly line up. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s10.webp" style="width:100%">
      <figcaption>10. Finished assembly. </figcaption>
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

In this exercise, you were introduced to yet another highly useful Featurescript for creating gussets. Additionally, notice that we only model 1 of each type of gusset in the part studio. For the tubes, we choose to model all of the tubes even though the two vertical tubes are the same - this is to make assembly more parametric since the tube would otherwise be difficult to mate.

It should be noted that while fixing the tube is not considered an [assembly best practice](/best-practices/assembly-setup#origin-cube-method "Assembly Best Practices Page"){:target="_blank"} for setting the origin of an assembly, it is sufficient for the purposes of these exercises.

!!! note "Verification"
    If all is done correctly your assembly should have 12 Instances, and weigh approximately 1.946lbs.
                          
### Exercise #4: Climber Hook

As you get more comfortable with modeling, we can begin to create more complex parts. For this exercise, you will create a climber hook and tube. Then, you will create the assembly and mate together the components.

You will utilize the `Spacer` Featurescript for this exercise.

**Navigate to the "Exercise #4 Climber Hook" part studio tab** in your copied document and **follow the instructions in the slides** to complete the second exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e4/e4s10.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e4/e4s1.webp" style="width:100%">
      <figcaption>1. Start by sketching the tube on the right plane.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e4/e4s2.webp" style="width:100%">
      <figcaption>2. Use the <code>Tube</code> Featurescript to create a thin-wall 1"x1" tube with no holes.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e4/e4s3.webp" style="width:100%">
      <figcaption>3. Draw the climber hook sketch. The construction geometry circle represents the bar on which the hook will grab onto. The hole on the far right would be to attach a rope to pull the hook with. Pay attention to the sketch constraints used.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e4/e4s4.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Use the <code>Linear Pattern</code> sketch tool to pattern the mounting holes. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e4/e4s5.webp" style="width:100%">
      <figcaption>5. Make the hook 3/16" thick. Select <code>New</code> as the extrude type to make the extrude a new part.  </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e4/e4s6.webp" style="width:100%">
      <figcaption>6. Fillet the bottom two corners with a 0.25" radius.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e4/e4s7.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>7. Use the <code>Spacer</code> Featurescript to add a 0.5" diameter spacer. Use the `Up to Face` end condition to make the spacer match the tube width. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e4/e4s8.webp" style="width:100%">
      <figcaption>8. Use the <code>Use</code> sketch tool to add the mounting holes to the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e4/e4s9.webp" style="width:100%">
      <figcaption>9. Name the key sketches and parts. Set the material of the hook and spacer to 6061 Aluminum. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e4/e4s10.webp" style="width:100%">
      <figcaption>10. Finished assembly. </figcaption>
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

In this exercise, you practiced more advanced sketching and were introduced to the `Spacer` Featurescript. 

!!! note "Verification"
    If all is done correctly your assembly should have 5 Instances, and weigh approximately 0.56lbs.

## Summary

Congratulations on completing Stage 1A! Remember, practice is essential – the more CAD models you create, the more proficient and efficient you'll become. Using keyboard shortcuts can significantly accelerate your CAD workflow. Be attentive to best practices to avoid developing any bad habits. Keep up the good work!

Here is a quick summary of what you have achieved in 1A:

* Learned how to use the Onshape interface and basic sketching and modeling features with the OnShape Learning Center courses
* Learned how to model basic FRC structures
* Learned how to use the `Gusset`, `Extrude Individual`, `Tube Converter`, and `Spacer` Featurescripts
* Learned how to assemble basic models using `Group` and `Fasten`
* Learned about leveraging default geometry to enable easy symmetry with intelligently placed origins

In stage 1B, you will be introduced to power transmissions, which enable your robot to move and score. 
<!-- 
## Check for Comprehension Questions for 1A

Before moving on to the next stage, take a moment to check your understanding of the key concepts from 1A. Try answering the following questions:

!!! note "Note"
    Feel free to refer back to the guide, but try your best to do these on your own.

1.  What is the primary advantage of using construction geometry in sketches?
    1.  It makes the sketch look more professional
    2.  It helps convey design intent and makes parts more parametric
    3.  It automatically creates dimensions
    4.  It reduces file size

2. Which Featurescript is used to create tubes with specified wall thickness and hole patterns?
    1. Extrude Individual
    2. Gusset
    3. Tube Converter
    4. Spacer

3. In a multi-part Part Studio, what extrude type should you select when creating a new part?
    1. Add
    2. Remove
    3. New
    4. Intersect

4. What is the purpose of the `Group` function in assemblies?
    1. To color-code parts
    2. To restrict relative motion between parts
    3. To hide parts from view
    4. To create a bill of materials

5. Short Answer: Describe the process of creating a gusset using the Gusset Featurescript.

6. What is the advantage of using the `Fasten` mate in an assembly compared to using `Fix`?
    1. It's faster to apply
    2. It allows for more degrees of freedom
    3. It's more parametric and maintains relationships between parts
    4. It automatically aligns parts

7. Short Answer: Explain why it's generally better to model all unique parts in a Part Studio, even if some parts are identical (like the vertical tubes in Exercise 3).

8. Short Answer: Describe two ways that using Featurescripts can improve your CAD workflow efficiency.

##  Answer Key for 1A Comprehension Check Questions
??? note "Answer Key"

    1. b: It helps convey design intent and makes parts more parametric

    2. c: Tube Converter

    3. c: New

    4. b: To restrict relative motion between parts

    5. Key points:
        * Select Gusset tool
        * Choose attachment holes
        * Adjust parameters if needed
        * Confirm creation

    6. c: It's more parametric and maintains relationships between parts

    7. Key points:
        * Easier future modifications
        * Maintains design intent
        * Simplifies assembly
        * More parametric

    8. Key points:
        * Automate complex/repetitive tasks
        * Ensure consistency across designs -->

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


