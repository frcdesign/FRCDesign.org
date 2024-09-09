<style>
* {box-sizing:border-box}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

.mySlides {
    display:none;
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

# 1D: Subsystem Workflow - Detailing the Drivebase

## Exercise: Bumpers
Bumper construction is described in each year’s FRC game manual. Typically, it is required to be two 2.5” diameter pool noodles backed by a 5” tall 3/4" thick plywood sheet. Refer to the latest game manual for the most up to date bumper rules. Bumper cutout and ground clearance rules will vary from year to year.

### Bumper Model
It is recommended to place the bumpers in a new part studio and assembly to keep your feature and assembly trees organized. The minimum level of detail should be a block model of the bumper. Some teams may opt to model the bumper wood, bumper wood holes, angle brackets for the bumper wood, and other details to assist with manufacturing. You should communicate with the rest of your team members to determine the level of detail that is required. 

### Instructions

**Add bumpers to your Stage 1C drivetrain.** You can take inspiration from the following instructions slides.

<!-- <center>**Sample Bumper Modeling Slides**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">
    <!-- Full-width images with number and caption text -->
    <div id="slide1" class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s0.webp" style="width:100%">
            <figcaption>0. Finished bumpers assembly inserted into drivetrain assembly. </figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s1.webp" style="width:100%">
            <figcaption>1. Create a new sketch in the Master Sketch part studio with the bumper profile. A 3/4" ground clearance and 1/4" gap between the bumper and frame is recommended.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s2.webp" style="width:100%">
            <figcaption>2. Create a new part studio in the drivetrain folder for the bumpers. Insert the Origin Cube and derive the drivetrain and bumper sketches from the Master Sketch.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s3.webp" style="width:100%">
            <figcaption>3. Sweep the bumper profile along the edges of the drivetrain top layout sketch to create the block model of the bumpers.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s4.webp" style="width:100%">
            <figcaption>4. Optionally add a fillet on the corners. Size it according to how your team wraps the bumper pool noodles.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s5.webp" style="width:100%">
            <figcaption>5. Optionally model the wood for the bumpers. This can be useful for manufacturing purposes.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s6.webp" style="width:100%">
            <figcaption>6. Create a bumper assembly in the drivetrain folder and insert all the components. Don’t forget to group all the components and mate the origin cube mate connector to the origin.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/bumpers/bumper1s0.webp" style="width:100%">
            <figcaption>7. Insert the bumper assembly into the drivetrain assembly.</figcaption>
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

Keeping the bumper part studio and assembly separate from the drivetrain keeps the drivetrain feature tree cleaner and allows for easier hiding/showing of the bumpers in the top level assembly since you can show and hide the entire bumper assembly at once.




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