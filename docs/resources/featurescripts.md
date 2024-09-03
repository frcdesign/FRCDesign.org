# Featurescripts

Onshape has its own scripting language to create custom features to automate aspects of design called [Featurescript](https://www.onshape.com/features/custom-features "Onshape Featurescript Page"){:target="_blank"}. There are a lot of featurescripts (what we call the custom features) that make designing for FRC much easier.

### How To Install Featurescripts

1. Open any Onshape document and go inside of a part studio
2. Click the rightmost button on the toolbar <img align="center" src="../../../../img/resources/featurescripts/addCustomFeatures.webp">
    - **Note:** If you have previously added any Featurescripts one of those may show up as the right most icon. In that case click the dropdown to show the add button.
3. Paste the link of the document with the featurescript(s) in it into the search bar
    - **Note:** Some of the below featurescripts exist in the same document, so you can add multiple from the same link.

4. Select the featurescript(s) you want to add to your profile, then exit the box. They will be accessible in all documents from then on in the same drop-down in the toolbar where you added the feature.

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true" poster="../../../../img/resources/featurescripts/addingFeaturescriptsTutorial.webp">
      <source src="../../../../img/resources/featurescripts/addingFeaturescriptsTutorial.webm" type="video/webm">
    </video>

!!! Note "Adding Featurescripts while in a Featurescript Document"
    When viewing a tab in a document that uses custom features, you can click a button near the top left that says 'custom features'. From here you can add custom features used in the document to your profile.

### Troubleshooting and Updating Featurescripts 

If a featurescript is not working as expected, the current version might be broken. You might have to update the featurescript. If it needs updating, the feature will show a blue icon to the right of it that, when hovered over, will say "change version of linked document."

1. The first way to update it is by individually by right clicking the feature you want updated in the feature list and clicking "Update linked document..."
2. The second, and slightly more permanent way (until the maintainer of the custom feature creates a new version), is by right clicking any of the featurescript icons in your toolbar or in the custom features dropdown and clicking "Update..." or "Update all..." From there, you can see the current versions of the custom features you have added to your profile and update selected ones to use the current latest version when you use a featurescript.

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true" poster="../../../../img/resources/featurescripts/updatingFeaturescriptDocuments.webp">
      <source src="../../../../img/resources/featurescripts/updatingFeaturescriptDocuments.webm" type="video/webm">
    </video>

## List of Featurescripts

!!! tip
    The title of each featurescript or group of featurescripts links to its respective document. Right click the title and click "copy link address" for installing it to your profile using the above process.

### **Highly Recommended**
These featurescripts are must haves to enhance your Onshape workflow. Many of these are developed by members of the FRC community and well maintained.

[**Origin Cube Featurescript**](https://cad.onshape.com/documents/321c197a842fc5f1a29e6621/w/fc3cdd5ca7edcd93e02f13cc/e/df3afdbec8d1356c2af15e4b?renderMode=0&uiState=6637caa6ccbcaa36badca03a "Origin Cube Featurescript Onshape Document"){:target="_blank"}

- Used to create an origin reference for assembly mating
- Optionally import design constants like bolt hole sizes, heat set insert hole sizes, etc
- Optionally import functions for calculating gear OD, pulley/sprocket pitch & outer diameters, and calculate belt/chain c-c distances
- See [Assembly Best Practices](../best-practices/assembly-setup.md#the-origin-cube) for more information on usage

??? Video "Video Example"
    <video controls="true" allowfullscreen="true">
      <source src="/img/resources/featurescripts/origincube.webm" type="video/webm">
    </video>
    <figcaption><center>Origin Cube's FRC Functions enables belt and chain calculations directly inside of sketches and fully captures design intent by capturing tooth counts.</center></figcaption>

[**Belt & Chain Gen**](https://cad.onshape.com/documents/53c0b14cad92676c14e04e97/w/1271c254ccb0a79563210195/e/7394c4a86d8d6c35c9a12041 "Belt & Chain Gen Featurescript Onshape Document"){:target="_blank"}

- Used in conjunction with Origin Cube FRC Functions to create highly customizable belts and chains
- Highly parametric - pulley/sprocket tooth count is automatically calculated from sketch pitch diameter.
- Create multi pulley, double sided belt, and multi sprocket transmissions with options for both toothed and round idlers
- Calculates belt and chain pitch; when used in conjunction with `Final` can allow for easy adjustment of path lengths
- Block model and high detail belt and chain model options available
- Allows for arbitrary placement of belts with a mate connector reference

??? Video "Video Example"
    <video controls="true" allowfullscreen="true">
      <source src="/img/resources/featurescripts/beltchaingen.webm" type="video/webm">
    </video>

[**Extrude Individual**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Extrude Individual Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

- Can extrude multiple regions as different parts with one feature, even if regions are adjacent
- Commonly used with tube converter to make punched aluminum tubes from a top view sketch

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true" poster="../../../../img/resources/featurescripts/EI.webp">
      <source src="../../../../img/resources/featurescripts/extrudeIndividual.mp4" type="video/mp4">
    </video>

[**Tube Converter**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Tube Converter Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

- Converts extrusions into punched tube, with customization and presets for hole pattern, wall thickness, and profile.

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true" poster="../../../../img/resources/featurescripts/TC.webp">
      <source src="../../../../img/resources/featurescripts/tubeConverter.mp4" type="video/mp4">
    </video>

[**Shaft Generator**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Shaft Generator Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

- Generates a shaft, with options for hex, rounded hex (13.75mm OD), MAXSpline, etc.
- Options for retention type on both ends
- Can be generated in-place and with offsets

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true" poster="../../../../img/resources/featurescripts/SG.webp">
      <source src="../../../../img/resources/featurescripts/shaftGenerator.mp4" type="video/mp4">
    </video>

[**Spacer Generator**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Spacer Generator Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

- Generates a spacer, with options for round, 3/8" hex, and 1/2" hex

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true" poster="../../../../img/resources/featurescripts/S.webp">
      <source src="../../../../img/resources/featurescripts/spacer.mp4" type="video/mp4">
    </video>

[**Part Lighten**](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d "Part Lighten Featurescript Onshape Document"){:target="_blank"} *(2471 Featurescripts)*

  - Better than "Lighten" and more complex than "Vent"
  - Better control over ribs, cut depth, fillets, etc.
  - Gives a nice estimate of how much weight is being saved

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true">
      <source src="/img/learning-course/stage1b/exercises/e2/e2s8.webm" type="video/mp4">
    </video>

[**FilletXpert (Fillet All Edges)**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Fillet All Edges Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

- After selecting a face, it adds a fillet to the corners of that face (all edges normal to the selected face)

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true" poster="../../../../img/resources/featurescripts/FAE.webp">
      <source src="../../../../img/resources/featurescripts/filletEdges.mp4" type="video/mp4">
    </video>


### Bundles
The below links contain several featurescripts each that you can add all at once. The more useful featurescripts from each bundle are demonstrated further below.

[**Julia's Featurescripts**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Julia's Featurescripts Onshape Document"){:target="_blank"}

[**Alex's Featurescripts**](https://cad.onshape.com/documents/9cffa92db8b62219498f89af/v/d1389fa34235160533671706/e/99672d1e329b38e647d90146 "Alex's Featurescripts Onshape Document"){:target="_blank"}

[**Abhi's Features & Configs**](https://cad.onshape.com/documents/96d32fd4fe5341563a402ecd/v/042060f84c30390d82d806f8/e/d7f04278e0325b6d4426ca34?jumpToIndex=2635&showReturnToWorkspaceLink=true "Abhi's Features & Configs Onshape Document"){:target="_blank"}

[**2471 Featurescripts**](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d "2471 Featurescripts Onshape Document"){:target="_blank"}

[**TLamp's Featurescripts**](https://cad.onshape.com/documents/f46510f08cc311a34733cac2/v/f7f3a1c996c58466f6b88a37/e/8e9fbf1ac2f0980e4bc34951 "TLamp's Featurescripts Onshape Document"){:target="_blank"}

[**CADSHARP's Featurescripts**](https://www.cadsharp.com/featurescripts/ "CADSHARP's Featurescripts"){:target="_blank"}

### Structure

[**Extrude Individual**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Extrude Individual Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

- Can extrude multiple regions as different parts with one feature, even if regions are adjacent
- Commonly used with tube converter to make punched aluminum tubes from a top view sketch

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true" poster="../../../../img/resources/featurescripts/EI.webp">
      <source src="../../../../img/resources/featurescripts/extrudeIndividual.mp4" type="video/mp4">
    </video>

[**Tube Converter**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Tube Converter Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

- Converts extrusions into punched tube, with customization and presets for hole pattern, wall thickness, and profile.

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true" poster="../../../../img/resources/featurescripts/TC.webp">
      <source src="../../../../img/resources/featurescripts/tubeConverter.mp4" type="video/mp4">
    </video>


[**Gusset Generator**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Gusset Generator Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

- Generate a gusset from hole selections
- **Warning**: Not a very parametric featurescript and causes lag, but can be useful in a pinch


[**Shaft Generator**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Shaft Generator Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

- Generates a shaft, with options for hex, rounded hex (13.75mm OD), MAXSpline, etc.
- Options for retention type on both ends
- Can be generated in-place and with offsets

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true" poster="../../../../img/resources/featurescripts/SG.webp">
      <source src="../../../../img/resources/featurescripts/shaftGenerator.mp4" type="video/mp4">
    </video>


[**Spacer Generator**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Spacer Generator Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

- Generates a spacer, with options for round, 3/8" hex, and 1/2" hex

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true" poster="../../../../img/resources/featurescripts/S.webp">
      <source src="../../../../img/resources/featurescripts/spacer.mp4" type="video/mp4">
    </video>
  
[**FilletXpert (Fillet All Edges)**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Fillet All Edges Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

- After selecting a face, it adds a fillet to the corners of that face (all edges normal to the selected face)

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true" poster="../../../../img/resources/featurescripts/FAE.webp">
      <source src="../../../../img/resources/featurescripts/filletEdges.mp4" type="video/mp4">
    </video>


[**Robot Spacer**](https://cad.onshape.com/documents/9cffa92db8b62219498f89af/v/d1389fa34235160533671706/e/99672d1e329b38e647d90146 "Robot Spacer Featurescript Onshape Document"){:target="_blank"} *(Alex's Featurescripts)*

  - A more complex alternative to Julia's spacer generator, if you need more config options

<!-- [**In-Place Bearings**](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d "In-P){:target="_blank"} *(2471 Featurescripts)*

  - Place different types of bearings in place in a part studio -->

[**Electronics Mounting**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "Electronics Mounting Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescri pts)*

  - Generates hole patterns for different electronic components using center points and mate connectors on sketches

[**MechSketch**](https://cad.onshape.com/documents/f46510f08cc311a34733cac2/v/f7f3a1c996c58466f6b88a37/e/8e9fbf1ac2f0980e4bc34951 "mechSketch Featurescript Onshape Document"){:target="_blank"} *(TLamp's Featurescripts)*

  - Incredibly useful, generates sketch profiles for a variety of things
  - Profiles for COTS parts like Maxspline, TTB inserts, maxtube, motors, and the versa patern
  - Profiles and holes for all electronics
  - Profile generator for pulleys and a spur gears


### Power Transmissions

<!-- [**Belt Gen**](https://cad.onshape.com/documents/b273b67c06b86b78b01b6f3a/v/56fb8fa8d7d90b925d8d9775/e/2fd838311a32255a728a8449?showReturnToWorkspaceLink=true "Belt Gen Featurescript Onshape Document"){:target="_blank"}

- Generates a belt path from belt pitch diameter circles
- Allows for multiple pulleys, tensioners, and double sided belts
- Options for simplified or realistic models
- Calculates resulting belt length

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true">
      <source src="../../../../img/resources/featurescripts/beltGen.mp4" type="video/mp4">
    </video> -->

<!-- [**Chain Gen**](https://cad.onshape.com/documents/b273b67c06b86b78b01b6f3a/w/f8670c98f827edfb8e96e7e9/e/9076725852f28d52fd6e796f "Chain Gen Featurescript Onshape Document"){:target="_blank"}

- Generates a chain path from sprocket pitch diameter circles
- Allows for multiple sprockets and tensioners
- Options for simplified or realistic models
- Calculates resulting chain length

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true">
      <source src="../../../../img/resources/featurescripts/chainGen.mp4" type="video/mp4">
    </video> -->

[**Belt & Chain Gen**](https://cad.onshape.com/documents/53c0b14cad92676c14e04e97/w/1271c254ccb0a79563210195/e/7394c4a86d8d6c35c9a12041 "Belt & Chain Gen Featurescript Onshape Document"){:target="_blank"}

- Used in conjunction with Origin Cube FRC Functions to create highly customizable belts and chains
- Highly parametric - pulley/sprocket tooth count is automatically calculated from sketch pitch diameter.
- Create multi pulley, double sided belt, and multi sprocket transmissions with options for both toothed and round idlers
- Calculates belt and chain pitch; when used in conjunction with `Final` can allow for easy adjustment of path lengths
- Block model and high detail belt and chain model options available
- Allows for arbitrary placement of belts with a mate connector reference

??? Video "Video Example"
    <video controls="true" allowfullscreen="true">
      <source src="/img/resources/featurescripts/beltchaingen.webm" type="video/webm">
    </video>

[**Belt & Pulley Generation**](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d "Belt and Pulley Generation Featurescript Onshape Document"){:target="_blank"} *(2471 Featurescripts)*

  - Configurable belt and pulley generation
  - Belt width, pulley tooth count, offset and fit adjustment, belt type, etc.
  - Options for bore and flanges for both pulleys

[**Timing Belt Pulley Generator**](https://cad.onshape.com/documents/55ae3138e0cd7c325239208b/v/bfe7a53a6752a35e56338377/e/b08c0071a21e9ab74baaf916 "Featurescript Onshape Document"){:target="_blank"}

- Generates GT2 pulleys

[**Sprocket**](https://cad.onshape.com/documents/96d32fd4fe5341563a402ecd/v/042060f84c30390d82d806f8/e/d7f04278e0325b6d4426ca34?jumpToIndex=2635&showReturnToWorkspaceLink=true "Sprocket Featurescript Onshape Document"){:target="_blank"} *(Abhi's Features & Configs)*

  - Generate a sprocket for common types of chain

[**Spur Gear**](https://cad.onshape.com/documents/9cffa92db8b62219498f89af/v/d1389fa34235160533671706/e/99672d1e329b38e647d90146 "Spur Gear Featurescript Onshape Document"){:target="_blank"} *(Alex's Featurescripts)*

  - Generates a spur gear with with many different options
  - Can be useful for 3D-printed parts.

[**Thrifty Insert**](https://cad.onshape.com/documents/c54b1ff25af8ec89778cac4f/v/5a909b5ad938a3116448922f/e/c4fc9251685f8516e9022bc6 "Thrify Insert Featurescript Onshape Document"){:target="_blank"}

- Cuts a profile in a part at a given location and depth to fit a [thriftybot insert](https://www.thethriftybot.com/products/qty-5-aluminum-insert-for-3d-printed-parts){:target="_blank"} into, for 3D-printed parts to stop them from stripping while being driven on an axle.

[**Polybelt Generator**](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d "Polybelt Generator Featurescript Onshape Document"){:target="_blank"} *(2471 Featurescripts)*

  - Generates polycord and pulleys based off of selected points


### Pocketing

[**Part Lighten**](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d "Part Lighten Featurescript Onshape Document"){:target="_blank"} *(2471 Featurescripts)*

  - Better than "Lighten" and more complex than "Vent"
  - Better control over ribs, cut depth, fillets, etc.
  - Gives a nice estimate of how much weight is being saved

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true">
      <source src="/img/learning-course/stage1b/exercises/e2/e2s8.webm" type="video/mp4">
    </video>

[**Vent**](https://cad.onshape.com/documents/702f94d6e4ffb0c64f611f87/w/f6ac7d31494b1215bb9c8a61/e/4bf4eb130870ebdf0008c5a4 "Vent Featurescript Onshape Document"){:target="_blank"}

- Used for pocketing and lightening plates
- Uses sketch regions to determine pocket and rib placement

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true" poster="../../../../img/resources/featurescripts/V.webp">
      <source src="../../../../img/resources/featurescripts/vent.mp4" type="video/mp4">
    </video>

[**Lighten**](https://cad.onshape.com/documents/573f7d70e4b0fddafb52148c/v/0edea0fa2707e715d040e74f/e/5eccf6d369b0312a728d77d3 "Lighten Featurescript Onshape Document"){:target="_blank"}

  - Less optimized and breaks more then vent.

[**CheeseIt!**](https://cad.onshape.com/documents/f46510f08cc311a34733cac2/v/f7f3a1c996c58466f6b88a37/e/8e9fbf1ac2f0980e4bc34951 "CheeseIt1 Featurescript Onshape Document"){:target="_blank"} *(TLamp's Featurescripts)*

  - Advanced lightening pattern generation
  - Isogrid, hexagon, or circle pattern

[**PatchIt!**](https://cad.onshape.com/documents/f46510f08cc311a34733cac2/v/f7f3a1c996c58466f6b88a37/e/8e9fbf1ac2f0980e4bc34951 "PatchIt! Featurescript Onshape Document"){:target="_blank"} *(TLamp's Featurescripts)*

- Patches specified pockets in a part


### Manufacturing

[**Auto Layout**](https://cad.onshape.com/documents/576e01dbe4b0cc2e7f46a55d/v/f697250aa149b6846173f4b1/e/887d6e2324589bfd2058c3e1?jumpToIndex=2346 "Auto Layout Featurescript Onshape Document"){:target="_blank"}

- Given some derived plates, either transformed from an in-context assembly (to maintain part count) or derived from a part studio, it will automatically lay them out into sheets of a given size, sorted by thickness. This is used to prepare a file to route or waterjet parts out of material with a machine.

[**Measure Cut List**](https://cad.onshape.com/documents/395304920b30c3b382fd312d/w/86481637ad1e9da01b0e5d60/e/e19230df69a29e1fc2259b9d?renderMode=0&tangentEdgeStyle=2&uiState=6642611f3aed1a692ef01f41 "Measure Cut List Featurescript Onshape Document"){:target="_blank"}

- Creates a table of measurements
- Great for creating cut lists for parts

[**Laser Joint**](https://cad.onshape.com/documents/578830e4e4b0e65410f9c34e/v/8916b9beca0f64d7dd945ce5/e/dfd5effddfd7f2ecce4b0246 "Laser Joint Featurescript Onshape Document"){:target="_blank"}

- Highly configurable featurescript that generates tab joints between overlapping parts
- Options to make it easier for cnc routers to cut parts
- Can use for bumper wood corners

[**Dogbone and Corner Overcut**](https://cad.onshape.com/documents/51695bc13e3d9fb286023c70/v/adff35c9e1ef83771d6dc29c/e/3a9512753b299d5fefc39f46 "Dog Bone Featurescript Onshape Document"){:target="_blank"}

- Features to make it easier for cnc routers to cut cavities in parts

### Onshape Functionality Extensions

[**Origin Cube Featurescript**](https://cad.onshape.com/documents/321c197a842fc5f1a29e6621/w/fc3cdd5ca7edcd93e02f13cc/e/df3afdbec8d1356c2af15e4b?renderMode=0&uiState=6637caa6ccbcaa36badca03a "Origin Cube Featurescript Onshape Document"){:target="_blank"}

- Used to create an origin reference for assembly mating
- Optionally import design constants like bolt hole sizes, heat set insert hole sizes, etc
- Optionally import functions for calculating gear OD, pulley/sprocket pitch & outer diameters, and calculate belt/chain c-c distances
- See [Assembly Best Practices](../best-practices/assembly-setup.md#the-origin-cube) for more information on usage

??? Video "Video Example"
    <video controls="true" allowfullscreen="true">
      <source src="/img/learning-course/stage1b/belt/beltCad2.webm" type="video/webm">
    </video>


[**Measure Value**](https://cad.onshape.com/documents/77baa8153589a7fc5f289829/w/cffd0f2a7077380d5378a885/e/d3174bf5315e6aafcb889367?renderMode=0&uiState=652ee7d25129162fc0afad5f "Measure Value Featurescript Onshape Document"){:target="_blank"}

- An extremely useful featurescript
- Creates variables from measured values
- Useful for creating parametric patterns, including hole patterns

[**Assembly Mirror**](https://cad.onshape.com/documents/0f7d68295ff4dab57adcf92c/v/88fbfa19a2e2555d18599db4/e/bcf3052f00f1f9d3d95a89c7?jumpToIndex=1392 "Assembly Mirror Featurescript Onshape Document"){:target="_blank"}

- Adds reflected mate connectors to a part so you can easily mate it reflected across a plane in an assembly (does not mirror geometry).

[**Part Color**](https://cad.onshape.com/documents/d997b0ffc30f659113b10c00/v/a9e4f209775174dbb9f2b5fa/e/b6db0c9545b9a2df1d7ea546 "Part Color Featurescript Onshape Document"){:target="_blank"}

- Give color to faces on a part retroactively
- Can use a variety of different color inputs
- Can be used for part color configurations

[**Set Materials**](https://cad.onshape.com/documents/96d32fd4fe5341563a402ecd/v/042060f84c30390d82d806f8/e/d7f04278e0325b6d4426ca34?jumpToIndex=2635&showReturnToWorkspaceLink=true "Set Materials Featurescript Onshape Document"){:target="_blank"} *(Abhi's Features & Configs)*

  - Parametrically set materials and appearances of parts in batches

[**Set Properties**](https://cad.onshape.com/documents/96d32fd4fe5341563a402ecd/v/042060f84c30390d82d806f8/e/d7f04278e0325b6d4426ca34?jumpToIndex=2635&showReturnToWorkspaceLink=true "Set Properties Featurescript Onshape Document"){:target="_blank"} *(Abhi's Features & Configs)*

  - Sets properties of parts in batches

[**2471's Part Numbering**](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d "2471 Part Number Featurescript Onshape Document"){:target="_blank"} *(2471 Featurescripts)*

  - Numbers parts based off of a given standard

[**Abhi's Part Numbering**](https://cad.onshape.com/documents/443e443bb2a37736743bf314/w/6539c7379d36307a6a2cc01d/e/ef4e1b0c40e1dbf2ee36d02e "Ahbi's Part Numbering Featurescript Onshape Document"){:target="_blank"}

- Used for quickly applying a system to number parts

[**3D Printed Mass**](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8 "3D Printed Mass Featurescript Onshape Document"){:target="_blank"} *(Julia's Featurescripts)*

- Modifies 3D-printed parts to have accurate mass with given material, infill, and wall thickness

??? Video "Video Tutorial"
    <video controls="true" allowfullscreen="true" poster="../../../../img/resources/featurescripts/3DP.webp">
      <source src="../../../../img/resources/featurescripts/3DPMass.mp4" type="video/mp4">
    </video>

[**Advanced Variables**](https://cad.onshape.com/documents/028ca8fb10baf53e1f6fce96/v/821c8b51ed0953526b51926e/e/a8b9e45297aac9f5688c871d "Advanced Variables Featurescript Onshape Document"){:target="_blank"} *(2471 Featurescripts)*

  - Can create a compound variable with path length, angle between edges, distance between planes, angle between planes, distance between points, pulley center distance, and chain center distance
  - Very useful for complex belt and chain runs
  - Include measurements that Onshape can't normally do

<br>