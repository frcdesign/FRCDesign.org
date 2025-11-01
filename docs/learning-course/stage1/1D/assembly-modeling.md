# 1D: Design Methodology - Simple Swerve Drivebase

## Assembly

Now that the part studio is finished, you can create the drivetrain assembly. 

<!-- Previously, in Stage 1A when you created assemblies one of the parts in the group mate was fixed in place. However, this is not considered a good practice as it is not parametric. This is where the origin cube comes in: the origin cube has a mate connector placed at the origin of the part studio.  -->

Just like with the practice exercises in the previous stage, after inserting and grouping all of the parts, you should fasten the origin cube to the origin of the assembly. This aligns the part studio origin and assembly origin.

### Instructions

Start by **creating a new assembly tab called `Drivetrain Assembly`** in the `Drivetrain` folder. **Follow the instructions in the slides** to complete the assembly.

<!-- <center>**Drivetrain Assembly**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/assy-0.webp" style="width:100%">
      <figcaption>0. The assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/assy-1.webp" style="width:100%">
      <figcaption>1. Add the part studio parts to the assembly. Like before, group mate the rigid components with the Origin Cube and mate the Origin Cube to the assembly origin.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/vPjp-Xay10s" width="768" height="432" frameborder="0" allowfullscreen vq="hd1080"></iframe>
      <figcaption>2. Insert the simplified MK4i module from FRCDesignLib into the assembly and mate it into place. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/PA8D-PvsyF0" width="768" height="432" frameborder="0" allowfullscreen vq="hd1080"></iframe>
      <figcaption>3. Use the <code>Circular Pattern</code> assembly tool to finish assembling the modules. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/assy-4.webp" style="width:100%">
      <figcaption>4. Insert, fasten, and replicate the 3/16" Aluminum Blind Rivet (WCP) (.125" - .250" Grip Length) from FRCDesignLib onto the bellypan holes. Make sure to leave the three holes shown in the image empty for bolts to be added on the next page.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/assy-0.webp" style="width:100%">
      <figcaption>5. To finish the assembly, organize your components into folders and name your replicates.</figcaption>
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

### Rivet Grip Length

As was mentioned in 1A, When selecting rivets to insert from the part library, you'll notice they have a configuration for **grip length**. The grip length of a rivet is the total thickness of material it can fasten together. Make sure you choose the appropriate grip length or they can either come out easily or not fasten the material together.

<figure>
    <img src="../images/pop-rivet-steps.webp" width="100%" style="border:5px solid #ADADAD; border-radius: 2%">
    <figcaption>Image Credit: https://animalia-life.club/qa/pictures/types-of-pop-rivets</figcaption>
</figure>
<br>