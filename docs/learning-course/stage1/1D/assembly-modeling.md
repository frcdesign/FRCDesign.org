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
      <video width="1920" controls>
        <source src="../images/drivetrain/assy-2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Insert the MK4i module from the MKCad app into the assembly and mate it into place. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="../images/drivetrain/assy-3.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>3. Use the <code>Circular Pattern</code> assembly tool to finish assembling the modules. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/assy-4.webp" style="width:100%">
      <figcaption>4. Insert, fasten, and replicate the 3/16" rivet from FRCDesignLib onto the bellypan holes. For the replicate feature, you can use "Select edges on face" rather than "Select individual edges" since we want all of the holes to have a rivet.</figcaption>
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

### Replicate Tool

The `Replicate` tool is a very powerful tool for duplicating parts in assemblies. `Replicate` works by creating a copy of the selected parts, and duplicates the selected mate onto the selected geometry. Note that the selected geometry must exactly match the origin mate geometry, eg: the hole diameter must be the same for replicate to copy a rivet. 

In your assembly, you use the select the face for replicate to apply to. What this does is identify all geometry that matches the original mate and then copy the selected components and mate to those matching locations on the selected face. If you want to replicate onto only specific holes, you can change the drop-down menu to "Match Individual Edges".

!!! Video "Match Individual Edges for Replicate"
    <video width="1920" controls>
      <source src="../images/replicate-example.webm" type="video/webm">
    </video>


<br>