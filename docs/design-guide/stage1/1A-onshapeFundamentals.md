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


# 1A: Onshape Fundamentals

<span class="left">[< 0D: Theory](../stage0/0D-theory.md)</span> <span class="right">[1B: Design Methodology >](1B-designMethodology.md)</span>
<br>

Welcome to Stage 1! Here, you'll engage in a series of Onshape exercises and projects designed to introduce and develop your CAD skills within an FRC context. Should you have any questions, feel free to ask on the Discord!

## Learning Center Courses

[Onshape's Learning Center](https://learn.onshape.com/) provides free learning courses and articles covering everything from document navigation and sketching to advanced surface and sheet metal modeling. It's a valuable resource for both novice and seasoned users alike.

Please complete these courses on the learning center to learn the fundamentals of Onshape CAD. 

- [Introduction to Parametric Feature-Based CAD](https://learn.onshape.com/courses/introduction-to-parametric-feature-based-cad)
- [Introduction to Part Design](https://learn.onshape.com/courses/introduction-to-part-design) 
- [Introduction to Assembly Design](https://learn.onshape.com/courses/introduction-to-assembly-design)
- [Introduction to Sketching](https://learn.onshape.com/courses/introduction-to-sketching)
- [Part Design Using Part Studios](https://learn.onshape.com/courses/fundamentals-part-design-using-part-studios)
- [Multi-Part Part Studios](https://learn.onshape.com/courses/fundamentals-multi-part-part-studios)
- [Onshape Assemblies](https://learn.onshape.com/courses/fundamentals-onshape-assemblies)


The structure of the courses includes some short videos and practice models, expected time is 2-4 hours.

Additionally, the [Onshape Help](https://cad.onshape.com/help/Content/EnterpriseHelp/Content/home.htm?tocpath=Welcome%20to%20Onshape%20Help%7C_____0) site is a great resource to use if you are unsure how a specific feature of Onshape works. 

!!! Warning
    The Onshape learning courses are important as they will teach you the Onshape interface and form a basic foundation for CAD skills. Unless you have prior experience using Onshape, you should not skip the learning courses as the 1A exercises assume that you have an understanding of CAD basics.

## Multi-Part Modeling

As introduced in the Onshape learning courses, Onshape is a software focused on multi-body modeling. In FRC, this usually means one part studio per subsystem. Check out [this page](../../best-practices/sub-document-setup.md) to learn more about best practices for sub-documents. The following practice exercises will help you reinforce these concepts.

Here's an example of a subsystem part studio. Notice how there's one instance of each unique part within this part studio. The part studio also resembles the completed product, as the parts are modeled relative to each other.

<center><img src="\img\design-guide\stage1a\1a-PartStudio.webp" width="45%"></center>
<center> *Example of a part studio.* </center>

## Assemblies

Assembling is the basic function of defining the position and motion of parts in an assembly.

As was introduced in the Onshape learning tutorials, when parts are inserted into an assembly, they free float. We can utilize a number of different assembly tools to constrain the motion of all the parts:

- **`Group`**: Restricts the relative motion between a group of parts.
- **`Fix`**: Locks a part in place within the assembly. (Not recommended as it's not parametric.)
- **`Mates`**: Tools to constrain the degrees of freedom between parts using "mate connectors." These connectors are automatically generated or manually created coordinate systems on parts. You can align the axes and apply offsets in any direction or rotation. Different mates constrain different degrees of freedom. Here are three commonly used mates:
    - `Fasten`: Prevents any movement between two mate connectors, such as a bolt in a hole.
    - `Revolute`: Allows rotational movement about the z-axis between two mate connectors, like an arm pivot. Eg: An arm pivot.
    - `Slider`: Enables linear movement along the z-axis between two mate connectors. Eg: An elevator.

<center><img src="\img\design-guide\stage1a\1a-fasten.gif"width="80%"></center>
<center> *Example of a fasten mate.* </center>

The best practices for constraining an assembly, along with other assembly tools like replicate, pattern, and standard content, will be learned through projects. Assembly best practices are outlined [here](../../best-practices/assembly-setup.md) and will be discussed in more detail in later stages.

## Practice Exercises
Now lets practice! Make a copy of the [Stage 1A Exercises Document](https://cad.onshape.com/documents/812b2974ed32b9c89e8f1e25/w/747e47444b6c685bd0bee334/e/58894354f0152cd6485fe45e?renderMode=0&uiState=663d81b7afce5246f0309e28). For each exercise, the final reference is available to you. Solutions are available [here](https://cad.onshape.com/documents/1bdaed8e23446ffe70a851a4/w/37cd1a4984497b01d74e4c41/e/fd6796321fb9611305e5ff7d?renderMode=0&uiState=663d81d5d060d67d3cd48855).

### Exercise 1: Simple Box Tube
In FRC, robot structures are typically constructed out of aluminum box tubing, similar to wood beams for a house. Aluminum box tubing is commonly found in 2"x1", 1"x1", and 2"x2" sizes with 1/8" (thickwall) or 1/16" (thinwall) wall thicknesses. Box tubing is typically referred to by its size, eg: 2x1, 1x1, and 2x2 (Spoken as "two-by-one", "one-by-one", and "two-by-two"). For the rest of the design-guide, we will use this notation when referring to box tube.

Here's an example of an aluminum box tube structure on a robot:

<center><img src="\img\design-guide\stage1a\tube.webp" width="45%"> </center>
<center> *Example of a 2x1 box tube.* </center>

For exercise 1, you will be modeling a simple 2x1 with some holes in it. For this exercise, do not use any Featurescripts.

<center>**Exercise 1 Instruction Slides**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e1/e1s6.webp" style="width:100%">
      <figcaption>0. The final part.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e1/e1s1.webp" style="width:100%">
      <figcaption>1. Start by sketching a center rectangle on the top plane.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e1/e1s2.webp" style="width:100%">
      <figcaption>2. Extrude the rectangle symmetrically, 2" tall.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e1/e1s3.gif" style="width:100%">
      <figcaption>3. Shell the block to turn it into a 1/16" wall tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e1/e1s4.gif" style="width:100%">
      <figcaption>4. Add the top holes. Set the centerpoint of the hole to be vertical with the midpoint of the bottom line, then Mirror the hole across, using the front plane as the mirror line. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e1/e1s5.gif" style="width:100%">
      <figcaption>5. Add the side holes. Create the layout for the side holes by creating a center point rectangle and turning it into construction geometry. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e1/e1s6.webp" style="width:100%">
      <figcaption>6. Name the key sketches and part. Set the material to be 6061 Aluminum. </figcaption>
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

If all is correct, the final mass of the part should be 0.350 lb.

Notice how we utilized construction geometry to define the location of the holes on the 2" face of the tube. Using construction geometry to assist with sketching makes your parts more parametric and betters conveys design intent compared to manually specifying the location of each hole with dimensions.

### Exercise 2: Box Tube and Gusset Joint
For this exercise, you will design two tubes and a part called a "gusset". A gusset is the flat part that connects the two tubes. This gusset will be created in the same part studio as the tubes that it is connecting! Here's an example of a gusset:

<center><img src="\img\design-guide\stage1a\8033-000-2024C_8.png" width="45%"> </center>
<center> *Example of a gusset.* </center>

You will utilize the `Extrude Individual` and `Tube Converter` Featurescripts for this exercise. Do not use the `Gusset` Featurescript for this exercise.

The `Extrude individual` Featurescript enables you to extrude sketch regions without merging them. In this exercise, if you were to extrude the sketch of the tubes with the standard <code>Extrude</code> tool, only a single part would generate.

The `Tube Converter` Featurescript condenses the steps of shelling, sketching and dimensioning holes, and extruding holes into a single, customizable feature to easily model tubes. 

!!! Tip
    When extruding a sketch in a part studio, you can decide whether to "add" to existing geometry, or to create a "new" part. Make sure that when you extrude your gusset, you tell Onshape to create a new part.

<center>**Exercise 2 Instruction Slides**</center>

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e2/e2s11.webp" style="width:100%">
      <figcaption>0. The finished parts.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e2/e2s1.webp" style="width:100%">
      <figcaption>1. Start by sketching the tubes on the right plane.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e2/e2s2.webp" style="width:100%">
      <figcaption>2. Use the <code>Extrude Individual</code> Featurescript to extrude the blocks. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e2/e2s3.webp" style="width:100%">
      <figcaption>3. Use <code>Tube Converter</code> Featurescript to turn the blocks into 1/16" wall tubes with a 0.5" spacing pattern of 0.196" holes.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e2/e2s4.webp" style="width:100%">
      <figcaption>4. Draw a triangle with construction geometry for the gusset. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e2/e2s5.webp" style="width:100%">
      <figcaption>5. Dimension the triangle to be 0.5" away from the edges of the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e2/e2s6.webp" style="width:100%">
      <figcaption>6. Use the <code>Offset Entities</code> tool to offset the construction geometry 0.25". This will be the outline of the gusset. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e2/e2s7.webp" style="width:100%">
      <figcaption>7. Use the <code>Sketch Fillet</code> tool to add a 0.25" fillet to the three corners of the gusset. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e2/e2s8.webp" style="width:100%">
      <figcaption>8. Delete the three points left over from the fillet. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e2/e2s9.webp" style="width:100%">
      <figcaption>9. Use the <code>Use (Project/Convert)</code> tool to project the tube holes onto the gusset sketch. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e2/e2s10.webp" style="width:100%">
      <figcaption>10. Extrude the gusset to be 1/8" thick. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e2/e2s11.webp" style="width:100%">
      <figcaption>11. Name the key sketches and parts. Set the material to be 6061 Aluminum. </figcaption>
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

If all is correct, the final mass of the parts should be 0.270 lb.

In this exercise, you can see the power of Featurescripts. What would have been a number of sketches, extrudes, and shells to create the tubes is packaged into a single, easy to use custom feature. 

### Exercise 3: Box Tube Frame
For this exercise, you will create a simple frame and two gussets. Then, you will create an assembly and mate together all the components.

You will utilize the `Extrude Individual`, `Tube Converter`, and `Gusset` Featurescripts for this exercise.

The `Gusset` Featurescript is an easy way to create gussets by selecting the locations of the holes the gusset should attach to.

<center>**Exercise 3 Instruction Slides**</center>

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e3/e3s10.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e3/e3s1.webp" style="width:100%">
      <figcaption>1. Start by sketching the tubes on the right plane.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e3/e3s2.webp" style="width:100%">
      <figcaption>2. Use the <code>Extrude Individual</code> Featurescript to extrude the blocks.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e3/e3s3.webp" style="width:100%">
      <figcaption>3. Use <code>Tube Converter</code> Featurescript to turn the blocks into 1/16" wall tubes with a 0.5" spacing pattern of 0.196" holes.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e3/e3s4.webp" style="width:100%">
      <figcaption>4. Use the <code>Gusset</code> tool to create the top gusset by selecting the holes on the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e3/e3s5.webp" style="width:100%">
      <figcaption>5. Use the <code>Gusset</code> tool to create the bottom gusset by selecting the holes on the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e3/e3s6.webp" style="width:100%">
      <figcaption>6. Name the key sketches and parts. The materials will have already been set to 6061 Aluminum from the Featurescripts.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e3/e3s7.gif" style="width:100%">
      <figcaption>7. Insert the parts into the assembly by directly clicking on the green checkmark. Then, <code>Group</code> all the parts together. Finally, <code>fix</code> the bottom tube in place. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e3/e3s8.gif" style="width:100%">
      <figcaption>8. Copy and paste the gussets four times. Then, use the <code>Fasten</code> mate to attach the gussets to the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e3/e3s9.gif" style="width:100%">
      <figcaption>9. Some gussets may need to have their <code>Fasten</code> mate reoriented in order to properly line up. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e3/e3s10.webp" style="width:100%">
      <figcaption>10. Finished assembly. </figcaption>
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

If all is correct, the final mass of the assembly should be 1.946 lb.

In this exercise, you were introduced to yet another highly useful Featurescript for creating gussets. Additionally, notice that we only model 1 of each type of gusset in the part studio. For the tubes, we choose to model all of the tubes even though the two vertical tubes are the same - this is to make assembly more parametric since the tube would otherwise be difficult to mate.

It should be noted that while fixing the tube is not considered an [assembly best practice](/best-practices/assembly-setup#origin-cube-method) for setting the origin of an assembly, it is sufficient for the purposes of these exercises.

### Exercise 4: Climber Hook

As you get more comfortable with modeling, we can begin to draw more complex parts. For this exercise, you will create a climber hook and tube. Then, you will create the assembly and mate together the components.

You will utilize the `Spacer` Featurescript for this exercise.

<center>**Exercise 4 Instruction Slides**</center>

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e4/e4s10.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e4/e4s1.webp" style="width:100%">
      <figcaption>1. Start by sketching the tube on the right plane.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e4/e4s2.webp" style="width:100%">
      <figcaption>2. Use the <code>Tube</code> Featurescript to create a thin-wall 1"x1" tube with no holes.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e4/e4s3.webp" style="width:100%">
      <figcaption>3. Draw the climber hook sketch. The construction geometry circle represents the bar on which the hook will grab onto. The hole on the far right would be to attach a rope to pull the hook with. Pay attention to the sketch constraints used.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e4/e4s4.gif" style="width:100%">
      <figcaption>4. Use the <code>Linear Pattern</code> sketch tool to pattern the mounting holes. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e4/e4s5.webp" style="width:100%">
      <figcaption>5. Make the hook 3/16" thick. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e4/e4s6.webp" style="width:100%">
      <figcaption>6. Fillet the bottom two corners with a 0.25" radius.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e4/e4s7.gif" style="width:100%">
      <figcaption>7. Use the <code>Spacer</code> Featurescript to add a 0.5" diameter spacer. Use the `Up to Face` end condition to make the spacer match the tube width. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e4/e4s8.webp" style="width:100%">
      <figcaption>8. Use the <code>Use</code> sketch tool to add the mounting holes to the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e4/e4s9.webp" style="width:100%">
      <figcaption>9. Name the key sketches and parts. Set the material of the hook and spacer to 6061 Aluminum. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e4/e4s10.webp" style="width:100%">
      <figcaption>10. Finished assembly. </figcaption>
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

If all is correct, the final mass of the assembly should be 0.560 lb.

### Exercise 5: Two Stage Gearbox

In this exercise, you will be CADing and assembling a two stage gearbox. The layout of the gearbox is already done, you just need to finish drawing the plate, model the spacers and shafts, and put together the assembly. Don't worry too much about the design aspect of the gearbox right now, you'll learn more about it Stage 1C.

The goal of this exercise is to introduce the `Shaft` and `Vent` Featurescripts, `Replicate` tool, MKCad parts library, part configurations, practice more complex sketches, and practice mating together larger assemblies.
<center>**Exercise 5 Instruction Slides**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e5/e5s14.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e5/e5s1.webp" style="width:100%">
      <figcaption>1. This is the layout sketch of the gearbox, it has been drawn for you already. The layout sketch models where the motors and gears will go and how the gears should mesh. You'll learn more about this in Stage 1C.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e5/e5s2.webp" style="width:100%">
      <figcaption>2. Open the "Finish This!" sketch and finish the plate. You can utilize the <code>Mirror</code> sketch tool to mirror the geometry from the left side to the right side. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e5/e5s3.webp" style="width:100%">
      <figcaption>3. Extrude the plate to be 1/4" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e5/e5s4.webp" style="width:100%">
      <figcaption>4. Use the <code>Spacer</code> Featurescript to create the gearbox spacer. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e5/e5s5.gif" style="width:100%">
      <figcaption>5. Use the <code>Shaft</code> Featurescript to create the first stage shaft. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e5/e5s6.webp" style="width:100%">
      <figcaption>6. Use the <code>Shaft</code> Featurescript to create the output shaft.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e5/e5s7.webp" style="width:100%">
      <figcaption>7. Create a sketch on the face of the plate and draw the lines for the pocketing ribs. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e5/e5s8.gif" style="width:100%">
      <figcaption>8. Use the <code>Vent</code> Featurescript to pocket the plate by selecting the sketch regions created by the previous sketch. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e5/e5s9.webp" style="width:100%">
      <figcaption>9. Name the key sketches and parts. Set the material of the plate and spacers to 6061 Aluminum. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e5/e5s10.gif" style="width:100%">
      <figcaption>10. Insert the assembly and only fix the gearbox plate. Mate the spacer to the plate. Then, use the <code>Replicate</code> tool to replicate the spacer and its associated mate onto the other spacer locations. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e5/e5s11.webp" style="width:100%">
      <figcaption>11. Copy the gearbox plate and mate it into place. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <li class="slideVideo">
      <video width="1920" controls>
        <source src="/img/design-guide/stage1a/exercises/e5/e5s12.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>12. Assemble the bearings, shafts, motor, and motor pinion gear using parts from the MKCad App. </figcaption>
    </li>
  </div>

  <div class="mySlides fade">
    <li class="slideVideo">
      <video width="1920" controls>
        <source src="/img/design-guide/stage1a/exercises/e5/e5s13.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>13. Assemble the spacers and gears using parts from the MKCad App. </figcaption>
    </li>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1a/exercises/e5/e5s14.webp" style="width:100%">
      <figcaption>13. Finished assembly. </figcaption>
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


Congratulations on completing Stage 1B! Remember, practice is essential – the more CAD models you create, the more proficient and efficient you'll become. Using keyboard shortcuts can significantly accelerate your CAD workflow. Be attentive to best practices to avoid developing any bad habits. Keep up the good work!

So far, you've been introduced to Onshape CAD modeling and the top-down master sketch design methodology. In Stage 1C, you'll explore how to design mechanisms and how to do the math to make your robot work!

<br>
<center>1A: Fundamentals</center> 
<span class="left">[< 0D: Theory](../stage0/0D-theory.md)</span> <span class="right">[1B: Design Methodology >](1B-designMethodology.md)</span>
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


