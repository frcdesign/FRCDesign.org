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

# 1B: Power Transmissions

<span class="left">[< 1A: Onshape Fundamentals](1A-onshapeFundamentals.md)</span> <span class="right">[1C: Design Methodology >](1C-designMethodology.md)</span>
<br>

So far the models you have made are all structural components, but this is only half of what makes a robot. In order to make our robots move and score, motors that generate rotational motion are typically utilized. In section 1B, you'll be introduced to modeling basic *power transmissions*. Power transmissions include the bearings, shafts, gears, belts, and chains that are used to transfer rotational motion from a motor or actuator to do just about anything. 

<center>**Power Transmission Examples**</center>
<!-- Slideshow container -->
  <div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
      <figure>
          <img src="/img/design-guide/stage1b/examples/intakeRollers.webp" style="width:80%">
          <figcaption> Belt and gear power transmission to spin intake rollers. </figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/design-guide/stage1b/examples/shooter.webp" style="width:80%">
          <figcaption> Belt and gear power transmission to spin shooter wheels.</figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/design-guide/stage1b/examples/ampArm.webp" style="width:60%">
          <figcaption> Gear and chain power transmission to rotate a small arm. </figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/design-guide/stage1b/examples/armGearbox.webp" style="width:75%">
          <figcaption> Gear and chain power transmission to rotate a large arm.</figcaption>
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

## Shafts and Bearings

Shafts transmit rotational power, with hex shafts being the most common in FRC. These hexagonal shafts, typically in 1/2" and 3/8" diameters (measured from flat to flat), may sometimes have rounded corners, creating "rounded hex shafts."

Bearings support the shafts and enable smooth spinning. Standard hex shafts use 1/2" hex bearings, while rounded hex shafts can use round bearings for easier assembly.

The easiest way to model shafts is to use the `Shaft` [Featurescript](/resources/featurescripts/). For bearings, insert your desired bearing from the MKCad app.

<center><img src="\img\design-guide\stage1b\bearingAndShaft.webp" style="width:75%"></center>
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

<center><img src="\img\design-guide\stage1b\gears\simpleGears.gif" style="width:40%"></center>
<center>*A simple animation of two gears meshing. Notice that meshed gears will spin in opposite directions.*</center>

In order to change the torque and speed from the input to output, different sized gears must be used. The ratio of the size of the two gears determines how the torque and speed are modified. This ratio is called the **Gear Ratio**, which is the ratio of the number of teeth between two gears. It is typically written as `n:m`, where `m` is the number of rotations of the output for `n` rotations of the input. 

<center>**Changing Speed and Torque**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
<div id="slide1" class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1b/gears/gearReduction.webp" style="width:100%">
        <figcaption>1. To increase torque and reduce speed, the output gear must be driven with a smaller gear. In this example, a 12T gear drives an 84T gear. The output is 7x larger than the input, so the torque is increased by 7x while the speed is decreased by 7x. (Image source: <a href="https://docs.wcproducts.com/frc-build-system/belts-chain-and-gears/gears">WCP</a>)</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1b/gears/gearUpduction.webp" style="width:100%">
        <figcaption>2. To decrease torque and increase speed, the output gear must be driven with a larger gear. In this example, a 48T gear drives an 24T gear. The input is 2x larger than the input, so the torque is decreased by 2x while the speed is increased by 2x. (Image source: <a href="https://docs.wcproducts.com/frc-build-system/belts-chain-and-gears/gears">WCP</a>)</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1b/gears/gearSwap.webp" style="width:100%">
        <figcaption>3. If the same size gears are used, there is no change in speed and torque. However, the direction of the rotation is flipped if there is an even number of gears from input to output. If there is an odd number of gears, the direction remains the same. (Image source: <a href="https://docs.wcproducts.com/frc-build-system/belts-chain-and-gears/gears">WCP</a>)</figcaption>
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

**Center to Center Calculation** 

To calculate how far apart to space the gears, you can use the following formula to calculate the center-to-center distance:

<center>**`CC = 0.5*PD1 + 0.5*PD2`**</center>

Where `PD1` and `PD2` are the *Pitch Diameters* of the two gears. The **Pitch Diameter (PD)**  is the size of the imaginary circle that passes through the center of the gear teeth. The pitch diameters of two gears should be tangent in order for the gears to properly mesh. The equation for PD is as follows:

<center>**`PD = (# of teeth) / DP`**</center>

Where DP stands for **Diametrical Pitch**. For now, you can assume it to always be 20. You can learn more about this in the Design Fundamentals pages.

<center><img src="\img\design-guide\stage1b\gears\gearDiagram.webp" style="width:70%"></center>
<center>*Illustration of pitch diameter and outer diameter. (Image source: <a href="https://docs.wcproducts.com/frc-build-system/belts-chain-and-gears/gears">WCP</a>).*</center>

**Modeling Gear Transmissions**

When modeling, an easy way to set the center-to-center distance between two gears is to draw two circles sized to the gears' pitch diameters and then set two circles to be tangent to each other. For example, if you need to mesh a 20T gear and a 60T gear, you can draw a `20/20 = 1"` and a `60/20 = 3"` circle and add a tangent constraint between the two circles. 

<center><img src="\img\design-guide\stage1b\gears\gearCad.webp" style="width:60%"></center>
<figcaption>Modeling gear C-C distance by constraining two pitch diameter construction circles tangent. The diameters of the circle are calculated by dividing the tooth count by 20.</figcaption>

It's recommended to input the pitch diameter fraction (Eg: `(60/20)"`) rather than the calculated pitch diameter (Eg: Only inputting `3"` as the dimension) so that you can easily see the tooth count of the designed gear. 

### Belts and Pulley Basics

Timing belt and pulley drives are mechanical systems used to transmit motion and power between rotating shafts using flexible belts and pulleys. The system consists of two main components: the belt, which is a flexible loop made of a material like rubber, and the pulleys, which are wheels with grooves that the belt wraps around. As one pulley rotates, it drives the belt, which in turn drives the other pulley, transferring motion and power from one shaft to another


<center><img src="\img\design-guide\stage1b\belt\beltAndPulley.webp" style="width:50%"></center>
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
        <img src="/img/design-guide/stage1b/belt/beltCad1.webp" style="width:75%">
        <figcaption>1. Use ReCalc to find the closest belt size to the desired C-C distance. Set the pitch diameter and select the closest smaller or larger belt, whichever fits your design better.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1b/belt/beltCad2.webp" style="width:100%">
        <figcaption>2. Draw two circles to represent pulley pitch diameters and connect them with tangent lines. Set the center distance with the calculated number from ReCalc.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1b/belt/beltCad3.gif" style="width:100%">
        <figcaption>3. Use the <code>Contextless Belts</code> Featurescript to generate a 3D model of the belt.</figcaption>
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


### Chain and Sprocket Basics

Roller chain and sprocket drives are very similar to belt and pulley transmissions. They consist of two main components: a chain, which is a series of interconnected links, and sprockets, which are toothed wheels that mesh with the chain. As the sprockets rotate, they engage with the chain, causing it to move and transmit power from one shaft to another. Bikes are an everyday object that use chain to transmit power. Chains excel at transmitting high force over long distances.

<center><img src="\img\design-guide\stage1b\chain\chainAnimation.gif" style="width:40%"></center>
<center>*A simple animation of chain and sprocket. Notice that the sprockets will spin in the same direction.*</center>

In order to change the torque and speed from the input to the output, different sized sprockets must be used. The ratio between the number of teeth on each sprocket determines how torque and speed are modified. Gear ratio is used to express the ratio of sprocket teeth. Note that unlike gears, the two sprockets will spin the same direction.

**Types of Chain**

The two commonly used sizes of roller chain in FRC is #25 and #35 chain, with 0.25" and 0.375" pitch respectively. For chain, the **pitch** is the length of each link. To calculate the pitch diameter, the following equation can be used:

<center>**`PD = Pitch * (# of Teeth) / 3.14`**</center>

Additionally, the **chain clearance diameter** describes the diameter of the sprocket with the chain wrapped around it. The following equation can be used:

<center>**`Clearance Diameter = PD + Pitch`**</center>

Below is an illustration of the pitch, pitch diameter, outside diameter, and chain clearance diameter of a sprocket.

<center><img src="\img\design-guide\stage1b\chain\chainDiagram.webp" style="width:70%"></center>
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
        <img src="/img/design-guide/stage1b/chain/chainCad1.webp" style="width:80%">
        <figcaption>1. Use ReCalc to find the closest C-C size to the desired C-C distance. Set the pitch diameter and select the closest smaller or larger chain link count, whichever fits your design better.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1b/chain/chainCad2.webp" style="width:100%">
        <figcaption>2. Draw two circles to represent sprocket pitch diameters and connect them with tangent lines. Set the center distance with the calculated number from ReCalc.</figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/design-guide/stage1b/chain/chainCad3.gif" style="width:100%">
        <figcaption>3. Use the <code>Chain Generator</code> Featurescript to generate a simplified 3D model of the chain.</figcaption>
    </figure>
</div>
<!-- Next and previous buttons -->
<a class="prev" onclick="plusSlides(-1,3)" style="background-color: #000; color: #fff;">&#10094;</a>
<a class="next" onclick="plusSlides(1,3)" style="background-color: #000; color: #fff;">&#10095;</a>
<!-- The dots/circles -->
<div class="dotsContainer" style="text-align:center">
<!-- Dots will be generated here -->
</div>
</div>


## Exercises

The following exercises are designed to practice modeling simple power transmissions in the form of stand alone gearboxes. In stage 2, you will begin to model more integrated power transmissions within mechanisms. Practice exercise solutions can be found [here](https://cad.onshape.com/documents/c6a8ec29479a2578841fb9f2/w/85094b3baa15a05c873920c9/e/21fa04df80572c41ab64f27b).

### Exercise 1: Simple Gearbox

In this exercise, you will be CADing and assembling a simple single stage gearbox. 

The goal of this exercise is to introduce how to model a very simple gear transmission. Additionally, you will learn how to use the the `Shaft` Featurescript, `Replicate` tool, MKCad parts library, and part configurations.

!!! Note
    Exercise 1 adds hardware (bolts and nuts) to the CAD models. You can read more about hardware standards on the [Design Fundamentals](/design-fundamentals/) page.

<center>**Exercise 1 Instruction Slides**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e1/e1s0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e1/e1s1.webp" style="width:100%">
      <figcaption> 1. Begin by creating the layout sketch for the gearbox. Draw the pitch circles for the 60T and 12T gears. Set the pitch circles tangent to constrain the center-to-center distance between the gears. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e1/e1s2.webp" style="width:100%">
      <figcaption> 2. Add the outline of the motor, a 2.5" diameter circle, around the 12T gear that the motor is attached to. The layout sketch is now finished.  </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e1/e1s3.webp" style="width:100%">
      <figcaption> 3. Create a new sketch for the motor plate. Using the layout as the reference, draw a 1.125" hole for the bearing and a 0.8" hole for the motor boss (the nub that sticks out from the motor). Note that depending on your manufacturing processes and tolerances, you may need to draw your bearing holes slightly larger or smaller than nominal (1.125"). </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e1/e1s4.webp" style="width:100%">
      <figcaption> 4. Add two mounting holes for the motor. A good practice to constrain the holes is to draw and dimension a <it>bolt circle</it>, then draw the holes for the bolts on the bolt circle. This constrains the distance of the holes from the center of the motor with a single dimension. The bolt circle for the motor we are using is 2". </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e1/e1s5.webp" style="width:100%">
      <figcaption>  5. Add the four bolt holes for connecting the two plates. Use a center rectangle to create the construction geometry so that only two dimensions are required to constrain the holes.    </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e1/e1s6.webp" style="width:100%">
      <figcaption> 6. Draw the outline for the plate around the holes and motor outline. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e1/e1s7.webp" style="width:100%">
      <figcaption> 7. Extrude the motor plate to be 1/4" thick. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e1/e1s8.webp" style="width:100%">
      <figcaption> 8. Use the <code>Spacer</code> Featurescript to add a round 3/8" diameter, 5/8" long spacer. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e1/e1s9.webp" style="width:100%">
      <figcaption> 9. Create the outer plate sketch on the face of the spacer. Copy over the shape of the motor plate, but add a round cutout at the top. Also copy over the holes in the plate. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e1/e1s10.webp" style="width:100%">
      <figcaption>10. Extrude the outer plate to be 1/4" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/design-guide/stage1b/exercises/e1/e1s11.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>11. Use the <code>Shaft</code> Featurescript to model the output shaft. Follow the settings used. You can learn more about the shaft retention property on the Design Fundamentals page. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e1/e1s12.webp" style="width:100%">
      <figcaption> 12. Finished part studio. Name the key sketches and parts. Set the material of the plate and spacers to 6061 Aluminum. The shaft has its material automatically determined from the <code>Shaft</code> Featurescript.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/design-guide/stage1b/exercises/e1/e1s13.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption> 13. Insert the part studio into the assembly and fix the gearbox plate. Group mate the two plates together and then mate the spacer to the motor plate. Then, use the <code>Replicate</code> tool to replicate the spacer and its associated mate onto the other spacer locations. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/design-guide/stage1b/exercises/e1/e1s14.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption> 14. Assemble the bearings and shaft using parts from the MKCad App.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/design-guide/stage1b/exercises/e1/e1s15.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption> 15. Assemble the motor and motor pinion gear using parts from the MKCad App.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/design-guide/stage1b/exercises/e1/e1s16.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption> 16. Assemble the shaft spacer and gear using parts from the MKCad App. Configurable parts will have a blue grid icon in the instance list. Notice how you were able to change the tooth count of the gear from 40T to 60T after mating it. Using configurable components like this makes your models more parametric since you can change the component without needing to re-insert and mate. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/design-guide/stage1b/exercises/e1/e1s17.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption> 17. Assemble the shaft retention bolts using the MKCad app parts. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/design-guide/stage1b/exercises/e1/e1s18.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption> 18. Assemble the motor bolts, gearbox bolts, and nuts using the Onshape Standard Content and MKCad app parts. When inserting Onshape Standard Content, you can use the snap mode to automatically add the mates when inserting or insert the component and then manually mate it. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e1/e1s0.webp" style="width:100%">
      <figcaption>19. Finished assembly. Make sure to sort your parts into folders and name your replicate features. </figcaption>
    </figure>
  </div>

  

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1,4)" style="background-color: #000; color: #fff;">&#10094;</a>
  <a class="next" onclick="plusSlides(1,4)" style="background-color: #000; color: #fff;">&#10095;</a>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

In this exercise you made your first gearbox. In doing so, you also used part configurations - which are a powerful tool that allows for variations of the same part. The gears that you inserted from MKCad were configurable - you were able to easily change the tooth count of the gear without needing to inserting a new component.

### Exercise 2: Two Stage Gearbox

In this exercise, you will be CADing and assembling a two stage gearbox. 

The goal of this exercise is to practice modeling more advanced gearboxes. You will also learn how to use the `Vent` Featurescript used for pocketing.

<center>**Exercise 2 Instruction Slides**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s1a.webp" style="width:100%">
      <figcaption>1a. Create the layout sketch for the gearbox. Start by drawing the 2nd stage, which is a 20T gear to a 50T gear.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s1b.webp" style="width:100%">
      <figcaption>1b. Draw the first stage, which is a 12T motor pinion gear to a 50T gear.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s1c.webp" style="width:100%">
      <figcaption>1c. Draw the outline of the motors as a 2.5" diameter circle. This is the finished layout sketch for the gearbox.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s2.webp" style="width:100%">
      <figcaption>2. Create a new sketch to draw the profile of the plate. Add the bearing holes, which are 1.125" diameter holes, as well as the motor boss holes, which are 0.8". Also add the motor mounting holes. You can utilize the <code>Mirror</code> sketch tool to mirror the geometry from the left side to the right side. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s3.webp" style="width:100%">
      <figcaption>3. Extrude the plate to be 1/4" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s4.webp" style="width:100%">
      <figcaption>4. Use the <code>Spacer</code> Featurescript to create the gearbox spacer. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s5.gif" style="width:100%">
      <figcaption>5. Use the <code>Shaft</code> Featurescript to create the first stage shaft. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s6.webp" style="width:100%">
      <figcaption>6. Use the <code>Shaft</code> Featurescript to create the output shaft.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s7.webp" style="width:100%">
      <figcaption>7. Create a sketch on the face of the plate and draw the lines for the pocketing ribs. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s8.gif" style="width:100%">
      <figcaption>8. Use the <code>Vent</code> Featurescript to pocket the plate by selecting the sketch regions created by the previous sketch. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s9.webp" style="width:100%">
      <figcaption>9. Finished part studio. Name the key sketches and parts. Set the material of the plate and spacers to 6061 Aluminum. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s10.gif" style="width:100%">
      <figcaption>10. Insert the part studio into the assembly and fix only the gearbox plate. Mate the spacer to the plate. Then, use the <code>Replicate</code> tool to replicate the spacer and its associated mate onto the other spacer locations. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s11.webp" style="width:100%">
      <figcaption>11. Copy the gearbox plate and mate it into place. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <li class="slideVideo">
      <video width="1920" controls>
        <source src="/img/design-guide/stage1b/exercises/e2/e2s12.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>12. Assemble the bearings and shafts using parts from the MKCad App. </figcaption>
    </li>
  </div>

  <div class="mySlides fade">
    <li class="slideVideo">
      <video width="1920" controls>
        <source src="/img/design-guide/stage1a/exercises/e5/e5s13.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>13. Assemble the motor and motor pinion gear using parts from the MKCad App. </figcaption>
    </li>
  </div>

  <div class="mySlides fade">
    <li class="slideVideo">
      <video width="1920" controls>
        <source src="/img/design-guide/stage1b/exercises/e2/e2s14.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>14. Assemble the shaft spacers and gears using parts from the MKCad App. </figcaption>
    </li>
  </div>

  <div class="mySlides fade">
    <li class="slideVideo">
      <video width="1920" controls>
        <source src="/img/design-guide/stage1b/exercises/e2/e2s15.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>15. Assemble the shaft retention bolts, motor bolts, gearbox bolts, and nuts using the Onshape Standard Content and MKCad app parts. </figcaption>
    </li>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e2/e2s0.webp" style="width:100%">
      <figcaption>15. Finished assembly. Make sure to sort your parts into folders and name your replicate features. </figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1,5)" style="background-color: #000; color: #fff;">&#10094;</a>
  <a class="next" onclick="plusSlides(1,5)" style="background-color: #000; color: #fff;">&#10095;</a>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

In this exercise, you practiced more complex gearbox modeling and mating together larger assemblies. 

### Exercise 3: Belt and Gear Transmission

<center>**Exercise 3 Part Studio Instruction Slides**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide0" class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s0.webp" style="width:100%">
      <figcaption>0. Final part studio.</figcaption>
    </figure>
    </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s1.webp" style="width:100%">
      <figcaption>1. Draw the tube profiles for the frame. There is a an 1/8" gap between the slanted tube and the vertical tube to allow for assembly tolerances. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s2.webp" style="width:100%">
      <figcaption>2. Use the <code>Extrude Individual</code> Featurescript to extrude the tube profiles.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s3.webp" style="width:100%">
      <figcaption>3. Use the <code>Tube Converter</code> Featurescript to convert the rectangles into hole patterned 1x1 thin-wall tube (1/16" thick wall).</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s4.webp" style="width:100%">
      <figcaption>4. Use the <code>Gusset</code> Featurescript to add a corner gusset between the lower two tubes.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s5.webp" style="width:100%">
      <figcaption>5. Create the gearbox layout sketch on the outer face of the bottom tube. Begin by drawing the two gears, a 60T and 20T gear. The 60T gear is the output, and we would like to constrain it to a specific location given by the 2" and 4.5" dimensions.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s6.webp" style="width:100%">
      <figcaption>6. Next, draw the 5mm pitch 12T and 36T pulleys. Use a line to connect the two pulleys. Pay attention to the expressions that were entered to calculate the pitch diameters of the pulleys. Also space the 36T pulley to be 0.25" from the vertical tube. This step fully constrains the location of the gears.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s7.webp" style="width:75%">
      <figcaption>7. Use a belt c-c calculator (eg: reca.lc) to calculate the pulley c-c. In this example, we know we have a 60T belt on hand, so we would like to use that specific belt in the design. The belt we are using is 5mm pitch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s8.webp" style="width:100%">
      <figcaption>8. Add the calculated c-c to the layout sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s9.webp" style="width:100%">
      <figcaption>9. Optionally draw two tangent lines to connect the two pulley circles. This represents the belt.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s10.webp" style="width:100%">
      <figcaption>10. Finally, sketch a 2.5" circle for the motor. Space the motor to be 1/8" away from the slanted tube. The layout sketch is now fully defined.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s11.webp" style="width:100%">
      <figcaption>11. Create the plate sketch on the outer face of the bottom tube. Begin by drawing the two 1.125" diameter bearing holes. Add a 0.95" for the bearing boss instead of the standard 0.8" so that the 12T pulley on the motor can fit through the hole to assist with real life assembly. This will become more clear when you create the gearbox assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s12.webp" style="width:100%">
      <figcaption>12. Add a 2" bolt circle for the motor. Constrain the center of the top left hole to be coincident with the center line between the pulleys. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s13.webp" style="width:100%">
      <figcaption>13. Add the tube mounting holes for the plate. Note that the holes reference the edges of the tube and not the holes on the tube. This is to make the model more parametric, as changes in the tube can change the locations of the holes and break the gearbox plate sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s14.webp" style="width:100%">
      <figcaption>14. Draw the outline for the plate. Space the bottom of the plate 0.25" from the edge of the pitch circle for the 60T gear. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s15.webp" style="width:100%">
      <figcaption>15. Add two holes for spacers. The construction circles represent the 3/8" diameter spacer. The top hole is tangent with the left edge of the plate and tangent with the 2.5" motor circle.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s16.webp" style="width:100%">
      <figcaption>16. Extrude the plate to be 1/4" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s17.webp" style="width:100%">
      <figcaption>17. On the opposite side, create a sketch for the inner plate. Utilize the <code>Use</code> sketch feature to copy over common geometry (holes, outline). Do not copy the motor holes, as there will be a cutout on the inner plate for the body of the motor.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s18.webp" style="width:100%">
      <figcaption>18. Finish the outline of the plate by adding an arc for the motor cutout.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s19.webp" style="width:100%">
      <figcaption>19. Extrude the inner plate to be 1/4" thick.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s20.webp" style="width:100%">
      <figcaption>20. Add a 3/16" radius fillet on the two edges for the motor cutout. The radius is selected to match the 3/8" diameter spacer.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s21.webp" style="width:100%">
      <figcaption>21. Model the 3/8" diameter spacer. The <code>Up to Face</code> end condition can be utilized to keep the spacer length parametric.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s22.webp" style="width:100%">
      <figcaption>22. Use the <code>Contextless Belt</code> Featurescript to create a simplified model of the belt. The pitch of the belt is 5mm and the width is 9mm.  </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s23.webp" style="width:100%">
      <figcaption>23. Use the <code>Shaft Generator</code> Featurescript to create the 1st stage shaft. Note that this length is simply an estimate. While you could calculate the length of the shaft based on the components that will go on it, it is often easier to create the assembly then measure what the shaft length should be and update accordingly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s24.webp" style="width:100%">
      <figcaption>24. Use the <code>Shaft Generator</code> Featurescript to create the output shaft.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s25.webp" style="width:100%">
      <figcaption>25. Optionally pocket the plates. To begin, create a sketch on the outer face of the motor plate and draw lines to create the struts.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s26.webp" style="width:100%">
      <figcaption>26. Use the <code>Vent</code> Featurescript to add the pocketing. Use 0.15" wide ribs and 0.15" tool radius. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s27.webp" style="width:100%">
      <figcaption>27. Create a sketch on the inner plate and draw the strut lines. You can utilize the <code>Use</code> sketch feature to copy over strut lines from the motor plate pocketing sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s28.webp" style="width:100%">
      <figcaption>28. Use the <code>Vent</code> Featurescript to add the pocketing. Again, uUse 0.15" wide ribs and 0.15" tool radius. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3s0.webp" style="width:100%">
      <figcaption>29. Finished part studio. Name the key sketches and parts. Set the material of the plate and spacers to 6061 Aluminum. The tube and shafts should have their materially automatically selected already. </figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1,6)" style="background-color: #000; color: #fff;">&#10094;</a>
  <a class="next" onclick="plusSlides(1,6)" style="background-color: #000; color: #fff;">&#10095;</a>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

<center>**Exercise 3 Assembly Instruction Slides**</center>
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/design-guide/stage1b/exercises/e3/e3a0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1,7)" style="background-color: #000; color: #fff;">&#10094;</a>
  <a class="next" onclick="plusSlides(1,7)" style="background-color: #000; color: #fff;">&#10095;</a>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

## Summary

Congratulations on completing Stage 1B! Keep up the good work!

Here is a quick summary of what you have achieved in stage 1B:

* Learned the basics of bearings, shafts, gears, chain and sprockets, and belt and pulleys
* Learned how to model power transmissions
* Learned how to use the `Contextless Belt` and `Chain Generator` Featurescripts
* Learned how to insert Standard Library components and mate bolts and nuts
* Learned how to use the `Shaft` and `Vent` Featurescripts
* Learned how to use the `Replicate` tool

Again, it should be noted that Stage 1B is a very basic introduction to modeling power transmissions and some details were glossed over. It is recommended to visit the [Design Fundamentals](/design-fundamentals/) power transmissions pages after completing stage 1 to gain a deeper understanding.

In stage 1C, you will begin to learn the basic workflow for robot modeling. This is the final step before being able to design a full mechanism!

<br>
<center>1B: Gearboxes</center> 
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