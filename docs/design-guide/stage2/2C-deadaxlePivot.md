<style>

    details {
        font-size: 0.7rem !important;
    }    

</style>

# 2C: Dead Axle Pivot

## Rotary Mechanisms & Dead Axles
A rotary mechanism allows us to pivot objects or mechanisms through rotational movement, typically using wrists or arms.

[INSERT 2 EXAMPLE IMAGES OF PIVOTS]

| **Axle Type** | **Description**  | **Pros**   | **Cons**  |
|---------------|------------------------------------------------------------|--------------------------|-----------------------------------|
| **Dead Axle** | The axle remains stationary, and the mechanism pivots around it.   | Stronger, larger axle, no risk of axle twisting.| Requires a separate method to transfer power. May have packaging issues  |
| **Live Axle** | The axle rotates with the mechanism. Commonly used with hex axles and hubs. Not recommended due to the risk of twisting.| Simple setup; direct power transfer.  | High risk of twisting; commonly weaker due to small diameter. |
| **Coaxial Axle** | The axle rotates for one mechanism, while something separate pivots around it| Can be extremely light and compact| Difficult to design, sensitive to friction| 

Out of these, dead axles (and coaxial designs as a result) are the best choice for pivots, especially ones that need to handle a significant amount of load.

- **Strength:** Larger diameter axles fastened to the rest of the structure are stronger, resist bending, and provide consistent motion.

- **Power Transmission:** Power is transferred through attached sprockets, pulleys, or gears, rather than through the axle itself.

### Key Design Rules
1. Keep the center of mass of the pivoting "arm" as close to the pivot as possible.
2. Ensure the axle is fully supported, using either box tube or nested plates.
3. Maintain a rigid support structure.
4. If the structure is wide, power both sides for additional rigidity.

<br>

## Applications/Examples

[NEEDS IMAGES]

### Wrist
- **Description:** Short, light rotary mechanisms. These are commonly seen to allow for ground pickup or pitch adjustments.
- **Axle Type:** You'll find coaxial, live, and dead axles for wrists. 
- **Friction Management:** Both bearings and bushings are common. 

### Large Pivots
- **Description:** Include pink arms, pivoting elevators, and large arms.
- **Axle Type:** Dead axle is preferred; consider using 35 chain for heavy loads.
- **Friction Management:** Bushings are more common, though thin x contact bearings are used occasionally.

### High Load Short Pivot
- **Description:** Pivots full mechanisms such as a shooter to adjust shot angle.
- **Axle Type:** Dead axle recommended with bearings or bushings.
- **Power Transmission:** Rack and pinion are gaining popularity.

<br>

## Project

This stage's project is a simple dead axle pivot, not for any specific game or in a specific context, but one that teaches concepts that would allow one to apply it to any rotary mechanism.

<center><img src="/img/design-guide/stage2-pivot/Top Level Pivot.webp" width="70%"></center>

The reference is provided in [**this document**](https://cad.onshape.com/documents/f781e567eaf7542338c1c0fe/w/168c72076cea4a10ae424f16/e/b3ca833c47e02e056cc1609f?renderMode=0&uiState=66c67dcad558b60d99f98938). Model a copy of it in your own document. Necessary concepts and a basic guide are both provided below.

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

    <br>
    <figure><img align="left"  src="/img/design-guide/stage2-pivot/wcpbushing.webp" width="40%"><img align="right" src="/img/design-guide/stage2-pivot/xcontact.webp" width="40%"></figure>
    <figcaption>A stepped bushing and a large x contact bearing sometimes used for large dead axles.</figcaption>
    <br>

    ![wcp bushing](wcpbushing.webp)
    ![x contact bearing](1131386891.webp)

??? Concept "Power Transmission"

    Sprocket and chain is used for transmitting power due to the load rating for chain and extremely low chance of it slipping. Using large sprockets bolted to the mechanism helps reduce backlash and increase load capacity, while ensuring that the axle remains a dead axle. Torque is transmitted directly to the rotating mechanism from the sprocket, while the entire thing only uses the axle as a structural member to rotate on.


??? Concept "Tensioning"

    To accommodate chain stretch over the course of a season and reduce backlash, an active tensioning system is required. If enough chain length is available, **inline tensioners** such as turnbuckles and Spartan tensioners are the simplest way to tension the chain. If there isn't enough space for an inline tensioner (if the chain moves too much, the tensioner might run into either of the sprockets), other methods, such as moving the position of one of the sprockets with a sliding or rotating gearbox or stage, may be used. 

    <br>
    <figure><img align="left"  src="/img/design-guide/stage2-pivot/turnbuckle.webp" width="40%"><img align="right" src="/img/design-guide/stage2-pivot/spartan_tensioner.webp" width="40%"></figure>
    <figcaption>Two types of inline tensioners, a turnbuckle and a Spartan tensioner.</figcaption>
    <br>

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


### Process
1. Lay out the pivot location and driving sprocket position.
2. Design the support plates.
3. Complete the pivot mechanism.
4. Finalize and review the design.

Good luck!

<br>
