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
  background-color: rgba(0,0,0,0.8);
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

<span class="left">[< 0D: Theory](../stage0/0D-theory.md)</span> <span class="right">[1B: Swerve Drivebase >](1B-swerveDrivebase.md)</span>
<br>

Welcome to Stage 1! Here, you'll engage in a series of Onshape exercises and projects designed to introduce and develop your CAD skills within an FRC context. Should you have any questions, feel free to ask on the Discord!


!!! Note
    If you have a prior experience using Onshape, you can skip the learning courses and jump straight to the 1A exercises. Otherwise, please do the learning courses first as they will teach you the Onshape interface and form the basic foundation for CAD skills.

## Learning Center Courses

[Onshape's Learning Center](https://learn.onshape.com/) provides free learning courses and articles on how to use Onshape, from document navigation and sketching all the way to advanced surface and sheet metal modeling. This is a great resource to reference for both new and experienced users.

Please complete these courses on the learning center to learn the fundamentals of Onshape CAD. 

- [Introduction to Parametric Feature-Based CAD](https://learn.onshape.com/courses/introduction-to-parametric-feature-based-cad)

- SKIP? [Introduction to Part Design](https://learn.onshape.com/courses/introduction-to-part-design) 
- SKIP? [Introduction to Assembly Design](https://learn.onshape.com/courses/introduction-to-assembly-design)

- [Introduction to Sketching](https://learn.onshape.com/courses/introduction-to-sketching)
- [Part Design Using Part Studios](https://learn.onshape.com/courses/fundamentals-part-design-using-part-studios)
- [Multi-Part Part Studios](https://learn.onshape.com/courses/fundamentals-multi-part-part-studios)
- [Onshape Assemblies](https://learn.onshape.com/courses/fundamentals-onshape-assemblies)

!!! Note
    The structure of the courses includes a few short videos and a practice models, expected time is # hours.

## Multi-Part Modeling

<span style="color: red;">The below text is pretty awful, need to fix.</span>  

When designing in Onshape, you typically have 1 part studio per subassembly. Take a look at [this page](../../best-practices/sub-document-setup.md) to learn more about sub-document best practices. The following practice exercises will allow you to practices these concepts. 

Here is an example of one of the future projects that you’ll be working on. Notice how there are multiple parts inside of this one part studio, and how it “almost” looks like the completed product.

<center><img src="\img\design-guide\stage1a\1a-PartStudio.webp" width="45%"></center>
<center> *Example of a part studio.* </center>

## Assemblies
<span style="color: red;">The below text is pretty awful, need to fix.</span> 

Assembling is the basic function of defining the position and motion of parts in an assembly.

When parts are inserted into an assembly, they free float. They can drag them around. The goal of assembling is to constrain the motion of all parts. There are few different ways to do this:

- **`Group`**: Limits the relative motion between a group of parts to none
- **`Fix`**: Fixes a part in space in the assembly (not recommended as it is not parametric)
- **`Mates`**: Tools to limit degrees of freedom between parts using "mate connectors", which are automatically generated (or manually created) coordinate systems on parts. You can align the axes and offset in any direction or rotation you want. Different types of mates constrain different degrees of freedom. Three commonly used mates are described below:
    - `Fasten`: The *fasten* mate does not allow any movement between two mate connectors. Eg: A bolt to a hole.
    - `Revolute`: The *revolute* mate only allows rotational movement along the z-axis between two mate connectors. Eg: An arm pivot.
    - `Slider`: The *slider* mate only allows linear movement along the z-axis between two mate connectors. Eg: An elevator.

<center><img src="\img\design-guide\stage1a\1a-fasten.gif"width="80%"></center>
<center> *Example of a fasten mate.* </center>

The best practices for constraining an assembly as well as other tools used for assembly, such as replicate, pattern, standard content, etc. will be discovered through the projects. Assembly best practices are also defined [here](../../best-practices/assembly-setup.md).


## Practice Exercises
Now lets practice! Make a copy of the [Fundamentals Exercises Document](link here). For each exercise, the final reference is available to you. Solutions are available [here](Link to solutions).

### Exercise 1: Simple Box Tube
For exercise 1, you will be modeling a 2x1 tube with some holes in it. For this exercise, do not use any Featurescripts.

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

If all is correct, the final weight of the part should be 0.350 lb.

### Exercise 2: Box Tube and Gusset Joint
For this exercise, you will design two tubes and a part called a "gusset", which connects the two tubes. This gusset will be created in the same part studio as the tubes that it is connecting! Here's an example of a gusset:

<center><img src="\img\design-guide\stage1a\8033-000-2024C_8.png" width="45%"> </center>
<center> *Example of a gusset.* </center>

You will utilize the `Extrude Individual` and `Tube Converter` Featurescripts for this exercise. Do not use the `Gusset` Featurescript for this exercise.

!!! Tip
    When extruding a sketch in a part studio, you can decide whether to "add" to existing geometry, or to create a "new" part. Make sure that when you extrude your gusset, you tell Onshape to create a new part.

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
      <figcaption>2. Use the <code>Extrude Individual</code> Featurescript to extrude the blocks.</figcaption>
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

If all is correct, the final weight of the parts should be 0.270 lb

### Exercise 3: Box Tube Frame
For this exercise, you will create a simple frame and two gussets. Then, you will create an assembly and mate together all the components.

You will utilize the `Extrude Individual`, `Tube Converter`, and `Gusset` Featurescripts for this exercise.

!!! Note
    Learning Objectives thing? idk

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

If all is correct, the final weight of the assembly should be 1.946 lb.

It should be noted that while fixing the tube is not considered an [assembly best practice](/best-practices/assembly-setup#origin-cube-method) for setting the origin of an assembly, it is sufficient for the purposes of these exercises.

### Exercise 4: Climber Hook

As you get more comfortable with modeling, we can begin to draw more complex parts. For this exercise, you will create a climber hook and tube. Then, you will create the assembly and mate together the components.

You will utilize the `Spacer` Featurescript for this exercise.

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

If all is correct, the final weight of the assembly should be 0.560 lb.

<br>
<center>1A: Fundamentals</center> 
<span class="left">[< 0D: Theory](../stage0/0D-theory.md)</span> <span class="right">[1B: Swerve Drivebase >](1B-swerveDrivebase.md)</span>
<br>
<br>




<!-- ------------------DO NOT TOUCH ANYTHING BELOW HERE------------------ -->

<script>
// Initialize slide index for each slideshow
let slideIndices = [];

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

window.onload = function() {
  // Automatically generate dots based on the number of slides
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
}
</script>


