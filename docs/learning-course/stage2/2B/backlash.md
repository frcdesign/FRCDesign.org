# 2B: Dead Axle Pivot

## Backlash

Especially for pivots, which you want to make as rigid as possible for better control, you want to take steps to reduce the backlash as much as possible.

| **Source**        | **Details**  | **Solution**  | Image |
|-------------------|----------------------------|---------------------------------------------------------------------|-----|
| **Hex Interfaces**| Gaps in hex to hex hole interfaces create backlash. | Use shim tape to reduce gaps.  | <img src="/img/design-handbook/DFC/hightide%20shim%20tape%20placement.webp" width=40%>
| **Sprocket Clocking** | Ensure correct alignment of sprockets to prevent uneven movement.   | Align notches on both sides. |<img src="\img\learning-course\stage2-pivot\wcp sprocket clock.webp" width=40%><figcaption>Note the notch on the sprocket</figcaption>
| **Mounting Slop** | Loose bolt-to-hole interfaces can introduce slop.  | Use proper bolting and strong spacers. |
| **Reduction Stages**| More reduction stages increase backlash. | Keep stages to 3 or fewer for optimal performance. One of the "stages" being the sprocket reduction|
| **Chain Stretch** | Chain stretching over time leading to backlash| Periodically check chain tension. If extremely high precision is needed (shooters), utilize a sector gear instead| 

Details on these solutions are covered in [the design handbook page discussing designing for controllability](../../../design-handbook/design-writeups/DFC.md "Designing for Controllability Page"){:target="_blank"}.


### Reference Design

Backlash typically arises as a result of real life tolerances so they are difficult to model in CAD. If the reference design were built in real life, it would utilize shim tape to reduce gear slop, aligned sprockets, and properly tensioned chain to minimize backlash.

<br>