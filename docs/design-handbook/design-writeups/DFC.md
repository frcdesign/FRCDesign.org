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

**Gears:** Gears are the most versatile type of power transmission. They are useful in virtually every application, whether it's switching direction on rollers or pivoting an arm. 

## Using Less Stages on a Gearbox

The easiest way to reduce backlash in a gearbox is to use less stages. In a single stage, there will always be some backlash present. Increasing the number of stages as a result increases the amount of backlash in the system as the backlash compounds. Reducing stages can be done through using larger reductions in a single stage.

!!! Note
    It's important to consider how much the total reduction in a system *needs* to be. Often, teams will over/underestimate the reduction needed, leading to problems down the line. With too much reduction, unnecessary backlash is added and, at worst, the torque output is too much for the mechanical system to handle. With too little, it may not be enough for the application or cause inaccuracy. To calculate the proper reduction needed, tools such as [recalc](reca.lc) should be utilized. 

## Shim Tape/Green Lockite

Shim tape and green loctite are two common solutions to backlash. They each solve the same problem: slop between the motion component and the axle itself. Although a common cause of backlash, it is relatively easy to solve. 

!!! Tip
    Tolerances vary from vendor to vendor. For example, a pulley from one vendor may not fit on an axle from another vendor, or be too loose. This may cause excessive slop in a system. Keep this in mind when assembling or ordering parts.

# Shim Tape

Shim tape is a thin, metal tape applied to the inside of motion components. The tape allows the component to hug the axle more, preventing slop between axle and component. 

<figure>
  <img src="/design-handbook/design-writeups/images/shimtapeprocess.webp" style="width:80%">
  <figcaption>Shim tape inserted in a gear. Credit: 4414<figcaption>
</figure>

The steps to using shim tape are as follows. (Credit: [4414](https://www.chiefdelphi.com/t/team-4414-hightide-2023-robot-tsunami/428584/231))

<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/design-handbook/design-writeups/images/shimtapestep1.webp" style="width:100%">
      <figcaption>Cut shim tape to length and apply to interior of component.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
      <img src="/design-handbook/design-writeups/images/shimetapestep2.webp" style="width:100%">
      <figcaption>Bend shim tape around edge. This is important because shim tape can slide along an axle as you're inserting the component.</figcaption>
    </figure>
  </div>


<div class="mySlides fade">
    <figure>
      <img src="/design-handbook/design-writeups/images/shimtapestep3.webp" style="width:100%">
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

## Tensioning



# Hardstops



# Encoders and Sensors



<!-- Tutorial for shimming gears to reduce hex-to-hex interface backlash:

[Link to Buy Shim Tape](https://www.mcmaster.com/1143N23)

<center><img src="\img\design-handbook/DFC/hightide shim tape gears.webp" style="width:60%"></center>
<center><img src="\img\design-handbook/DFC/hightide shim tape length.webp" style="width:60%"></center>
<center><img src="\img\design-handbook/DFC/hightide shim tape placement.webp" style="width:60%"></center> -->



<br>