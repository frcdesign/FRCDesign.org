# 1C: Practice Mechanisms

## Exercise 4: Telescoping Hook

In this exercise, you will be modeling a telescoping climber. This mechanism features [WCP GreyT telescoping bearing blocks](https://wcproducts.com/products/greyt-telescope "GreyT Telescope Product Page"){:target="_blank"} and [REV MAXPlanetary](https://www.revrobotics.com/frc/maxplanetary-system/ "Rev MAXPlanetary System Product Page"){:target="_blank"} mounting gearbox plates. Be sure to pay close attention to hook and gearbox sketches when modeling. 

!!! warning
    From this point on the specific lengths of shafts and offsets of belts may not be provided, you should consider what components are going on the shafts when setting distances. It is always ok to go back and change these lengths later if needed. When you get to making your own mechanisms there wont be a step by step guide for it! These exercises try and gradually pull back the guard rails as your progress to get you ready for build season. If you get stuck feel free to refer to the ![solution doc](https://cad.onshape.com/documents/99b4fd36c41bdb5b3e6d5ceb/w/f8e04439667e38aedb8f8196/e/8843ec3a6b3828f461343955), or ask a mentor for help!

### Leveraging COTS Components
Using COTS components is crucial in a time-constrained build season. 
Even if you have the capability to fabricate every part, relying on COTS parts allows you to spend your time on more important tasks—like refining designs or testing. 
This helps ensure your time is spent where it makes the most impact, rather than on re-inventing parts that are already readily available.

???+ Example "Exercise 4 COTS Components"
    <div class="grid cards" markdown>

    -   <center><img src="../images/telescope/greyt.webp" width="100%"></center>

    -   <center><img src="../images/telescope/maxplanetary.webp" width="100%"></center>

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
    <img src="../images/telescope/crush-block-plate.webp" width="65%">
    <figcaption>A 3D printed crush block (left) and crush plate (right). Crush plates tend to work well for the middle of the tubes where it may be difficult to insert a crush block.</figcaption>
    </figure>

### Part Studio Instructions

**Navigate to the "Exercise #4 Part Studio" tab** in your copied document and **follow the instructions in the slides** to complete the part studio for this exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-1.webp" style="width:100%">
      <figcaption>1. Begin by creating a side profile sketch of the telescope tubes on the right plane.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-2.webp" style="width:100%">
      <figcaption>2. Use two extrudes to create the solid bodies for the tubes. Then, use the Tube Converter Featurescript (or shell feature) to convert the solid bodies into two thin-wall tubes with no hole pattern.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-3.webp" style="width:100%">
      <figcaption>3. Add the holes for the WCP bearing blocks to the inner and outer tubes. The dimensions are from <a href="https://docs.wcproducts.com/greyt-telescope/overview-and-features/tubing-hole-pattern">WCP's documentation</a>.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-4.webp" style="width:100%">
      <figcaption>4. Model the crush block at the top of the inner tube. Make sure to account for 3D-printing tolerances by giving a little bit of clearance for the crush block inside of the tube. You will add the holes that go through the crush block after you model the hook.</figcaption>
    </figure>
  </div>
  
  
  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-5.webp" style="width:100%">
      <figcaption>5. Sketch the hook. Pay attention to the sketch relations in the solution document.</figcaption>
    </figure>
  </div>


  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-6.webp" style="width:100%">
      <figcaption>6. Extrude the hook, then extrude the mounting holes to cut through the tube and the crush block. Also add the hook spacer.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/Kt2l8vujAUE?rel=0&controls=1&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>7. Model the hook 3d printed spacer. With sketch imprinting enabled, we only need to draw the line for where the 3d printed block starts. There is no need to use the <code>Use</code> feature to copy the hook profile into the sketch.</figcaption>
    </div>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-8.webp" style="width:100%">
      <figcaption>8. Sketch the gearbox mounting plate on the outside of the tube. There should be a small 0.01" gap between the 3/8" clamping spacers and the tube to make sure that the gearbox can be assembled properly. The 13.75 mm construction circle represents the rounded hex spool. A hole will be placed on the point on the left side of the plate.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-9.webp" style="width:100%">
      <figcaption>9. Sketch the pull down string by creating a line tangent to the rounded hex spool. Note that we will use this line to create a sweep of the rope, therefore this line cannot be construction geometry.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-10.webp" style="width:100%">
      <figcaption>10. Extrude the plate. This plate will not be pocketed so that the surface clamped to the tube is spreads out the force. Optionally, you could partially pocket it and leave 1/16" of material on the side of the plate clamped against the tube.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-11.webp" style="width:100%">
      <figcaption>11. Add a 10-32 hole for the bolt that is threaded into the gearbox plate, then mirror the plate to the other side.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-12.webp" style="width:100%">
      <figcaption>12. Model the gearbox spacer and the shaft.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-13.webp" style="width:100%">
      <figcaption>13. Use the mate connector at the end of the sketched rope line to create a sketch of a 3mm circle lined up with the center of the shaft.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-14.webp" style="width:100%">
      <figcaption>14. Sweep the circle along the vertical line from the gearbox to create a model of the rope.</figcaption>
    </figure>
  </div>


  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/parts-0.webp" style="width:100%">
      <figcaption>15. Finish the part studio by naming your features and putting them into folders. Also assign materials according to the reference design. </figcaption>
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
      <img src="../images/telescope/assy-0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/ch1kZ_IOCjs?rel=0&controls=1&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>1. Insert the climber components and group only the base stage components together to the Origin Cube. This is because the inner stage moves relative to the base stage, so we cannot group them together.</figcaption>
    </div>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/assy-2.webp" style="width:100%">
      <figcaption>2. Fasten the inner stage components together. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/Vt1ld7z8ovI?rel=0&controls=1&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>3. Insert and fasten the WCP GreyT telescope bearing blocks from the <a href="https://cad.onshape.com/documents/3f21b4b70302525a1e1f2c29/v/4ec8cc58f734f29f41a0fdb8/e/4646e6fc60ff8c4fe2a9d4dd" target="_blank">WCP GreyT telescope document</a>.</figcaption>
    </div>
  </div>

  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/Oz_Ta0b86_w?rel=0&controls=1&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>4. Use two <code>Slider</code> mates to constrain the inner stage. By using two slider mates, one for the bottom and one for the top, the inner stage motion constraint is parametric to length changes in the base stage. We do not need to explicitly specify a travel length. </figcaption>
    </div>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/assy-5.webp" style="width:100%">
      <figcaption>5. Fasten the spacer and replicate it. Insert and fasten the shaft bearing to the plate and shaft. Note that we only require one bearing on the plate since the MAXPlanetary gearbox has another bearing at its output as we do not want to overconstrain the shaft.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/assy-6.webp" style="width:100%">
      <figcaption>6. Insert and fasten the MAXPlanetary gearbox and NEO Vortex from FRCDesignLib. We will use the 90 degree output with a 25:1 gear ratio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/assy-7.webp" style="width:100%">
      <figcaption>7. Insert, fasten, and replicate all of the required fasteners.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/assy-8.webp" style="width:100%">
      <figcaption>8. Close up of the bolt used to pin the gearbox in place. This bolt keeps the gearbox from sliding up and down.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/telescope/assy-0.webp" style="width:100%">
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
      <iframe src="https://www.youtube.com/embed/6oiVBMGkCOs?rel=0&controls=1&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>Creating a section view to get a better view of the pinning bolt.</figcaption>
    </figure>

<br>