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
                          
## Exercise #4: Climber Hook

As you get more comfortable with modeling, we can begin to create more complex parts. For this exercise, you will create a climber hook and tube. Then, you will create the assembly and mate together the components.

You will utilize the `Spacer` Featurescript for this exercise.

### Instructions

**Navigate to the "Exercise #4 Climber Hook" part studio tab** in your copied document and **follow the instructions in the slides** to complete the exercise.

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
  <button class="prev" onclick="plusSlides(-1,0)" style="background-color: #000; color: #fff;">&#10094;</button>
  <button class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</button>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

!!! success "Verification"
    If all is done correctly your assembly should have 5 Instances, and weigh approximately 0.56lbs.

In this exercise, you practiced more advanced sketching and were introduced to the `Spacer` Featurescript. 



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


