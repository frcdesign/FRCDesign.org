# 2D: Cascade Elevator

## Part Studio
1. Add the `Origin Cube` feature and derive the master sketches if you made them in a separate part studio.
2. Use extrude individual to create the tubes (without creating only duplicates; this means only the bottoms of stages on one side).
3. Convert the extrusions into tubes.

    ??? Tip "Converting Extrusions into Tubes"
        Tube converter is the easiest way to do this, as demonstrated before, but the hole pattern can break things and be misaligned pretty easily if the dimensions of the elevator end up changing. The most parametric way is to shell the tubes manually, then use a mix of sketches and linear patterns to create the hole pattern. This way you can build design intent into the hole pattern so it won't be misaligned with anything when dimensions change.

        To create parametric hole patterns, you can start by using the [**Measure Value**](https://cad.onshape.com/documents/77baa8153589a7fc5f289829/w/cffd0f2a7077380d5378a885/e/d3174bf5315e6aafcb889367?renderMode=0&uiState=652ee7d25129162fc0afad5f "Measure Value Featurescript Onshape Document"){:target="_blank"} featurescript from CADSHARP to measure the length of the tube. You create your first hole at the top of the tube, then create a feature pattern or sketch pattern down the length of the tube with the distance of 0.5" and the instance count set to `((#frame_side_tube/inch)*2)-1`. This method keeps the hole count parametric to the length of the tube.

4. Transform and copy the tubes to complete the structure.

    !!! Tip
        At this point, as design lead, you could create mate connectors, subassemblies, and top level assembly, and hand off the elevator to other people to parallelize the process if that's how your team works.

5. Model any unique crushblocks

    !!! Info 
        Crushblocks and tube plugs are commonly used for most superstructures and elevators nowadays. Find out what they are and why they're useful on [the design handbook page about structure](../../../design-handbook\structure\structure.md "Structure Handbook Page"){:target="_blank"}.

<figure markdown="span">
    <img src="/img/learning-course/stage2-elevator/tubesAndCrushblocks.webp" style="width:75%">
    <figcaption> Finished elevator tubes </figcaption>
</figure>

6. Decide where you want your rigging (rope) and model it with a path, profile, and sweep.
7. Derive the [TTB chain comb](https://www.thethriftybot.com/products/elevator-25h-chain-drive-kit "TTB Chain Comb Product Page"){:target="_blank"} into place on a first stage tube. This is for knowing how much to space the chain off from the tubes.
8. Sketch the chain transmission and crossmember, including the bearing holes for the sprockets.
9. Create the plates and tube for the crossmember. The clamp for the rigging will be mounted to the crossmember, but it's also for the rigidity of the base stage.
10. Derive the [TTB cable clamp](https://www.thethriftybot.com/products/elevator-dyneema-pulley-kit "TTB Cable Clamp Product Page"){:target="_blank"} into place on the crossmember and create mounting holes for it, and a crushblock if bolting all the way through the tube.
11. Add holes for the tube plugs on the crossmember.
12. Create the chain transmission, including the chain, any custom spacers, and axles
13. Derive some maxplanetary parts to build the gearbox around. Create spacers and mounting for both maxplanetaries. Make sure to leave them easily accessible and replaceable
14. Add plates at the bottom of the elevator to support the MAXplanetary shafts.
15. Optionally, derive nut strips and a ratchet plate for the carriage and create the shaft for the rigging to be tied to.
16. Create a reference mate in the middle of the base tube, owned by the origin cube, to later mate the subassemblies together with.

<figure markdown="span">
    <img src="/img/learning-course/stage2-elevator/elevatorPartStudio.webp" style="width:75%">
    <figcaption> Finished elevator part studio </figcaption>
</figure>

<br>