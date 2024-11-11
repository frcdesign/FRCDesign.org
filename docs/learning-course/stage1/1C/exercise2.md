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

This exercise introduces you to the use of the [Configurable Rollers Document](https://cad.onshape.com/documents/b75886a5660c38eee7d50e47/w/58faeca16d5b2008a9485b5c/e/6274f59b451ed6222cd7523d "Configurable Rollers Onshape Document"){:target="_blank"}. The assembly instruction slides have you copy this link to insert the rollers.

<!-- [`Assembly Mirror` Featurescript](https://cad.onshape.com/documents/0f7d68295ff4dab57adcf92c/v/88fbfa19a2e2555d18599db4/e/bcf3052f00f1f9d3d95a89c7?jumpToIndex=1392 "Assembly Mirror Featurescript"){:target="_blank"}. -->

### Part Studio Instructions

**Navigate to the "Exercise #2 Part Studio" tab** in your copied document and **follow the instructions in the slides** to complete the part studio for this exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s1.webp" style="width:100%">
      <figcaption>1. Start the layout sketch on the Right Plane. Sketch the hole for a bearing and four #10-32 clearance holes on a 2" bolt circle. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s2.webp" style="width:100%">
      <figcaption>2. Sketch the pulleys and belt paths for the first two rollers. You will use 5mm pitch 24T pulleys. We subtract 0.015" from the calculated c-c distance to decrease the friction that results from linking together multiple belts. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s3.webp" style="width:100%">
      <figcaption>3. Add the pulley and belt path for the 3rd roller.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s4.webp" style="width:100%">
      <figcaption>4. Sketch 2" construction circles to represent the rollers, which are 2" OD. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s5.webp" style="width:100%">
      <figcaption>5. Sketch the pulleys and belt path for the motor. Since the motor transmission will also utilize a 24T pulley, we can reutilize the same pulley PD sketch from the first roller. The motor pulley will be a 12T pinion.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s6.webp" style="width:100%">
      <figcaption>6. Sketch the OD of the Kraken motor, which is 60 mm.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s7.webp" style="width:100%">
      <figcaption>7. Create the plate sketch by using an offset mate connector from the layout sketch as the origin entity. Select the motor pulley and offset by 12".</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s8.webp" style="width:100%">
      <figcaption>8. Sketch the plate outline. Pay attention to the sketch constraints in the solutions document. We offset the curve on the top right 0.25" away from the belt to that it is fully covered by the plate.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s9.webp" style="width:100%">
      <figcaption>9. Add the holes for the mounting point by using the <code>Use</code> feature and selecting the layout sketch entities to convert over.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s10.webp" style="width:100%">
      <figcaption>10. Sketch the motor bore and #10-32 clearance holes for motor mounting. Note that we only use 3 out of 6 of the patterned mounting holes, the rest are left as construction geometry. Also sketch the #10-32 clearance holes for the dead axle shafts. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s11.webp" style="width:100%">
      <figcaption>11. Extrude the plate to be 1/4" thick. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/dead-axle-rollers/s12.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>12. Add the 9 mm wide HTD 5mm belts. Use the plate as the reference plane and select the pulley PDs from the layout sketch. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s13.webp" style="width:100%">
      <figcaption>13. Your belt tooth count and pitch length should match the solution document. The two 70T belts have a pitch length slightly less than 350 mm since we subtracted 0.015" from the c-c's in the layout. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s14.webp" style="width:100%">
      <figcaption>14. Use the Assembly Mirror Featurescript to add a mate connector for mating the opposite side plate. There is no reason to use a part mirror since the two plates will be identical and we have no need to reference the other plate in the part studio. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/s0.webp" style="width:100%">
      <figcaption>15. Finish the part studio by naming your features and organizing them into folders. Assign the plate material to be polycarbonate. </figcaption>
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
      <img src="/img/learning-course/stage1c/dead-axle-rollers/a0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/dead-axle-rollers/a1.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>1. Insert the parts from the part studio and group the plate with the Origin Cube. Fasten the Origin Cube to the origin. We leave the belts un-grouped since they should be fastened to the pulleys. </figcaption>
    </figure>
  </div>

  <div id="slide1" class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/dead-axle-rollers/a2.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Copy the plate and fasten the plate's mate connector to the mate connector generated by the <code>Assembly Mirror</code> Featurescript.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/dead-axle-rollers/a3.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>3. Insert the Configurable Roller assembly from the link at the top of this page. 
                  Follow the settings exactly as described to generate a 24" wide, 2" OD roller with 24T HTD 5mm pulleys on each end. 
                  The length specified is the <i>effective length</i> meaning the distance between the plates, not the length of the roller itself.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/dead-axle-rollers/a4.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Copy the roller assembly two more times and fasten them to the plate. Make sure you select the entire roller assembly when you copy, otherwise it will only copy one of the roller parts instead of the entire roller assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/dead-axle-rollers/a5.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. Fasten the belts to their respective pulleys.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/dead-axle-rollers/a6.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>6. Using MKCad, insert a 3/8" OD, 1" long spacer that we will use for mounting the motor. Fasten it to the plate and then replicate it.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/dead-axle-rollers/a7.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>7. Insert the Kraken motor and mate it to the spacers. While in most cases we wouldn't care to align the motor exactly with the mounting holes, since we are mounting to spacers, we need to align it properly. To do so, use a revolute and a cylindrical mate. 
                  Also insert and fasten the motor pulley.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/a8.webp" style="width:100%">
      <figcaption>8. Insert a 1.5" long, #10-32 button head bolt for the motor. Fasten one instance and replicate the other two.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/a9.webp" style="width:100%">
      <figcaption>9. Insert a 3/4" long, #10-32 button head bolt for the roller shafts. Fasten one instance and replicate the other 5.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dead-axle-rollers/a0.webp" style="width:100%">
      <figcaption>10. Finish your assembly by organizing the parts into folders and naming your replicates.</figcaption>
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
    Make sure to have you and/or a more experienced member/mentor of your team [**review your CAD!**](../1A/focusing-on-improvement.md "Focusing on Improvement Page"){:target="_blank"} Your assembly should have 17 instances.

### Minimizing Unique Part Count

You may have noticed that the 3rd roller has a 24T pulley on both ends despite there only being a belt connected to one end. 
While the configurable roller does allow you to choose no pulley for the end with no belt, it can be advantageous to still keep the pulley in situations like this to reduce the number of unique parts. 
By doing so, all three rollers are identical, making part tracking and spare parts easier.

<br>
