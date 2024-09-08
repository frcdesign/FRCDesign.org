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

# 1C: Design Methodology

## Top Level Robot Assembly
Now that you have a drivebase, you can create a *top level robot assembly*. The top level robot assembly is the highest in the assembly hierarchy. Organizing the assemblies in this way keeps thing organized from both a CAD assembly and real life assembly standpoint. 

You will create a top level robot assembly to go with your drivebase. The mechanism you'll be adding is the scoring mechanism from [1678's 2023 robot](https://www.thebluealliance.com/team/1678/2023 "1678 2023 Blue Alliance Page"). The scoring mechanism CAD can be accessed from here:

<center>[1678 2023 Scoring Mechanism Document](https://cad.onshape.com/documents/28a750426de8e2bc17d5b900/w/8e79c6217ae2ce07ff57d900/e/a4d266d03289620078d13a80 "Team 1678 2023 Scoring Mechanism Onshape Document"){:target="_blank" .md-button .md-button--primary }</center>

### Instructions

Start by, **creating a new assembly tab above the `Master Sketch` part studio** and name it **`Top Level Robot Assembly`**. **Follow the instructions in the slides** to complete the top level robot assembly.

<!-- <center>**Top Level Robot Assembly**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/TopLevel/topL0.webp" style="width:100%">
      <figcaption>0. Finished top level robot assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/TopLevel/topL1.webm" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>1. Insert the drivetrain assembly and fasten the origin cube to the assembly origin. You may need to unhide the origin cube to mate it.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/TopLevel/topL2.webm" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Insert the 1678 2023 scoring assembly by pasting the scoring mechanism link into the <code>Insert</code> menu textbox. Then, fasten its origin cube to the assembly origin. You may need to hide the drivetrain's origin cube to access the origin of the assembly for mating.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/TopLevel/topL0.webp" style="width:100%">
      <figcaption>3. Finished top level assembly. </figcaption>
    </figure>
  </div>

  <!-- Next and previous buttons -->
  <button class="prev" onclick="plusSlides(-1,0)"style="background-color: #000; color: #fff;">&#10094;</button>
  <button class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</button>
  <!-- The dots/circles -->
  <div class="dotsContainer" style="text-align:center">
    <!-- Dots will be generated here -->
  </div>
</div>

!!! success "Verification"
    Your tab manager should now looks like this:
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtTabManager2.webp" style="width:100%">
    </figure>

And that's all there is to the top level robot assembly! The use of the origin cube makes it very easy to mate together assemblies. In later stages you will explore how to create flexible assemblies (arms, elevators, etc) with the origin cube. If you are interested, you can get a sneak peek [here](/best-practices/assembly-setup/#utilizing-origin-cube-for-flexible-assemblies "Origin Cube Information Page"){:target="_blank"}.


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