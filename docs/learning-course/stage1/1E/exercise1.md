# 1E: Practice Mechanisms

## Exercise 1: Flat Intake

In this exercise, you will be modeling a sort of flat game piece manipulator. This mechanism features live-axle compliant wheels, a Kraken belt reduction, and tube plugs.

This exercise introduces you to the use of the the [Assembly Mirror Featurescript](https://cad.onshape.com/documents/0f7d68295ff4dab57adcf92c/v/88fbfa19a2e2555d18599db4/e/bcf3052f00f1f9d3d95a89c7?jumpToIndex=1392&showReturnToWorkspaceLink=true "Assembly Mirror FS Onshape Document"){:target="_blank"} which is a useful tool to  help make your assembly more parametric. Make sure to add this to your Featurescripts if you have not already.

### Part Studio Instructions

**Navigate to the "Exercise #1 Part Studio" tab** in your copied document and **follow the instructions in the slides** to complete the part studio for this exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s1.webp" style="width:100%">
      <figcaption>1. Create the layout sketch on the Right plane. Begin by sketching the tube profiles. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s2.webp" style="width:100%">
      <figcaption>2. Using the Origin Cube functions you learned previously, sketch the pulleys and belt. This is a 5mm pitch 12T to 30T transmission with a 70T belt. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s3.webp" style="width:100%">
      <figcaption>3. Finish the layout sketch by sketching a 60 mm circle to represent the motor and a 2" circle for the intake wheel.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1e/flat-intake/s4.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Create the tube sketch plane by using an offset mate connector reference.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s5.webp" style="width:100%">
      <figcaption>5. Sketch the tubes by tracing over the layout sketch. There should be no dimensions in this sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s6.webp" style="width:100%">
      <figcaption>6. Extrude the lower and use tube converter to turn it into a thin-wall 1x1 with a 0.5" hole spacing pattern. We will create the upper tube in a later step.  </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s7.webp" style="width:100%">
      <figcaption>7. Create the plate sketch on the outside face of the 1x1 tube. Begin by sketching the bearing hole and motor bore hole.</figcaption>
    </figure>
  </div>

  <!-- switch  s8 to a video? -->

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s8.webp" style="width:100%">
      <figcaption>8. Sketch the 2" bolt circle for mounting motor. You can utilize the Origin Cube variable for a #10-32 clearance hole by typing <code>#10_32</code> into the dimension and selecting the <code>#Clearance_Fit_10_32</code> variable. Use a <code>Circular pattern</code> to pattern the hole sketch. Although we pattern the hole 6 times, we only utilize 3. Set the left most hole to be coincident with the centerline between the pulleys. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s9.webp" style="width:100%">
      <figcaption>9. Sketch the mounting holes by using a linear pattern. The tube holes are 0.196" in diameter (A #10-32 "close fit") so we will use the same size for the plate.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s10.webp" style="width:100%">
      <figcaption>10. Finish the plate sketch by drawing the plate outline around the sketch features.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s11.webp" style="width:100%">
      <figcaption>11. Extrude the plate to be 1/4" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s12.webp" style="width:100%">
      <figcaption>12. Create the pocketing sketch on the outside face of the plate. Sketch ribs to connect the mounting points.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s13.webp" style="width:100%">
      <figcaption>13. Use the <code>Part Lighten</code> Featurescript to pocket the plate. We use 3/16" rib and wall thickness, and 0.26" tool diameter.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s14.webp" style="width:70%">
      <figcaption>14. You may have noticed in the previous step that the pocketing created some unsightly bumps along the outside contour as a result of the mounting holes. We will make these edges smooth with a simple trick in the next slide. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s15.webp" style="width:100%">
      <figcaption>15. Open the pocketing sketch and sketch two lines spaced exactly half the pocketing wall thickness away from the outer edge of the mounting hole (NOT the center of the circle). In our case, this would be half of 3/16". This "tricks" the Part Lighten Featurescript by creating an extra rib where the bumps would have been.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s16.webp" style="width:100%">
      <figcaption>16. Edit the <code>Part Lighten</code> feature to include the two new ribs. The pocketed part should no longer have the bumps. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s17.webp" style="width:100%">
      <figcaption>17. To create a reference for extruding the upper tube, we use the <code>Mirror</code> feature to mirror the plate across the Right plane. Since we do not want to actually use this component in the assembly, we can change the color of the part and add <code>zREF</code> to the part name so that it will appear at the very bottom of the part list when inserting parts in the assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1e/flat-intake/s18.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>18. In the assembly, we would like the location of the two plates to be fully parametric. Since OnShape does not support assembly mirroring, we can instead use the <code>Assembly Mirror</code> Featurescript which provides a workaround to assembly mirroring by generating a pair of mate connectors to simulate an assembly mirror. The featurescript will generate a mate connector at the origin of the selected part, and another at the center of the virtually mirrored part. The usage of these two mate connectors will become clear when we create the assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s19.webp" style="width:100%">
      <figcaption>19. Using the tube sketch we created earlier in the part studio, we can now extrude the upper tube profile up to the mirrored plate's inside face. This ensures that the upper tube is parametric to changes in intake width.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s20.webp" style="width:100%">
      <figcaption>20. Convert the solid into a 2x1 thin-wall tube with 0.5" hole pattern spacing. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s21.webp" style="width:100%">
      <figcaption>21. Create the bottom polycarbonate plate on the top face of the bottom tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s22.webp" style="width:100%">
      <figcaption>22. Model the roller shaft with the <code>Shaft</code> Featurescript. You can estimate the length first and then adjust it once you create the assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s23.webp" style="width:100%">
      <figcaption>23. Model the belt using the <code>Belt & Chain Gen</code> Featurescript. Use a mate connector offset from the plate's bearing hole as the reference plane. Select the layout sketch pulley PDs to use as the guides.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/s0.webp" style="width:100%">
      <figcaption>24. Finish the part studio by naming your features and organizing them into folders. Assign the part materials accordingly.</figcaption>
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

**Next, navigate to the "Exercise #1 Assembly" tab** in your copied document and **follow the instructions in the slides** to complete this exercise. 

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/flat-intake/a0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1e/flat-intake/a1.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>1.  </figcaption>
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
    If all is done correctly your assembly should have 32 Instances.

### Parametric Modeling

Some of the steps we took to complete this exercise could have been simplified.
For instance, we didn’t necessarily *need* to use the Assembly Mirror feature for the plate.
We didn’t *need* to use an “Up to face” extrude for the upper tube. 
We didn’t *need* to [something here].

However, we practice these techniques because, while they may marginally increase modeling time upfront, they can save ***significant*** amounts of time when *going back and editing&.
CAD is an iterative process — your models and designs won’t be perfect the first time around, so making your model easier to modify and more robust to changes (e.g., changing the width of this intake) will save you time and effort in the long run.
As you use best practices, they’ll become second nature.

<br>