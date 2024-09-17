

# 1C: Design Methodology

## Assembly

Now that the part studio is finished, you can create the drivetrain assembly. 

Previously, in Stage 1A when you created assemblies one of the parts in the group mate was fixed in place. However, this is not considered a good practice as it is not parametric. This is where the origin cube comes in: the origin cube has a mate connector placed at the origin of the part studio. After inserting and grouping all of the parts, you can fasten the origin cube to the origin of the assembly. This aligns the part studio origin and assembly origin.

### Instructions

Start by **creating a new assembly tab called `Drivetrain Assembly`** in the `Drivetrain` folder. **Follow the instructions in the slides** to complete the assembly.

<!-- <center>**Drivetrain Assembly**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtAssy0.webp" style="width:100%">
      <figcaption>0. The assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtAssy1.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>1. Insert the parts into the assembly, <code>Group</code> them, then fasten the origin cube to the origin of the assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtAssy2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Insert the MK4i module from the MKCad app into the assembly and mate it into place. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtAssy3.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>3. Use the <code>Circular Pattern</code> assembly tool to finish assembling the modules. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtAssy4.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Insert a 3/16" rivet from the MKCad app into the assembly and mate it. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtAssy5.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. Use the <code>Replicate </code> assembly tool to replicate the rivet and rivet mate onto all matching geometry on the bottom face of the bellypan</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtAssy0.webp" style="width:100%">
      <figcaption>6. The assembly.</figcaption>
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
      <source src="/img/learning-course/stage1c/replicateExample.webm" type="video/mp4">
    </video>


<br>