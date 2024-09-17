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


