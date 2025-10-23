# 1D: Design Methodology - Simple Swerve Drivebase

## Adding More Components

When you model more parts in the part studio, you can insert them into the assembly in a similar to fashion to before. Hit insert and immediately click on the green checkmark. Then, edit the initial `Group` you made and add the part to the group. By doing this, you ensure that added parts will always stay in the same place it was modeled in the part studio.

Let's add a gusset to connect the 2"x2" tube to the 2"x1" tube.

### Instructions

Start by **navigating to the `Drivetrain` Part Studio** in the `Drivetrain` folder. **Follow the instructions in the slides** to add the gusset.

<!-- <center>**Adding a Gusset**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/add-0.webp" style="width:100%">
      <figcaption>0. Finished drivetrain assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/add-1.webp" style="width:100%">
      <figcaption>1. Add the gusset for the crosstube with the <code>Gusset</code> Featurescript.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="../images/drivetrain/add-2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Insert the gusset into the assembly and add it to the <code>Group</code>.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/add-3.webp" style="width:100%">
      <figcaption>3. Copy the gusset and mate it to the other side. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="../images/drivetrain/add-4.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Edit the replicate feature to add rivets to the gusset. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/add-0.webp" style="width:100%">
      <figcaption>4. Finished drivetrain assembly.</figcaption>
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

Make sure you sort the instances in your assembly into folders (i.e. frame, swerve modules) and name any patterns and replicates used. This will help you locate components in the assembly later down the line.

!!! success "Verification"
    Make sure to have you and/or a more experienced member/mentor of your team [**review your CAD!**](../1A/focusing-on-improvement.md "Focusing on Improvement Page"){:target="_blank"} 
    
    Your assembly should weigh approximately 37.2lbs.

    Your tab manager should have the following tabs and folder:
    <figure>
      <img src="../images/tab-manager.webp" style="width:100%">
    </figure>

### Level of Detail

It should be noted that while modeling every detail of the robot hardware (bolts, rivets, nuts) is beneficial for purchasing and real life assembly purposes, it isn't strictly necessary. Time is a precious resource, especially during build season, so you should spend it on what will give you the biggest return.

More details about best practices for Onshape assemblies are included on the [Assembly Best Practices Page](/best-practices/assembly-setup/ "Assembly Best Practices Page"){:target="_blank"}.


<br>