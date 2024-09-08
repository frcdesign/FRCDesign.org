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

## Exercise #2: Box Tube and Gusset Joint

For this exercise, you will design two box tubes attached together with a gusset. This gusset will be created in the same part studio as the tubes that it is connecting!

### Gussets

Aluminum box tubes are commonly connected together with 'gussets'. A gusset is a flat plate that, when attached to both tubes, helps create rigidity in the structure. 

!!! Example "Gusset Example"
    <figure>
    <center><img src="\img\learning-course\stage1a\8033-000-2024C_8.png" width="70%"> </center>
    <figcaption> A gusset connecting two tubes on a robot. </ficaption>
    </figure>

<br>

### Featurescripts

!!! Warning
    If you haven't already, please add [MKCAD](../../../stage0/0B/MKCad/ "Adding MKCAD Tutorial Page"){:target="_blank"} and the [required featurescripts](../../../stage0/0B/featurescripts/ "Stage 0 Featurescripts Page"){:target="_blank"} for the learning course.

You will utilize the [`Extrude Individual` and `Tube Converter` Featurescripts](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Julia's Featurescripts Onshape Document"){:target="_blank"} for this exercise. **Do not use the `Gusset` Featurescript for this exercise.**


- The `Extrude individual` Featurescript enables you to extrude sketch regions without merging them. In this exercise, if you were to extrude the sketch of the tubes with the standard <code>Extrude</code> tool, only a single part would generate.

- The `Tube Converter` Featurescript condenses the steps of shelling, sketching and dimensioning holes, and extruding holes into a single, customizable feature to easily model tubes. 


### Instructions

???+ Warning "Creating New Parts"
    When extruding a sketch in a part studio, you can decide whether to `Add` to existing geometry, or to create `New` geometry. `New` creates a new body, whereas `Add` will merge the feature with existing parts. Make sure that when you extrude your gusset, you tell Onshape to create a new part.
    <center><img src="\img\learning-course\stage1a\1a-merge.png" width="20%"></center>
    <center> *The different options for extruding* </center>

**Navigate to the "Exercise #2 Gusset" tab** in your copied document and **follow the instructions in the slides** to complete the exercise.

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
  <button class="prev" onclick="plusSlides(-1,0)" style="background-color: #000; color: #fff;">&#10094;</button>
  <button class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</button>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

!!! success "Verification"
    If all is done correctly your parts should weigh a combined 0.27lbs

In this exercise, you can begin to see the power of Featurescripts. What would have been a number of sketches, extrudes, and shells to create the tubes is packaged into a single, easy to use custom feature. 


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


