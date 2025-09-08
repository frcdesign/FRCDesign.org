# Intro to 3D Printing

An overview of 3D printing and its use cases in FRC robots.

## The Power of 3D Printing for FRC

1. **Enabling rapid iteration and prototyping of robot components.**   
    3D printing allows quick production of physical prototypes. You can test them, find flaws, and rapidly improve designs. This speeds up the design cycle, which is critical for FRC.

2. **Facilitating the creation of custom, specialized parts for unique challenges.**   
   FRC Robots often need unique 3D geometries. 3D printing enables geometry not often possible with other fabrication methods.

3. **Offering a pathway to lightweight yet strong designs.**  
   3D printing enables creating complex internal structures called “infill” inside the part that reduce overall material usage and weight. This can be done while maintaining or increasing strength where needed, enabling lighter mechanism designs.

4. **Providing a cost-effective manufacturing solution for custom parts.**  
   3D printing can be a cost-effective way to make custom parts. You can get 1 kg / 2.2 lbs of basic printing material (filament) for under $20 USD.

## Core Concepts of 3D Printing

### What is 3D Printing?

Subtractive manufacturing (for example CNC milling) removes material from an initial form to reveal the final part. 3D printing, or additive manufacturing, builds objects layer by layer.

   <figure>
    <img src="/img/design-handbook/design-for-3d-printing/3dp-process.png" style="width:60%">
    <figcaption>3D printing process </figcaption>
  </figure>

### Overview of the 3D Printing Workflow

1. **Export From Design (CAD)** Once your design is created you need to process it through 3D printing software, so you’ll need to export it from your CAD software.  

2. **Slicing** Slicing software "slices" the model into horizontal layers. It then creates G-code: instructions telling the printer how to print each layer, including nozzle movements, temperatures, and speeds. This is where you configure things like part infill, material, supports etc.  
3. **Printing** The G-code is loaded onto the 3D printer and it precisely deposits material layer by layer, building the object from the bottom until complete.  
4. **Post-Processing** After printing, some parts may need further work. Post processing can include removing support structures, sanding, painting, or assembling multiple printed components. 	

## Types of 3D Printers

Many 3D printing technologies exist, but Fused Deposition Modeling (FDM) is most common and accessible. Common FDM printers are made by companies like Prusa, Bambu Lab, Creality, Stratasys, and Markforged.

   <figure>
    <img src="/img/design-handbook/design-for-3d-printing/3dp-bambu-a1.png" style="width:60%">
    <figcaption>Bambu A1 <a href="http://Bambulab.com" target="_blank">Bambulab.com </a></figcaption>
  </figure>

### Fused Deposition Modeling (FDM)

FDM printers feed filament into the extruder, melt it, and push it through a heated nozzle. The molten plastic is deposited onto the build plate in thin lines, forming the first layer. The print head moves up, and the next layer adheres as it cools. This repeats until the object is built.

1. **Advantages (Affordability, Material Variety, Ease of Use)** FDM printers are generally affordable, great for education. They print with many thermoplastics, and are relatively simple to operate.  
2.  **Disadvantages (Layer Lines, Anisotropy)** FDM prints often show visible layer lines. Parts can be anisotropic, meaning strength varies based on force being applied in different directions. FDM parts are usually strongest along X and Y axes, and are weaker along the printer Z axis (normal to the print bed).

### Other Printer Types

1. **Stereolithography (SLA):** Uses a UV laser to cure liquid resin layer by layer. Known for high detail and smooth surfaces, but depending on the resin, parts can be brittle.   
2. **Digital Light Processing (DLP):** Similar to SLA, but uses a projector to cure whole resin layers at once, for faster prints. Typically a more expensive technology.  
3. **Selective Laser Sintering (SLS):** Uses a laser to fuse powdered material (like nylon) layer by layer. Produces strong, functional parts without supports.

### Slicing Software

Slicing software connects your 3D model to your 3D printer. It translates your design into printer instructions.

1. **What is a Slicer?** A slicer takes a 3D model (STL or OBJ) and converts it into thin layers. For each layer, it determines tool paths, extrusion, temperatures, and speeds. It generates G-code, a language that directs the printer's actions.  
2. **Popular Slicers** Some printers require specific slicers, but others are compatible with a range of slicers. Common slicers are Bambu Studio, Prusa Slicer, Orca Slicer and Cura.   
3. **Slicer Setup** There are many intricacies to slicing 3D models that are not covered in this guide. See the appendix for resources to learn more about slicing.  
4. **Previewing the Slice** Most slicers have a preview mode. This shows exactly how the printer builds your part, layer by layer. This is a vital tool to spot issues (like unsupported overhangs or thin walls) before printing, saving time and material.  
5. **File Formats to Import (STL, STEP)**  
    1. **STL (Stereolithography):** Represents a 3D model as connected triangles, a “mesh” format. Good for very intricate models such as sculptures, characters, freeform designs, and works with nearly every slicer. However, it does **not** contain unit information, so you must be careful about exporting and importing that the units match. When exported at low quality there will be tessellation artifacts that can affect the accuracy of things like holes or critical dimensions.  
    2. **STEP :** Another popular format that can store color and texture, less common for basic FDM printing than STL. Works by feature data instead of thousands of tiny triangles. Contains unit data so there is no conversion required in the slicer. 

### Materials (Filaments for FDM)

The type of filament significantly affects your 3D printed part's properties. See the appendix for a table of different filament properties. If you are new to 3D printing PLA will be the easiest to get started with and PETG is a great next step for a better balance of strength and durability as reasonable cost.

1. **Common Materials**   
    1. **PLA (Polylactic Acid):** Easy to print, good for prototyping, low heat resistance.   
    2. **PETG (Polyethylene Terephthalate Glycol):** Strong, durable, good for functional parts.   
    3. **ABS (Acrylonitrile Butadiene Styrene):** Strong, heat-resistant, but more challenging to print.  
2. **Advanced Materials**  
   These are more difficult to print and are best reserved for when you really need them:  
    1. **TPU (Flexible):** Makes flexible, rubber-like parts. Buying different durometer material or changing the part thickness/infill changes how flexible the part is.  
    2. **Nylon PA-6 (Polyamide):** Engineering grade material. Good for strength and durability. Relatively easy to print with higher end printers.  
    3. **Carbon Fiber Reinforced Filaments:** Many of the materials above can have carbon fiber pieces added to the filament. This offers increased stiffness and strength, often at higher cost. 
    !!! Warning 
        Chopped fiber filaments can be hazardous to sand, drill, or handle as it can release microscopic carbon rods into the air or skin.

    4. **Continuous Carbon Fiber:** Some 3D printers such as certain offerings from Markforged can print with embedded continuous carbon fiber strands. This can offer part strength that matches or even exceeds that of aluminum.  
    5. **Polycarbonate (PC):** Extremely strong, impact-resistant, and high heat tolerance.  
    6. **More Niche Filaments:** PPS, PPA, ASA, Tullomer, PEEK, Ultem \- These filaments have some really unique properties that can be beneficial for different use cases.  
3. **Material Storage and Handling** Filaments absorb moisture from the air (hygroscopic). This can cause print issues like stringing, bubbling, and even weaker parts. Store filaments dry, in sealed containers, ideally with desiccant. Read the filament vendor’s instructions on drying filament.  
   

**Resources**

1. What to buy:
      1. One of the more popular printer brands among FRC teams is Bambu Lab <a href="http://Bambulab.com" target="_blank">(Bambulab.com) </a>. Their printers are very well tuned from the factory and several of their printers are capable of printing with advanced filaments like carbon fiber reinforced nylon, polycarbonate, TPU, etc.
      2. Other brands of printers are Prusa, Markforged, Creality, Elegoo, Snapmaker, Anycubic, Ultimaker, Stratasys, Lulzbot and others. It can be somewhat daunting to pick a good 3D printer, but 3D printing has an extensive online community with many guides and review videos to help you make a good decision.
2. <a href="https://all3dp.com/2/3d-printing-for-beginners-all-you-need-to-know-to-get-started/" target="_blank">ALL3DP Guide to Beginning 3D Printing </a> []()  
3. <a href="https://bambulab.com/en-us/support/academy/3" target="_blank">Bambu Studio Guide </a>


