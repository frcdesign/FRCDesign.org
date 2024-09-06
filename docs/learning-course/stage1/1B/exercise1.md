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

# 1B: Power Transmissions


## Practice Exercises
Time to practice! Start by **make a copy of the Stage 1B Exercises Document** through the button below, just like you did with the Stage 1A Exercises Document. Each exercise has a folder, a "reference" tab (a preview of what the final model should look like), and a tab or two for doing your exercise in. Solutions are also provided in the 1B Exercise Solutions Document to check your work afterwards.

<center>[1B Exercises Document](https://cad.onshape.com/documents/ce41613fac38db8c00e65020/w/a65651477167d5e36fe871c0/e/b31e08475df637b12d58f61e?renderMode=0&uiState=66cf9bde38437847c7b79c0c "1B Exercises Onshape Document"){:target="_blank" .md-button .md-button--primary }
[1B Exercise Solutions](https://cad.onshape.com/documents/c6a8ec29479a2578841fb9f2/w/85094b3baa15a05c873920c9/e/21fa04df80572c41ab64f27b "1B Exercise Solutions Onshape Document"){:target="_blank" .md-button .md-button--primary } </center>

## Exercise 1: Simple Gearbox 

In this exercise, you will be CADing and assembling a simple single stage gearbox. The goal of this exercise is to introduce how to model a very simple gear transmission. Additionally, you will learn how to use the the `Shaft` Featurescript, `Replicate` tool, MKCad parts library, and part configurations.

!!! Note
    Exercise 1 adds hardware (bolts and nuts) to the CAD models. You can read more about hardware standards on the [Design Handbook](/design-handbook/structure/fasteners/ "Design Handbook Fasteners Page"){:target="_blank"} page.

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
      <figcaption> 3. Create a new sketch for the motor plate. Using the layout as the reference, draw a 1.125" hole for the bearing and a 0.8" hole for the motor boss (the nub that sticks out from the motor). Note that depending on your manufacturing processes and tolerances, you may need to draw your bearing holes slightly larger or smaller than nominal (1.125"). </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s4.webp" style="width:100%">
      <figcaption> 4. Add two mounting holes for the motor. A good practice to constrain the holes is to draw and dimension a <it>bolt circle</it>, then draw the holes for the bolts on the bolt circle. This constrains the distance of the holes from the center of the motor with a single dimension. The bolt circle for the motor we are using is 2". </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s5.webp" style="width:100%">
      <figcaption>  5. Add the four bolt holes for connecting the two plates. Use a center rectangle to create the construction geometry so that only two dimensions are required to constrain the holes.    </figcaption>
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
      <figcaption> 8. Use the <code>Spacer</code> Featurescript to add a round 3/8" diameter, 5/8" long spacer. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e1/e1s9.webp" style="width:100%">
      <figcaption> 9. Create the outer plate sketch on the face of the spacer. Use the <code>Use</code> sketch tool to copy the geometry and holes of the motor plate, but add a round cutout at the top.</figcaption>
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
      <figcaption> 3. Assemble the motor and motor pinion gear using parts from the MKCad App. You will need to use mate inference locking to fasten the motor to the motor pinion: See the below drop down to learn how. </figcaption>
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

!!! note "Verification"
    If all is done correctly your assembly should have 19 Instances, and weigh approximately 2.3lb.


### Configurable Parts

In this exercise you made your first gearbox. In doing so, you also used part configurations - a powerful tool that allows for variations of the same part. The gears that you inserted from MKCad were configurable - you were able to easily change the tooth count of the gear without needing to inserting a new component. Try and use configurable parts when they are available to make your models more parametric.

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