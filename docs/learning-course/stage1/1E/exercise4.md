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

## Exercise 4: Telescoping Hook

In this exercise, you will be modeling a telescoping climber. This mechanism features WCP telescoping bearing blocks and half-pocketed MAXPlanetary mounting gearbox plates. Be sure to pay attention to hook and gearbox sketches when modeling. 

### Part Studio Instructions

**Navigate to the "Exercise #4 Part Studio" tab** in your copied document and **follow the instructions in the slides** to complete the part studio for this exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/s0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/s1.webp" style="width:100%">
      <figcaption>1. Begin by creating a side profile sketch of the telescope tubes on the right plane.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/s2.webp" style="width:100%">
      <figcaption>2. Use two extrudes to create the solid bodies for the tubes. Then, use the Tube Converter Featurescript to convert the solid bodies into two thin-wall tubes with no hole pattern.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/s3.webp" style="width:100%">
      <figcaption>3. Add the holes for the WCP bearing blocks to the inner and outer tubes. The dimensions are from <a href="https://docs.wcproducts.com/greyt-telescope/overview-and-features/tubing-hole-pattern">WCP's documentation</a>.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/s4.webp" style="width:100%">
      <figcaption>4. Model the crush block at the top of the inner tube. You will add the holes that go through the crush block after you model the hook.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/s5.webp" style="width:100%">
      <figcaption>5. Sketch the hook. Pay attention to the sketch relations in the solution document.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/s6.webp" style="width:100%">
      <figcaption>6. Extrude the hook. Then, extrude the mounting holes to cut through the tube and the crush block. Also add the hook spacer.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1e/telescope/s7.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>7. Model the hook 3d printed spacer. With sketch imprinting enabled, we only need to draw the line for where the 3d printed block starts. There is no need to use the <code>Use</code> feature to copy the hook profile into the sketch.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/s8.webp" style="width:100%">
      <figcaption>8. Sketch the gearbox mounting plate on the outside of the tube. There should be a small 0.01" gap between the 3/8" clamping spacers and the tube to make sure that the gearbox can be assembled properly. The 13.75 mm construction circle represents the rounded hex spool. The #10-32 tapped hole allows for a bolt to thread into the plate and sit flush with the inside of the outer tube to lock the gearbox in place without interfering with the inner tube.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/s9.webp" style="width:100%">
      <figcaption>9. Sketch the pull down string by creating a line tangent to the rounded hex spool. Note that we will use this line to create a sweep of the rope, therefore this line cannot be construction geometry.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/s10.webp" style="width:100%">
      <figcaption>10. Extrude the plate, then add half depth pockets. The pockets should leave 1/16" of material on the bottom. The half-depth pocketing allows the contact face between the gearbox plate and tube to be solid. The plate should be mirrored to generate the opposite hand version on the other side of the tube.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/s11.webp" style="width:100%">
      <figcaption>11. Add a 10-32 clearance hole for the bolt that is threaded into the gearbox plate. Also model the gearbox spacer and the shaft.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/s12.webp" style="width:100%">
      <figcaption>12. Model the rope by creating an 3 mm circle on the end of the vertical line from the gearbox. Then, sweep the circle along the vertical line from the gearbox to create a model of the rope. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/s0.webp" style="width:100%">
      <figcaption>13. Finish the part studio by naming your features and putting them into folders. Also assign materials according to the reference design. </figcaption>
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

**Next, navigate to the "Exercise #4 Assembly" tab** in your copied document and **follow the instructions in the slides** to complete this exercise. 

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/a0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1e/telescope/a1.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>1. Insert the climber components and group only the base stage components together to the Origin Cube. This is because the inner stage moves relative to the base stage, so we cannot group them together.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/a2.webp" style="width:100%">
      <figcaption>2. Fasten the inner stage components together. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/a3.webp" style="width:100%">
      <figcaption>3. Insert and fasten the WCP GreyT telescope bearing blocks from the <a href="https://cad.onshape.com/documents/3f21b4b70302525a1e1f2c29/v/4ec8cc58f734f29f41a0fdb8/e/4646e6fc60ff8c4fe2a9d4dd" target="_blank">WCP GreyT telescope document</a>.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1e/telescope/a4.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Use two <code>Slider</code> mates to constrain the inner stage. By using two slider mates, one for the bottom and one for the top, the inner stage motion constraint is parametric to length changes in the base stage. We do not explicitly specify a travel length. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/a5.webp" style="width:100%">
      <figcaption>5. Fasten the spacer and replicate it. Insert and fasten the shaft bearing to the plate and shaft. Note that we only require one bearing on the plate since the MAXPlanetary gearbox has another bearing at its output as we do not want to overconstrain the shaft.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/a6.webp" style="width:100%">
      <figcaption>6. Insert and fasten the MAXPlanetary gearbox from MKCad. We use the 90 degree output with a 25:1 gear ratio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/a7.webp" style="width:100%">
      <figcaption>7. Insert, fasten, and replicate all of the required fasteners.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/a8.webp" style="width:100%">
      <figcaption>8. Close up of the bolt used to pin the gearbox in place. This bolt keeps the gearbox from sliding up and down.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/telescope/a0.webp" style="width:100%">
      <figcaption>9. Finish your assembly by organizing the parts into folders and naming your replicates.</figcaption>
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
    If all is done correctly your assembly should have 27 Instances.

### Section Views

Section views are a helpful tool that allow you to reveal the internal features of a part or assembly by slicing through it along a specified plane. You can select a plane, planar face, cylinder, cone, or mate connector to use as the sectioning plane. You can also choose to include or exclude specific parts from the section view.

!!! Tip "Creating a Section View"
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1e/telescope/section-view.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>Creating a section view to get a better view of the pinning bolt.</figcaption>
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