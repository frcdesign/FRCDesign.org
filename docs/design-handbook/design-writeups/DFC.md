# Designing for Controllability

A guide on designing mechanisms and power transmissions for controllability. Make your programmer's life easier.

# Backlash

In mechanical systems where precision is needed, it is imperative to reduce backlash. **Backlash** is defined as the distance/angle that a component can move before it engages with another component. For example, in gears there is a tiny amount of space between the interlocking teeth of two gears, which allows one gear to move slightly before moving the next gear. This slop in a system caused by gaps in the parts. For FRC, this could be gaps between gears or between the motion component and the axle. Too much backlash in a system, especially for cases that require high precision (like pivots), will make the system unstable and inaccurate. Thankfully, there are many ways to reduce backlash.

<figure>
  <img src="/design-handbook/design-writeups/images/backlashimage.webp" style="width:80%">
  <figcaption>Diagram of backlash between gears.<figcaption>
</figure>

## Power Transmission Methods

When choosing how to transmit rotational power, understanding which methods cause the most backlash can guide decision making. Of the three main types of power transmission in FRC (chain, belts, gears), each have their own pros and cons. 

**Chain:** Chain works well in high-torque scenarios, commonly in pivots. Chain transmissions are capable of having large backlash that reduces a mechanicam's accuracy significantly. However, if designed right, chain transmissions can have minimal backlash. This means having as much wrap as possible around sprockets and including chain tensioning. More information on chain tensioning can be seen in the [tensioning section](google.com) under the design writeups. 

**Belts:** Belts work well in low-torque, high speed scenarios. They are used in many applications such as rollers, elevators, and sometimes small pivots. They are notable for having nearly zero backlash due to the way the belt engages with the pulleys. However, they are also weaker than chain, so they are not suitable for most pivots where minimal backlash is useful. They can still be very useful in elevators, where many designs utilize belt for linear extensions. 

**Gears:** Gears are the most versatile type of power transmission. They are useful in virtually every application, whether it's switching direction on rollers or pivoting an arm. They can also work well in final reductions, such as in **rack and pinions** or **10 DP gear pivots** which have extremely low backlash at the cost of being harder to assemble and manufacture than chain. 

<figure>
  <img src="/design-handbook/design-writeups/images/1678rackpinion.webp" style="width:80%">
  <figcaption>Example of a simple rack and pinion setup to pivot a shooter. (Credit: 1678)<figcaption>
</figure>

## Using Less Stages on a Gearbox

The easiest way to reduce backlash in a gearbox is to use less stages. In a single stage, there will always be some backlash present. Increasing the number of stages as a result increases the amount of backlash in the system as the backlash compounds. Reducing stages can be done through using larger reductions in a single stage.

!!! Note
    It's important to consider how much the total reduction in a system *needs* to be. Often, teams will over/underestimate the reduction needed, leading to problems down the line. With too much reduction, unnecessary backlash is added and, at worst, the torque output is too much for the mechanical system to handle. With too little, it may not be enough for the application or cause inaccuracy. To calculate the proper reduction needed, tools such as [recalc](reca.lc) should be utilized. 

## Shim Tape/Green Lockite

Shim tape and green loctite are two common solutions to backlash. They each solve the same problem: slop between the motion component and the axle itself. Although a common cause of backlash, it is relatively easy to solve. 

!!! Tip
    Tolerances vary from vendor to vendor. For example, a pulley from one vendor may not fit on an axle from another vendor, or be too loose. This may cause excessive slop in a system. Keep this in mind when assembling or ordering parts.

### Shim Tape

Shim tape is a thin, metal tape applied to the inside of motion components. The tape allows the component to hug the axle more, preventing slop between axle and component. The steps to using shim tape are as follows. (Credit: [4414](https://www.chiefdelphi.com/t/team-4414-hightide-2023-robot-tsunami/428584/231))

<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/design-handbook/design-writeups/images/shimtapestep1.webp" style="width:50%">
      <figcaption>Cut shim tape to length and apply to interior of component.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/design-handbook/design-writeups/images/shimtapestep2.webp" style="width:50%">
      <figcaption>Bend shim tape around edge. This is important because shim tape can slide along an axle as you're inserting the component.</figcaption>
    </figure>
  </div>


<div class="mySlides fade">
    <figure>
      <img src="/design-handbook/design-writeups/images/shimtapestep3.webp" style="width:50%">
      <figcaption>Component is ready to slide along axle. </figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <button class="prev" onclick="plusSlides(-1,1)"style="background-color: #000; color: #fff;">&#10094;</button>
  <button class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</button>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

### Green Loctite (WIP)

Green loctite can be used to fill spaces between the shaft and the component. Like most other loctite derivatives, it can act as an adhesive. 

## Tensioning

When using chain, it is necessary to include tensioning options. Over time, chain can stretch and loosen which causes slop in a system or skipping at worst. Tensioning ensures that, when the chain stretches, it can be properly tightened as needed to prevent slop. More information on chain tensioning can be found in the [chain tensioning](google.com) section under the design write-ups. 

When using belts in high-torque scenarios, it may be necessary to tension the belt so that it does not skip. This can be done in much the same ways that tensioning chain is done (aside from in-line tensioners). 

<figure>
  <img src="/design-handbook/design-writeups/images/chaintensioner.webp" style="width:67%">
  <figcaption>Adjustable in-line chain tensioner on an elevator.<figcaption>
</figure>

# Hardstops

Hardstops makes tracking position of a mechanism easier and more consistent. It allows mechanisms to be zeroed at the same location every time and provides a definite limit for the mechanism. Hardstops can be used on many different types of moving mechanisms, from elevators to arms. There are both mechanical and non-mechanical ways to make hardstops.

## Mechanical Hardstops

Mechanical hardstops are the simplest and most important to incorporate in a design. Essentially, hardstops physically prevent the mechanism from moving further than wanted. This can be very useful to prevent damage or to have a consistent zeroing location. Mechanical hardstops can be made in many ways. They can be separately designed in, or utilize an already existing structure to hardstop on, making them fairly easy to implement. However, they are susceptible to wear over time (which may not be significant for an FRC season) and breakage. "Softstops" can be used to lessen the force, such as using TPU stops or adding a protective foam, at the cost of less consistency. Mechanical hardstops are still incredibly useful and are great to implement whereever possible. Below are examples of mechanical hardstops. 

<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/design-handbook/design-writeups/images/elevatorhardstop.webp" style="width:50%">
      <figcaption>Upper hardstop on a continuous elevator. Prevents the elevator from extending too far.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/design-handbook/design-writeups/images/citrusstop.webp" style="width:50%">
      <figcaption>1678's 2024 shooter hardstops on the swerve modules to limit its angle, showing that hardstops do not need to be definitely defined and can hardstop on existing structures.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/design-handbook/design-writeups/images/254hardstop.webp" style="width:50%">
      <figcaption>254's 2022 intake hardstops on itself. This type of hardstop is special to four bar intakes. For more information on four bar intakes, check out the mechanism examples for intakes.</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <button class="prev" onclick="plusSlides(-1,1)"style="background-color: #000; color: #fff;">&#10094;</button>
  <button class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</button>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

## Non-Mechanical Hardstops

In cases where mechanical hardstops are impossible to include, non-mechanical hardstops using sensors can be used. These types of hardstops also have the advantage of being essentially immune to wear and tear, which may be necessary for mechanisms with large forces. They are commonly implemented with Hall Effect sensors and magnets. When the magnet passes the sensor, the sensor is activated and can then be used as a zeroing location. 

<figure>
  <img src="/design-handbook/design-writeups/images/1540elevatorstop.webp" style="width:80%">
  <figcaption>Example of a non-mechanical hardstop using a Hall Effect sensor on Stage 0 (highlighted in yellow) and a magnet on Stage 2 (highlighted in blue).<figcaption>
</figure>

# Encoders for Rotational Position

Motors have a built in relative encoder which allows them to track their own position, and as a result the position of mechanisms like pivots or elevators. In many cases, relying on the relative encoder of a motor is not enough or impossible, such as when there is too much backlash or hardstops are not possible. **Absolute encoders**, which calculate the rotational position of the pivoting shaft itself, can be used in these cases. Even then, using an absolute encoder ensures precision in position and negates the need for zeroing. 

Some absolute encoders, known as **Through-Bore Encoders**, are added directly onto a shaft to track it's position. However, this can only be used on *live axle* systems where the shaft spins to pivot a mechanism. Most absolute encoders are difficult to implement because they must track the position of the shaft, which is impossible on *dead axle* systems. However, there are several ways teams have found to design for encoders. 

<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/design-handbook/design-writeups/images/1678encodershooter.webp" style="width:50%">
      <figcaption>The encoder is put off of the shaft and is powered separately. However, it is powered with the same reduction as the shaft itself, meaning the encoder is essentially at the same position as the shaft. This is one of the easier ways to implement an encoder and works well, however it is not finding the direct position of the shaft which may cause differences if there is enough slop in the system. (Credit: 1678)</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/design-handbook/design-writeups/images/6995encoder.webp" style="width:50%">
      <figcaption>A belt goes directly off the pivoting shaft and connects to an encoder. Since the power transmission is belt, there is virtually zero backlash in the system, allowing for extreme precision. (Credit: 6995)</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <button class="prev" onclick="plusSlides(-1,0)"style="background-color: #000; color: #fff;">&#10094;</button>
  <button class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</button>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

<!-- there really should be a section on encoders for linear extensions here, but idk how they work lol-->

# Calculating Gear Ratios (WIP)

Guide on calculating the optimal gear ratio and using [ReCalc](reca.lc) <!-- unsure if i'll include anyways-->

For more information about gear ratios (and manual calculations without the use of ReCalc), check out [971's presentation on Designing for Controllability](https://www.spartanrobotics.org/workshops) by Travis Schuh.

# Offsetting Forces (WIP)

Guide on springs and constant force springs to offset forces. 

<!-- Tutorial for shimming gears to reduce hex-to-hex interface backlash:

[Link to Buy Shim Tape](https://www.mcmaster.com/1143N23)

<center><img src="\img\design-handbook/DFC/hightide shim tape gears.webp" style="width:60%"></center>
<center><img src="\img\design-handbook/DFC/hightide shim tape length.webp" style="width:60%"></center>
<center><img src="\img\design-handbook/DFC/hightide shim tape placement.webp" style="width:60%"></center> -->

<br>