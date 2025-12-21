# Designing for Controllability

A guide on designing mechanisms and power transmissions for controllability. Make your programmer's life easier.

# Backlash

In mechanical systems where precision is needed, it is imperative to reduce backlash. **Backlash** is defined as the distance/angle that a component can move before it engages with another component. For example, in gears there is a tiny amount of space between the interlocking teeth of two gears, which allows one gear to move slightly before moving the next gear. This slop in a system caused by gaps in the parts. For FRC, this could be gaps between gears or between the motion component and the axle. Too much backlash in a system, especially for cases that require high precision (like pivots), will make the system unstable and inaccurate. Thankfully, there are many ways to reduce backlash.

## Power Transmission Methods

When choosing how to transmit rotational power, understanding which methods cause the most backlash can guide decision making. Of the three main types of power transmission in FRC (chain, belts, gears), each have their own pros and cons. 

**Chain:** Chain works well in high-torque scenarios, commonly in pivots. Chain transmissions are capable of having large backlash that reduces a mechanicam's accuracy significantly. However, if designed right, chain transmissions can have minimal backlash. This means having as much wrap as possible around sprockets and including chain tensioning. More information on chain tensioning can be seen in the [tensioning section](google.com) under the design writeups. 

**Belts:** Belts work well in low-torque, high speed scenarios. They are used in many applications such as rollers, elevators, and sometimes small pivots. They are notable for having nearly zero backlash due to the way the belt engages with the pulleys. However, they are also weaker than chain, so they are not suitable for most pivots where minimal backlash is useful. They can still be very useful in elevators, where many designs utilize belt for linear extensions. 

**Gears:** Gears are the most versatile type of power transmission. They are useful in virtually every application, whether it's switching direction on rollers or pivoting an arm. 

## Using Less Stages on a Gearbox

The easiest way to reduce backlash in a gearbox is to use less stages.  

## Shim Tape/Green Locktite



## Tensioning



# Hardstops



# Encoders and Sensors



<!-- Tutorial for shimming gears to reduce hex-to-hex interface backlash:

[Link to Buy Shim Tape](https://www.mcmaster.com/1143N23)

<center><img src="\img\design-handbook/DFC/hightide shim tape gears.webp" style="width:60%"></center>
<center><img src="\img\design-handbook/DFC/hightide shim tape length.webp" style="width:60%"></center>
<center><img src="\img\design-handbook/DFC/hightide shim tape placement.webp" style="width:60%"></center> -->



<br>