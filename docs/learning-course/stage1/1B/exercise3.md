

# 1B: Power Transmissions

## Exercise 3: Belt and Gear Transmission

In this exercise, you will be modeling a two stage gearbox that uses gears and belts. This gearbox will also include elements like frame and gussets, which you previously learned in Stage 1A. The goal of this exercise is to continue to ramp up your modeling skills. Always make sure to fully define your sketches and keep your feature and instance trees organized.

### Part Studio Instructions

**Navigate to the "Exercise #3 Part Studio" tab** in your copied document and **follow the instructions in the slides** to complete the part studio for this exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s0.webp" style="width:100%">
      <figcaption>0. Final part studio.</figcaption>
    </figure>
    </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s1.webp" style="width:100%">
      <figcaption>1. Draw the tube profiles for the frame. There is a an 1/8" gap between the slanted tube and the vertical tube to allow for assembly tolerances. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s2.webp" style="width:100%">
      <figcaption>2. Use the <code>Extrude Individual</code> Featurescript to extrude the tube profiles.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s3.webp" style="width:100%">
      <figcaption>3. Use the <code>Tube Converter</code> Featurescript to convert the rectangles into hole patterned 1x1 thin-wall tube (1/16" thick wall).</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s4.webp" style="width:100%">
      <figcaption>4. Use the <code>Gusset</code> Featurescript to add a corner gusset between the lower two tubes.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s5.webp" style="width:100%">
      <figcaption>5. Create the gearbox layout sketch on the outer face of the bottom tube. Begin by drawing the two gears, a 60T and 20T gear. The 60T gear is the output, and we would like to constrain it to a specific location given by the 2" and 4.5" dimensions.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s6.webp" style="width:100%">
      <figcaption>6. Next, draw the 5mm pitch 12T and 36T pulleys. Use a line to connect the two pulleys. Use the <code>#PulleyPD_5mm()</code> function to calculate the pitch diameters of the pulleys. Also space the 36T pulley to be 0.25" from the vertical tube. This step fully constrains the location of the gears.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s8.webp" style="width:100%">
      <figcaption>7. Add the belt c-c to the layout sketch for a 60T HTD5 belt using the <code>#BeltCTC_5mm()</code> function.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s9.webp" style="width:100%">
      <figcaption>8. Optionally draw two tangent lines to connect the two pulley circles. This represents the belt.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s10.webp" style="width:100%">
      <figcaption>9. Finally, sketch a 2.5" circle for the motor. Space the motor to be 1/8" away from the slanted tube. The layout sketch is now fully defined.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s11.webp" style="width:100%">
      <figcaption>10. Create the plate sketch on the outer face of the bottom tube. Begin by drawing the two 1.125" diameter bearing holes. Add a 0.95" for the bearing boss instead of the standard 0.8" so that the 12T pulley on the motor can fit through the hole to assist with real life assembly. This will become more clear when you create the gearbox assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s12.webp" style="width:100%">
      <figcaption>11. Add a 2" bolt circle for the motor with a circular pattern. Constrain the center of the top left hole to be coincident with the center line between the pulleys (coincident uses an infinite extension of the line) </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s13.webp" style="width:100%">
      <figcaption>12. Add the tube mounting holes for the plate. Note that the holes reference the edges of the tube and not the holes on the tube. This is to make the model more parametric, as changes in the tube can change the locations of the holes and break the gearbox plate sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s14.webp" style="width:100%">
      <figcaption>13. Draw the outline for the plate using centerpoint arcs and tangent lines. Space the bottom of the plate 0.25" from the edge of the pitch circle for the 60T gear. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s15.webp" style="width:100%">
      <figcaption>14. Add two holes for spacers. The construction circles represent the 3/8" diameter spacer. The top hole is tangent with the left edge of the plate and tangent with the 2.5" motor circle.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s16.webp" style="width:100%">
      <figcaption>15. Extrude the plate to be 1/4" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s17.webp" style="width:100%">
      <figcaption>16. On the opposite side, create a sketch for the inner plate. Utilize the <code>Use</code> sketch feature to copy over common geometry (holes, outline). Do not copy the motor holes, as there will be a cutout on the inner plate for the body of the motor.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s18.webp" style="width:100%">
      <figcaption>17. Finish the outline of the plate by adding an arc for the motor cutout.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s19.webp" style="width:100%">
      <figcaption>18. Extrude the inner plate to be 1/4" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s20.webp" style="width:100%">
      <figcaption>19. Add a 3/16" radius fillet on the two edges for the motor cutout. The radius is selected to match the 3/8" diameter spacer.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s21.webp" style="width:100%">
      <figcaption>20. Model the 3/8" diameter spacer. The <code>Up to Face</code> end condition can be utilized to keep the spacer length parametric.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e3/e3s22.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>21. Use the <code>Belt & Chain Gen</code> Featurescript to create a model of the belt. The pitch of the belt is 5mm and the width is 9mm. Offset the reference plane by 0.5" so that the belt does not collide with the plate. Optionally turn on teeth modeling - note that this option will significantly increase rebuild time. Notice that the <code>Belt & Chain</code> Featurescript also calculates the pitch length of the belt which allows us to verify that we calculated the correct C-C in step 7 and 8. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s23.webp" style="width:100%">
      <figcaption>22. Use the <code>Shaft Generator</code> Featurescript to create the 1st stage shaft. Note that this length is simply an estimate. While you could calculate the length of the shaft based on the components that will go on it, it is often easier to create the assembly then measure what the shaft length should be and update accordingly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s24.webp" style="width:100%">
      <figcaption>23. Use the <code>Shaft Generator</code> Featurescript to create the output shaft.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s25.webp" style="width:100%">
      <figcaption>24. Optionally pocket the plates. To begin, create a sketch on the outer face of the motor plate and draw lines to create the struts.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s26.webp" style="width:100%">
      <figcaption>25. Use the <code>Part Lighten</code> Featurescript to add the pocketing by selecting the previous sketch. Use 0.15" wide ribs and 0.26" tool diameter. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s27.webp" style="width:100%">
      <figcaption>26. Create a sketch on the inner plate and draw the strut lines. You can utilize the <code>Use</code> sketch feature to copy over strut lines from the motor plate pocketing sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s28.webp" style="width:100%">
      <figcaption>27. Use the <code>Part Lighten</code> Featurescript to add the pocketing by selecting the previous sketch. Again, use 0.15" wide ribs and 0.26" tool diameter. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3s0.webp" style="width:100%">
      <figcaption>28. Finished part studio. Name the key sketches and parts. Set the material of the plate and spacers to 6061 Aluminum. The tube, gusset, and shafts should have their material automatically set already. </figcaption>
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

Now that you've completed the part studio, **navigate to the "Exercise #3 Assembly" tab** in your copied document and **follow the instructions in the slides** to finish this exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3a0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e3/e3a1.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>1. Insert the part studio into the assembly and fix only the bottom tube. Use the group mate on the tubes, plates, and gusset. Copy the gusset and mate it to the other side of the tube. Next, mate the spacer to the plate and use the <code>Replicate</code> tool to replicate the spacer. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e3/e3a2.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Assemble the bearings and shafts using parts from the MKCad App. Use the <code>Replicate</code> tool to replicate the bearing.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e3/e3a3.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>3. Assemble the 36T pulley, belt, motor, and motor pinion pulley using parts from the MKCad App. Notice that the motor pinion is offset 1/16" from the bottom of the shaft to better align with the belt. Additionally, notice that the belt requires only a single fasten mate since its orientation was determined by how it was modeled in the part studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e3/e3a4.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Assemble the shaft spacers and gears using parts from the MKCad App. Notice that this time we used a pocketed gear for the 60T gear. Pocketed gears are the same as normal gears except they have some material removed to save weight. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e3/e3a5.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. At this point, you have all of the core components assembled and can update the length of the first stage shaft. Copy the measured shaft length and update the part studio accordingly. It is recommended to round up to the nearest 0.01" for manufacturability. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e3/e3a6.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>6. Assemble the shaft retention bolts using MKCad app parts.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e3/e3a7.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>7. Assemble the motor bolts, gearbox bolts, and nuts using the Onshape Standard Content and MKCad app parts</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1b/exercises/e3/e3a8.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>8. Assemble the gusset rivets using the MKCad app parts.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1b/exercises/e3/e3a0.webp" style="width:100%">
      <figcaption>9. Finished assembly. Make sure to sort your parts into folders and name your replicate features. </figcaption>
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

!!! note "Verification"
    If all is done correctly your assembly should have 31 Instances.

In this exercise, you modeled a fairly complex gearbox that was integrated with some frame elements. At this point, you should be begin to feel comfortable with the sketching and extrude tools. You should also familiarize yourself with all the options present in the Featurescripts that you have used up until this point by playing around with different settings. 



### Parametric Modeling

To get a feel for how parametric your model is, you can try and change certain key dimensions in the layout sketches, such as the length of the tubes, angle of the tubes, length of the belt, and the size of the gears. Play around with which modifications will update smoothly and which require additional fixes in the CAD.

You may also be curious as to how things like the hole sizes, materials, etc were selected in each of these designs. You are encouraged to learn more by browsing the [Design Handbook](/design-handbook/ "Design Handbook Page"){:target="_blank"} pages which contain in-depth information on a wide range of topics, or by discussing with your team and or other students and mentors on the DDS Discord.

<br>


