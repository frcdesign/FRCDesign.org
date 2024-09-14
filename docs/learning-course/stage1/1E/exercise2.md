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

## Exercise 2: Dead Axle Rollers

In this exercise, you will be modeling some dead axle rollers. To spin things, whether it be rollers, wheels, or even arms, two types of axles can be utilized: "live" and "dead" axles. 

You'll learn more about live and dead axle design in Stage 2, but for now, all you need know is that live axle means we power the *shaft* to spin our mechanism, where as with dead axle, we directly power the spinning component.
For live axle, the shaft spins on fixed bearings, while for dead axle, the shaft does **not** spin and the bearings are instead on the spinning component. Take a look at the visual below to better understand.

!!! Example "Live vs Dead Axle Rollers"
    pic here

This exercise introduces you to the use of the [Configurable Rollers Document](https://cad.onshape.com/documents/b75886a5660c38eee7d50e47/w/58faeca16d5b2008a9485b5c/e/6274f59b451ed6222cd7523d "Configurable Rollers Onshape Document"){:target="_blank"} and
[`Assembly Mirror` Featurescript](https://cad.onshape.com/documents/0f7d68295ff4dab57adcf92c/v/88fbfa19a2e2555d18599db4/e/bcf3052f00f1f9d3d95a89c7?jumpToIndex=1392 "Assembly Mirror Featurescript"){:target="_blank"}.

### Part Studio Instructions

**Navigate to the "Exercise #2 Part Studio" tab** in your copied document and **follow the instructions in the slides** to complete the part studio for this exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s1.webp" style="width:100%">
      <figcaption>1. Start the layout sketch on the Right Plane. Sketch the hole for a bearing and four #10-32 clearance holes with a 2" bolt circle. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s2.webp" style="width:100%">
      <figcaption>2. Sketch the pulleys and belt paths for the first two rollers. You will use 5mm pitch 24T pulleys. We subtract 0.015" from the calculated c-c distance to decrease friction from linking together multiple belts. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s3.webp" style="width:100%">
      <figcaption>3. Add the pulley and belt path for the 3rd roller.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s4.webp" style="width:100%">
      <figcaption>4. Sketch 2" construction circles to represent the rollers, which are 2" OD. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s5.webp" style="width:100%">
      <figcaption>5. Sketch the pulleys and belt path for the motor. Since the motor transmission will also utilize a 24T pulley, we can reutilize the same pulley PD sketch from the first roller. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s6.webp" style="width:100%">
      <figcaption>6. Sketch the OD of the Kraken motor, which is 60 mm.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s7.webp" style="width:100%">
      <figcaption>7. Create the plate sketch by using an offset mate connector from the layout sketch as the origin entity. Select the motor pulley and offset by 12".</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s8.webp" style="width:100%">
      <figcaption>8. Sketch the plate outline. Pay attention to the sketch constraints in the solutions document. We offset the curve on the top right 0.25" away from the belt to that it is fully covered by the plate.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s9.webp" style="width:100%">
      <figcaption>9. Add the holes for the mounting point by using the <code>Use</code> feature and selecting the layout sketch entities to convert over.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s10.webp" style="width:100%">
      <figcaption>10. Sketch the 2" bolt circle of #10-32 bolts and bore for the motor. Note that we only use 3 out of 6 of the patterned mounting holes, the rest are left as construction geometry. Sketch the bolts holes for the dead axle shafts. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s11.webp" style="width:100%">
      <figcaption>11. Extrude the plate to be 1/4" thick. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1e/dead-axle-rollers/s12.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>12. Add the 9 mm wide HTD 5mm belts. Use the plate as the reference plane and select the pulley PDs from the layout sketch. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s13.webp" style="width:100%">
      <figcaption>13. Your belt tooth count and pitch length should match the solution document. The two 70T belts have a pitch length slightly less than 350 mm since we subtracted 0.015" from the c-c's in the layout. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s14.webp" style="width:100%">
      <figcaption>14. Use the Assembly Mirror Featurescript to add a mate connector for mating the opposite side plate. There is no reason to use a part mirror since the two plates will be identical. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/s0.webp" style="width:100%">
      <figcaption>15. Finsh the part studio by naming your features and putting them into folders. Assign the plate material to be polycarbonate. </figcaption>
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

**Next, navigate to the "Exercise #XXX Assembly" tab** in your copied document and **follow the instructions in the slides** to complete this exercise. 

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/dead-axle-rollers/a0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1e/dead-axle-rollers/a1.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>1.  </figcaption>
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
    If all is done correctly your assembly should have 17 Instances.



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