# 1C: Practice Mechanisms

## Exercise 1: Flat Intake

In this exercise, you will be modeling a sort of flat game piece manipulator. This mechanism features live-axle compliant wheels, a belt reduction, and tube plugs.

### Tube Plugs
Tube plugs are a great way to build simple and robust structures.
Many vendors including [WCP](https://wcproducts.com/products/tube-plugs "WCP Tube Plug Product Page"){:target="_blank"}, [REV](https://www.revrobotics.com/MAXTube-Endcaps/ "REV Tube Plugs Product Page"){:target="_blank"}, [Andymark](https://www.andymark.com/products/tube-plugs "Andymark Tube Plug Product Page"){:target="_blank"}, and [Last Anvil](https://lastanvil.com/products/1-x-1-x-0-0625-end-cap "Last Anvil Tube Plug Product Page"){:target="_blank"} offer in various tubing sizes.
They can be used to connect plates to the open face of tubes or to connect tubes to each other without the use of a gusset.

???+ Example "Tube Plugs"

    <div class="grid cards" markdown>

    -   <center markdown><img src="/img/learning-course/stage1c/flat-intake/high-tide-tube-plugs.webp" width="100%"></center>

    -   <center markdown><img src="/img/learning-course/stage1c/flat-intake/miso-tube-plug.webp" width="100%"></center>

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
      <img src="/img/learning-course/stage1c/flat-intake/PS-S0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S1.webp" style="width:100%">
      <figcaption>1. Start the layout sketch on the Right plane. Begin by sketching the shape of the bottom tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S2.webp" style="width:100%">
      <figcaption>2. Draw a rectangle on top of the tube to represent the floor of this intake</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S3.webp" style="width:100%">
      <figcaption>3. Create a circle to represent the wheels, and a circle to represent the motor. Use the origin cube belt ctc function to position them correctly, this is similar to the layout sketch in 1B Exercise 3</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S4.webp" style="width:100%">
      <figcaption>4. Draw the pitch circles for both pulleys and add connecting lines for them to represent the belt path. Use the origin cube PulleyPD function to define the pulley circles</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S5.webp" style="width:100%">
      <figcaption>5. Draw a rectangle to represent a 2x1 tube. This should be dimensioned above from the wheels and aligned with the edge of the bottom tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S6.webp" style="width:100%">
      <figcaption>6. Create a new sketch using a mate connector offset from the origin. This sketch should be offset in the "Right" direction as shown.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S7.webp" style="width:100%">
      <figcaption>7. Transfer the rectangles for the tubes from the layout sketch using the "Use" tool. Make sure these are not construction lines as you will need to extrude them.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S8.webp" style="width:100%">
      <figcaption>8. Extrude the bottom tube by 1" and apply Tube Converter to it</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S9.webp" style="width:100%">
      <figcaption>9. Start a sketch on the Right side of the 1x1 tube. Make sure to disable imprinting. Add circles centered on the motor and wheel circles from the layout sketch. Also transfer the CTC line with the use tool.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S10.webp" style="width:100%">
      <figcaption>10. Create the bolt circle pattern by drawing a circle on the CTC line, then use the pattern tool to duplicate it around the motor center point. This pattern should have 8 holes, and have a diameter of 2" to match the standard 2" motor bolt circle. We only need 3 of the 8 holes on this pattern so make the rest construction holes.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S11.webp" style="width:100%">
      <figcaption>11. Add mounting holes along the bottom tube, spaced 2" apart. Add two more hole centered on the top tube spaced 1" apart.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S12.webp" style="width:100%">
      <figcaption>12. Draw the plate outline around the holes. Draw arcs around all of the edge holes and connect them with tangent lines.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S13.webp" style="width:100%">
      <figcaption>13. Extrude to create the plate. If you properly disabled imprinting on slide 9 you should only have one face to select to extrude this plate.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S14.webp" style="width:100%">
      <figcaption>14. Mirror this plate across the Right plane to create a reference plate. You should color this plate an abnormal color so it is easily distinguishable from the main plate. Name this reference plate "zREF Plate". This will make it appear at the bottom of the insert menu, making it harder to accidentally use in the assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S15.webp" style="width:100%">
      <figcaption>15. Extrude the top tube shape. Make sure to use the "Up to Face" setting to extrude the tube parametrically to the reference plate.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S16.webp" style="width:100%">
      <figcaption>16. Use Tube Converter on this new tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S17.webp" style="width:100%">
      <figcaption>17. Make a sketch on top of the 1x1 tube, again making sure to disable imprinting. Sketch the plate as shown.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S18.webp" style="width:100%">
      <figcaption>18. Use the Robot Belt Featurescript to make a belt between the motor and wheel holes. Pay close attention to the starting offset and teeth values.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S19.webp" style="width:100%">
      <figcaption>19. Create the wheel shaft using the Robot Shaft Featurescript. The start mate connector should be placed in the middle of the belt and run up to the left face of the reference plate. The shaft should be offset from the end by 1/16" to account for the bearing flange. The shaft should also have a starting offset of 9/32" to put it through the wheel pulley.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S20.webp" style="width:100%">
      <figcaption>20. Now that our parts are all done, we can pocket the side plate. Create a sketch on the Right side of the plate, and draw the rib lines. The top left line is dimensioned away from the top bolt holes.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/flat-intake/PS-S21.webp" style="width:100%">
      <figcaption>21. Use the Part Lighten Featurescript to pocket the plate. Select the face of the plate, and the entire rib line sketch as shown.</figcaption>
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