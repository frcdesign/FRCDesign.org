# 1C: Practice Mechanisms

## Exercise 8: Indexer Centering

In this exercise, you will be modeling a centering indexer for 9.5" diameter balls, similar to [1678's 2022 indexer](https://www.youtube.com/watch?v=RiUaItTKomUhttps://www.youtube.com/watch?v=RiUaItTKomU "1678 2022 Robot Reveal Video"){:target="_blank"}. This mechanism features belts, chain, gear, and tube crush blocks. Be sure to pay attention to the plate sketches when modeling. 

### Crush Blocks
3D-printed crush blocks can be used to reinforce thin-walled tubing in assemblies where bolts pass through without a plate. 
Since the strength of bolts comes from their clamping force, without anything to support the thin walls, the tube can collapse before achieving proper clamping force. 
Crush blocks distribute the load, allowing for full clamping force while maintaining the tube’s structural integrity.

Alternatively, a "crush plate" can also be utilized to distribute the fastener force to achieve a similar effect as a crush block.

In this exercise, you will use a [configurable 3D printed crush block](https://cad.onshape.com/documents/e9e11d824a8fd8257028a1dc/v/0c7982f1d3823153c353cbdb/e/b6f099050d1db039691ace49 "Configurable Crush Block Onshape Document"){:target="_blank"}.

???+ example "Crush Blocks and Crush Plates"
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/crush-blocks.webp" width="65%">
      <figcaption>A 3D printed crush block (left) and crush plate (right). Crush plates tend to work well for the middle of the tubes where it may be difficult to insert a crush block.</figcaption>
    </figure>

### Part Studio Instructions

**Navigate to the "Exercise #8 Part Studio" tab** in your copied document and **refer to the solution document** to complete the part studio for this exercise. The **following instruction slides** only provide a general outline and some key details.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/s0.webp" style="width:100%">
      <figcaption>0. Final Part Studio.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/s1.webp" style="width:100%">
      <figcaption>1. Begin by creating the layout sketch on the top plane.
                  Just like with the previous exercise, we define the distance between the rollers by mirroring the indexer wheel.
                  We add 0.016" to the chain c-c to account for stretch in the chain.  </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/s2.webp" style="width:100%">
      <figcaption>2. Model the thin-wall 2x1 tubes with Extrude Individual and Tube Converter.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/s3.webp" style="width:100%">
      <figcaption>3. Model the top plates and bottom plates. 
                  The top plates can be modeled in the same sketch since they are on the same plane.
                  Pay close attention to the plate constraints in the solution document.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/s4.webp" style="width:100%">
      <figcaption>4. Pocket the plates using the <code>Part Lighten</code> featurescript. 
                  Recall that you can select an entire sketch to automatically select all the ribs.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/index-centering/s5.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. Model the #25 chain using the <code>Belt & Chain Gen</code> Featurescript.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/s6.webp" style="width:100%">
      <figcaption>6. Model the 5mm HTD belt.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/s7.webp" style="width:100%">
      <figcaption>7. Model the shafts.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/s0.webp" style="width:100%">
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
      <img src="/img/learning-course/stage1c/index-centering/a0.webp" style="width:100%">
      <figcaption>0. Final assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/a1.webp" style="width:100%">
      <figcaption>1. Add the part studio parts to the assembly. Like before, group mate the rigid components with the Origin Cube and mate the Origin Cube to the assembly origin. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/a2.webp" style="width:100%">
      <figcaption>2. Insert, fasten, and replicate the 2" long, 3/8" OD plate spacers. 
                Insert, fasten, and replicate the 1.5" long, 3/8" OD motor spacers.
                Copy and fasten the bottom gear plate to the 2" spacer.
                Insert, fasten, and replicate the 1/2" rounded hex shaft bearings.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/index-centering/a3.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>3. Insert, fasten, and replicate the 3D printed crush blocks from the document linked at the top of this page.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/a4.webp" style="width:100%">
      <figcaption>4. Insert and fasten the motor, motor pulley, 48T 3D printed HTD pulley with 1/2" hex insert, 30T gears, and configurable spacer stacks fro MKCad. Fasten the belt to the pulley. Also fasten the shafts.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/index-centering/a5.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. Insert and fasten the chain sprockets. Then, fasten the chain to the sprocket.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/index-centering/a6.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>6. Insert and fasten the 6" Omni-wheels from <a href="https://cad.onshape.com/documents/a65c1d6e95e4616e720a3f09/v/a6fbccfafd4bcd323ed0cb23/e/26e504413265b4491ec033b8?showReturnToWorkspaceLink=true" target="_blank">this document</a> and MAXHubs from MKCad.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/a7.webp" style="width:100%">
      <figcaption>7. Insert, configure, and fasten the Configurable Spacer Stack to fill the gap on the wheel shaft.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/a8.webp" style="width:100%">
      <figcaption>8. Insert, fasten, and replicate all of the required fasteners. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/index-centering/a0.webp" style="width:100%">
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

!!! note "Verification"
    If all is done correctly your assembly should have 63 Instances.

<br>