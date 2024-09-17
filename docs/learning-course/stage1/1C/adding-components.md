

# 1C: Design Methodology - Simple Swerve Drivebase

## Adding More Components

When you model more parts in the part studio, you can insert them into the assembly in a similar to fashion to before. Hit insert and immediately click on the green checkmark. Then, edit the initial `Group` you made and add the part to the group. By doing this, you ensure that added parts will always stay in the same place it was modeled in the part studio.

Let's add a gusset to connect the 2"x2" tube to the 2"x1" tube.

### Instructions

Start by **navigating to the `Drivetrain` Part Studio** in the `Drivetrain` folder. **Follow the instructions in the slides** to add the gusset.

<!-- <center>**Adding a Gusset**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtAdd0.webp" style="width:100%">
      <figcaption>0. Finished drivetrain assembly.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtAdd1.webp" style="width:100%">
      <figcaption>1. Add the gusset for the crosstube with the <code>Gusset</code> Featurescript.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtAdd2.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>2. Insert the gusset into the assembly and add it to the <code>Group</code>.</figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtAdd3.webp" style="width:100%">
      <figcaption>3. Copy the gusset and mate it to the other side. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <video width="1920" controls>
        <source src="/img/learning-course/stage1c/SwerveBase/dtAdd4.mp4" type="video/mp4">
        Your browser does not support the video tag.
      </video>
      <figcaption>4. Edit the replicate feature to add rivets to the gusset. </figcaption>
    </figure>
  </div>

  <div class="mySlides fade">
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtAdd0.webp" style="width:100%">
      <figcaption>4. Finished drivetrain assembly.</figcaption>
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

Make sure you sort the instances in your assembly into folders (i.e. frame, swerve modules) and name any patterns and replicates used. This will help you locate components in the assembly later down the line.

!!! success "Verification"
    If all is done correctly your assembly should weigh approximately 37.2lbs.

    Your tab manager should have the following tabs and folder:
    <figure>
      <img src="/img/learning-course/stage1c/SwerveBase/dtTabManager.webp" style="width:100%">
    </figure>

### Level of Detail

It should be noted that while modeling every detail of the robot hardware (bolts, rivets, nuts) is beneficial for purchasing and real life assembly purposes, it isn't strictly necessary. Time is a precious resource, especially during build season, so you should spend it on what will give you the biggest return.

More details about best practices for Onshape assemblies are included on the [Assembly Best Practices Page](/best-practices/assembly-setup/ "Assembly Best Practices Page"){:target="_blank"}.


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