# 2B: Dead Axle Pivot

## Rotary Mechanisms
Rotary mechanisms enable the pivoting of mechanisms through rotational movement. These mechanisms come in many shapes and sizes but there are a couple good practices that should be followed when designing powered pivots.

<figure><img align="left"  src="/img/learning-course/stage2-pivot/6036pivot.gif" width="46%" style="border:5px solid #ADADAD"><img align="right"  src="\img\learning-course\stage2-pivot\2910video.gif" width="48%" style="border:5px solid #ADADAD"></figure>
<center><figcaption>6036's 2023 Arm and 2910's 2023 Arm</figcaption></center>

Take a look at [Team 2910's 2023 robot reveal video](https://youtu.be/R5r28-MQqzg?si=wgrmD0YIbUkkHDyv&t=65 "2910 2023 Reveal Video"){:target="_blank"} to see their pivoting arm in action. 


### Pivot Drive Systems

Two types of pivot drive systems exist: Dead Axles and Live Axles. The following table compares the pros and cons of the two types.


| **Axle Type** | **Description**  | **Pros**   | **Cons**  | **Picture** | 
|---------------|------------------------------------------------------------|--------------------------|-----------------------------------|------|
| **Dead Axle** | The axle remains stationary, and the mechanism pivots around it.   | Stronger, larger axle, no risk of axle twisting.| Requires a separate method to transfer power. May run into packaging issues  | ![dead axle](\img\learning-course\stage2-pivot\dead-axle-side.webp){width=70%}
| **Live Axle** | The axle rotates with the mechanism. Commonly used with hex axles and hubs.| Simple setup. Direct power transfer.  | Risk of twisting the axle. Commonly done with 1/2 hex which may be too weak for the application| ![live axle](\img\learning-course\stage2-pivot\liveAxlePivot.webp){width=70%}

Out of these, dead axles (and coaxial designs as a result) are the best choice for pivots, especially ones that need to handle a significant amount of load.

Some key points when designing pivoting mechanisms are: 

1. Keep the center of mass of the pivoting "arm" as close to the pivot as possible.
2. Ensure the axle is fully supported, using either box tube or nested plates.
3. Maintain a rigid support structure.
4. If the structure is wide, power both sides for additional rigidity.

### Applications & Examples

| **Mechanism Type**       | **Description**                                                                 | **Axle Type**                                                        | **Friction Management**                                             | **Images**                                                                                                     |
|--------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------|--------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| **Wrist**                | Short, light rotary mechanisms. These are commonly seen to allow for ground pickup or pitch adjustments. | You'll find coaxial, live, and dead axles for wrists.                 | Both bearings and bushings are common.                           | <center><img src="\img\learning-course\stage2-pivot\973-wrist.webp" width="50%"></center>                           |
| **Large Pivots**         | Include pink arms, pivoting elevators, and large arms.                           | Dead axle is preferred; consider using 35 chain for heavy loads.     | Bushings are more common, though thin x contact bearings are used occasionally. | <center><img src="\img\learning-course\stage2-pivot\2910-pivot.webp" width="50%"></center>                           |
| **High Load Short Pivot**| Pivots full mechanisms such as a shooter to adjust shot angle.                   | Same as for large pivots.                                            | Both bearings and bushings are used.                             | <center><img src="\img\learning-course\stage2-pivot\citrus-pivot.webp" width="50%"></center>                           |


Other mechanism examples and deep dives for pivots can be found on the [pivots page](/mechanism-examples/pivots/index.md "Pivot Mechanism Examples Page"){:target="_blank"}. The mechanism fundamentals page is yet to be made but will also be a helpful resource.


<br>