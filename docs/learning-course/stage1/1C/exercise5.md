# 1C: Practice Mechanisms

Starting with exercise 5, only an outline of the design process and key details will be provided to you. This is to prepare you for stage 2, where the exercises are less guided.

Focus on capturing design intent and maintaining best practices in your part studios and assemblies. Follow the workflow of the solution document.

## Exercise 5: Flipped Gearbox

In this exercise, you will be modeling a two motor, two-stage flipped gearbox. These types of gearboxes are referred to as "flipped" because the output shaft points in the opposite direction as the input motors. 
This style of gearbox can be desired in some situations to meet packaging constraints.

### Part Studio Instructions

**Navigate to the "Exercise #5 Part Studio" tab** in your copied document and **refer to the solution document** to complete the part studio for this exercise. The **following instruction slides** only provide a general outline and some key details.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flipped-gb/s0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flipped-gb/s1.webp" style="width:100%">
      <figcaption>1. Start by modeling the tube that the gearbox mounts on.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flipped-gb/s2.webp" style="width:100%">
      <figcaption>2. Create the layout sketch on the tube face. Remember to only include essential information in the layout sketch. In this case, only the gear PD's and motor OD's are required. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flipped-gb/s3.webp" style="width:100%">
      <figcaption>3. Sketch the outer plate. We only require two bolts to hold the motor on and choose the two holes that form a line perpendicular to the c-c line between the motor pinion and the gear. This ensures that the motor bolts will be accessible at all times.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flipped-gb/s4.webp" style="width:100%">
      <figcaption>4. When sketching the inner plate, verify that there is clearance between the motor and the inner plates. Pay close attention to the tangency of all the edges so that the plate contour is smooth.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flipped-gb/s0.webp" style="width:100%">
      <figcaption>5. Model the shafts and pocket the gearbox plates. For the shafts, you can first estimate how long they need to be and then set them to the correct length after you complete the assembly.</figcaption>
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

**Next, navigate to the "Exercise #5 Assembly" tab** in your copied document and **refer to the solution document** to complete the assembly for this exercise. The **following instruction slides** only provide a general outline and some key details.

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flipped-gb/a0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flipped-gb/a1.webp" style="width:100%">
      <figcaption>1. Add the frame, gearbox plates, gearbox spacer, and shafts to the assembly. Like before, group mate the rigid components with the Origin Cube and mate the Origin Cube to the assembly origin.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flipped-gb/a2.webp" style="width:100%">
      <figcaption>2. Insert and fasten the motors and bearings.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flipped-gb/a3.webp" style="width:100%">
      <figcaption>3. Insert and fasten the power transmission components, which includes the gears, pinions, spacers, and sprocket. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flipped-gb/a4.webp" style="width:100%">
      <figcaption>4. Finally, insert and replicate all the required fasteners.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flipped-gb/a5.webp" style="width:60%">
      <figcaption>5. We use a single 1/2" spacer rather than two 1/4" spacers on each side of the gear to reduce part count. In real life, it's much easier to assemble if there's only one spacer, and centering the gear between the bearings has no tangible benefit. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/flipped-gb/a6.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>6. Check that the motors do not interfere with the inner plate with the <code>Check Interference</code> tool.</figcaption>
    </figure>
  </div>

  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flipped-gb/a0.webp" style="width:100%">
      <figcaption>7. To finish the assembly, organize your components into folders and name your replicates.</figcaption>
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
    Make sure to have you and/or a more experienced member/mentor of your team [**review your CAD!**](../1A/focusing-on-improvement.md "Focusing on Improvement Page"){:target="_blank"} Your assembly should have 30 instances.

### Interference Detection

Catch errors in the CAD rather than in real life! Always double and triple check your CAD models for mistakes like interferences. An extra 10 minutes verifying the correctness of your CAD can save you hours of rework if an erroneous part slips through and is fabricated.

!!! warning "Interference Detection"
    If an interference is detected with the Check Interference tool, it will highlight the intersected volumes in red.
    <figure>
      <img src="/img/learning-course/stage1c/flipped-gb/interference.webp" style="width:80%">
      <figcaption>Interference between a motor and plate detected by the Check Interference tool.</figcaption>
    </figure>

<br>