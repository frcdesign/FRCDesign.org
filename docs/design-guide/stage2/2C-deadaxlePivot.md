<style>
    .centeredImages {
        display: inline-block;
        margin-left: auto;
        margin-right: auto;
        height: 60px; 
    }
    details {
        font-size: 0.7rem !important;
    }    
    
    #wrapper{
    text-align:center;
    }

</style>

# 2C: Dead Axle Pivot

## Rotary Mechanisms & Dead Axles
Rotary mechanisms enable the pivoting of mechanisms through rotational movement. These mechanisms come in many shapes and sizes but there are a couple good practices that should be followed when designing powered pivots.

<br>
<figure><img align="left"  src="/img/design-guide/stage2-pivot/sushiPivot.webp" width="45%"><img align="right" src="/img/mechanism-examples/pivots/2910/2910pivotcropped.webp" width="45%"></figure>
<figcaption>7461's 2023 Dead Axle Pivot and 2910's 2023 Dead Axle Pivot</figcaption>
<br>

Take a look at [this video](https://youtu.be/R5r28-MQqzg?si=wgrmD0YIbUkkHDyv&t=65) to see team 2910's 2023 robot pivoting arm in action. 

Two types of pivot drive systems exist: Dead Axles and Live Axles. The following table compares the pros and cons of the two types.


| **Axle Type** | **Description**  | **Pros**   | **Cons**  | **Picture** | 
|---------------|------------------------------------------------------------|--------------------------|-----------------------------------|------|
| **Dead Axle** | The axle remains stationary, and the mechanism pivots around it.   | Stronger, larger axle, no risk of axle twisting.| Requires a separate method to transfer power. May run into packaging issues  | ![dead axle](\img\design-guide\stage2-pivot\dead-axle-side.webp){width=70%}
| **Live Axle** | The axle rotates with the mechanism. Commonly used with hex axles and hubs.| Simple setup. Direct power transfer.  | Risk of twisting the axle. | ![live axle](\img\design-guide\stage2-pivot\liveAxlePivot.webp){width=70%}

Out of these, dead axles (and coaxial designs as a result) are the best choice for pivots, especially ones that need to handle a significant amount of load.

Some key points when designing pivoting mechanisms are: 

1. Keep the center of mass of the pivoting "arm" as close to the pivot as possible.
2. Ensure the axle is fully supported, using either box tube or nested plates.
3. Maintain a rigid support structure.
4. If the structure is wide, power both sides for additional rigidity.

<br>

### Applications/Examples

### Wrist
- **Description:** Short, light rotary mechanisms. These are commonly seen to allow for ground pickup or pitch adjustments.
- **Axle Type:** You'll find coaxial, live, and dead axles for wrists. 
- **Friction Management:** Both bearings and bushings are common. 
<center><img src="\img\design-guide\stage2-pivot\973-wrist.webp" width="50%"></center>

### Large Pivots
- **Description:** Include pink arms, pivoting elevators, and large arms.
- **Axle Type:** Dead axle is preferred; consider using 35 chain for heavy loads.
- **Friction Management:** Bushings are more common, though thin x contact bearings are used occasionally.
<center><img src="\img\design-guide\stage2-pivot\2910-pivot.webp" width="50%"></center>

### High Load Short Pivot
- **Description:** Pivots full mechanisms such as a shooter to adjust shot angle.
- **Axle Type:** Dead axle recommended with bearings or bushings.
- **Power Transmission:** Rack and pinion are gaining popularity.
<center><img src="\img\design-guide\stage2-pivot\citrus-pivot.webp" width="50%"></center>

Other mechanism examples and deep dives for pivots can be found on the [pivots page](/mechanism-examples/pivots/). The mechanism fundamentals page is yet to be made but will also be a helpful resource.


<br>

## Project

This stage's project is a simple dead axle pivot, not for any specific game or in a specific context, but one that teaches concepts that would allow one to apply it to any rotary mechanism.

<center><img src="/img/design-guide/stage2-pivot/Top Level Pivot.webp" width="70%"></center>

The reference is provided in [**this document**](https://cad.onshape.com/documents/f781e567eaf7542338c1c0fe/w/168c72076cea4a10ae424f16/e/b3ca833c47e02e056cc1609f?renderMode=0&uiState=66c67dcad558b60d99f98938). You should model a copy of it in your own document. The mechanism design concepts, decisions made for this design, and a basic guide are all provided below.

### Requirements
- **Reduction:** Use Max planetaries.
- **Chain:** Utilize 25 chain with a large sprocket reduction.
- **Axle:** Use 7/8 inch tube for the dead axle and ensure proper support.

### Engineering Concepts & Decisions

The following sections describe the intentions and concepts behind the design of the pivot you will be copying. This helps integrate functional mechanism design with the differing CAD concepts for each mechanism for a complete lesson.

??? Concept "Strength"

    The primary considerations for the strength of a pivot are the rigidity (resistance to bending) and resistance to twisting. Dead axles provide superior strength to live axles due to the way they don't transmit any load and can be fastened to the rest of the structure. Larger round tube (such as 3/4" and 7/8" diameter) is preferred to 1/2" hex for its strength-to-weight ratio and resistance to twisting.

??? Concept "Friction"

    Friction must be minimized since the mechanism pivots around the axle. This can be done using either bushings or bearings. Bushings can handle higher loads at lower speeds, while bearings are more suited for higher speeds and lower loads, but larger bearings can be used for large dead axles. Bushings are used for this dead axle example because they package well, are suitable for the low speeds and potential higher loads of an arm, and it is easy to source ones made specifically for sprockets and tube from FRC vendors.

    <div id="wrapper">
        <img id="centeredImages" border="0" src="/img/design-guide/stage2-pivot/wcpbushing.webp"  width="30%">
        <img id="centeredImages" border="0" src="/img/design-guide/stage2-pivot/xcontact.webp" width="30%">
    <figcaption>A stepped bushing and a large x contact bearing sometimes used for large dead axles.</figcaption>
    </div>

??? Concept "Power Transmission"

    Sprocket and chain is used for transmitting power due to the load rating for chain and extremely low chance of it slipping. Using large sprockets bolted to the mechanism helps reduce backlash and increase load capacity, while ensuring that the axle remains a dead axle. Torque is transmitted directly to the rotating mechanism from the sprocket, while the entire thing only uses the axle as a structural member to rotate on.

    <br>
    <figure>
    <img src="\img\design-guide\stage2-pivot\power-example.webp" alt="Power Example" width="60%">
    <figcaption> A chain and Sprocket</figcaption>
    </figure>
    <br>

??? Concept "Tensioning"

    To accommodate chain stretch over the course of a season and reduce backlash, an active tensioning system is required. If enough chain length is available, **inline tensioners** such as turnbuckles and Spartan tensioners are the simplest way to tension the chain. If there isn't enough space for an inline tensioner (if the chain moves too much, the tensioner might run into either of the sprockets), other methods, such as moving the position of one of the sprockets with a sliding or rotating gearbox or stage, may be used. 

    <div id="wrapper">
        <img id="centeredImages" border="0" src="/img/design-guide/stage2-pivot/turnbuckle.webp" width="30%">
        <img id="centeredImages" border="0" src="/img/design-guide/stage2-pivot/spartan_tensioner.webp" width="30%">
    <figcaption>Two types of inline tensioners, a turnbuckle and a Spartan tensioner</figcaption>
    </div>

    For this design, enough chain length was provided for a simple inline spartan tensioner to work well.


??? Concept "Other Sources of Backlash"

    Especially for pivots, which you want to make as rigid as possible for better control, you want to take steps to reduce the backlash as much as possible.

    | **Source**        | **Details**  | **Solution**  |
    |-------------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
    | **Hex Interfaces**| Gaps in hex to hex hole interfaces create backlash. | Use shim tape to reduce gaps.  |
    | **Sprocket Clocking** | Ensure correct alignment of sprockets to prevent uneven movement.   | Align notches on both sides. |
    | **Mounting Slop** | Loose bolt-to-hole interfaces can introduce slop.  | Use proper bolting and strong spacers. |
    | **Reduction Stages**| More stages increase backlash. | Keep stages to 3 or fewer for optimal performance.|

    Details on these solutions are gone over in [the design fundamentals page about designing for controllability](../../design-fundamentals/design-writeups/DFC.md).



<br>

### Master Sketch

The master sketch is very simple as it uses maxplanetaries for most of the reduction. 

1. Use the origin cube featurescript to insert the origin cube
2. Dimension the cross bar
3. Lay out the pivot location and driving sprocket position above the cross bar. Dimension a construction line between them a distance that will give enough chain length to use an inline tensioner.
4. Create construction circles to represent the pitch circles of both sprockets and the diameter of the motor.

<center><img src="/img/design-guide/stage2-pivot/pivotMasterSketch.webp" width="70%"></center>

### Part Studio

1. Create a mate connector on the pivot point of the master sketch, owned by the origin cube. This will be used in the top level assembly to define motion between the subassemblies.
2. Create the cross bar tubes
3. Create the pivot support plates
4. Create the chain and hex axle using featurescripts
5. Create the dead axle tube, spacer, and washer.
6. Create the tubes for the arm, including access holes for bolts.
7. Create the plate to space the sprocket off from the arm.
8. Name and give materials and appearances to all your parts

<center><img src="/img/design-guide/stage2-pivot/PivotPartStudio.webp" width="70%"></center>

!!! Note
    Keep in mind you should be creating folders for related features while modeling the mechanism! It's easier doing it throughout the process than saving all the clean-up for the end.

### Assembly

Because this subsystem contains a static part and a moving part, we want to separate them into rigid (no movement) assemblies, then combine them at the top level. This makes load times significantly less.

Create an assembly for the static parts, insert the parts and origin cube from the part studio with the green checkmark, and group them together. Fasten the origin cube to the origin. Add the rest of the parts from the part studio, MKCAD, and standard content, using replicate and patterns when you can.

<center><img src="/img/design-guide/stage2-pivot/Dead Axle Subassembly.webp" width="60%"></center>

Create an assembly for the arm portion of the mechanism and do the same thing as above to complete the assembly and make it rigid.

<center><img src="/img/design-guide/stage2-pivot/Arm Subassembly.webp" width="60%"></center>

!!! Tip
    Below is an example of the instance list of a rigid assembly. Notice the icon in the top left indicating it's rigid. You can tell what can still move in the assembly by a "degree of freedom" icon (3 arrows to indicate the 3 axis.)
    <center><img src="/img/design-guide/stage2-pivot/deadAxleInstanceList.webp" width="20%"></center>

Now create a top level assembly and insert the static assembly (fasten to the origin) and intake arm assembly. Create a revolute mate between the mate connectors from the origin cubes in both assemblies and add a limit to it. This completes the deadaxle pivot assembly.

<center><img src="/img/design-guide/stage2-pivot/Top Level Pivot.webp" width="70%"></center>

## Summary

You've completed Stage 2C! To summarize what you've learned in this stage:

- Different types of axle usage
- Principles of designing a good pivot
- Applications of pivots (wrists, arms)
- One way of tensioning chain
- Different sources of backlash in a power transmission
- How to model a subsystem with multiple moving parts using the origin cube

This mechanism being completed leads to many more mechanisms that have multiple moving parts. Most robots have at least one pivot, though each one can be designed differently depending on the use case and packaging. Each pivot has some things in common though: try to minimize backlash, use a dead axle (usually with chain), and it will obviously need a power transmission included. In the next stage, you'll apply very similar concepts to an intake with a pivot and several rollers.

<br>
