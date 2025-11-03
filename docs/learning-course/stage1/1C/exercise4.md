# 1C: Practice Mechanisms

## Exercise 4: Telescoping Hook

In this exercise, you will be modeling a telescoping climber. This mechanism features [WCP GreyT telescoping bearing blocks](https://wcproducts.com/products/greyt-telescope "GreyT Telescope Product Page"){:target="_blank"} and [REV MAXPlanetary](https://www.revrobotics.com/frc/maxplanetary-system/ "Rev MAXPlanetary System Product Page"){:target="_blank"} mounting gearbox plates. Be sure to pay close attention to hook and gearbox sketches when modeling. 

### Leveraging COTS Components
Using COTS components is crucial in a time-constrained build season. 
Even if you have the capability to fabricate every part, relying on COTS parts allows you to spend your time on more important tasks—like refining designs or testing. 
This helps ensure your time is spent where it makes the most impact, rather than on re-inventing parts that are already readily available.

???+ Example "Exercise 4 COTS Components"
    <div class="grid cards" markdown>

    -   <center><img src="/img/learning-course/stage1c/telescope/greyt.webp" width="100%"></center>

    -   <center><img src="/img/learning-course/stage1c/telescope/maxplanetary.webp" width="100%"></center>

    </div>

    <figure>
      <figcaption>The telescoping bearing blocks have complex geometry that would be difficult and time consuming to manufacture for most teams.
                  The REV MAXPlanetary is an easy way to get a large gearbox reduction without the need for a custom gearbox. (Photo Credits: WCP, REV)</figcaption>
    </figure>

### Crush Blocks

3D-printed crush blocks can be used to reinforce thin-walled tubing in assemblies where bolts pass through without a plate.
Since the strength of bolts comes from their clamping force, without anything to support the thin walls, the tube can collapse before achieving proper clamping force.
Crush blocks distribute the load, allowing for full clamping force while maintaining the tube’s structural integrity.

Alternatively, a "crush plate" can also be utilized to distribute the fastener force to achieve a similar effect as a crush block.

???+ example "Crush Blocks and Crush Plates"
    <figure>
    <img src="../images/indexer-centering/crush-block-plate.webp" width="65%">
    <figcaption>A 3D printed crush block (left) and crush plate (right). Crush plates tend to work well for the middle of the tubes where it may be difficult to insert a crush block.</figcaption>
    </figure>

### Part Studio Instructions

**Navigate to the "Exercise #4 Part Studio" tab** in your copied document and **follow the instructions in the slides** to complete the part studio for this exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/s0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/s1.webp" style="width:100%">
      <figcaption>1. Begin by creating a side profile sketch of the telescope tubes on the right plane.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/s2.webp" style="width:100%">
      <figcaption>2. Use two extrudes to create the solid bodies for the tubes. Then, use the Tube Converter Featurescript to convert the solid bodies into two thin-wall tubes with no hole pattern.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/s3.webp" style="width:100%">
      <figcaption>3. Add the holes for the WCP bearing blocks to the inner and outer tubes. The dimensions are from <a href="https://docs.wcproducts.com/greyt-telescope/overview-and-features/tubing-hole-pattern">WCP's documentation</a>.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/s4.webp" style="width:100%">
      <figcaption>4. Model the crush block at the top of the inner tube. You will add the holes that go through the crush block after you model the hook.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/s5.webp" style="width:100%">
      <figcaption>5. Sketch the hook. Pay attention to the sketch relations in the solution document.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/s6.webp" style="width:100%">
      <figcaption>6. Extrude the hook. Then, extrude the mounting holes to cut through the tube and the crush block. Also add the hook spacer.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/telescope/s7.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>7. Model the hook 3d printed spacer. With sketch imprinting enabled, we only need to draw the line for where the 3d printed block starts. There is no need to use the <code>Use</code> feature to copy the hook profile into the sketch.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/s8.webp" style="width:100%">
      <figcaption>8. Sketch the gearbox mounting plate on the outside of the tube. There should be a small 0.01" gap between the 3/8" clamping spacers and the tube to make sure that the gearbox can be assembled properly. The 13.75 mm construction circle represents the rounded hex spool. The #10-32 tapped hole allows for a bolt to thread into the plate and sit flush with the inside of the outer tube to lock the gearbox in place without interfering with the inner tube.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/s9.webp" style="width:100%">
      <figcaption>9. Sketch the pull down string by creating a line tangent to the rounded hex spool. Note that we will use this line to create a sweep of the rope, therefore this line cannot be construction geometry.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/s10.webp" style="width:100%">
      <figcaption>10. Extrude the plate, then add half depth pockets. The pockets should leave 1/16" of material on the bottom. The half-depth pocketing allows the contact face between the gearbox plate and tube to be solid. The plate should be mirrored to generate the opposite hand version on the other side of the tube.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/s11.webp" style="width:100%">
      <figcaption>11. Add a 10-32 clearance hole for the bolt that is threaded into the gearbox plate. Also model the gearbox spacer and the shaft.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/s12.webp" style="width:100%">
      <figcaption>12. Model the rope by creating an 3 mm circle on the end of the vertical line from the gearbox. Then, sweep the circle along the vertical line from the gearbox to create a model of the rope. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/s0.webp" style="width:100%">
      <figcaption>13. Finish the part studio by naming your features and putting them into folders. Also assign materials according to the reference design. </figcaption>
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

**Next, navigate to the "Exercise #4 Assembly" tab** in your copied document and **follow the instructions in the slides** to complete this exercise. 

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/a0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/telescope/a1.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>1. Insert the climber components and group only the base stage components together to the Origin Cube. This is because the inner stage moves relative to the base stage, so we cannot group them together.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/a2.webp" style="width:100%">
      <figcaption>2. Fasten the inner stage components together. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/a3.webp" style="width:100%">
      <figcaption>3. Insert and fasten the WCP GreyT telescope bearing blocks from the <a href="https://cad.onshape.com/documents/3f21b4b70302525a1e1f2c29/v/4ec8cc58f734f29f41a0fdb8/e/4646e6fc60ff8c4fe2a9d4dd" target="_blank">WCP GreyT telescope document</a>.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/telescope/a4.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Use two <code>Slider</code> mates to constrain the inner stage. By using two slider mates, one for the bottom and one for the top, the inner stage motion constraint is parametric to length changes in the base stage. We do not need to explicitly specify a travel length. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/a5.webp" style="width:100%">
      <figcaption>5. Fasten the spacer and replicate it. Insert and fasten the shaft bearing to the plate and shaft. Note that we only require one bearing on the plate since the MAXPlanetary gearbox has another bearing at its output as we do not want to overconstrain the shaft.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/a6.webp" style="width:100%">
      <figcaption>6. Insert and fasten the MAXPlanetary gearbox from MKCad. We use the 90 degree output with a 25:1 gear ratio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/a7.webp" style="width:100%">
      <figcaption>7. Insert, fasten, and replicate all of the required fasteners.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/a8.webp" style="width:100%">
      <figcaption>8. Close up of the bolt used to pin the gearbox in place. This bolt keeps the gearbox from sliding up and down.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/telescope/a0.webp" style="width:100%">
      <figcaption>9. Finish your assembly by organizing the parts into folders and naming your replicates.</figcaption>
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
    Make sure to have you and/or a more experienced member/mentor of your team [**review your CAD!**](../1A/focusing-on-improvement.md "Focusing on Improvement Page"){:target="_blank"} Your assembly should have 27 instances.

### Section Views

Section views are a helpful tool that allow you to reveal the internal features of a part or assembly by slicing through it along a specified plane. You can select a plane, planar face, cylinder, cone, or mate connector to use as the sectioning plane. You can also choose to include or exclude specific parts from the section view.

!!! Tip "Creating a Section View"
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/telescope/section-view.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>Creating a section view to get a better view of the pinning bolt.</figcaption>
    </figure>

<br>