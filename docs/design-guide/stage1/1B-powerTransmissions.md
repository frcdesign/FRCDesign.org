<style>
.right{
    float:right;
}
.center{
    text-align:center;
}
.left{
    float:left;
}
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
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
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

# 1C: Power Transmissions

<span class="left">[< 1A: Onshape Fundamentals](1A-onshapeFundamentals.md)</span> <span class="right">[1C: Design Methodology >](1C-designMethodology.md)</span>
<br>

So far the models you have made are all structural components, but this is only half of what makes a robot. In order to make our robots move and score, motors that generate rotational motion are typically utilized. In section 1C, you'll be introduced to modeling basic *power transmissions*. Power transmissions include the bearings, shafts, gears, belts, and chains that are used to transfer rotational motion from a motor or actuator to do just about anything. 

## Shafts and Bearings

Shafts transmit rotational power, with hex shafts being the most common in FRC. These hexagonal shafts, typically in 1/2" and 3/8" diameters (measured from flat to flat), may sometimes have rounded corners, creating "rounded hex shafts."

Bearings support the shafts and enable smooth spinning. Standard hex shafts use 1/2" hex bearings, while rounded hex shafts can use round bearings for easier assembly.

The easiest way to model shafts is to use the `Shaft` Featurescript which was previously introduced in Stage 1A. For bearings, simply insert your desired bearing from the MKCad app.

<center><img src="\img\design-guide\stage1c\bearingAndShaft.webp" style="width:75%"></center>
<center>*A rounded 1/2" hex bearing (Left) and 1/2" rounded hex shaft (Right). (Image Source: WCP)*</center>

## Torque and Speed

When designing power transmissions, there are two interlinked quantities that we are trying to modify: torque and speed. Torque refers to the rotational force applied to an object, while speed denotes how quickly that object rotates. 

!!! Note
    Speed and torque are inversely related in mechanical systems. This means that as one increases, the other decreases, and vice versa. For example, if speed is decreased by 4x, torque is increased by 4x.

Gears, sprockets, and chain all tradeoff speed for torque (and vice versa) by changing the size of the transmission components.


In this stage, you'll focus on the basics of power transmissions, with an emphasis on how to create them in CAD. While you won't be calculating optimal power transmission ratios or exploring advanced technical details, you'll gain a solid foundation to build upon.

## Types of Power Transmissions

In FRC, the three most common types of power transmissions are gears, chain and sprocket, and belt and pulley. Although they all achieve the same end result of changing speed and torque, they each excel in different situations. In the following sections you'll be introduced to each of them and how to model them.

### Gear Basics
Gears are mechanical devices with teeth that mesh with each other to transmit motion or power between rotating shafts. They're like wheels with teeth that fit together, allowing them to transfer torque, change speed, and change direction of rotation. 

<center><img src="\img\design-guide\stage1c\gears\simpleGears.gif" style="width:40%"></center>
<center>*A simple animation of two gears meshing. Notice that meshed gears will spin in opposite directions.*</center>

In order to change the torque and speed from the input to output, different sized gears must be used. The ratio of the size of the two gears determines how the torque and speed are modified. This ratio is called the **Gear Ratio**, which is the ratio of the number of teeth between two gears. It is typically written as `n:m`, where `m` is the number of rotations of the output for `n` rotations of the input. 

<center>**Changing Speed and Torque**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
<div id="slide1" class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/gears/gearReduction.webp" style="width:100%">
        <figcaption>1. To increase torque and reduce speed, the output gear must be driven with a smaller gear. In this example, a 12T gear drives an 84T gear. The output is 7x larger than the input, so the torque is increased by 7x while the speed is decreased by 7x. (Image source: <a href="https://docs.wcproducts.com/frc-build-system/belts-chain-and-gears/gears">WCP</a>)</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/gears/gearUpduction.webp" style="width:100%">
        <figcaption>2. To decrease torque and increase speed, the output gear must be driven with a larger gear. In this example, a 48T gear drives an 24T gear. The input is 2x larger than the input, so the torque is decreased by 2x while the speed is increased by 2x. (Image source: <a href="https://docs.wcproducts.com/frc-build-system/belts-chain-and-gears/gears">WCP</a>)</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/gears/gearSwap.webp" style="width:100%">
        <figcaption>3. If the same size gears are used, there is no change in speed and torque. However, the direction of the rotation is flipped if there is an even number of gears from input to output. If there is an odd number of gears, the direction remains the same. (Image source: <a href="https://docs.wcproducts.com/frc-build-system/belts-chain-and-gears/gears">WCP</a>)</figcaption>
    </figure>
</div>

<!-- Next and previous buttons -->
<a class="prev" onclick="plusSlides(-1,0)" style="background-color: #000; color: #fff;">&#10094;</a>
<a class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</a>
<!-- The dots/circles -->
<div class="dotsContainer" style="text-align:center">
<!-- Dots will be generated here -->
</div>
</div>

**Center to Center Calculation** 

To calculate how far apart to space the gears, you can use the following formula to calculate the center-to-center distance:

<center>**`CC = 0.5*PD1 + 0.5*PD2`**</center>

Where `PD1` and `PD2` are the *Pitch Diameters* of the two gears. The **Pitch Diameter (PD)**  is the size of the imaginary circle that passes through the center of the gear teeth. The pitch diameters of two gears should be tangent in order for the gears to properly mesh. The equation for PD is as follows:

<center>**`PD = (# of teeth) / DP`**</center>

Where DP stands for **Diametrical Pitch**. For now, you can assume it to always be 20. You can learn more about this in the Design Fundamentals pages.

<center><img src="\img\design-guide\stage1c\gears\gearDiagram.webp" style="width:70%"></center>
<center>*Illustration of pitch diameter and outer diameter. (Image source: <a href="https://docs.wcproducts.com/frc-build-system/belts-chain-and-gears/gears">WCP</a>).*</center>

**Modeling Gear Transmissions**

When modeling, an easy way to set the center-to-center distance between two gears is to draw two circles sized to the gears' pitch diameters and then set two circles to be tangent to each other. For example, if you need to mesh a 20T gear and a 60T gear, you can draw a `20/20 = 1"` and a `60/20 = 3"` circle and add a tangent constraint between the two circles. 

<center><img src="\img\design-guide\stage1c\gears\gearCad.webp" style="width:60%"></center>
<figcaption>Modeling gear C-C distance by constraining two pitch diameter construction circles tangent. The diameters of the circle are calculated by dividing the tooth count by 20.</figcaption>

It's recommended to input the pitch diameter fraction (Eg: `(60/20)"`) rather than the calculated pitch diameter (Eg: Only inputting `3"` as the dimension) so that you can easily see the tooth count of the designed gear. 

### Belts and Pulley Basics

Timing belt and pulley drives are mechanical systems used to transmit motion and power between rotating shafts using flexible belts and pulleys. The system consists of two main components: the belt, which is a flexible loop made of a material like rubber, and the pulleys, which are wheels with grooves that the belt wraps around. As one pulley rotates, it drives the belt, which in turn drives the other pulley, transferring motion and power from one shaft to another


<center><img src="\img\design-guide\stage1c\belt\beltAndPulley.webp" style="width:50%"></center>
<center>*A belt and pulley transmission. (Image Source: [ReCalc](https://www.reca.lc/belts))*</center>

In order to change the torque and speed from the input to the output, different sized pulleys must be used. The ratio between the number of teeth on each pulley determines how torque and speed are modified. Gear ratio is also used to express the ratio of pulley teeth. Note that unlike gears, the two pulleys will spin the same direction.

**Types of Belt**

Like gears, belts also have a pitch. The pitch is defined as the distance between each tooth on the belt. In FRC, this is typically 5 mm. To calculate the pitch diameter of a pulley, the following equation can be used:

<center>**`PD = Pitch * (# of Teeth) / 3.14`**</center>

Belts also come in various widths. In FRC, you will typically use either 9 mm or 15 mm wide belts.

**Center to Center Calculation**

To calculate the center-to-center distance of the pulleys, it is recommended to use an online calculator, such as [ReCalc](https://www.reca.lc/belts). In the calculator, you can set the belt pitch, desired center distance, and the number of teeth on each pulley to get the closest integer belt size  (belt tooth counts must be whole numbers) and corresponding center to center distance.

**Modeling Belt Transmissions**

When modeling, you will typically draw either the pitch diameter of the two pulleys and connect them with tangent lines to represent the belt. A simplified 3D model of the belt can be generated using the `Contextless Belts` Featurescript from [Julia's Featurescripts](/resources/featurescripts/#julias-featurescripts).

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
<div id="slide1" class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/belt/beltCad1.webp" style="width:75%">
        <figcaption>1. Use ReCalc to find the closest belt size to the desired C-C distance. Set the pitch diameter and select the closest smaller or larger belt, whichever fits your design better.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/belt/beltCad2.webp" style="width:100%">
        <figcaption>2. Draw two circles to represent pulley pitch diameters and connect them with tangent lines. Set the center distance with the calculated number from ReCalc.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/belt/beltCad3.gif" style="width:100%">
        <figcaption>3. Use the <code>Contextless Belts</code> Featurescript to generate a 3D model of the belt.</figcaption>
    </figure>
</div>

<!-- Next and previous buttons -->
<a class="prev" onclick="plusSlides(-1,1)" style="background-color: #000; color: #fff;">&#10094;</a>
<a class="next" onclick="plusSlides(1,1)" style="background-color: #000; color: #fff;">&#10095;</a>
<!-- The dots/circles -->
<div class="dotsContainer" style="text-align:center">
<!-- Dots will be generated here -->
</div>
</div>


### Chain and Sprocket Basics

Roller chain and sprocket drives are very similar to belt and pulley transmissions. They consist of two main components: a chain, which is a series of interconnected links, and sprockets, which are toothed wheels that mesh with the chain. As the sprockets rotate, they engage with the chain, causing it to move and transmit power from one shaft to another. Bikes are an everyday object that use chain to transmit power. Chains excel at transmitting high force over long distances.

<center><img src="\img\design-guide\stage1c\chain\chainAnimation.gif" style="width:40%"></center>
<center>*A simple animation of chain and sprocket. Notice that the sprockets will spin in the same direction.*</center>

In order to change the torque and speed from the input to the output, different sized sprockets must be used. The ratio between the number of teeth on each sprocket determines how torque and speed are modified. Gear ratio is used to express the ratio of sprocket teeth. Note that unlike gears, the two sprockets will spin the same direction.

**Types of Chain**

The two commonly used sizes of roller chain in FRC is #25 and #35 chain, with 0.25" and 0.375" pitch respectively. For chain, the **pitch** is the length of each link. To calculate the pitch diameter, the following equation can be used:

<center>**`PD = Pitch * (# of Teeth) / 3.14`**</center>

Additionally, the **chain clearance diameter** describes the diameter of the sprocket with the chain wrapped around it. The following equation can be used:

<center>**`Clearance Diameter = PD + Pitch`**</center>

Below is an illustration of the pitch, pitch diameter, outside diameter, and chain clearance diameter of a sprocket.

<center><img src="\img\design-guide\stage1c\chain\chainDiagram.webp" style="width:70%"></center>
<center>*Illustration of chain sprocket diameter measures. (Image source: <a href="https://docs.wcproducts.com/frc-build-system/belts-chain-and-gears/sprockets-and-chain">WCP</a>)*</center>

In FRC, #25 chain is most commonly used as it is strong yet relatively lightweight. #35 is sometimes used on very high torque transmissions, but it is heavy and bulky. 

**Center to Center Calculation** 

To calculate the center-to-center distance of the sprockets, it is recommended to use an online calculator, such as [ReCalc](https://www.reca.lc/chains). In the calculator, you can set the chain size, desired center distance, and the number of teeth on each sprocket to get the required center distance.

When modeling, you will typically draw either the pitch diameter or chain clearance diameter of the two sprockets and connect them with tangent lines to represent the links. A simplified 3D model of the chain can be generated using the `Chain Generator` Featurescript from [Julia's Featurescripts](/resources/featurescripts/#julias-featurescripts).

<center>**Modeling Chain Transmissions**</center>


<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
<div id="slide1" class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/chain/chainCad1.webp" style="width:80%">
        <figcaption>1. Use ReCalc to find the closest C-C size to the desired C-C distance. Set the pitch diameter and select the closest smaller or larger chain link count, whichever fits your design better.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/chain/chainCad2.webp" style="width:100%">
        <figcaption>2. Draw two circles to represent sprocket pitch diameters and connect them with tangent lines. Set the center distance with the calculated number from ReCalc.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/chain/chainCad3.gif" style="width:100%">
        <figcaption>3. Use the <code>Chain Generator</code> Featurescript to generate a simplified 3D model of the chain.</figcaption>
    </figure>
</div>
<!-- Next and previous buttons -->
<a class="prev" onclick="plusSlides(-1,2)" style="background-color: #000; color: #fff;">&#10094;</a>
<a class="next" onclick="plusSlides(1,2)" style="background-color: #000; color: #fff;">&#10095;</a>
<!-- The dots/circles -->
<div class="dotsContainer" style="text-align:center">
<!-- Dots will be generated here -->
</div>
</div>


## Exercise

### Arm Gearbox

### Intake Belts

## Summary

Congratulations on completing Stage 1C! Keep up the good work!

Here is a quick summary of what you have achieved in 1C:

* Learned the basics of bearings, shafts, gears, chain and sprockets, and belt and pulleys
* Learned how to model power transmissions
* Learned how to use the `Contextless Belt` and `Chain Generator` Featurescripts

In Stage 2, you will begin to model robot mechanisms using all the skills you have learned in Stage 0 and Stage 1!

<br>
<center>1C: Gearboxes</center> 
<span class="left">[< 1A: Onshape Fundamentals](1A-onshapeFundamentals.md)</span> <span class="right">[1C: Design Methodology >](1C-designMethodology.md)</span>
<br>
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