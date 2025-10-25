# 1C: Practice Mechanisms

## Exercise 3: Ball Shooter

Starting with exercise 3, the instruction slides will only provide part-by-part instructions and key details. 
For exact feature details, you should refer to the exercise solutions document. 
This is to prepare you for later exercises that are gradually less guided.

In this exercise, you will be modeling a very simple 2.5" ball shooter. 
This mechanism features 3D-printed pulleys, a 3D-printed ramp, and nut strips. Be sure to pay attention to layout sketches when modeling. 

### 3D-printed Pulleys
Thus far, you've only utilized COTS pulleys in your assemblies. 
However, 3D-printed pulleys are a fantastic alternative since they are cheaper, readily available (assuming you have a 3D printer), and highly customizable.
<!-- Most applications that utilize pulleys (rollers, shooter wheels, etc) are low torque so 3D-printed pulleys provide more than adequate strength. -->

3D-printed pulleys can easily be generated using pulley generators, such as the ones included in FRCDesignLib and the Robot Pulley Featurescript.
However, close attention must be paid to the shaft interface. 3D-printed hex profiles can easily strip out, so a metal insert (Available from vendors like [WCP](https://wcproducts.com/products/adapters "WCP Adapater Product Page"){:target="_blank"} or [Thrifty Bot](https://www.thethriftybot.com/products/qty-5-aluminum-insert-for-3d-printed-parts "Thrifty Bot 3D Print Adapter Product Page"){:target="_blank"}) should be used to better transfer torque.
Take a look below at some examples of 3D-printed pulleys with different types of inserts. 

???+ example "3D-printed Pulley Inserts"
    <figure>
      <img src="/img/learning-course/stage1c/shooter/3dp-pulleys.webp" style="width:80%">
      <figcaption>3D-printed pulleys with hex insert for hex shaft (left), SplineXS insert for Kraken motors (center), and pinion gear insert for NEO/CIM motors (right). </figcaption>
    </figure>

!!! Warning
    Since 3D-printed pulley bores are easily worn out, you should try to always use a metal insert or a pinion gear insert.
    A cheap alternative to buying COTS inserts is to order them from a laser cutting service like [Fabworks](https://www.fabworks.com "Fabworks Sheet Metal Cutting"){:target="_blank"}. In large quantities (~20 pieces), they only cost around $1 each.

### Nut Strips
Nut strips are a very versatile structural component often used to connect perpendicular plates or a plate to a tube.
Vendors like [WCP](https://wcproducts.com/products/nut-strips){:target="_blank"}, [REV](https://www.revrobotics.com/3-8in-nut-strips/ "REV Nut Strips Product Page"){:target="_blank"}, and [Last Anvil](https://lastanvil.com/products/nut-strip){:target="_blank"} carry nut strips in 6" long segments with either #10-32 or #8-32 tapped holes.
These nut strips are very robust and can be easily cut to any length.
In the exercise you just completed, the nut strips would allow you to easily mount the shooter onto any surface.

???+ example "Nut Strips"
    <figure>
      <img src="/img/learning-course/stage1c/shooter/nut-strips-real.webp" style="width:65%">
      <!-- <figcaption>Example of using a nut strip to connect two perpendicular plates (left) as well as a plate to a tube (right)</figcaption> -->
      <figcaption>Nut strips can be used to connect a plate to a tube or a plate to a perpendicular plate. (Photo Credits: FRC 4414)</figcaption>
    </figure>

### Block Motors
When creating mechanisms, sometimes you need to reference specific COTS components when creating custom parts. While most of the time construction geometry in sketches will suffice (think motor outlines), sometimes you need to make more complex references. Instead of deriving a full detail component into the part studio (which can significantly slow down load times), you can create or derive "block" geometry, like the "block motor" from FRCDesignLib used in this exercise. 

<figure>
  <img src="../images/exercise-3/block-motor-example.webp" style="width:90%; border:5px solid #ADADAD">
</figure>

When inserting a block motor from FRCDesignLib, it is important to use the "Differentiation Variable" because of how Onshape handles derived parts. Assigning a unique value to each block motor prevents these errors in your part studio.

### Part Studio Instructions

**Navigate to the "Exercise #3 Part Studio" tab** in your copied document and **follow the instructions in the slides** to complete the part studio for this exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/parts-0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/parts-1.webp" style="width:100%">
      <figcaption>1. Create the layout sketch on the Right plane. Begin by sketching the 4" shooter wheel, 2" feeder wheel, and the ball path. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/parts-2.webp" style="width:100%">
      <figcaption>2. On the right plane, create a new sketch with the belts, pulleys, and motors. The bottom most construction line defines the bottom of our shooter.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/parts-3.webp" style="width:100%">
      <figcaption>3. Using a mate connector offset 1.375" from the layout sketch plane as the sketch plane, sketch the side plate. Use a circular pattern to sketch the #10-32 clearance holes around the shooter hood. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/parts-4.webp" style="width:100%">
      <figcaption>4. Extrude the plate as 1/4", then mirror it across the Right plane. We use a mirror because the opposite side plate is the same except for an extra cutout for the motors.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/parts-5.webp" style="width:100%">
      <figcaption>5. Sketch a cutoff boundary to remove the motor mounting from the mirrored plate. Make sure imprinting is enabled. You don't need to sketch the whole region, since the plate outline itself will be used in the extrude.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/parts-6.webp" style="width:100%">
      <figcaption>6. Extrude the motor mounting region on the mirrored part to remove the geometry from the part.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/parts-7.webp" style="width:100%">
      <figcaption>7. Model the large 3D print that goes in between the plates. There should only be three dimensions you need to sketch, all other entities should be defined by the layout or plate geometry. Use an "Up to face" extrude to ensure that the width is parametric.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/rGf0Vt8ahOQ?si=5FDcsAFnDDLgelkz" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption>8. Use the <code>Fillet All Edges</code> Featurescript to add a 3/16" radius fillet to all of the 3D-printed part edges. To select the face of the part, you can utilize the <code>Isolate</code> tool, which will make all other components that are not currently selected transparent or hidden.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
        <iframe src="https://www.youtube.com/embed/DUJ8MbPS4Zg?si=sLsoXcp6KuWWdfuR" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption>9. Insert a block motor from FRCDesignLib. Use the <code>Transform</code> feature to transform the block motor to the motor bore.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/parts-10.webp" style="width:100%">
      <figcaption>10. Add the HTD 5mm pitch belts. Double check that the pitch length is a multiple of 5 mm to ensure that the belt has an integer number of teeth.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
        <iframe src="https://www.youtube.com/embed/wFNDLm2Tisc?si=IDRokT62-V330Awh" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption>11. Model the shooter wheel and feeder wheel shaft using the <code>Robot Shaft</code> featurescript.</figcaption>
    </figure>
  </div> 

  <div class="mySlides fade">
    <figure>
        <iframe src="https://www.youtube.com/embed/L8HWApw3luM?si=p6KEZF1owz2MqMD3" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption>12. Add a mate connector on the layout sketch for fastening the feeder wheel. Set the owner of the mate connector to the feeder shaft. This mate connector marks the center point between the two plates and will help with assembly.</figcaption>
    </figure>
  </div> 

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/parts-13.webp" style="width:100%">
      <figcaption>13. Repeat the same steps as before to add a mate connector to the shooter wheel shaft. Make sure you select the shooter wheel shaft as the mate connector owner.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/parts-0.webp" style="width:100%">
      <figcaption>14. Finish the part studio by naming your features and organizing them into folders. </figcaption>
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

**Next, navigate to the "Exercise #3 Assembly" tab** in your copied document and **follow the instructions in the slides** to complete this exercise. 

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/assy-0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/assy-1.webp" style="width:100%">
      <figcaption>1. Insert all the part studio components. Group all the components except for the shafts and belts. Fasten the Origin Cube to the origin.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
        <iframe src="https://www.youtube.com/embed/7Zplj3xG83s?si=AJfLODE8KtOT2PCc" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption>2. Insert and fasten 4.5" long nut strips from the FRCDesignLib app. Pay close attention to which side is fastened to the plate—the nut strip holes on adjacent sides are staggered.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/assy-3.webp" style="width:100%">
      <figcaption>3. Insert and fasten the two NEO motors. Insert, fasten, and replicate the bearings. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/RsCl6xD8tMs?si=_urVOe5uRayJJMCc" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption>4. Insert and configure the shooter pulley to be 24T with 1/2" Hex w/ TTB insert. 
                  Copy and paste the pulley and TTB insert to create the motor pulley.
                  Using a 3/16" spacer, fasten the shooter pulley to the shooter bearing. 
                  Then, fasten the motor pulley to the belt. 
                  Finally, use the <code>Isolate</code> tool to fasten the 8mm NEO shaft to 1/2" hex adapter.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/vEuopW1B9r4?si=ZSKo9ywlPG_gwWsj" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption>5. Insert and configure the feeder pulley to be 36T with a TTB 1/2" hex insert. 
                  Configure the motor pulley to be 18T with a 12T 20DP gear insert. 
                  Using a 1/16" spacer, fasten the feeder pulley to the feeder bearing. 
                  Then, fasten the motor pulley to the belt. 
                  Finally, use the <code>Isolate</code> tool to fasten the 12T motor pinion.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/assy-6.webp" style="width:100%">
      <figcaption>6. Fasten the shafts to the pulleys. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <iframe src="https://www.youtube.com/embed/GuyhDXkKwho?si=0zYPMbq9xaxIE9MS" width="768" height="432" frameborder="0" allowfullscreen></iframe>
      <figcaption>7. Insert and fasten the shooter and feeder wheels to the shaft centering mate connectors. 
                  Then, Use the <code>Measure</code> tool to measure the gaps between the bearings and the wheels.
                  Create spacers to fill the gaps on the sides of the wheels.
                  Finally, use the <code>Assembly Mirror</code> tool to mirror the spacers and the shooter wheel across the feeder wheel's mate connector.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/assy-8.webp" style="width:100%">
      <figcaption>8. Insert and fasten the 4" SDS Flywheel to the other side of the shooter. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/assy-9.webp" style="width:100%">
      <figcaption>9. Insert, fasten, and replicate all of the required fasteners and remaining hardware.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/exercise-3/assy-0.webp" style="width:100%">
      <figcaption>10. Finish your assembly by organizing the parts into folders and naming your replicates. You can also insert and position the ball to visualize it. </figcaption>
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
    Make sure to have you and/or a more experienced member/mentor of your team [**review your CAD!**](../1A/focusing-on-improvement.md "Focusing on Improvement Page"){:target="_blank"} Your assembly should have 54 instances.

### Isolate, Hide, and Make Transparent

The Isolate tool hides all other parts except the selected ones, helping focus on specific components. 
The Hide tool removes the selected parts from view, while Make transparent allows you to see through the selected parts without removing it, useful for accessing obscured components. 

Rather than deleting or moving parts, you should use these tools to access the parts you need for your task. If you hide parts, don't forget to un-hide them for the next person!

<!-- TODO: Update to new video -->
!!! Tip "Isolate, Hide, and Make Transparent"
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/shooter/isolate-hide-transparent.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>Isolate parts, hide parts, or make parts transparent to help with assembly. </figcaption>
    </figure>

!!! Tip "Keyboard Shortcuts"
    Just like most other tools and constraints in Onshape, hide/show has a nice keyboard shorctut combination. Hover over a part with your cursor or select it and press `y` to hide it. Hover over the same space and press `shift+y` to unhide the part.


<br>