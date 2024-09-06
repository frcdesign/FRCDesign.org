<style>
* {box-sizing:border-box}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Hide the images by default */
.mySlides {
  display: none;
}
#slide1 {display:block}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 250px;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 3px 3px 3px 3px;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.6);
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 0.25s;
}

@keyframes fade {
  from {opacity: .4}
  to {opacity: 1}
}
</style>

# 1B Power Transmissions

## Belts and Pulley Basics

Timing belt and pulley drives are mechanical systems used to transmit motion and power between rotating shafts using flexible belts and pulleys. The system consists of two main components: the belt, which is a flexible loop made of a material like rubber, and the pulleys, which are wheels with grooves that the belt wraps around. As one pulley rotates, it drives the belt, which in turn drives the other pulley, transferring motion and power from one shaft to another


<center><img src="\img\learning-course\stage1b\belt\beltAndPulley.webp" style="width:50%"></center>
<center>*A belt and pulley transmission. (Image Source: [ReCalc](https://www.reca.lc/belts){:target="_blank"})*</center>

In order to change the torque and speed from the input to the output, different sized pulleys must be used. The mechanical advantage for belt transmissions, similar to gears, is based on the ratio between the number of teeth of the output pulley to the number of teeth of the input pulley. Note that unlike gears, pulleys will spin in the same direction.

### Types of Belt

Like gears, belts also have a pitch. The pitch is defined as the distance between each tooth on the belt. In FRC, this is typically 5 mm. To calculate the pitch diameter of a pulley, the following equation can be used:

<center>**`PD = Pitch * (# of Teeth) / 3.14`**</center>

Belts also come in various widths. In FRC, you will typically use either 9 mm or 15 mm wide belts.

### Center to Center Calculation

To calculate the center-to-center distance of the pulleys, it is recommended to use an online calculator, such as [ReCalc](https://www.reca.lc/belts "ReCalc Design Calculator"){:target="_blank"}. In the calculator, you can set the belt pitch, desired center distance, and the number of teeth on each pulley to get the closest integer belt size  (belt tooth counts must be whole numbers) and corresponding center to center distance.

!!! Note "Capturing Design Intent"
    In order to capture design intent, it should be clear where dimensions are derived from. Simply copy pasting the calculated center to center distance from ReCalc into the sketch does not convey any information about the belt.

    Thus, to capture the design intent, you wil use the FRC functions functionality of the [`Origin Cube` Featurescript](https://cad.onshape.com/documents/321c197a842fc5f1a29e6621/w/fc3cdd5ca7edcd93e02f13cc/e/2b321cb91b74224b9c14b433 "Origin Cube Featurescript Onshape Document"){:target="_blank"}, which will allow you to calculate belt and chain center to center distances directly inside sketches. The Origin Cube also has additional functionality for robot and mechanism assemblies that will be discussed in Stage 1C. The Origin Cube feature will be **the first feature in all part studios** from here on out.

### Modeling Belt Transmissions

When modeling, you should draw the pitch diameter of the two pulleys and the centerline then connect the pulley circles with tangent lines to represent the belt. A 3D model of the belt can be generated using the [`Belt & Chain Gen` Featurescript](https://cad.onshape.com/documents/53c0b14cad92676c14e04e97/w/1271c254ccb0a79563210195/e/7394c4a86d8d6c35c9a12041 "Belt & Chain Gen Featurescript Onshape Document"){:target="_blank"}.

You will utilize use the following functions from the [`Origin Cube` Featurescript](https://cad.onshape.com/documents/321c197a842fc5f1a29e6621/w/fc3cdd5ca7edcd93e02f13cc/e/2b321cb91b74224b9c14b433 "Origin Cube Featurescript Onshape Document"){:target="_blank"} FRC functions:

* `#PulleyPD_5mm(n)`: Calculates the pitch diameter of a 5 mm pitch pulley with `n` teeth.
    * Ex: `#PulleyPD_5mm(18)` returns the pitch diameter of an 18T 5mm pitch pulley.

* `#BeltCTC_5mm(n1, n2, n3)`: Calculates the c-c distance of a `n1` tooth 5 mm pitch belt connecting pulleys with tooth count `n2` and pulley with tooth count `n3`.
    * Ex: `#BeltCTC_5mm(80,18,36)` returns the center distance for an 80T 5 mm pitch belt connecting an 18T pulley to a 36T pulley.

The following slides demonstrate the workflow one would go through to model a belt transmission. 

<!-- Slideshow container -->
<div class="slideshow-container">
    <!-- Full-width images with number and caption text -->
    <div id="slide1" class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage1b/belt/beltCad1.webp" style="width:60%">
            <figcaption>1. Use ReCalc to find the closest belt size to the desired C-C distance. Set the pitch diameter and select the closest smaller or larger belt, whichever fits your design better. In this example, we choose 80T.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage1b/belt/oCube.webp" style="width:100%">
            <figcaption>2. Insert the <code>Origin Cube</code> feature using the <code>Origin Cube</code> Featurescript. For the exercises in 1B we do not require the cube generated by the feature so we will uncheck it.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
        <video width="1920" controls>
            <source src="/img/learning-course/stage1b/belt/beltCad2.webm" type="video/webm">
            Your browser does not support the video tag.
        </video>
            <figcaption>3. Draw two circles to represent pulley pitch diameters. Set the diameters using the <code>#PulleyPD_5mm(# of teeth)</code> function. Draw the center line to connect the pulleys and set the c-c distance using the belt size calculated from ReCalc and the <code>#BeltCTC_5mm(# belt teeth, # pulley 1 teeth, # pulley 2 teeth)</code> function. Finally, connect the circles with tangent lines.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage1b/belt/beltCad4.webp" style="width:100%">
            <figcaption>4. Finished layout sketch. Checking the <code>Show Expressions</code> box enables you to see the designed belt pitch, pulley tooth counts, and belt tooth count.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
        <video width="1920" controls>
            <source src="/img/learning-course/stage1b/belt/beltCad3.webm" type="video/webm">
            Your browser does not support the video tag.
        </video>
        <figcaption>5. Use the <code>Belt & Chain Gen</code> Featurescript to generate a 3D model of the belt. The reference plane mate connector sets the location of the centerline of the belt. You can modify the selected mate connector offset the location of the belt. You can also choose to generate belt teeth, but do not that this will significantly increase rebuild time.</figcaption>
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

<br>

<!-- ------------------DO NOT TOUCH ANYTHING BELOW HERE------------------ -->

<script>
// Initialize slide index for each slideshow
let slideIndices = [];

let slideshows = document.getElementsByClassName("slideshow-container");
  for (let no = 0; no < slideshows.length; no++) {
    slideIndices[no] = 1;
    let dotsContainer = slideshows[no].getElementsByClassName("dotsContainer")[0];
    let slides = slideshows[no].getElementsByClassName("mySlides");
    for (let i = 0; i < slides.length; i++) {
      let dot = document.createElement("span");
      dot.className = "dot";
      dot.onclick = function() { currentSlide(i+1, no); };
      dotsContainer.appendChild(dot);
    }
    showSlides(1, no);
  }

// Next/previous controls
function plusSlides(n, no) {
  showSlides(slideIndices[no] += n, no);
}

// Thumbnail image controls
function currentSlide(n, no) {
  showSlides(slideIndices[no] = n, no);
}

function showSlides(n, no) {
  let i;
  let x = document.getElementsByClassName("slideshow-container")[no].getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("slideshow-container")[no].getElementsByClassName("dot");
  if (n > x.length) {slideIndices[no] = 1}    
  if (n < 1) {slideIndices[no] = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  x[slideIndices[no]-1].style.display = "block";  
  dots[slideIndices[no]-1].className += " active";
}

</script>