# 1C: Practice Mechanisms

## Exercise 7: Vertical Rollers

In this exercise, you will be modeling some vertical rollers. This mechanism features the [Configurable Rollers](https://cad.onshape.com/documents/b75886a5660c38eee7d50e47/w/58faeca16d5b2008a9485b5c/e/6274f59b451ed6222cd7523d "Configurable Rollers Onshape Document"){:target="_blank"} assembly and a 3D printed motor spacer. Be sure to pay attention to the layout sketch and assembly mating when modeling. 

### 3D Printing to Reduce Part Count
3D printing can be used to create spacer blocks. 
Rather than using multiple spacers to connect two components, we can opt to use a 3D printed block that combines all of the spacers into a single part, which can help reduce part count and make assembly easier.
If you have a 3D printer, this can be a good option.

???+ example "3D Printed Spacer Block"
    <figure>
      <img src="../images/vertical-rollers/3dp-spacer.webp" width="65%">
      <figcaption>Multiple spacers can be combined into single 3D printed block to reduce part count. </figcaption>
    </figure>

### Part Studio Instructions

**Navigate to the "Exercise #7 Part Studio" tab** in your copied document and **refer to the solution document** to complete the part studio for this exercise. The **following instruction slides** only provide a general outline and some key details.

<!-- Slideshow container -->
<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/parts-0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/parts-1.webp" style="width:100%">
      <figcaption>1. Begin by creating the layout sketch on an offset mate connector 3" above the origin. 
                  We subtract 0.015" from each of the belt c-c's to reduce friction since we are linking multiple belts in series.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/parts-2.webp" style="width:100%">
      <figcaption>2. Use the <code>Mirror</code> sketch tool to create a right hand reference for the rollers and tube location. Use the distance between the roller pairs to drive the roller locations. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/parts-3.webp" style="width:100%">
      <figcaption>3. Create the bottom plate. Then, create the top plate offset 7" from the bottom plate. 
                    Pay close attention to the plate sketches in the solution document. 
                    Note that the 1x1" tube plug requires a 4 holes spaced 3/8" apart from each other in a square pattern.
                    We dont need all 4 so we will only use 2 of them.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/parts-4.webp" style="width:100%">
      <figcaption>4. Sketch, extrude, then tube convert the thin-wall 1x1 tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/parts-5.webp" style="width:100%">
      <figcaption>5. Model the the 3D printed motor spacer block and extrude it to be 1" long.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/parts-6.webp" style="width:100%">
      <figcaption>6. Model the belts. The calculated pitch length is slightly under a multiple of 5 mm since we subtracted 0.015" from each c-c.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/parts-0.webp" style="width:100%">
      <figcaption>7. Finish the part studio by naming your features and organizing them into folders. Assign the part materials accordingly.</figcaption>
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
      <img src="../images/vertical-rollers/assy-0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/assy-1.webp" style="width:100%">
      <figcaption>1. Add the part studio parts to the assembly. Like before, group mate the rigid components with the Origin Cube and mate the Origin Cube to the assembly origin.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/assy-2.webp" style="width:100%">
      <figcaption>2. Add 1x1 Tube Plugs to the vertical 1x1 tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/assy-3.webp" style="width:100%">
      <figcaption>3. Insert a Kraken X44 and 12t pulley into the assembly. Mate the pulley to the motor, and fasten the motor to the spacer.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/assy-4.webp" style="width:100%">
      <figcaption>4. Insert the "Tube Roller System" assembly from FRCDesignLib.
                  Set the overall roller length to 7" and use 24T pulleys on each end. 
                  Duplicate and fasten the other 2 rollers.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/assy-5.webp" style="width:100%">
      <figcaption>5. Fasten the belts to the roller pulleys.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/assy-6.webp" style="width:100%">
      <figcaption>6. Insert, fasten, and replicate all of the required fasteners. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/assy-7.webp" style="width:100%">
      <figcaption>7. Use Assembly Mirror to copy the left side assembly to the right side. Make sure all items have the mirror strategy set to transform so you don't end up making new parts.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/vertical-rollers/assy-0.webp" style="width:100%">
      <figcaption>8. Finish the assembly by organizing your instances into folders.</figcaption>
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

!!! Success "Verification"
    Make sure to have you and/or a more experienced member/mentor of your team [**review your CAD!**](../1A/focusing-on-improvement.md "Focusing on Improvement Page"){:target="_blank"} Your assembly should have approximately 25 instances.


<br>
