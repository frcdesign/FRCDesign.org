---
hide:
  - toc
---

# List of Featurescripts

Onshape has its own scripting language to create custom features to automate aspects of design called [Featurescript](https://www.onshape.com/features/custom-features "Onshape Featurescript Page"){:target="_blank"}. There are a lot of featurescripts (what we call the custom features) that make designing for FRC much easier.

!!! tip
    The title of each featurescript or group of featurescripts links to its respective document. Right click the title and click "copy link address" for installing it to your profile using the process described on [the featurescript help page](featurescript-help.md).

## Recommended
These featurescripts are must haves to enhance your Onshape workflow. Many of these are developed by members of the FRC community and well maintained.

<div class="grid cards" markdown>

- [**Origin Cube Featurescript**](https://cad.onshape.com/documents/321c197a842fc5f1a29e6621/w/fc3cdd5ca7edcd93e02f13cc/e/c66db2b954da7f29d438195a "Origin Cube Featurescript Onshape Document"){:target="_blank"}
    
    ***

    <center markdown>![](../images/featurescripts/origin-cube.webp){width=80%}</center>

    - Used to create an origin reference for assembly mating
    - Optionally import design constants like bolt hole sizes, heat set insert hole sizes, etc
    - Optionally import functions for calculating gear OD, pulley/sprocket pitch & outer diameters, and calculate belt/chain c-c distances
    - See [Assembly Best Practices](../best-practices/assembly-setup.md#the-origin-cube) for more information on usage

    ??? Video "Video Example"
        <video controls="true" allowfullscreen="true">
          <source src="../images/featurescripts/origincube.webm" type="video/webm">
        </video>
        <figcaption><center>Origin Cube's FRC Functions enables belt and chain calculations directly inside of sketches and fully captures design intent by capturing tooth counts.</center></figcaption>

- [**Belt & Chain Gen**](https://cad.onshape.com/documents/53c0b14cad92676c14e04e97/w/1271c254ccb0a79563210195/e/7394c4a86d8d6c35c9a12041 "Belt & Chain Gen Featurescript Onshape Document"){:target="_blank"}

    ***

    <center markdown>![](../images/featurescripts/belt-chain-gen.webp){width=80%}</center>

    - Used in conjunction with Origin Cube FRC Functions to create highly customizable belts and chains
    - Highly parametric - pulley/sprocket tooth count is automatically calculated from sketch pitch diameter.
    - Create multi pulley, double sided belt, and multi sprocket transmissions with options for both toothed and round idlers

    ??? Video "Video Example"
        <video controls="true" allowfullscreen="true">
          <source src="../images/featurescripts/beltchaingen.webm" type="video/webm">
        </video>

- [**Robot Shaft**](https://cad.onshape.com/documents/9cffa92db8b62219498f89af/w/06b332ccabc9d2e0aa0abf88/e/2e6e4b559832eeff8391e933 "Robot Shaft Featurescript Onshape Document"){:target="_blank"} *(Alex's Featurescripts)*

    ***

    <center markdown>![](../images/featurescripts/robot-shaft.webp){width=80%}</center>

    - Generates a shaft, with options for hex, rounded hex (13.75mm OD), MAXSpline, etc.
    - Options for retention type on both ends
    - Can be generated in-place and with offsets

- [**Robot Spacer**](https://cad.onshape.com/documents/9cffa92db8b62219498f89af/w/06b332ccabc9d2e0aa0abf88/e/2e6e4b559832eeff8391e933 "Robot Spacer Featurescript Onshape Document"){:target="_blank"} *(Alex's Featurescripts)*
    
    ***

    <center markdown>![](../images/featurescripts/robot-spacer.webp){width=80%}</center>

    - Generates a spacer, with options for round, 3/8" hex, 1/2" hex, MAXSpline, etc.
    - Can be generated in-place and with offsets


- [**Extrude Individual**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/7f62400703032fab9a7a3320 "Extrude Individual Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

    ***

    <center markdown>![](../images/featurescripts/extrude-individual.webp){width=80%}</center>

    - Can extrude multiple regions as different parts with one feature, even if regions are adjacent
    - Commonly used with tube converter to make punched aluminum tubes from a top view sketch

    ??? Video "Video Example"
        <video controls="true" allowfullscreen="true" poster="../images/featurescripts/EI.webp">
            <source src="../images/featurescripts/extrudeIndividual.mp4" type="video/mp4">
        </video>

- [**Tube Converter**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/7f62400703032fab9a7a3320 "Tube Converter Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

    ***

    <center markdown>![](../images/featurescripts/tube-converter.webp){width=80%}</center>

    - Converts extrusions into punched tube, with customization and presets for hole pattern, wall thickness, and profile.
    - Can be slow - try moving to the end of the part studio

    ??? Video "Video Example"
        <video controls="true" allowfullscreen="true" poster="../images/featurescripts/TC.webp">
            <source src="../images/featurescripts/tubeConverter.mp4" type="video/mp4">
        </video>



- [**Part Lighten**](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d "Part Lighten Featurescript Onshape Document"){:target="_blank"} *(2471 Featurescripts)*

    ***

    <center markdown>![](../images/featurescripts/part-lighten.webp){width=80%}</center>

    - Better control over ribs, cut depth, fillets, etc.
    - Gives a nice estimate of how much weight is being saved

    ??? Video "Video Example"
        <video controls="true" allowfullscreen="true">
        <source src="../images/featurescripts/part-lighten.webm" type="video/mp4">
        </video>

- [**FilletXpert (Fillet All Edges)**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/7f62400703032fab9a7a3320 "Fillet All Edges Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*
    
    ***
    
    <center markdown>![](../images/featurescripts/fillet-all-edges.webp){width=80%}</center>

    - After selecting a face, it adds a fillet to the corners of that face (all edges normal to the selected face)

    ??? Video "Video Example"
        <video controls="true" allowfullscreen="true" poster="../images/featurescripts/FAE.webp">
            <source src="../images/featurescripts/filletEdges.mp4" type="video/mp4">
        </video>

- [**Spur Gear**](https://cad.onshape.com/documents/5742c8cde4b06c68b362d748/w/b493e0cb681bbf9497d9f4b3/e/01a666571e625f8b819fd75b "Spur Gear Featurescript Onshape Document"){:target="_blank"}
    
    ***

    <center markdown>![](../images/featurescripts/spur-gear.webp){width=80%}</center>

    - Generates a spur gear with with many different options
    - Can be useful for 3D-printed parts and custom sector gears

- [**3D Printed Mass**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/7f62400703032fab9a7a3320 "3D Printed Mass Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

    ***

    <center markdown>![](../images/featurescripts/3D-printed.webp){width=80%}</center>

    - Modifies 3D-printed parts to have accurate mass with given material, infill, and wall thickness

    ??? Video "Video Example"
        <video controls="true" allowfullscreen="true" poster="../images/featurescripts/3DP.webp">
            <source src="../images/featurescripts/3DPMass.mp4" type="video/mp4">
        </video>

</div>

## Bundles
The below links contain several featurescripts each that you can add all at once. The more useful featurescripts from each bundle are demonstrated further below.

<div class="grid cards" markdown>

- [**Julia's Featurescripts**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/7f62400703032fab9a7a3320 "Julia's Featurescripts Onshape Document"){:target="_blank"}

- [**Alex's Featurescripts**](https://cad.onshape.com/documents/9cffa92db8b62219498f89af/w/06b332ccabc9d2e0aa0abf88/e/2e6e4b559832eeff8391e933 "Alex's Featurescripts Onshape Document"){:target="_blank"}

- [**Abhi's Features & Configs**](https://cad.onshape.com/documents/96d32fd4fe5341563a402ecd/v/042060f84c30390d82d806f8/e/d7f04278e0325b6d4426ca34?jumpToIndex=2635&showReturnToWorkspaceLink=true "Abhi's Features & Configs Onshape Document"){:target="_blank"}

- [**2471 Featurescripts**](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d "2471 Featurescripts Onshape Document"){:target="_blank"}

- [**TLamp's Featurescripts**](https://cad.onshape.com/documents/f46510f08cc311a34733cac2/v/f7f3a1c996c58466f6b88a37/e/8e9fbf1ac2f0980e4bc34951 "TLamp's Featurescripts Onshape Document"){:target="_blank"}

- [**CADSHARP's Featurescripts**](https://www.cadsharp.com/featurescripts/ "CADSHARP's Featurescripts"){:target="_blank"}

</div>

## Other
Below is a list of other featurescripts that can be useful but are more niche.

### Structure

<div class="grid cards" markdown>

- [**Gusset Generator**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/7f62400703032fab9a7a3320 "Gusset Generator Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

    - Generate a gusset from hole selections
    - **Warning**: Not a very parametric featurescript and causes lag, but can be useful in a pinch

- [**Robot Bearing Hat**](https://cad.onshape.com/documents/9cffa92db8b62219498f89af/w/06b332ccabc9d2e0aa0abf88/e/2e6e4b559832eeff8391e933 "Robot Bearing Hat Featurescript Onshape Document"){:target="_blank"} *(Alex's Featurescripts)*

    - Creates a custom bearing hat given a set of mounting locations and a bearing hole
    - Can create tapped holes

- [**Spacer Generator**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/7f62400703032fab9a7a3320 "Spacer Generator Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

    - Generates a spacer, with options for round, 3/8" hex, and 1/2" hex

    ??? Video "Video Example"
        <video controls="true" allowfullscreen="true" poster="../images/featurescripts/S.webp">
            <source src="../images/featurescripts/spacer.mp4" type="video/mp4">
        </video>

- [**Electronics Mounting**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/7f62400703032fab9a7a3320 "Electronics Mounting Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

    - Generates hole patterns for different electronic components using center points and mate connectors on sketches

- [**MechSketch**](https://cad.onshape.com/documents/f46510f08cc311a34733cac2/v/f7f3a1c996c58466f6b88a37/e/8e9fbf1ac2f0980e4bc34951 "mechSketch Featurescript Onshape Document"){:target="_blank"} *(TLamp's Featurescripts)*

    - Incredibly useful, generates sketch profiles for a variety of things
    - Profiles for COTS parts like Maxspline, TTB inserts, maxtube, motors, and the versa patern
    - Profiles and holes for all electronics
    - Profile generator for pulleys and a spur gears

- [**Robot Spline Profile**](https://cad.onshape.com/documents/9cffa92db8b62219498f89af/w/06b332ccabc9d2e0aa0abf88/e/2e6e4b559832eeff8391e933 "Robot Spline Profile Featurescript Onshape Document"){:target="_blank"} *(Alex's Featurescripts)*

    - Creates an inside or outside profile/extrusion of MAXSpline or SplineXL
    - Has all the standard extrude parameters

</div>

### Power Transmissions

<div class="grid cards" markdown>

- [**Robot Pulley**](https://cad.onshape.com/documents/9cffa92db8b62219498f89af/w/06b332ccabc9d2e0aa0abf88/e/2e6e4b559832eeff8391e933 "Robot Pulley Featurescript Onshape Document"){:target="_blank"} *(Alex's Featurescripts)*

    - Creates a set of pulleys  in the part studio given belt curves or mate connectors

- [**Belt & Pulley Generation**](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d "Belt and Pulley Generation Featurescript Onshape Document"){:target="_blank"} *(2471 Featurescripts)*

    - Configurable belt and pulley generation
    - Belt width, pulley tooth count, offset and fit adjustment, belt type, etc.
    - Options for bore and flanges for both pulleys

- [**Timing Belt Pulley Generator**](https://cad.onshape.com/documents/55ae3138e0cd7c325239208b/v/bfe7a53a6752a35e56338377/e/b08c0071a21e9ab74baaf916 "Featurescript Onshape Document"){:target="_blank"}

    - Generates GT2 pulleys

- [**Sprocket**](https://cad.onshape.com/documents/96d32fd4fe5341563a402ecd/v/042060f84c30390d82d806f8/e/d7f04278e0325b6d4426ca34?jumpToIndex=2635&showReturnToWorkspaceLink=true "Sprocket Featurescript Onshape Document"){:target="_blank"} *(Abhi's Features & Configs)*

    - Generate a sprocket for common types of chain

- [**doesinlinechaintensionerfit**](https://cad.onshape.com/documents/0a4b1991c2c84d83452b66db/w/16955b48319c55202a97d587/e/2c07d47526c2d94d25697091 "doesinlinetensionerfit Featurescipt Onshape Document"){:target="_blank"}

    - Calculates whether or not an inline chain tensioner will fit on a chain transmission
    - For when you are too lazy to do basic math

- [**Thrifty Insert**](https://cad.onshape.com/documents/c54b1ff25af8ec89778cac4f/v/5a909b5ad938a3116448922f/e/c4fc9251685f8516e9022bc6 "Thrify Insert Featurescript Onshape Document"){:target="_blank"}

    - Cuts a profile in a part at a given location and depth to fit a [thriftybot insert](https://www.thethriftybot.com/products/qty-5-aluminum-insert-for-3d-printed-parts){:target="_blank"} into, for 3D-printed parts to stop them from stripping while being driven on an axle.

- [**Polybelt Generator**](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d "Polybelt Generator Featurescript Onshape Document"){:target="_blank"} *(2471 Featurescripts)*

    - Generates polycord and pulleys based off of selected points

</div>

### Pocketing

<div class="grid cards" markdown>

- [**Vent**](https://cad.onshape.com/documents/702f94d6e4ffb0c64f611f87/w/f6ac7d31494b1215bb9c8a61/e/4bf4eb130870ebdf0008c5a4 "Vent Featurescript Onshape Document"){:target="_blank"}

    - Used for pocketing and lightening plates
    - Uses sketch regions to determine pocket and rib placement

    ??? Video "Video Example"
        <video controls="true" allowfullscreen="true" poster="../images/featurescripts/V.webp">
            <source src="../images/featurescripts/vent.mp4" type="video/mp4">
        </video>

- [**Robot Grid**](https://cad.onshape.com/documents/9cffa92db8b62219498f89af/w/06b332ccabc9d2e0aa0abf88/e/2e6e4b559832eeff8391e933 "Robot Grid Featurescript Onshape Document"){:target="_blank"} *(Alex's Featurescripts)*

    - Creates a grid of holes on a part (e.g. a bellypan)

- [**CheeseIt!**](https://cad.onshape.com/documents/f46510f08cc311a34733cac2/v/f7f3a1c996c58466f6b88a37/e/8e9fbf1ac2f0980e4bc34951 "CheeseIt! Featurescript Onshape Document"){:target="_blank"} *(TLamp's Featurescripts)*

    - Advanced lightening pattern generation
    - Isogrid, hexagon, or circle pattern

- [**PatchIt!**](https://cad.onshape.com/documents/f46510f08cc311a34733cac2/v/f7f3a1c996c58466f6b88a37/e/8e9fbf1ac2f0980e4bc34951 "PatchIt! Featurescript Onshape Document"){:target="_blank"} *(TLamp's Featurescripts)*

    - Patches specified pockets in a part

</div>

### Manufacturing

<div class="grid cards" markdown>

- [**Auto Layout**](https://cad.onshape.com/documents/576e01dbe4b0cc2e7f46a55d/v/f697250aa149b6846173f4b1/e/887d6e2324589bfd2058c3e1?jumpToIndex=2346 "Auto Layout Featurescript Onshape Document"){:target="_blank"}

    - Given some derived plates, either transformed from an in-context assembly (to maintain part count) or derived from a part studio, it will automatically lay them out into sheets of a given size, sorted by thickness. This is used to prepare a file to route or waterjet parts out of material with a machine.

- [**Measure Cut List**](https://cad.onshape.com/documents/395304920b30c3b382fd312d/w/86481637ad1e9da01b0e5d60/e/e19230df69a29e1fc2259b9d?renderMode=0&tangentEdgeStyle=2&uiState=6642611f3aed1a692ef01f41 "Measure Cut List Featurescript Onshape Document"){:target="_blank"}

    - Creates a table of measurements
    - Great for creating cut lists for parts

- [**Laser Joint**](https://cad.onshape.com/documents/578830e4e4b0e65410f9c34e/v/8916b9beca0f64d7dd945ce5/e/dfd5effddfd7f2ecce4b0246 "Laser Joint Featurescript Onshape Document"){:target="_blank"}

    - Highly configurable featurescript that generates tab joints between overlapping parts
    - Options to make it easier for cnc routers to cut parts
    - Can use for bumper wood corners

- [**Dogbone and Corner Overcut**](https://cad.onshape.com/documents/51695bc13e3d9fb286023c70/v/adff35c9e1ef83771d6dc29c/e/3a9512753b299d5fefc39f46 "Dog Bone Featurescript Onshape Document"){:target="_blank"}

    - Features to make it easier for cnc routers to cut cavities in parts

</div>

### Onshape Functionality Extensions

<div class="grid cards" markdown>

- [**Advanced Variables**](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d "Advanced Variables Featurescript Onshape Document"){:target="_blank"} *(2471 Featurescripts)*

    - Can create a compound variable with path length, angle between edges, distance between planes, angle between planes, distance between points, pulley center distance, and chain center distance
    - Very useful for complex belt and chain runs
    - Include measurements that Onshape can't normally do

- [**Part Color**](https://cad.onshape.com/documents/d997b0ffc30f659113b10c00/v/a9e4f209775174dbb9f2b5fa/e/b6db0c9545b9a2df1d7ea546 "Part Color Featurescript Onshape Document"){:target="_blank"}

    - Give color to faces on a part retroactively
    - Can use a variety of different color inputs
    - Can be used for part color configurations

- [**Set Materials**](https://cad.onshape.com/documents/96d32fd4fe5341563a402ecd/v/042060f84c30390d82d806f8/e/d7f04278e0325b6d4426ca34?jumpToIndex=2635&showReturnToWorkspaceLink=true "Set Materials Featurescript Onshape Document"){:target="_blank"} *(Abhi's Features & Configs)*

     - Parametrically set materials and appearances of parts in batches

- [**Set Properties**](https://cad.onshape.com/documents/96d32fd4fe5341563a402ecd/v/042060f84c30390d82d806f8/e/d7f04278e0325b6d4426ca34?jumpToIndex=2635&showReturnToWorkspaceLink=true "Set Properties Featurescript Onshape Document"){:target="_blank"} *(Abhi's Features & Configs)*

    - Sets properties of parts in batches

- [**2471's Part Numbering**](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d "2471 Part Number Featurescript Onshape Document"){:target="_blank"} *(2471 Featurescripts)*

    - Numbers parts based off of a given standard

- [**Abhi's Part Numbering**](https://cad.onshape.com/documents/443e443bb2a37736743bf314/w/6539c7379d36307a6a2cc01d/e/ef4e1b0c40e1dbf2ee36d02e "Ahbi's Part Numbering Featurescript Onshape Document"){:target="_blank"}

    - Used for quickly applying a system to number parts

</div>

<br>
