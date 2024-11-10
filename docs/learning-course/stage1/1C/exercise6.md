# 1C: Practice Mechanisms

## Exercise 6: Direction Swap

In this exercise, you will be modeling a power transmission with a direction swap gear. 
This mechanism features features a 1:1 gear transmission that inverts the direction of the motor, which can be useful when you want two different shafts to be powered by the same motor but spin in opposite directions.
Be sure to pay attention to the layout and plate sketches when modeling. 

### 3D Printed, COTS, and Custom Aluminum Spacers
So far, you've used both custom spacers generated with the `Spacer` Featurescript as well as COTS 3/8" OD spacers from the MKCad library (the [WCP Aluminum Spacers](https://wcproducts.com/products/aluminum-spacers "WCP Aluminum Spacers Product Page"){:target="_blank"}).
There are pros and cons to using COTS or custom spacers that you should discuss with your team.

3D printed spacers are a fantastic option for teams with 3D prints, they are cheap and easy to fabricate. 
If you want to use aluminum spacers but do not have access to machinery to cut them (e.g. a lathe), COTS aluminum spacers can be a good option as they can also be pre-stocked.
However, they can be pricy and only come in certain lengths, though you can easily get around this by designing for standard spacer lengths.

???+ Example "Spacer Stock"
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/spacers.webp" width="100%">
      <figcaption>Spacers can be 3D printed (left), purchased as COTS pre-cut spacers (center), or fabricated in-house from spacer stock (right). (Image Source: WCP)</figcaption>
    </figure>

When modeling, it is recommended to use the `Spacer` Featurescript for spacers that you will fabricate in house (e.g. 3D printing or using [round tube stock](https://wcproducts.com/products/shaft-stock "WCP Tube Stock Product Page"){:target="_blank"}) and use the configurable MKCad spacer part for COTS spacers.
This helps make it clear which parts are custom and which are COTS.

### Part Studio Instructions

**Navigate to the "Exercise #6 Part Studio" tab** in your copied document and **refer to the solution document** to complete the part studio for this exercise. The **following instruction slides** only provide a general outline and some key details.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/s0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/s1.webp" style="width:100%">
      <figcaption>1. Begin by creating the layout sketch on the right plane. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/s2.webp" style="width:100%">
      <figcaption>2. Using a mate connector offset 0.5" from the Right plane as the sketch plane, sketch the plate. 
                  Pay close attention to the clearances used to define the edges of the plate.
                  The location of the two spacers to the left of the motor are driven by the tangency between the 3/8" OD spacer and the 2.5" motor clearance circle.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="100%" controls>
        <source src="/img/learning-course/stage1c/dir-swap/s3.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>3. Use a <code>Driven Dimension</code> to show the distance between the left gear and the spacer and verify that there is enough clearance. A driven dimension, as opposed to a driving dimension, just reports the distance between the selected elements and is faded gray to indicate that it does not define the sketch geometry.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/s4.webp" style="width:100%">
      <figcaption>4. Mirror the plate across the Right plane and add the motor cutout.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/s5.webp" style="width:100%">
      <figcaption>5. If you choose to not use COTS spacers, you can use the <code>Spacer</code> Featurescript to create the plate spacer.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/s6.webp" style="width:100%">
      <figcaption>6. Model all of the shafts and belts. You should be feeling very comfortable using the <code>Shaft</code> and <code>Belt & Chain Gen</code> Featurescripts at this point.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/s7.webp" style="width:100%">
      <figcaption>7. Pocket the two plates. Since the plates are identical apart from the motor cutout, you can use same sketch to pocket both plates. Only create one sketch with the ribs.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/s0.webp" style="width:100%">
      <figcaption>8. Finish the part studio by naming your features and organizing them into folders. Assign the part materials accordingly.</figcaption>
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

**Next, navigate to the "Exercise #6 Assembly" tab** in your copied document and **refer to the solution document** to complete the assembly for this exercise. The **following instruction slides** only provide a general outline and some key details.

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/a0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/a1.webp" style="width:100%">
      <figcaption>1. Add the part studio parts to the assembly. Like before, group mate the rigid components with the Origin Cube and mate the Origin Cube to the assembly origin.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/a2.webp" style="width:100%">
      <figcaption>2. Fasten the spacer to the plate and replicate it.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/a3.webp" style="width:100%">
      <figcaption>3. Insert, fasten, and replicate the bearings. Also insert the 2" flex wheel and Kraken motor from MKCad.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/a4.webp" style="width:100%">
      <figcaption>4. Insert and fasten the pulleys pulleys and spacers. Use the Configurable Spacer Stack from MKCad for all the spacers. 
                  For the pulleys, you can utilize 3D printed HTD pulleys from the MKCad library with 1/2" hex inserts.
                  Also fasten the belts into place. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/a5.webp" style="width:100%">
      <figcaption>5. Insert, fasten, and replicate all of the required fasteners.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/a6.webp" style="width:100%">
      <figcaption>6. When replicating the plate bolts, flip the mounting side for this bolt so that the nut does not hit the belt. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/dir-swap/a0.webp" style="width:100%">
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
    Make sure to have you and/or a more experienced member/mentor of your team [**review your CAD!**](../1A/focusing-on-improvement.md) Your assembly should have 38 instances.


### Driving and Driven Dimensions

In sketches, driving dimensions define and control the geometry, appearing black and editable. 
Driven dimensions,on the other hand, are light gray and reflect existing geometry without altering it, useful for maintaining design intent like keeping a specific clearance or thickness. 

To toggle between them, right-click the dimension and select "Driving/Driven" from the context menu—useful when a new dimension would over-constrain the sketch or when you need to inspect geometry without changing it.

!!! tip "Switching Between Driving and Driven Dimensions"
    <figure>
      <video width="100%" controls>
        <source src="/img/learning-course/stage1c/dir-swap/driven-dims.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>Switch a dimension from driving to driven and vice versa by right-clicking the dimension. Notice that the driven dimension will update based on other features.</figcaption>
    </figure>

<br>
