# 1D: Design Methodology - Simple Swerve Drivebase

## Adding More Components

When you model more parts in the part studio, you can insert them into the assembly in a similar to fashion to before. Hit insert and immediately click on the green checkmark. Then, edit the initial `Group` you made and add the part to the group. By doing this, you ensure that added parts will always stay in the same place it was modeled in the part studio.

Let's add a gusset to connect the 2"x2" tube to the 2"x1" tube.

### Instructions

Start by **navigating to the `Drivetrain` Part Studio** in the `Drivetrain` folder. **Follow the instructions in the slides** to add the gusset.

???+ Tip "Manually Define Mounting Holes"
    When you project the holes off of the tube or use the gusset featurescript, those references can break easily if the tube converter or length of the tube gets changed. Try to dimension manually defined holes from the edge of the tube or only project one hole and use a linear pattern to minimize the amount of things you need to fix if something changes.

    <figure>
      <img src="../images/define-holes.webp" style="width:60%; border:5px solid #ADADAD; border-radius: 2%">
    </figure>

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
      <figcaption>1. Sketch and extrude a 1/8" thick gusset to connect the crosstube to the top of the frame using the holes shown.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/n8lWSdOV-Ks?controls=1&rel=0&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>2. Insert the gusset into the assembly and add it to the <code>Group</code>.</figcaption>
    </div>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/add-3.webp" style="width:100%">
      <figcaption>3. Add 2-1/2" #10-32 bolts to the three holes in the bellypan on each side so they go through the gusset holes on the other side. Add nylock nuts to the holes on the gusset. As you learned in 1C, this is to help prevent rivets from loosening and falling out over time.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/CC017qPw2Mk?controls=1&rel=0&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>4. Edit the replicate feature to add rivets to the gusset.</figcaption>
    </div>
  </div>

  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/0O1ojhHTgMI?controls=1&rel=0&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>5. Mirror the gusset, bolts, and rivets to the other side of the drivetrain using a mate connector on the origin cube.</figcaption>
    </div>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/drivetrain/add-0.webp" style="width:100%">
      <figcaption>6. Finished drivetrain assembly.</figcaption>
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