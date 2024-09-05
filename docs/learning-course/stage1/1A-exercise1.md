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


## Box Tubes

In FRC, robot structures are typically constructed out of aluminum box tubing, similar to wood beams for a house. Aluminum box tubing is commonly found in 2"x1", 1"x1", and 2"x2" sizes with 1/8" (thickwall) or 1/16" (thinwall) wall thicknesses. Box tubing is typically referred to by its size, eg: 2x1, 1x1, and 2x2 (Spoken as "two-by-one", "one-by-one", and "two-by-two"). For the rest of the learning course, we will use this notation when referring to box tube.


???+ Example "Box Tube Example"
    <center><img src="\img\learning-course\stage1a\tube.webp" width="45%"> </center>

<br>

## Exercise #1: Simple Box Tube

For this exercise, you will be modeling a simple 2x1 with some holes in it. For this exercise, do not use any Featurescripts. 

### Instructions

**Navigate to the "Exercise #1 Box Tube" tab** in your copied document and **follow the instructions in the slides** to complete your first exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure markdown="span">
      <img src="/img/learning-course/stage1a/exercises/e1/e1s0.webp" style="width:100%; data-description="0. The final part"">
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
      <figcaption>5. Extrude the top holes to cut all the way through the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e1/e1s6.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>6. Add the side holes. Create the layout for the side holes by creating a center point rectangle and turning it into construction geometry. Again, having the origin at the center of the tube lets us place the center of the pattern at the center of the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e1/e1s7.webp" style="width:100%; data-description="6. Name the key sketches and part. Set the material to be 6061 Aluminum."">
      <figcaption>7. Extrude the side holes to cut all the way through the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e1/e1s8.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>8. Name the key sketches and part. You can set part appearances and materials by right clicking on the part instance. Set the material to be 6061 Aluminum. To see the mass of parts, use the <code>Display Mass Properties</code> Menu </figcaption>
    </figure>
  </div>


  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e1/e1s0.webp" style="width:100%; data-description="6. Name the key sketches and part. Set the material to be 6061 Aluminum."">
      <figcaption>9. Finished Part Studio. </figcaption>
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
    If you did everything correctly your box tube should weigh about 0.35lbs

Notice how we utilized construction geometry to define the location of the holes on the 2" face of the tube. Using construction geometry to assist with sketching makes your parts more parametric and betters conveys design intent compared to manually specifying the location of each hole with dimensions.

!!! Note
    Some sketches and features have been renamed (i.e. "Tube Profile"). You can rename sketches and features by hovering over the name in the dialogue box and clicking the pencil icon, or right clicking a sketch or feature in the feature list and clicking "rename". 

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


