# 1C: Practice Mechanisms
## Introduction

Welcome to stage 1C! In this stage, you will be modeling a number of different mechanisms to practice your CAD skills and execution of small details. You will be introduced to new COTS parts and Onshape tips and tricks along the way to help your workflow.

Because these mechanisms are designed specifically to help practice skills and introduce concepts, they are modeled out-of-context of a full robot.

### Layout Sketches

Make sure to use a layout sketch for each mechanism just like the ones introduced in the Stage 1B exercises. Layout sketches are useful no matter the scale, as most of your important dimensions can be defined in one sketch, ready to be easily changed if needed. 

!!! Tip
    Add the components that drive the design to the layout sketch (e.g. power transmission, gamepiece path, rollers, etc.) and keep specific details in their own sketches and features (e.g. a separate sketch for the bearing holes and plate outline, to be extruded).

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
      <figure>
          <img src="/img/learning-course/stage1c/exercise_1_layout.webp" style="width:80%">
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/learning-course/stage1c/exercise_1_layout_final.webp" style="width:80%">
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

As mentioned in previous sections of Stage 1, you should maintain a consistent origin between your part studio and assembly. You will use the [`Origin Cube` Featurescript](https://cad.onshape.com/documents/321c197a842fc5f1a29e6621/w/fc3cdd5ca7edcd93e02f13cc/e/2b321cb91b74224b9c14b433 "Origin Cube Featurescript Onshape Document"){:target="_blank"} to achieve this.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/origin-cube-tutorial/origin-cube-tutorial-1.webp" style="width:90%">
      <figcaption>Place the Origin Cube featurescript as the first feature in the part studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/origin-cube-tutorial/origin-cube-tutorial-2.webp" style="width:90%">
      <figcaption>Model your mechanism.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/origin-cube-tutorial/origin-cube-tutorial-3.webp" style="width:90%">
      <figcaption>Insert the part studio into the assembly with the green checkmark.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/origin-cube-tutorial/origin-cube-tutorial-4.webp" style="width:90%">
      <figcaption>Group all static parts together with the Origin Cube part.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/origin-cube-tutorial/origin-cube-tutorial-5.webp" style="width:90%">
      <figcaption>Fasten the mate connector on the Origin Cube to the origin of the assembly.</figcaption>
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

Following these steps will allow the origin of the assembly to be tied to a part that will never change or disappear. The relation of the other parts in relation to the origin cube will stay the same as in the part studio, even when things are changed in the part studio.

### Exercise Documents

**Make a copy of the Stage 1C Exercises Document** through the button below. Each exercise has a folder, a "reference" tab (a preview of what the final model should look like), and a tab or two for doing your exercise in. Solutions are also provided in the 1C Exercise Solutions Document to check your work afterwards. You **do not** need to make a copy of the solutions document.

<center>
[1C Exercises Document](https://cad.onshape.com/documents/a9be0985d5e798d784f8b4cb/w/5c862e02b9b471157ba3ca40/e/c96f153b351bc1f1eafdef8a "1A Exercises Onshape Document"){:target="_blank"  .md-button .md-button--primary}
[1C Exercise Solutions Document](https://cad.onshape.com/documents/99b4fd36c41bdb5b3e6d5ceb/w/f8e04439667e38aedb8f8196/e/08676a32914225413f14b28b "1C Exercise Solutions Onshape Document"){:target="_blank" .md-button .md-button--primary}
</center>

<div class="grid cards" markdown>

-   <center>![](../../../..\img\learning-course\stage1c\Exercise 1 Assembly.webp)</center>

-   <center>![](../../../..\img\learning-course\stage1c\Exercise 3 Assembly.webp)</center>

</div>
<figure>
<figcaption>Two of the exercises in this section</figcaption>
</figure>


Each exercise should take no more than 40 to 45 minutes to complete.

As you progress through the exercises, the level of guidance will gradually decrease. This is to help transition you from more guided exercises to projects that have little more than the parts to be added and the reference model, as will be the norm for the rest of Stages 1 and 2. While you should reference the solutions document to ensure your model and modeling methods are correct, try to avoid *blindly* copying the model later in the exercises.

!!! Note "Primary Goal"
    The primary goal of this stage is to get you enough practice with CAD and modeling in the context of FRC where you won't need guidance in every step that you do. If you find that you struggle without guidance on the later exercises, feel free to try and model more small mechanisms of your choice, making sure to get feedback on them from [the Discord Server](https://discord.gg/jHXTdNjYCg "David's Design Server Invite"){:target="_blank"} or your team.

Focus on refining your CAD techniques and following best practices such as fully constraining your sketches, modeling in a way that captures design intent, and naming your features and parts.

<br>

<!-- The following is just notes that can be used in the final content of the page.

Remember, practice is essential – the more CAD models you create, the more proficient and efficient you'll become. Using keyboard shortcuts can significantly accelerate your CAD workflow. Be attentive to best practices to avoid developing any bad habits.


Change this feedback form out and add one at the end of each section? Or do that but keep this one and edit the questions a bit and add one at the end of stage 2, since there's useful content here like the time it takes to complete it that we maybe wouldn't get from the smaller feedback forms? Idk I'll figure this out

Optionally, please fill out [this feedback form](https://forms.gle/J1QNvRkvpi7xyfuU8 "Learning Course Feedback Form"){:target="_blank"} about stages 0 and 1. -->