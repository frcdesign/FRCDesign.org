# 1E: Practice Mechanisms

## Exercise 3: Ball Shooter

Starting with exercise 3, the instruction slides will only provide part-by-part instructions and key details. 
For exact feature details, you should refer to the exercise solutions document. 
This is to prepare you for later exercises that are gradually less guided.

In this exercise, you will be modeling a very simple 2.5" foam ball shooter. 
This mechanism features 3D printed pulleys, a 3D printed ramp, and nut strips. Be sure to pay attention to layout sketches when modeling. 

### 3D Printed Pulleys
Thus far, you've only utilized COTS pulleys in your assemblies. 
However, 3D printed pulleys are a fantastic alternative since they are cheaper, readily available (assuming you have a 3D printer), and highly customizable.
<!-- Most applications that utilize pulleys (rollers, shooter wheels, etc) are low torque so 3D printed pulleys provide more than adequate strength. -->

3D printed pulleys can easily be generated using pulley generators, such as the one included in MKCad.
Close attention must be paid to the shaft interface however. 3D printed hex profiles can easily strip out, so a metal insert (Available from vendors like [WCP](https://wcproducts.com/products/adapters "WCP Adapater Product Page"){:target="_blank"} or [Thrifty Bot](https://www.thethriftybot.com/products/qty-5-aluminum-insert-for-3d-printed-parts "Thrifty Bot 3D Print Adapter Product Page"){:target="_blank"}) should be used to better transfer torque.
Take a look below at some examples of 3D printed pulleys with different types of inserts. 

???+ example "3D Printed Pulley Inserts"
    <figure>
      <img src="/img/learning-course/stage1e/shooter/3dp-pulleys.webp" style="width:100%">
      <figcaption>3D printed pulleys with hex insert for hex shaft (left), SplineXL insert for Kraken motors (center), and pinion gear insert for Neo/CIM motors (right). </figcaption>
    </figure>

### Nut Strips
Nut strips are a very versatile structural component often used to connect perpendicular plates or a plate to a tube.
Vendors like [WCP](https://wcproducts.com/products/nut-strips){:target="_blank"} and [Last Anvil](https://lastanvil.com/products/nut-strip){:target="_blank"} carry nut strips in 6" long segments with either #10-32 or #8-32 tapped holes.
These nut strips are very robust and can be easily cut to any length. 

???+ example "Nut Strips"
    <figure>
      <img src="/img/learning-course/stage1e/shooter/nut-strips-real.webp" style="width:80%">
      <!-- <figcaption>Example of using a nut strip to connect two perpendicular plates (left) as well as a plate to a tube (right)</figcaption> -->
      <figcaption>Nut strips can be used to connect a plate to a tube or a plate to a perpendicular plate. (Photo Credits: FRC 4414)</figcaption>
    </figure>


### Part Studio Instructions

**Navigate to the "Exercise #3 Part Studio" tab** in your copied document and **follow the instructions in the slides** to complete the part studio for this exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/shooter/s0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1e/shooter/s1.webp" style="width:100%">
      <figcaption>1. </figcaption>
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
      <img src="/img/learning-course/stage1e/shooter/a0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1e/shooter/a1.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>1.  </figcaption>
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
    If all is done correctly your assembly should have XX Instances.

<br>