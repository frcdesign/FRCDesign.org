# 1D: Design Methodology - Simple Swerve Drivebase

## Deriving Layout Sketches and Part Modeling

Now that you have created the layout sketch, you can begin modeling the individual parts. The critical dimensions of the parts, such as the length of the tubes, will be driven by the layout sketch. This way, the tubes will automatically update with any changes in the size of the drivebase in the layout sketch.

### Instructions

Start by **creating a new folder tab in your Document called `Drivetrain`**. Then, **create a new part studio called `Drivetrain`** within the `Drivetrain` folder. **Follow the instructions in the slides** to complete the part studio. Remember that the Origin Cube should be the first feature in your part studio.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/parts-0.webp" style="width:100%">
      <figcaption>0. The part studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/parts-1.webp" style="width:100%">
      <figcaption>1. Start by inserting the origin cube. Then, use the <code>Derived</code> tool to insert the layout sketches you previously drew from the Main Layout Sketch part studio. This feature will automatically update if changes are made to the layout sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/parts-2.webp" style="width:100%">
      <figcaption>2. Use the <code>Extrude Individual</code> and <code>Tube Converter</code> Featurescripts to model the tubes. The 2"x1" tubes should be 1/8" wall for strength, while the 2"x2" tube can be 1/16" wall.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/parts-3.webp" style="width:100%">
      <figcaption>3. Start with one corner of the bellypan. The corner is cut out to create room for the swerve module. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/gk03kkl98NU" width="768" height="432" frameborder="0" allowfullscreen vq="hd1080"></iframe>
      <figcaption>4. Use the <code>Fillet</code> sketch tool to add a 1" radius sketch fillet on the two internal corners of the cutout. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/ivUXyr0Lacs" width="768" height="432" frameborder="0" allowfullscreen vq="hd1080"></iframe>
      <figcaption>5. Next, use the <code>Circular Pattern </code> sketch tool to pattern the other three corners. Extrude the bellypan to be 1/8" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/parts-6.webp" style="width:100%">
      <figcaption>6. Use the <code> Fillet All Edges</code> Featurescript to add a 0.25" radius fillet to the remaining edges on the bellypan by selecting the bottom face of the bellypan.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/parts-7.webp" style="width:100%">
      <figcaption>7. Add the mounting holes for the bellypan. Use a mix of <code>Linear Pattern</code> and <code>Circular Pattern</code> to pattern the 0.196" rivet and bolt holes. As was learned in 1C Exercise 1, bolts can be used to stop rivets from loosening over time.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/mUVoTxoniCY" width="768" height="432" frameborder="0" allowfullscreen vq="hd1080"></iframe>
      <figcaption>8. Extrude the holes into the bellypan. If the sketch is correctly drawn, you should not need to select each individual hole.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/parts-0.webp" style="width:100%">
      <figcaption>9. Finally, name your sketches and organize them into a folder in the feature tree. Additionally, set the material of the bellypan to Aluminum 6061 and name your parts.</figcaption>
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

### Derived Feature

In this section, you were introduced to the `Derived` feature. This feature is extremely powerful and can be used to import parts from one part studio into another to enable references for modeling. However, you must be careful to not overuse this function as it can significantly slow down your part studios.

### Feature Tree Organization

At this point, you should be feeling more and more comfortable with Onshape modeling and using Featurescripts. Always make sure to clean up your feature tree while working to keep it organized and easy to use. You can more learn about feature tree organization on the [Feature Tree Best Practices](/best-practices/feature-tree-setup/ "Feature Tree Best Practices Page"){:target="_blank"} page.

<br>

