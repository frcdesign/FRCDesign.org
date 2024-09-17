

# 1C: Design Methodology - Simple Swerve Drivebase

## Top Level Robot Assembly
Now that you have a drivebase, you can create a *top level robot assembly*. The top level robot assembly is the highest in the assembly hierarchy. Organizing the assemblies in this way keeps thing organized from both a CAD assembly and real life assembly standpoint. 

You will create a top level robot assembly to go with your drivebase. The mechanism you'll be adding is the scoring mechanism from [1678's 2023 robot](https://www.thebluealliance.com/team/1678/2023 "1678 2023 Blue Alliance Page"). The scoring mechanism CAD can be accessed from here:

<center>[1678 2023 Scoring Mechanism Document](https://cad.onshape.com/documents/28a750426de8e2bc17d5b900/w/8e79c6217ae2ce07ff57d900/e/a4d266d03289620078d13a80 "Team 1678 2023 Scoring Mechanism Onshape Document"){:target="_blank" .md-button .md-button--primary }</center>

### Instructions

Start by, **creating a new assembly tab above the `Master Sketch` part studio** and name it **`Top Level Robot Assembly`**. **Follow the instructions in the slides** to complete the top level robot assembly.

<!-- <center>**Top Level Robot Assembly**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/TopLevel/topL0.webp" style="width:100%">
      <figcaption>0. Finished top level robot assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/TopLevel/topL1.webm" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>1. Insert the drivetrain assembly and fasten the origin cube to the assembly origin. You may need to unhide the origin cube to mate it.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/TopLevel/topL2.webm" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Insert the 1678 2023 scoring assembly by pasting the scoring mechanism link into the <code>Insert</code> menu textbox. Then, fasten its origin cube to the assembly origin. You may need to hide the drivetrain's origin cube to access the origin of the assembly for mating.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/TopLevel/topL0.webp" style="width:100%">
      <figcaption>3. Finished top level assembly. </figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <button class="prev" onclick="plusSlides(-1,0)"style="background-color: #000; color: #fff;">&#10094;</button>
  <button class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</button>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

!!! success "Verification"
    Your tab manager should now looks like this:
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtTabManager2.webp" style="width:100%">
    </figure>

And that's all there is to the top level robot assembly! The use of the origin cube makes it very easy to mate together assemblies. In later stages you will explore how to create flexible assemblies (arms, elevators, etc) with the origin cube. If you are interested, you can get a sneak peek [here](/best-practices/assembly-setup/#utilizing-origin-cube-for-flexible-assemblies "Origin Cube Information Page"){:target="_blank"}.


<br>