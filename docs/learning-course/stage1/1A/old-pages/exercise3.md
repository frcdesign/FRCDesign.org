# 1A: Onshape Fundamentals

## Exercise #3: Box Tube Frame

For this exercise, you will create a simple frame and two gussets in the part studio, then create an assembly and mate together all the components.

### Featurescripts

You will utilize the [`Extrude Individual`, `Tube Converter`, and `Gusset` Featurescripts](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Julia's Featurescripts Onshape Document"){:target="_blank"} for this exercise.

- The `Gusset` Featurescript is an easy way to create simple gussets by selecting the locations of the holes the gusset should attach to. 
    - Usually you will want to manually sketch a gusset because you want more control over the shape of it, a more complex shape, or to make it more parametric.
    - Using the holes of tubes created by tube converter can cause sketches and features to break when the length of the tube changes

### Instructions

**Navigate to the "Exercise #3 Structure" part studio tab** in your copied document and **follow the instructions in the slides** to complete the exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s10.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s1.webp" style="width:100%">
      <figcaption>1. Start by sketching the tubes on the right plane.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s2.webp" style="width:100%">
      <figcaption>2. Use the <code>Extrude Individual</code> Featurescript to extrude the blocks.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s3.webp" style="width:100%">
      <figcaption>3. Use <code>Tube Converter</code> Featurescript to turn the blocks into 1/16" wall tubes with a 0.5" spacing pattern of 0.196" holes.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s4.webp" style="width:100%">
      <figcaption>4. Use the <code>Gusset</code> tool to create the top gusset by selecting the holes on the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s5.webp" style="width:100%">
      <figcaption>5. Use the <code>Gusset</code> tool to create the bottom gusset by selecting the holes on the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s6.webp" style="width:100%">
      <figcaption>6. Name the key sketches and parts. The materials will have already been set to 6061 Aluminum from the Featurescripts.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e3/e3s7.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>7. Insert the parts into the assembly by directly clicking on the green checkmark. Then, <code>Group</code> all the parts together. Finally, <code>fix</code> the bottom tube in place. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e3/e3s8.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>8. Copy and paste the gussets four times. Then, use the <code>Fasten</code> mate to attach the gussets to the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e3/e3s9.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>9. Some gussets may need to have their <code>Fasten</code> mate reoriented in order to properly line up. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e3/e3s10.webp" style="width:100%">
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
    Make sure to have you and/or a more experienced member/mentor of your team [**review your CAD!**](../1A/focusing-on-improvement.md "Focusing on Improvement Page"){:target="_blank"} Your assembly should have 12 instances and weigh approximately 1.95 lbs.

In this exercise, you were introduced to yet another highly useful Featurescript for creating gussets. Additionally, notice that we only model 1 of each type of gusset in the part studio. For the tubes, we choose to model all of the tubes even though the two vertical tubes are the same - this is to make assembly more parametric since the tube would otherwise be difficult to mate.

It should be noted that while fixing the tube is not considered an [assembly best practice](/best-practices/assembly-setup#origin-cube-method "Assembly Best Practices Page"){:target="_blank"} for setting the origin of an assembly, it is sufficient for the purposes of these exercises.

<br>

