<style>
* {box-sizing:border-box}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Hide the images by default */
.mySlides {
  display: none;
}
#slide1 {display:block}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 250px;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 3px 3px 3px 3px;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.6);
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 0.25s;
}

@keyframes fade {
  from {opacity: .4}
  to {opacity: 1}
}
</style>

# 1C: Design Methodology - Simple Swerve Drivebase

## Drivetrain Master Sketches
To begin, you will be creating a layout sketch of the drivetrain. This will dictate the size and position of the drive tubes. The layout will be drawn from the side and top view of the drivetrain. For your swerve drivebase, you will make it 26"x26".

### Instructions

Start by **creating a new Onshape Document called `Stage 1C Robot`** and within it, **a new part studio called `Master Sketch`**. Then, use the `Origin Cube` Featurescript to create an origin cube. **Follow the instructions in the slides** to complete the master sketch.


<!-- <center>**Drivetrain Layout Sketch Slides**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtFinalLayout.webp" style="width:100%">
      <figcaption>0. The final layout sketch.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/originCube.webp" style="width:100%">
      <figcaption>1. Start by inserting the origin cube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtSideLayout1.webp" style="width:100%">
      <figcaption>2. Draw the side profile of the drivetrain on the Right Plane. We place the tube 1.75" from the ground, which is the offset from the ground to the bottom of the tube for the MK4i modules.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtSideLayout2.webp" style="width:100%">
      <figcaption>3. Draw the wheel clearance box, which represents the area that the wheel takes up. For the MK4i modules, the box is 4.625" wide. The side layout of the drivebase is now finished.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtTopLayout1.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Create the top layout sketch by using the bottom mate connector on the vertical line of the side layout. Utilizing auto-generated mate connectors for sketch planes is a very useful tool to have. Press the “Top” button on the view cube to get a top view.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtTopLayout2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>5. Sketch the top outline of the drive base. Make the rectangle a square and set the side length equal to the length of the side layout tube. This ensures that the size of the top layout always matches the side layout, which makes the design parametric. Notice that the sketch is fully defined despite having no sketch dimensions.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtTopLayout3.webp" style="width:100%">
      <figcaption>6. To sketch the tubes, draw a square 1" smaller than the previous square. This will represent the four 2"x1" tubes that make up the outer frame. Then, draw the top profile of the 2"x2" tube.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtTopLayout4.webp" style="width:100%">
      <figcaption>7. Next, we need to make the cutouts on the drivetube for the swerve modules. Start by drawing two lines, each offset by 4.25" from the edge. This is the required offset for MK4i modules. Other modules will differ.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtTopLayout5.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>8. To apply the cutout for all four tubes, we use the <code>Circular Pattern</code> sketch tool to copy the lines to all four corners. For a  <code>Circular Pattern</code> we first define the number of instances and then the axis of rotation.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtFinalLayout.webp" style="width:100%">
      <figcaption>9. Finally, name your sketches and organize them into folders in the feature tree. Your sketches should all be fully defined.</figcaption>
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

As previously explained, this method of top-down modeling is extremely powerful as it enables you to capture the most important dimensions all in one place. However, you should be careful to not over-detail master sketches. You will be practicing master sketches all throughout Stage 2, and use them in Stage 3 alongside multi-document practices to design a whole robot.

<br>

<!-- ------------------DO NOT TOUCH ANYTHING BELOW HERE------------------ -->

<script>

// Initialize slide index for each slideshow

let slideIndices = [0];

let slideshows = document.getElementsByClassName("slideshow-container");
  for (let no = 0; no < slideshows.length; no++) {
    slideIndices[no] = 1;
    let dotsContainer = slideshows[no].getElementsByClassName("dotsContainer")[0];
    let slides = slideshows[no].getElementsByClassName("mySlides");
    for (let i = 0; i < slides.length; i++) {
      let dot = document.createElement("span");
      dot.className = "dot";
      dot.onclick = function() { currentSlide(i+1, no); };
      dotsContainer.appendChild(dot);
    }
    showSlides(1, no);
  }

  currentSlide(1);

// Next/previous controls
function plusSlides(n, no) {
  showSlides(slideIndices[no] += n, no);
}

// Thumbnail image controls
function currentSlide(n, no) {
  showSlides(slideIndices[no] = n, no);
}

function showSlides(n, no) {
  let i;
  let x = document.getElementsByClassName("slideshow-container")[no].getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("slideshow-container")[no].getElementsByClassName("dot");
  if (n > x.length) {slideIndices[no] = 1}    
  if (n < 1) {slideIndices[no] = x.length}
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  x[slideIndices[no]-1].style.display = "block";  
  dots[slideIndices[no]-1].className += " active";
}

</script>