# 1A: Onshape Fundamentals

## Exercise #1: Simple Box Tube

For this exercise, you will be modeling a simple 2x1 with some holes in it. For this exercise, do not use any Featurescripts. 

### Box Tubes

In FRC, robot structures are typically constructed out of aluminum box tubing, similar to wood beams for a house. Aluminum box tubing is commonly found in 2"x1", 1"x1", and 2"x2" sizes with 1/8" (thickwall) or 1/16" (thinwall) wall thicknesses. Box tubing is typically referred to by its size, eg: 2x1, 1x1, and 2x2 (Spoken as "two-by-one", "one-by-one", and "two-by-two"). For the rest of the learning course, we will use this notation when referring to box tube.


???+ Example "Box Tube Example"
    <figure>
      <img src="\img\learning-course\stage1a\tube.webp" width="45%">
      <figcaption>2x1 thinwall tube forming part of a robot structure. (Photo Credit: FRC 3647) </figcaption>
    </figure>

<br>

### Instructions

**Navigate to the "Exercise #1 Box Tube" tab** in your copied document and **follow the instructions in the slides** to complete your first exercise.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure markdown="span">
      <img src="/img/learning-course/stage1a/exercises/e1/e1s0.webp" style="width:100%; data-description="0. The final part"">
      <figcaption>0. The final part.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e1/e1s1.webp" style="width:100%; data-description="1. Start by sketching a center rectangle on the top plane."">
      <figcaption>1. Start by sketching a center rectangle on the top plane. Notice that we put the origin of the part at the center of the tube so that we can leverage the default geometry later on. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e1/e1s2.webp" style="width:100%; data-description="2. Extrude the rectangle symmetrically, 2 inches tall."">
      <figcaption>2. Extrude the rectangle symmetrically, 2" tall.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e1/e1s3.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>3. Shell the block to turn it into a 1/16" wall tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e1/e1s4.webm" type="video/webm"> 
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Add the top holes. Set the centerpoint of the hole to be vertical with the midpoint of the bottom line, then Mirror the hole across, using the front plane as the mirror line. We are able to use the front plane to mirror since we intelligently placed the origin at the center of the tube in step 1. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e1/e1s5.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. Extrude the top holes to cut all the way through the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e1/e1s6.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>6. Add the side holes. Create the layout for the side holes by creating a center point rectangle and turning it into construction geometry. Again, having the origin at the center of the tube lets us place the center of the pattern at the center of the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e1/e1s7.webp" style="width:100%; data-description="6. Name the key sketches and part. Set the material to be 6061 Aluminum."">
      <figcaption>7. Extrude the side holes to cut all the way through the tube. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1a/exercises/e1/e1s8.webm" type="video/webm">
        Your browser does not support the video tag.
      </video>
      <figcaption>8. Name the key sketches and part. You can set part appearances and materials by right clicking on the part instance. Set the material to be 6061 Aluminum. To see the mass of parts, use the <code>Display Mass Properties</code> Menu </figcaption>
    </figure>
  </div>


  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1a/exercises/e1/e1s0.webp" style="width:100%; data-description="6. Name the key sketches and part. Set the material to be 6061 Aluminum."">
      <figcaption>9. Finished Part Studio. </figcaption>
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

!!! Note
    Some sketches and features have been renamed (i.e. "Tube Profile"). You can rename sketches and features by hovering over the name in the dialogue box and clicking the pencil icon, or right clicking a sketch or feature in the feature list and clicking "rename". 

!!! Success "Verification"
    Make sure to have you and/or a more experienced member/mentor of your team review your CAD [following the instructions on the previous page](focusing-on-improvement.md)! Your box tube should weigh about 0.35 lbs. 




### Construction Geometry

Notice how we utilized construction geometry to define the location of the holes on the 2" face of the tube. Using construction geometry to assist with sketching makes your parts more parametric and betters conveys design intent compared to manually specifying the location of each hole with dimensions.


<br>

