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

## Exercise: Bumper Mounting

Similar to battery mounting, good bumper mounting is often overlooked. While a robust bumper mounting system won’t win you any matches, a poor bumper mounting system can certainly lose you a match. Poor bumper mounting can lead to [bumper damage](https://youtu.be/9mawtTD6v7M?si=RyM0fE6GrR4QlMEU&t=78 "3647 Bumpers Breaking"){:target="_blank"}, long bumper swap time, or even lead to your [bumpers falling off](https://youtu.be/pBUKxWKGV-Q?si=hmJtt9N6C7vGLFpL&t=42 "Bumpers Falling Off"){:target="_blank"}.

In the reference design, the threaded stud bumper mounting system is implemented. 

!!! Example "Threaded Stud Bumper Mounting System"
    <center><img src="\img\learning-course\stage2-drivebase\bumpers\studMount.png" style="width:50%"></center>
    <center><figcaption>Section view of the threaded stud bumper mount system. The threaded stud is attached to the bumper wood and the nut holds the bumpers tight against the frame.</figcaption></center>


### Instructions

**Add your desired bumper mounts to your Stage 1C drivetrain.** You can take inspiration from the following instructions slides.
<!-- 
You can learn more about bumpers and different bumper mounting options in the [Design Handbook](/design-handbook/) pages.  -->

<!-- <center>**Sample Bumper Mount Modeling Slides**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">
    <!-- Full-width images with number and caption text -->
    <div id="slide1" class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/bumpers/bumper2s0.webp" style="width:100%">
            <figcaption>0. Finished bumper mounts. </figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/bumpers/bumper2s1.webp" style="width:100%">
            <figcaption>1. Model the bumper mount. This part should be 3/16” thick aluminum. The threaded stud falls into the slot.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/bumpers/bumper2s2.webp" style="width:100%">
            <figcaption>2. Add the pocket for the nut that screws onto the threaded stud. This nut keeps the bumpers tight with the frame. The pocket secures the nut and prevents the bumper from lifting up.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/bumpers/bumper2s3.webp" style="width:100%">
            <figcaption>3. Optionally pocket the mount. 0.15" wide ribs and 1/8" tool radius are recommended. </figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/bumpers/bumper2s4.webp" style="width:100%">
            <figcaption>4. Insert the mount and add it to the <code>Group</code>. Copy three more mounts and mate them onto the drivetrain assembly. If your team runs multi piece bumpers (eg: two C shaped bumpers) you may need to add more mounts to secure the bumpers.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/bumpers/bumper2s0.webp" style="width:100%">
            <figcaption>5. Finished bumper mounts in drivetrain assembly.</figcaption>
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
