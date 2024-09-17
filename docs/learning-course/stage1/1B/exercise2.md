

# 1B: Power Transmissions

## Exercise 2: Two Stage Gearbox

In this exercise, you will be CADing and assembling a two stage gearbox. The goal of this exercise is to practice modeling more advanced gearboxes. You will also learn how to use the `Part Lighten` Featurescript used for lightening parts.

### Part Studio Instructions
**Navigate to the "Exercise #2 Part Studio" tab** in your copied document and **follow the instructions in the slides** to complete the part studio. 
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e2/e2s9.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e2/e2s1a.webp" style="width:100%">
      <figcaption>1a. Create the layout sketch for the gearbox. Start by drawing the 2nd stage, which is a 20T gear to a 50T gear.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e2/e2s1b.webp" style="width:100%">
      <figcaption>1b. Draw the first stage, which is a 12T motor pinion gear to a 50T gear.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e2/e2s1c.webp" style="width:100%">
      <figcaption>1c. Draw the outline of the motors as a 2.5" diameter circle. This is the finished layout sketch for the gearbox.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e2/e2s2.webp" style="width:100%">
      <figcaption>2. Create a new sketch to draw the profile of the plate. Add the bearing holes, which are 1.125" diameter holes, as well as the motor boss holes, which are 0.8". Also add the motor mounting holes. You can utilize the <code>Mirror</code> sketch tool to mirror the geometry from the left side to the right side. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e2/e2s3.webp" style="width:100%">
      <figcaption>3. Extrude the plate to be 1/4" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e2/e2s4.webp" style="width:100%">
      <figcaption>4. Use the <code>Spacer</code> Featurescript to create the gearbox spacer. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e2/e2s5.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. Use the <code>Shaft</code> Featurescript to create the first stage shaft. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e2/e2s6.webp" style="width:100%">
      <figcaption>6. Use the <code>Shaft</code> Featurescript to create the output shaft.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e2/e2s7.webp" style="width:100%">
      <figcaption>7. Create a sketch on the face of the plate and draw the lines for the pocketing ribs. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e2/e2s8.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>8. Use the <code>Part Lighten</code> Featurescript to pocket the plate by selecting the ribs created by the previous sketch. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e2/e2s9.webp" style="width:100%">
      <figcaption>9. Finished part studio. Name the key sketches and parts. Set the material of the plate and spacers to 6061 Aluminum. </figcaption>
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

**Next, navigate to the "Exercise #2 Assembly" tab** in your copied document and **follow the instructions in the slides** to complete this exercise. 

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e2/e2s0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e2/e2s10.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>1. Insert the part studio into the assembly and fix only the gearbox plate. Mate the spacer to the plate. Then, use the <code>Replicate</code> tool to replicate the spacer and its associated mate onto the other spacer locations. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e2/e2s11.webp" style="width:100%">
      <figcaption>2. Copy the gearbox plate and mate it into place. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <li class="slideVideo">
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e2/e2s12.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>3. Assemble the bearings and shafts using parts from the MKCad App. </figcaption>
    </li>
  </div>

  <div class="mySlides fade">
    <li class="slideVideo">
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e2/e2s13.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Assemble the motor and motor pinion gear using parts from the MKCad App. </figcaption>
    </li>
  </div>

  <div class="mySlides fade">
    <li class="slideVideo">
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e2/e2s14.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. Assemble the shaft spacers and gears using parts from the MKCad App. </figcaption>
    </li>
  </div>

  <div class="mySlides fade">
    <li class="slideVideo">
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e2/e2s15.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>6. Assemble the shaft retention bolts, motor bolts, gearbox bolts, and nuts using the Onshape Standard Content and MKCad app parts. </figcaption>
    </li>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e2/e2s0.webp" style="width:100%">
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
    If all is done correctly your assembly should have 27 Instances.

In this exercise, you practiced more complex gearbox modeling and mating together larger assemblies. 



<br>

