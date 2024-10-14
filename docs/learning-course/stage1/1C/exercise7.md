# 1C: Practice Mechanisms

## Exercise 7: Vertical Rollers

In this exercise, you will be modeling some vertical rollers. This mechanism features the [Configurable Rollers](https://cad.onshape.com/documents/b75886a5660c38eee7d50e47/w/58faeca16d5b2008a9485b5c/e/6274f59b451ed6222cd7523d "Configurable Rollers Onshape Document"){:target="_blank"} assembly and a 3D printed motor spacer. Be sure to pay attention to the layout sketch and assembly mating when modeling. 

### 3D Printing to Reduce Part Count
3D printing can be used to create spacer blocks. 
Rather than using multiple spacers to connect two components, we can opt to use a 3D printed block that combines all of the spacers into a single part, which can help reduce part count and make assembly easier.
If you have a 3D printer, this can be a good option.

???+ example "3D Printed Spacer Block"
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/3dp-spacer.webp" width="65%">
      <figcaption>Multiple spacers can be combined into single 3D printed block to reduce part count. </figcaption>
    </figure>

### Part Studio Instructions

**Navigate to the "Exercise #7 Part Studio" tab** in your copied document and **refer to the solution document** to complete the part studio for this exercise. The **following instruction slides** only provide a general outline and some key details.

<!-- Slideshow container -->
<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/s0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/s1.webp" style="width:100%">
      <figcaption>1. Begin by creating the layout sketch on an offset mate connector 3" above the origin. 
                  We subtract 0.015" from each of the belt c-c's to reduce friction since we are linking multiple belts in series.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/vertical-rollers/s2.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Use the <code>Mirror</code> sketch tool to create a right hand reference for the rollers and tube location. Use the distance between the roller pairs to drive the roller locations. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/s3.webp" style="width:100%">
      <figcaption>3. Extrude the bottom plate. Then, create the top plate offset 5" from the bottom plate. 
                    Pay close attention to the plate sketches in the solution document. 
                    Note that the 1x1" tube plug requires a 4 holes spaced 3/8" apart from each other in a square pattern. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/s4.webp" style="width:100%">
      <figcaption>4. Sketch, extrude, then tube convert the thin-wall 1x1 tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/s5.webp" style="width:100%">
      <figcaption>5. Model the the 3D printed motor spacer block and extrude it to be 1" long.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/s6.webp" style="width:100%">
      <figcaption>6. Model the belts. The calculated pitch length is slightly under a multiple of 5 mm since we subtracted 0.015" from each c-c.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/s7.webp" style="width:100%">
      <figcaption>7. Use the <code>Assembly Mirror</code> Featurescript to create a reference mate connector for the 1x1 tube. This will be used in the assembly for mating.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/s0.webp" style="width:100%">
      <figcaption>8. Finish the part studio by naming your features and organizing them into folders. Assign the part materials accordingly.</figcaption>
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

**Next, navigate to the "Exercise #7 Assembly" tab** in your copied document and **refer to the solution document** to complete the assembly for this exercise. The **following instruction slides** only provide a general outline and some key details.

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/a0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/a1.webp" style="width:100%">
      <figcaption>1. Add the part studio parts to the assembly. Like before, group mate the rigid components with the Origin Cube and mate the Origin Cube to the assembly origin.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/vertical-rollers/a2.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Copy the 1x1 tube and fasten the Assembly Mirror mate connectors together.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/a3.webp" style="width:100%">
      <figcaption>3. Insert four 1x1 tube plugs and fasten them into place on the 1x1 tubes.
                    Then, copy and fasten the rest of the frame pieces on the right hand side.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/a4.webp" style="width:100%">
      <figcaption>4. Insert the Configurable Roller assembly from the link at the top of this page.
                  Set the overall roller length to 5" and use 24T pulleys on each end. Duplicate and fasten the roller assembly into place.
                  Then, insert and fasten the motor and motor pulleys. Also fasten the left hand side belts into place. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/vertical-rollers/a5.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. Copy and fasten the right hand side belts. 
                  Note that you will need to flip the fasten mate in order for the belt to line up correctly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/a6.webp" style="width:100%">
      <figcaption>6. Insert, fasten, and replicate all of the required fasteners. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/vertical-rollers/a0.webp" style="width:100%">
      <figcaption>7. To finish the assembly, organize your components into folders and name your replicates.</figcaption>
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
    If all is done correctly your assembly should have 37 Instances.


<br>
