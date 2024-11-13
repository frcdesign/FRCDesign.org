# 1C: Practice Mechanisms

## Exercise 1: Flat Intake

In this exercise, you will be modeling a sort of flat game piece manipulator. This mechanism features live-axle compliant wheels, a belt reduction, and tube plugs.

### Tube Plugs
Tube plugs are a great way to build simple and robust structures.
Many vendors including [WCP](https://wcproducts.com/products/tube-plugs "WCP Tube Plug Product Page"){:target="_blank"}, [REV](https://www.revrobotics.com/MAXTube-Endcaps/ "REV Tube Plugs Product Page"){:target="_blank"}, [Andymark](https://www.andymark.com/products/tube-plugs "Andymark Tube Plug Product Page"){:target="_blank"}, and [Last Anvil](https://lastanvil.com/products/1-x-1-x-0-0625-end-cap "Last Anvil Tube Plug Product Page"){:target="_blank"} offer in various tubing sizes.
They can be used to connect plates to the open face of tubes or to connect tubes to each other without the use of a gusset.

???+ Example "Tube Plugs"
    <div class="grid cards" markdown>

    -   <center><img src="/img/learning-course/stage1c/flat-intake/high-tide-tube-plugs.webp" width="100%"></center>

    -   <center><img src="/img/learning-course/stage1c/flat-intake/miso-tube-plug.webp" width="100%"></center>

    </div>

    <figure>
      <figcaption>Tube plugs can be used to create gusset-less tube to tube (left) and tube to plate (right) connections. (Photo Credits: FRC 4414, FRC 9442)</figcaption>
    </figure>

This exercise also introduces you to the use of the the [`Assembly Mirror Featurescript`](https://cad.onshape.com/documents/0f7d68295ff4dab57adcf92c/v/88fbfa19a2e2555d18599db4/e/bcf3052f00f1f9d3d95a89c7?jumpToIndex=1392&showReturnToWorkspaceLink=true "Assembly Mirror FS Onshape Document"){:target="_blank"}. Make sure to add this to your Featurescripts if you have not already. 

- This featurescript generates allows you to mirror the position of a duplicate part in the assembly. 
- This is often useful so you can avoid creating a duplicate part in the part studio (to preserve the Bill of Materials) and keep the assembly parametric.
- The featurescript takes a part and a mirror plane and generates a pair of mate connectors to simulate an mirror in the assembly.
- In the assembly, you simply have to copy the part and mate it to the mate connector on the other side. Show mate connnectors by pressing the `k` key.


### Part Studio Instructions

**Navigate to the "Exercise #1 Part Studio" tab** in your copied document and **follow the instructions in the slides** to complete the part studio for this exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s1.webp" style="width:100%">
      <figcaption>1. Create the layout sketch on the Right plane. Begin by sketching the tube profiles. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s2.webp" style="width:100%">
      <figcaption>2. Using the Origin Cube functions you learned previously, sketch the pulleys and belt. This is a 5mm pitch 12T to 30T transmission with a 70T belt. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s3.webp" style="width:100%">
      <figcaption>3. Finish the layout sketch by sketching a 60 mm circle to represent the motor and a 2" circle for the intake wheel.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/flat-intake/s4.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Create the tube sketch plane by using an offset mate connector reference.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s5.webp" style="width:100%">
      <figcaption>5. Sketch the tubes by tracing over the layout sketch. There should be no dimensions in this sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s6.webp" style="width:100%">
      <figcaption>6. Extrude the lower and use tube converter to turn it into a thin-wall 1x1 with a 0.5" hole spacing pattern. We will create the upper tube in a later step.  </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s7.webp" style="width:100%">
      <figcaption>7. Create the plate sketch on the outside face of the 1x1 tube. Begin by sketching the bearing hole and motor bore hole.</figcaption>
    </figure>
  </div>

  <!-- switch  s8 to a video? -->

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s8.webp" style="width:100%">
      <figcaption>8. Sketch the 2" bolt circle for mounting motor. You can utilize the Origin Cube variable for a #10-32 clearance hole by typing <code>#10_32</code> into the dimension and selecting the <code>#Clearance_Fit_10_32</code> variable. Use a <code>Circular pattern</code> to pattern the hole sketch. Although we pattern the hole 6 times, we set three of them to construction geometry as we only need 3. Set the left most hole to be coincident with the centerline between the pulleys. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s9.webp" style="width:100%">
      <figcaption>9. Sketch the mounting holes by using a linear pattern. The tube holes are 0.196" in diameter (A #10-32 "close fit") so we will use the same size for the plate.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s10.webp" style="width:100%">
      <figcaption>10. Finish the plate sketch by drawing the plate outline around the sketch features.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s11.webp" style="width:100%">
      <figcaption>11. Extrude the plate to be 1/4" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s12.webp" style="width:100%">
      <figcaption>12. Create the pocketing sketch on the outside face of the plate. Sketch ribs to connect the mounting points.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s13.webp" style="width:100%">
      <figcaption>13. Use the <code>Part Lighten</code> Featurescript to pocket the plate. We use 3/16" rib and wall thickness, and 0.26" tool diameter.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s14.webp" style="width:70%">
      <figcaption>14. You may have noticed in the previous step that the pocketing created some unsightly bumps along the outside contour as a result of the mounting holes. We will make these edges smooth with a simple trick in the next slide. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s15.webp" style="width:100%">
      <figcaption>15. Open the pocketing sketch and sketch two lines spaced exactly half the pocketing wall thickness away from the outer edge of the mounting hole (NOT the center of the circle). In our case, this would be half of 3/16". This "tricks" the Part Lighten Featurescript by creating an extra rib where the bumps would have been.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s16.webp" style="width:100%">
      <figcaption>16. Edit the <code>Part Lighten</code> feature to include the two new ribs. The pocketed part should no longer have the bumps. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s17.webp" style="width:100%">
      <figcaption>17. To create a reference for extruding the upper tube, we use the <code>Mirror</code> feature to mirror the plate across the Right plane. Since we do not want to actually use this component in the assembly, we can change the color of the part and add <code>zREF</code> to the part name so that it will appear at the very bottom of the part list when inserting parts in the assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s18.webp" style="width:100%">
      <figcaption>18. Using the tube sketch we created earlier in the part studio, we can now extrude the upper tube profile up to the mirrored plate's inside face. This ensures that the upper tube is parametric to changes in intake width.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s19.webp" style="width:100%">
      <figcaption>19. Convert the solid into a 2x1 thin-wall tube with 0.5" hole pattern spacing. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s20.webp" style="width:100%">
      <figcaption>20. Sketch and extrude the 0.125" thick polycarbonate plate on the top face of the bottom tube. It will have a mounting hole in each corner and be spaced away from the edges of the 1x1 tube by 0.125".</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s21.webp" style="width:100%">
      <figcaption>21. Model the roller shaft with the <code>Shaft</code> Featurescript. You can estimate the length first and then adjust it once you create the assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s22.webp" style="width:100%">
      <figcaption>22. Model the belt using the <code>Belt & Chain Gen</code> Featurescript. Use a mate connector offset from the plate's bearing hole as the reference plane and offet by 3/8". Select the layout sketch pulley PDs to use as the guides.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/flat-intake/s23.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>23. Use the Assembly Mirror Featurescript (you can add this using the link above the slides). The featurescript will generate a mate connector at the origin of the selected part, and another at the center of the virtually mirrored part. The usage of these two mate connectors will become clear when we create the assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/s0.webp" style="width:100%">
      <figcaption>24. Finish the part studio by naming your features and organizing them into folders. Assign the part materials accordingly.</figcaption>
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

**Next, navigate to the "Exercise #1 Assembly" tab** in your copied document and **follow the instructions in the slides** to complete this exercise. 

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/a0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/flat-intake/a1.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>1. Insert all of the part studio components, except for the zREF part, and group the plates, tubes, and shaft with the origin cube. Fasten the cube to the origin.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/flat-intake/a2.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Copy the side plate and use the mate connectors generated by the <code>Assembly Mirror</code> Featurescript to fasten the plate into place. The location of the "mirrored" plate is fully parametric as the mate connectors generated by the Featurescript will automatically update when changes to the plate occur. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/flat-intake/a3.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>3. Insert the upper tube plugs and make a copy of the lower tube. Fasten all the components to their correct locations.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/a4.webp" style="width:100%">
      <figcaption>4. Insert the motor and roller pulleys and fasten them into place. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/flat-intake/a5.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. Fasten the belt to the roller pulley. Double check that the motor pulley is properly lined up with the belt.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/flat-intake/a6.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>6. Insert and fasten the Configurable Spacer Stack and flex wheel. The spacer stack is a configurable assembly that will automatically calculate the optimal stack of spacers to fill a gap. While this functionality is not used for this exercise, it will be very useful in later exercises. When fastening the Spacer Stack assembly, make sure to select the pre-generated mate connectors on each end and NOT the spacer body. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/flat-intake/a7.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>7. Use the <code>Linear Pattern</code> feature to pattern the spacer and wheel.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/flat-intake/a8.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>8. Copy the Spacer Stack and modify it to be 0.5" long, then fasten it into place to finish the roller.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/a9.webp" style="width:100%">
      <figcaption>9. Insert, fasten, and replicate 3/16" rivets from MKCad to attach the plate to the lower tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/a10.webp" style="width:100%">
      <figcaption>10. Insert, fasten, and replicate 0.5" long #10-32 bolts from the Standard Content Library for attaching the the tube plug on the upper tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/a11.webp" style="width:100%">
      <figcaption>10. Insert, fasten, and replicate 1/2" long 10-32 boltwashers from MKCad for shaft retention.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/a12.webp" style="width:100%">
      <figcaption>11. Insert, fasten, and replicate 0.5" long #10-32 bolts from the Standard Content Library for attaching the motor.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/a13.webp" style="width:100%">
      <figcaption>12. Insert, fasten, and attach 1.5" long #10-32 bolts from the Standard Content Library for attaching the polycarb panel. Also add #10-32 thin jam nuts from MKCad Library.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/a0.webp" style="width:100%">
      <figcaption>13. Finish your assembly by organizing the parts into folders and naming your replicates.</figcaption>
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
    Make sure to have you and/or a more experienced member/mentor of your team [**review your CAD!**](../1A/focusing-on-improvement.md "Focusing on Improvement Page"){:target="_blank"} Your assembly should have 32 instances.

### Parametric Modeling

Some of the steps we took to complete this exercise could have been simplified.
For instance, we didn’t necessarily *need* to use the Assembly Mirror feature for the plate.
We didn’t *need* to use an “Up to face” extrude for the upper tube. 

However, we practice these techniques because, while they may marginally increase modeling time upfront, they can save ***significant*** amounts of time when going back and editing.
CAD is an iterative process — your models and designs won’t be perfect the first time around, so making your model easier to modify and more robust to changes (e.g., changing the width of this intake) will save you time and effort in the long run.
As you use best practices, they’ll become second nature.

!!! question "Tweaking Your Model"
    Try playing around to get a feel for what things are and aren't parametric in exercise 1. You can try changing things like the width, length, tube positions, or gear ratio. Which dimensions are easy to change and which are difficult? Which dimension changes cause rebuild or assembly error?

<br>