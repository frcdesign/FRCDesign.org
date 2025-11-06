# 1C: Practice Mechanisms

## Exercise 2: Dead Axle Rollers

In this exercise, you will be modeling some dead axle rollers. To spin things, whether it be rollers, wheels, or even arms, two types of axles can be utilized: "live" and "dead" axles. 

### Live and Dead Axle Rollers

You'll learn more about live and dead axle design in Stage 2, but for now, all you need know is that live axle means we power the shaft to spin our mechanism, whereas with dead axle, we directly power the spinning component.
For live axle, the shaft spins on fixed bearings, while for dead axle, the bearings are on the spinning component. Take a look at the visual below to better understand.

???+ Example "Live vs Dead Axle Rollers"
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/dead-vs-live.webp" style="width:65%">
      <figcaption>Section view of a dead axle (left) and live axle (right) roller. The dead axle roller sits on bearings and needs to be directly powered (in this case, through the integrated pulley). The live axle roller is powered from a pulley farther down the hex shaft.</figcaption>
    </figure>

### Part Studio Instructions

**Navigate to the "Exercise #2 Part Studio" tab** in your copied document and **follow the instructions in the slides** to complete the part studio for this exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/PS-S0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/PS-S1.webp" style="width:100%">
      <figcaption>1. Create a new sketch on the right plane for the Layout Sketch. Start by sketching a pivot axle hole with a bolt pattern around it.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/PS-S2.webp" style="width:100%">
      <figcaption>2. Sketch the first belt run between rollers to the left of the pivot hole.</figcaption>
    </figure>
  </div>
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/PS-S3.webp" style="width:100%">
      <figcaption>3. Create a second belt run of the same length as the first.</figcaption>
    </figure>
  </div>
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/PS-S4.webp" style="width:100%">
      <figcaption>4. Add 2" circles around the ends of the belt runs to represent the rollers.</figcaption>
    </figure>
  </div>
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/PS-S5.webp" style="width:100%">
      <figcaption>5. Sketch the motor belt run off the first roller angled back towards the pivot point.</figcaption>
    </figure>
  </div>
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/PS-S6.webp" style="width:100%">
      <figcaption>6. Add a 60mm circle to represent the motor, this will be useful information when making the plate.</figcaption>
    </figure>
  </div>
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/PS-S7.webp" style="width:100%">
      <figcaption>7. Create the plate sketch offset from the layout sketch. This is similar to the previous exercise.</figcaption>
    </figure>
  </div>
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/PS-S8.webp" style="width:100%">
      <figcaption>8. Start the plate sketch by copying the bolt pattern and pivot axle hole, and adding bolt holes for the rollers. Also add the bolt pattern for the motor, this should be done in the same way as the previous exercise but with a 6 hole pattern. Like before we will only make 3 of these real holes. The rest will be construction circles.</figcaption>
    </figure>
  </div>
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/PS-S9.webp" style="width:100%">
      <figcaption>9. Draw the plate outline based on the holes created in the previous slide.</figcaption>
    </figure>
  </div>
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/PS-S10.webp" style="width:100%">
      <figcaption>10. Extrude the plate in the "Right" direction.</figcaption>
    </figure>
  </div>
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/parts-11.webp" style="width:100%">
      <figcaption>11. Use Belt & Chain Gen to make the motor belt. The offsets don't matter here since you will be mating the belts to the pulleys.</figcaption>
    </figure>
  </div>
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/parts-12.webp" style="width:100%">
      <figcaption>12. Use Belt & Chain Gen to make the first roller belt.</figcaption>
    </figure>
  </div>
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/parts-13.webp" style="width:100%">
      <figcaption>13. Use Belt & Chain Gen to make the second roller belt.</figcaption>
    </figure>
  </div>
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/PS-S0.webp" style="width:100%">
      <figcaption>14. Finish the part studio by naming your features and organizing them into folders. Assign the plate material to be polycarbonate. </figcaption>
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

**Next, navigate to the "Exercise #2 Assembly" tab** in your copied document and **follow the instructions in the slides** to complete this exercise. 

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/A-S0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/fDDM02mGCvg?rel=0&controls=1&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>1. Start the assembly by inserting the part studio and grouping the origin cube and plate together. Then fasten the cube to the origin.</figcaption>
    </div>
  </div>

  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/0k2pSyg_nA0?rel=0&controls=1&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>2. Use Assembly Mirror to copy the plate to the other side.</figcaption>
    </div>
  </div>

  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/J_dtYxcaCL8?rel=0&controls=1&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>3. Insert a roller from FRCDesignLib. Make sure the length is set to 24", and has bolt endcaps set to the HTD option. You can mate the first roller to one of the holes in the side plate. You can replicate the single roller to the other two holes. Make sure you select the whole assembly for the replicate as shown.</figcaption>
    </div>
  </div>

  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/DqiNcoXHYNE?rel=0&controls=1&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>4. Mate the belts to the rollers using the center mate point for the belts, and the roller pulleys.</figcaption>
    </div>
  </div>

  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/BnFXhMRt_us?rel=0&controls=1&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>5. Insert the Motor, Pulley, Shaft Spacers, and Shaft Bolt. Assemble the motor components together and mate the pulley to the center of the belt.</figcaption>
    </div>
  </div>

  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/WUW7gB-it7I?rel=0&controls=1&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>6. Measure the distance between the plate and motor by clicking the face of each component. Copy this distance to your clipboard. Open the FRCDesignLib Inserter and insert a custom round ID spacer with the length you copied. There is no need to change other configurations. Attach this spacer to the plate and use replicate to add it to the other three plate holes.</figcaption>
    </div>
  </div>

  <div class="mySlides fade">
    <div class="slide-content">
      <iframe src="https://www.youtube.com/embed/FkXr6tEHoSc?rel=0&controls=1&showinfo=0&vq=hd1080" frameborder="0" allowfullscreen></iframe>
      <figcaption>7. Add fasteners to your assembly. Note the use of washers on each bolts When bolting to polycarbonate plates it is best practice to use washers. This helps prevent the plates from cracking. The Rollers should be attached with 1/2" #10-32 bolts, and the motor with 1.75" #10-32 bolts.</figcaption>
    </div>
  </div>

  <div class="mySlides fade">
    <figure>
     <img src="/img/learning-course/stage1c/dead-axle-rollers/A-S0.webp" style="width:100%">
      <figcaption>8. Organize your assembly with folders</figcaption>
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
    Make sure to have you and/or a more experienced member/mentor of your team [**review your CAD!**](../1A/focusing-on-improvement.md "Focusing on Improvement Page"){:target="_blank"}.

### Minimizing Unique Part Count

You may have noticed that the 3rd roller has a 24T pulley on both ends despite there only being a belt connected to one end. 
While the configurable roller does allow you to choose no pulley for the end with no belt, it can be advantageous to still keep the pulley in situations like this to reduce the number of unique parts. 
By doing so, all three rollers are identical, making part tracking and spare parts easier.

<br>
