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

# 1E: Practice Mechanisms

Starting with exercise 5, only an outline of the design process and key details will be provided to you. This is to prepare you for stage 2, where the exercises are less guided.

Focus on capturing design intent and maintaining best practices in your part studios and assemblies. Follow the workflow of the solution document.

## Exercise 5: Flipped Gearbox

In this exercise, you will be modeling a two motor, two-stage, flipped gearbox. The reason these types of gearboxes are referred to as flipped "flipped" is because the output points in the opposite direction as the input motors. 
This style of gearbox can be desired in some situations to meet packaging constraints.

### Part Studio Instructions

**Navigate to the "Exercise #5 Part Studio" tab** in your copied document and **refer to the solution document** to complete the part studio for this exercise. The **following instructions slides** only provide a general outline and some key details.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flipped-gb/s0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flipped-gb/s1.webp" style="width:100%">
      <figcaption>1. Start by modeling the tube that the gearbox mounts on.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flipped-gb/s2.webp" style="width:100%">
      <figcaption>2. Create the layout sketch on the tube face. Remember to only include essential information in the layout sketch. In this case, only the gear PD's and motor OD's are required. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flipped-gb/s3.webp" style="width:100%">
      <figcaption>3. Sketch the outer plate. We only require two bolts to hold the motor on and choose the two holes that form a line perpendicular to the c-c line between the motor pinion and the gear. This ensures that the motor bolts will be accessible at all times.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flipped-gb/s4.webp" style="width:100%">
      <figcaption>4. When sketching the inner plate, verify that there is clearance between the motor and the inner plates. Pay close attention to the tangency of all the edges so that the plate contour is smooth.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flipped-gb/s0.webp" style="width:100%">
      <figcaption>5. Model the shafts and pocket the gearbox plates. For the shafts, you can first estimate how long they need to be and then set them to the correct length after you complete the assembly.</figcaption>
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

**Next, navigate to the "Exercise #5 Assembly" tab** in your copied document and **refer to the solution document** to complete the assembly for this exercise. The **following instruction slides** only provide a general outline and some key details.

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flipped-gb/a0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flipped-gb/a1.webp" style="width:100%">
      <figcaption>1. Add the frame, gearbox plates, gearbox spacer, and shafts to the assembly. Like before, group mate the rigid components with the Origin Cube and mate the Origin Cube to the assembly origin.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flipped-gb/a2.webp" style="width:100%">
      <figcaption>2. Insert and fasten the motors and bearings.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flipped-gb/a3.webp" style="width:100%">
      <figcaption>3. Insert and fasten the power transmission components, which includes the gears, pinions, spacers, and sprocket. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flipped-gb/a4.webp" style="width:100%">
      <figcaption>4. Finally, insert and replicate all the required fasteners.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flipped-gb/a5.webp" style="width:60%">
      <figcaption>5. We use a single 1/2" spacer rather than two 1/4" spacers on each side of the gear to reduce part count. In real life, it's much easier to assemble if there's only one spacer, and centering the gear between the bearings has no tangible benefit. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1e/flipped-gb/a6.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>6. Check that the motors do not interfere with the inner plate with the <code>Check Interference</code> tool.</figcaption>
    </figure>
  </div>

  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flipped-gb/a0.webp" style="width:100%">
      <figcaption>7. To finish the assembly, organize your components into folders and name your replicates.</figcaption>
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
    If all is done correctly your assembly should have 30 Instances.

### Interference Detection

Catch errors in the CAD rather than in real life! Always double and triple check your CAD models for mistakes like interferences. An extra 10 minutes verifying the correctness of your CAD can save you hours of rework if an erroneous part slips through and is fabricated.

!!! warning "Interference Detection"
    If an interference is detected with the Check Interference tool, it will highlight the intersected volumes in red.
    <figure>
      <img src="/img/learning-course/stage1e/flipped-gb/interference.webp" style="width:100%">
      <figcaption>Interference between a motor and plate detected by the Check Interference tool.</figcaption>
    </figure>

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