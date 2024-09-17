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

# 2A: Full Detail Drivebase

## Exercise: Battery Holder

In the reference design, the battery is placed horizontally on the bellypan. It is secured with a 2" wide strap that wraps around the battery and bellypan to secure it. 

### Instructions

**Add a battery holder to your Stage 1C drivetrain.** You can take inspiration from the following instructions slides. 

<!-- <center>**Sample Battery Holder Modeling Slides**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
      <figure>
          <img src="/img/learning-course/stage2-drivebase/batt/batt1s0.webp" style="width:100%">
          <figcaption>0. Finished battery holder w/ mounting holes, strap cutout in bellypan, and strap.</figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/learning-course/stage2-drivebase/batt/batt1s1.webp" style="width:100%">
          <figcaption>1. Layout of battery and battery mount plate. To fit the battery with 1/16” radius fillets on the inner corners, the cutout should be around 6.705” x 7.225”.</figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/learning-course/stage2-drivebase/batt/batt1s2.webp" style="width:100%">
          <figcaption>2. 1/8" thick aluminum is a good option for this plate. Also add a 3/8" diameter spacers to connect to the bellypan.</figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/learning-course/stage2-drivebase/batt/batt1s3.webp" style="width:100%">
          <figcaption>3. Add the mounting holes and cut out for the battery strap on the bellypan. </figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/learning-course/stage2-drivebase/batt/batt1s4.webp" style="width:100%">
          <figcaption>4. Optionally model the battery strap.</figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/learning-course/stage2-drivebase/batt/batt1s5.webp" style="width:100%">
          <figcaption>5. Optionally pocket the battery holder. 0.2" wide ribs are recommended. </figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/learning-course/stage2-drivebase/batt/batt1s0.webp" style="width:100%">
          <figcaption>6. Insert the battery holder, spacers, and battery into the assembly. Don't forget to organize your feature tree, name your parts, assign part materials, and organize your assembly file tree.</figcaption>
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




<br>
