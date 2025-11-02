# 1C: Practice Mechanisms

## Exercise 8: Indexer Centering

In this exercise, you will be modeling a centering indexer for 9.5" diameter balls, similar to [1678's 2022 indexer](https://www.youtube.com/watch?v=RiUaItTKomUhttps://www.youtube.com/watch?v=RiUaItTKomU "1678 2022 Robot Reveal Video"){:target="\_blank"}. This mechanism features belts, chain, gear, and tube crush blocks. Be sure to pay attention to the plate sketches when modeling.

### Crush Blocks

3D-printed crush blocks can be used to reinforce thin-walled tubing in assemblies where bolts pass through without a plate.
Since the strength of bolts comes from their clamping force, without anything to support the thin walls, the tube can collapse before achieving proper clamping force.
Crush blocks distribute the load, allowing for full clamping force while maintaining the tube’s structural integrity.

Alternatively, a "crush plate" can also be utilized to distribute the fastener force to achieve a similar effect as a crush block.

In this exercise, you will use a [configurable 3D printed crush block](https://cad.onshape.com/documents/e9e11d824a8fd8257028a1dc/v/0c7982f1d3823153c353cbdb/e/b6f099050d1db039691ace49 "Configurable Crush Block Onshape Document"){:target="\_blank"}.

???+ example "Crush Blocks and Crush Plates"
    <figure>
    <img src="../images/indexer-centering/crush-block-plate.webp" width="65%">
    <figcaption>A 3D printed crush block (left) and crush plate (right). Crush plates tend to work well for the middle of the tubes where it may be difficult to insert a crush block.</figcaption>
    </figure>

### Part Studio Instructions

**Navigate to the "Exercise #8 Part Studio" tab** in your copied document and **refer to the solution document** to complete the part studio for this exercise. The **following instruction slides** only provide a general outline and some key details.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
  <img src="../images/indexer-centering/slides/part-studio/s0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
  <img src="../images/indexer-centering/slides/part-studio/s1.webp" style="width:100%">
      <figcaption>1. Begin by creating the layout sketch on the top plane.
                  Just like with the previous exercise, we define the distance between the rollers by mirroring the indexer wheel.
      </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
  <img src="../images/indexer-centering/slides/part-studio/s2.webp" style="width:100%">
      <figcaption>2. Model the thin-wall 2x1 tubes with Extrude Individual and Tube Converter.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
  <img src="../images/indexer-centering/slides/part-studio/s3.webp" style="width:100%">
      <figcaption>3. Model the top plates and bottom plates. 
                  The top plates can be modeled in the same sketch since they are on the same plane.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
  <img src="../images/indexer-centering/slides/part-studio/s4.webp" style="width:100%">
      <figcaption>4. Model a basic crush block that extends into the tube far enough for the first row of holes. Make sure to add the side holes for the bolts to pass through. Chamfer the edges to make it easier to install during irl assembly.</figcaption>
    </figure>
  </div>
  
  <div class="mySlides fade">
    <figure>
  <img src="../images/indexer-centering/slides/part-studio/s6.webp" style="width:100%">
      <figcaption>5. Model the belts using the <code>Robot Belt</code> Featurescript.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/indexer-centering/slides/part-studio/s5.webp" style="width:100%">
      <figcaption>6. Model the shafts <code>Robot Shaft</code> Featurescript. The exact length of the longer shafts is somewhat arbitrary for this exercise, just make them semi long as shown.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
  <img src="../images/indexer-centering/slides/part-studio/s7.webp" style="width:100%">
      <figcaption>7. Pocket the plates using the <code>Part Lighten</code> featurescript. 
                  Recall that you can select an entire sketch to automatically select all the ribs.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/indexer-centering/slides/part-studio/s0.webp" style="width:100%">
      <figcaption>8. Finish the part studio by naming your features and organizing them into folders. Assign the part materials accordingly.</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->

<button class="prev" onclick="plusSlides(-1,0)" style="background-color: #000; color: #fff;">&#10094;</button>
<button class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</button>

  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

### Assembly Instructions

**Next, navigate to the "Exercise #8 Assembly" tab** in your copied document and **refer to the solution document** to complete the assembly for this exercise. The **following instruction slides** only provide a general outline and some key details.

<div class="slideshow-container">
  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="../images/indexer-centering/slides/assembly/s0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/indexer-centering/slides/assembly/s1.webp" style="width:100%">
      <figcaption>1. Add the part studio parts to the assembly. Like before, group mate the rigid components with the Origin Cube and mate the Origin Cube to the assembly origin. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/indexer-centering/slides/assembly/s2.webp" style="width:100%">
      <figcaption>2. Insert, fasten, and replicate the 2" long, 3/8" OD plate spacers. 
                Insert, fasten, and replicate the 1.5" long, 3/8" OD motor spacers.
                Copy and fasten the bottom gear plate to the 2" spacer.
                Insert, fasten, and replicate the 1/2" rounded hex shaft bearings.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/indexer-centering/slides/assembly/s3.webp" style="width:100%">
      <figcaption>3. Copy, fasten, and replicate the 3D printed crush block to the other tube ends.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/indexer-centering/slides/assembly/s4.webp" style="width:100%">
      <figcaption>4. Insert and fasten the motor, motor pulley, 48T 3D printed HTD pulley with 1/2" hex insert, 30T gears, and configurable spacer stacks from FRCDesignLib. Fasten the belt to the pulley. Also fasten the shafts.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/indexer-centering/slides/assembly/s5.webp" style="width:100%">
      <figcaption>5. Insert and fasten the bottom belt pulleys.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/indexer-centering/slides/assembly/s6.webp" style="width:100%">
      <figcaption>6. Insert and fasten the 6" REV Omni-wheels and 1/2" Hex MAXHubs from FRCDesignLib. Fasten the hubs to the wheels and fasten the wheel assemblies to the long shaft ends.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/indexer-centering/slides/assembly/s7.webp" style="width:100%">
      <figcaption>7. Insert, configure, and fasten 1/2" Hex spacers to fill the gap between the wheel's and plates. These can either be stacked COTS spacers, or a single custom spacer depending on preference.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/indexer-centering/slides/assembly/s8.webp" style="width:100%">
      <figcaption>8. Insert, fasten, and replicate all of the required fasteners.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="../images/indexer-centering/slides/assembly/s0.webp" style="width:100%">
      <figcaption>9. To finish the assembly, organize your components into folders and name your replicates.</figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->

<button class="prev" onclick="plusSlides(-1,1)" style="background-color: #000; color: #fff;">&#10094;</button>
<button class="next" onclick="plusSlides(1,1)" style="background-color: #000; color: #fff;">&#10095;</button>

  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

!!! Success "Verification"
    Make sure to have you and/or a more experienced member/mentor of your team [**review your CAD.!**](../1A/focusing-on-improvement.md "Focusing on Improvement Page"){:target="\_blank"}.

<br>
