# 1C: Practice Mechanisms
## Introduction

Welcome to stage 1C! In this stage, you will be modeling a number of different mechanisms to practice your CAD skills and execution of small details. You will be introduced to new COTS parts and Onshape tips and tricks along the way to help your workflow.

Because these mechanisms are designed specifically to help practice skills and introduce concepts, they are modeled out-of-context of a full robot. 
While these mechanisms do include some good design techniques, they are not necessarily complete systems. The models are strictly for CAD practice and not recommended for use on real robots.

### Layout Sketches

Make sure to use a layout sketch for each mechanism, like the ones introduced in the Stage 1B exercises. Layout sketches are helpful at any scale, letting you define key dimensions in a single sketch, which makes it easy to adjust when needed.

!!! Tip
    Add the components that drive the design to the layout sketch (i.e. power transmission, game piece path, rollers, etc.) while keeping specific part details in their own sketches and features (i.e. a separate sketch for the bearing holes and plate outline, to be extruded).

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
      <figure>
          <img src="../images/exercise-1-layout.webp" style="width:80%">
      <figcaptions>Exercise 1 layout sketch. Notice that only key geometry details are included in the layout sketch.</figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="../images/exercise-1-layout-final.webp" style="width:80%">
          <figcaptions>Exercise 1 side view. Notice how the layout sketch drives the geometry of the mechanism.</figcaption>
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

!!! Note
    The concept of layout sketches will be expanded upon later when you start to use them in the context of a robot.

### Maintaining Consistent Origins

As mentioned in previous sections of Stage 1, you should maintain a consistent origin between your part studio and assembly. You will use the [`Origin Cube` Featurescript](https://cad.onshape.com/documents/321c197a842fc5f1a29e6621/w/fc3cdd5ca7edcd93e02f13cc/e/2b321cb91b74224b9c14b433 "Origin Cube Featurescript Onshape Document"){:target="_blank"} to achieve this. **Make sure that the origin cube is always the first feature in any part studio.** The below slides provide a demonstration of how to use the origin cube.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="../images/origin-cube-tutorial/origin-cube-tutorial-1.webp" style="width:90%">
      <figcaption>Place the Origin Cube featurescript as the first feature in the part studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/origin-cube-tutorial/origin-cube-tutorial-2.webp" style="width:90%">
      <figcaption>Model your mechanism.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/H6y1S_cHLKk?rel=0&controls=1&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>Insert the part studio into the assembly with the green checkmark. Group all static parts together with the Origin Cube part, then fasten the mate connector on the Origin Cube to the origin of the assembly.</figcaption>
    </div>
  </div>

  <!-- Next and previous buttons -->
  <button class="prev" onclick="plusSlides(-1,1)" style="background-color: #000; color: #fff;">&#10094;</button>
  <button class="next" onclick="plusSlides(1,1)" style="background-color: #000; color: #fff;">&#10095;</button>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

Following these steps will allow the origin of the assembly to be tied to a part that will never change or disappear. The position of the other parts relative to the origin cube will consistent with the part studio, even when things are changed in the part studio. This will be particularly useful for flexible assemblies, such as an arm or elevator, in stage 2 and beyond.

<br>

<!-- The following is just notes that can be used in the final content of the page.

Remember, practice is essential – the more CAD models you create, the more proficient and efficient you'll become. Using keyboard shortcuts can significantly accelerate your CAD workflow. Be attentive to best practices to avoid developing any bad habits.


Change this feedback form out and add one at the end of each section? Or do that but keep this one and edit the questions a bit and add one at the end of stage 2, since there's useful content here like the time it takes to complete it that we maybe wouldn't get from the smaller feedback forms? Idk I'll figure this out

Optionally, please fill out [this feedback form](https://forms.gle/J1QNvRkvpi7xyfuU8 "Learning Course Feedback Form"){:target="_blank"} about stages 0 and 1. -->