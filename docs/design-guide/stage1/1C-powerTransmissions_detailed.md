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

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
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

<span class="left">[< 1B: Design Methodology](1B-designMethodology.md)</span> <span class="right">[Stage 2A >](../stage2/2A-drivebaseFullDetail.md)</span>
<br>

So far, all the dimensions in the models you have been working on have largely been hand waived. In section 1C you'll begin to uncover some of these mysteries, beginning with ***power transmissions***. Motors are one way to animate your robot through rotational motion. Power transmission are then the gears, belts, and chains that are used to transfer this rotational motion from the motor to do just about anything you can design. 

<!-- ## Introduction to Power Transmissions

Before you can begin designing, you'll need to know 

*what* power transmissions are and the types used within FRC. Some of these you may have seen before around everyday objects or on robots. You'll be introduced to the three most commonly used types within FRC. You can use the following sections as a quick reference for the rest of this stage. -->

## Torque and Speed

Before learning about power transmissions, you'll first need to understand torque and speed. If you've taken a physics class before, this should be very straight forward. In this stage, we won't delve into calculating optimal power transmission ratios or performing power calculations; instead, you'll just focus on how to CAD them.

When designing power transmissions, there are two interlinked quantities that we are trying to modify: torque and speed. Torque refers to the rotational force applied to an object, while speed denotes how quickly that object rotates. 

!!! Note
    Speed and torque are inversely related in mechanical systems. This means that as one increases, the other decreases, and vice versa. For example, if speed is decreased by 4x, torque is increased by 4x.

Gears, sprockets, and chain all tradeoff speed for torque (or vice versa) by changing the size of the transmission components.

## Types of Power Transmissions

In FRC, the three most common types of power transmissions are gears, chain and sprocket, and belt and pulley. Although they all achieve the same end result of changing speed and torque, they each excel in different situations. 

### Gear Basics
Gears are mechanical devices with teeth that mesh with each other to transmit motion or power between rotating shafts (rods that spin to transmit power). They're like wheels with teeth that fit together, allowing them to transfer rotational force and change the speed or direction of rotation. In the following sections you'll be introduced to each of them and how to model them.

<center><img src="\img\design-guide\stage1c\gears\simpleGears.gif" style="width:40%"></center>
<center>*A simple animation of two gears meshing. Notice that the gears will spin in opposite directions.*</center>

In order to change the torque and speed from the input to output, different sized gears must be used. The ratio of the size of the two gears determines how the torque and speed are modified. This ratio is called the **Gear Ratio**, which is the ratio of the number of teeth between two gears. It is typically written as `n:m`, which is the ratio between the number of rotations `m` of the output for `n` rotations of the input.

<center>**Changing Speed and Torque**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
<div class="mySlides fade">
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
        <figcaption>3. If the same size gears are used, there is no change in speed and torque. However, the direction of the rotation is flipped if there is an even number of gears from input to output. If there is an odd number of gears, the direction is the same. (Image source: <a href="https://docs.wcproducts.com/frc-build-system/belts-chain-and-gears/gears">WCP</a>)</figcaption>
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

To calculate the center-to-center distance, you can use the following formula:

<center>**`CC = 0.5*PD1 + 0.5*PD2`**</center>

Where `PD1` and `PD2` are the *Pitch Diameters* of the two gears. The **Pitch Diameter (PD)** , is the diameter of the imaginary circle that passes through the center of the gear teeth. The size of this circle can be calculated with the **Diametrical Pitch (DP)**, which is the the number of gear teeth per inch of the pitch diameter. The relationship is as follows:

<center>**`PD = (Number of teeth) / DP`**</center>

The most commonly used gears in FRC are **20DP**. For example, a 20DP 80T gear will have a pitch diameter of 4". However, it should be noted that special gears are addendum modified and have a pitch diameter that does not correspond to the tooth count. If you are curious, you can read more about this [here](https://docs.wcproducts.com/frc-build-system/belts-chain-and-gears/gears#addendum-modified-gears). Typically this is only used on special motor pinion gears and will be marked as such.

<center><img src="\img\design-guide\stage1c\gears\gearDiagram.webp" style="width:70%"></center>
<center>*Illustration of gear pitch and outer diameter. Some vendors will label the gear with the <b>Tooth Count</b>. (Image source: <a href="https://docs.wcproducts.com/frc-build-system/belts-chain-and-gears/gears">WCP</a>).*</center>*

When modeling, an easy way to set the center distance between two gears is to draw two circles sized to the gears' pitch diameters and then set two circles to be tangent to each other. For example, if you need to mesh a 20T gear and a 60T gear, you can draw a 1" and 3" pitch diameter circle and add a tangent constraint between the two circles.

<center>**Modeling Gear Transmissions**</center>

<!-- Slideshow container -->
<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
      <figure>
          <img src="/img/design-guide/stage1c/gears/gears1.webp" style="width:60%">
          <figcaption>1. A typical <b>Spur Gear</b> utilized in FRC. These types of gears can be purchased from most FRC vendors. (Image source: <a href="https://wcproducts.com/products/pocketed-gears">WCP</a>)</figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/design-guide/stage1c/gears/gears6.webp" style="width:100%">
          <figcaption>6. </figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/design-guide/stage1c/gears/gears2.gif" style="width:80%">
          <figcaption>2. A <b>Gearbox</b> whose input is a Kraken motor and applies a reduction.</figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/design-guide/stage1c/gears/gears3.webp" style="width:100%">
          <figcaption>3. </figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/design-guide/stage1c/gears/gears4.webp" style="width:100%">
          <figcaption>4. This is a 1:0.25 reduction. Four rotations of the input gear will result in 1 rotation of the output. </figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/design-guide/stage1c/gears/gears5.webp" style="width:100%">
          <figcaption>5. The <b>Center Distance </b> between two gears. </figcaption>
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

**When to Use**

Gears are most commonly used with gearboxes to increase the torque of a motor. Before designing a gearbox, careful selection of the gear ratio is required so that there is enough torque to achieve the desired motions. 

Out of the three power transmission methods discussed in this section, gears are the most compact. Gears should also be used if a change in rotational direction is required. Belts and chain cannot typically change rotational direction.

Gears should not be used to transfer motion long distances; belts or chain are much more weight efficient for long distances. Also, gears are not suited for shock loads, which are very high spikes in torque, such as crashing an arm into something. Compared to chain and belt, gears transfer torque through a single tooth so they cannot handle shock loads as well.


### Belts and Pulley Basics


**When to Use**


### Chain and Sprocket Basics

Roller chain and sprocket drives are mechanical systems used to transmit motion and power between rotating shafts. They consist of two main components: a chain, which is a series of interconnected links, and sprockets, which are toothed wheels that mesh with the chain. As the sprockets rotate, they engage with the chain, causing it to move and transmit power from one shaft to another. Bikes are an everyday object that use chain to transmit power. Chains excel at transmitting high force over long distances.

<center><img src="\img\design-guide\stage1c\chain\chainAnimation.gif" style="width:40%"></center>
<center>*A simple animation of chain and sprocket. Notice that the sprockets will spin in the same direction.*</center>

In order to change the torque and speed from the input to the output, different sized sprockets must be used. The of the number of teeth of the sprockets determines how torque and speed are modified. Gear ratio is also used to express the ratio of sprocket teeth. Note that unlike gears, the two sprockets will spin the same direction. Also, the number of chain links must be even, unless a "half-link" is used, but this is not a recommended practice as half-link are weaker than normal links.

**Types of Chain**

The two commonly used sizes of roller chain in FRC is #25 and #35, with 0.25" and 0.375" pitch respectively. The **pitch** is the measure of the length of each link. #25 is most commonly used as it is strong and fairly lightweight. #35 is sometimes used on very high torque transmissions, such as on a large arm, but it is heavy and bulky.

**Center to Center Calculation** 

To calculate the center-to-center distance of the sprockets, it is recommended to use an online calculator, such as [ReCalc](https://www.reca.lc/chains). In the calculator, you can set the desired center distance and the number of teeth on each sprocket to get the required center distance.

Similar to gears and belts, chain also has a pitch diameter. A chain clearance diameter also exists to describe the diameter of the sprocket with the chain wrapped around it. These quantities can be calculated with the following equations:

<center>**`PD = Pitch * Teeth / 3.14`**</center>

<center>**`Clearance Diameter = PD + Pitch`**</center>

<center><img src="\img\design-guide\stage1c\chain\chainDiagram.webp" style="width:70%"></center>
<center>*Illustration of chain sprocket diameter measures. Some vendors will label the gear with the <b>Tooth Count</b>. (Image source: <a href="https://docs.wcproducts.com/frc-build-system/belts-chain-and-gears/sprockets-and-chain">WCP</a>)*</center>

**Chain Tensioning**

Unlike gears and belts, chain will stretch over time and increase in length and this must be accounted for in the design. Chain requires proper tension for system integrity. Improperly tensioned chain can skip (when the chain moves but not the sprocket). To compensate for this, a tensioning system should be added. The easiest way is to add an in-line chain tensioner. By tightening and loosing the chain tensioner, the length (and therefore the tension) of the chain can be adjusted. You can read more about chain tensioning methods in [Design Fundamentals](/design-fundamentals/)

<center><img src="\img\design-guide\stage1c\chain\inlineTensioner.webp" style="width:40%"></center>
<center>*An inline #25 chain tensioner. The tensioner is wrapped in tape to prevent it from loosening.*</center>

When modeling, you will typically draw either the pitch diameter or chain clearance diameter of the two sprockets and connect them with tangent lines to represent the links. A simplified model of the chain can be generated using the `Chain Generator` Featurescript from [Julia's Featurescripts](/resources/featurescripts/#julias-featurescripts).


<center>**Modeling Chain Transmissions**</center>

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/gears/gears1.webp" style="width:60%">
        <figcaption>1. A typical <b>Spur Gear</b> utilized in FRC. These types of gears can be purchased from most FRC vendors. (Image source: <a href="https://wcproducts.com/products/pocketed-gears">WCP</a>)</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/gears/gears6.webp" style="width:100%">
        <figcaption>6. </figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/gears/gears2.gif" style="width:80%">
        <figcaption>2. A <b>Gearbox</b> whose input is a Kraken motor and applies a reduction.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/gears/gears3.webp" style="width:100%">
        <figcaption>3. </figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/gears/gears4.webp" style="width:100%">
        <figcaption>4. This is a 1:0.25 reduction. Four rotations of the input gear will result in 1 rotation of the output. </figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1c/gears/gears5.webp" style="width:100%">
        <figcaption>5. The <b>Center Distance </b> between two gears. </figcaption>
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

**When to Use**



## Exercise

### Arm Gearbox

### Intake Belts

## Summary

Summary of when to use each type of power transmission:

| Transmission Type    | When to use | When not to use |
| -------- | ------- | ------- |
| Gears  |     | |
| Belts and Pulleys |     | |
| Chain and Sprocket |   | |





<!-- Though you can buy premade planetary gearboxes from vendors (which are still very good in a lot of use cases and packaging), custom gearboxes are typically more versatile in tight packaging situations, and can be tuned better to avoid backlash.
[comment]: <> (Link to designing for control page for reducing backlash)

## Transfer of Motion
Motors are used to add movement to your robot through rotation. Gears, belts, and chains are used to both transfer motion (torque and speed) from one shaft/mechanism to another, both to move mechanisms and spin rollers and wheels. Object manipulation, movement around the field, just about anything on your robot can be moved with the right motors and mechanical advantage.

<center><img src="\img\design-guide\stage1c\powertrains.webp"></center>

### Mechanical Advantage

Mechanical advantage is a measure of the ratio of output force to input force in a system. Given a set speed and torque from a motor, you can use the difference between gear teeth, pulley teeth, or sprocket teeth to transfer speed to torque, or vice versa. This is described using a ratio of mechanical advantage (e.g. 3:1 reduction, 1:2 upduction). 

- A small gear on your motor meshing with a large gear on another axle will decrease the output speed but increase the torque, and is called a *reduction*. The opposite is true as well: a large gear meshing with a smaller gear will increase output speed but decrease the torque, and is called an *upduction*.
- Besides rollers and shooter wheels, reductions are necessary to optimize motor speed vs. torque. This reduction can be calculated with [ReCalc](https://www.reca.lc/) or a variety of spreadsheet calculators found on ChiefDelphi, such as [KLib](https://www.chiefdelphi.com/t/klib-a-tool-for-frc-design/398904/16).
- The choice between gears, belts, or chain for making the reduction or upduction depends on the purpose and packaging constraints.

### Types of Power Transfer

- Gears mesh together directly and cause the direction of rotation to switch, belts/pulleys and chain/sprockets work at a distance and don't cause a change in direction of rotation.
- Belts are lightweight and drive high speed mechanisms well, but can skip with high loads if not tensioned perfectly
- Chains are heavy duty and handle high torque well, but always need an extra tensioning mechanism for maintenance as they stretch through use

### Bearings

- Allows things to spin easily on the inside vs. the outside
- Can fix the bearing to a plate and fit an axle through it to allow the axle to spin
- Alternatively, put something on bearings on a fixed axle and you can spin something without putting potential strain on the axle
- 0.5in hex axles are the most common in FRC, and rounded versions can use special bearings with an inside diameter of 13.75mm (referred to as thunderhex bearings)

## Dimensions for Gearboxes

- 0.196 inches = #10-32 bolt (hardware standard) close fit hole. As #10-32 hardware is standardized for most COTS parts, we try to exclusively use this except where stronger 1/4-20 bolts are needed
- 1.127 inches = Rounded hex bearing hole. This size may change depending on your team's machining tolerances. Ask someone more experienced if they know, otherwise use this reference number.

### CIM Class Motor Dimensions

- Kraken, Vortex, Neo, CIM
- 60mm = Motor diameter
- 2 inches = Mounting hole circle
- 0.8 inches = Center hole

### Gear Dimensions
The pitch diameter is the diameter of the gear where if two pitch diameters are touching, allows the gears to perfectly mesh. 

<center><img src="\img\design-guide\stage1c\gearDiagram.webp" width="40%"></center>

- Pitch Diameter = number of teeth/diametrical pitch
- Diametrical pitch = dp, the number of teeth per inch of diameter. Pretty much every gear we use in FRC will be 20 DP.
- In CAD, this means you can make bearing holes for axles based off of two construction circles representing gears (dimensioned with the pitch diameters) that are tangent to each other

!!! Tip
    Most teams add a little bit to each pitch diameter circle to give room for manufacturing tolerances and allow the gears to mesh smoother. This is usually from .001 inches to .003 inches per pitch circle (.002-.006 in total). For mechanisms where you want more precise control over the rotation (i.e. less backlash), like a pivot, you can use exact center-center distance.

### Belt/Chain Dimensions
- Pitch is the distance between the teeth
- Belts and chains are defined by pitch, teeth (or links), and width (only matters for pulley width)
- Length (pitch x teeth = length)
- Standard belt pitch can be different: HTD5 is 5mm, GT2 in FRC is usually 3mm, and RT25 (sold only by REV) is .25in
- **KEY IDEA: You can only buy set lengths of belts.** Designing for belts requires a [center-to-center distance calculator](https://wcproducts.com/pages/calculator-belt) that will give you the closest center-center distance to a given preferred distance, pitch and pulley sizes
- You can use whatever center-to-center distance you want for a chain as long as you provide [a way to tension it](../../design-fundamentals/design-writeups/chainTensioning.md) (which is heavily recommended for all chains used)

!!! Tip
    Pulley center-to-center distances usually have an offset of about -0.02in (makes pulleys closer) to make it easier to put the belt on the pulleys. Similar to gears, though, for more precise mechanisms, use exact center-to-center distance for less chance of skipping.
  
## Gearbox 1
The first gearbox introduces you to some basic ideas. As always, it's a mix between CAD fundamentals and FRC fundamentals. By the end of this you should be able to design a simple 1-stage gearbox with a motor.

This project is a little less guided than the last one, and introduces you to basic plate design, the spacer and shaft featurescripts, and way more assembly fundamentals and MKCAD insertion. Try to copy [this gearbox](https://cad.onshape.com/documents/ff20a652374bc6dccedba340/w/c40a663858e835275eedc6be/e/df046387942e63628ef3d99c?renderMode=0&uiState=66328dd3b89a596adab116a3), making sure to use a single sketch to drive the whole gearbox structure, especially all the hole placements. 

You can watch this video for a full tutorial:
<center><iframe width="880" height="550" src="https://www.youtube.com/embed/OE-NVLBxm6I" frameborder="0" allowfullscreen></iframe></center>


## Gearbox 2
The second gearbox introduces you to some more featurescripts as well as more design fundamentals. Try to copy [this gearbox](https://cad.onshape.com/documents/dbfca47b976b572e1ed949ec/w/3e1d28e9efa9b31b349bcd33/e/03fe2e65fe5e7e357d04ce9e?renderMode=0&uiState=662da16d9cc5a27a76e8e6b8), again keeping in mind to use layout sketches:

<center>![Gearbox](../../img/design-guide/stage1c/gearbox.webp){width=45% height=45%}</center>

Check out these two videos to learn concepts about plate design and belt/pulley design (which will both be used for this gearbox):

<center>
<iframe width="880" height="550" src="https://www.youtube.com/embed/9ckB7p3kp6c" frameborder="0" allowfullscreen></iframe>

<iframe width="880" height="550" src="https://www.youtube.com/embed/fX-BLKZHsJM" frameborder="0" allowfullscreen></iframe>
</center>

Once you've finished both of the gearboxes, you can move on to Stage 2 and start working on more complex mechanisms! -->

<br>
<center>1C: Gearboxes</center> 
<span class="left">[< 1B: Design Methodology](1B-designMethodology.md)</span> <span class="right">[Stage 2A >](../stage2/2A-drivebaseFullDetail.md)</span>
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