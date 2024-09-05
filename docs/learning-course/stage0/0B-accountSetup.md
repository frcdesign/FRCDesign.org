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
  right: 0px;
  border-radius: 3px 3px 3px 3px;
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

# 0B: Onshape Setup

!!! Tip
    Remember to take a look at the [website feature guide](../../website-feature-guide.md "Website Feature Guide Page"){:target="_blank"} to gain an understanding of the different features used throughout the learning course!

## Registering for Onshape

Onshape offers a free education license for students to use their software. It is highly recommended to use the education plan, as it allows for the creation of private documents, as well as other useful features.

To start registering, go to the [Onshape for Education](https://onshape.com/education-plan "Onshape Education Plan"){:target="_blank"} page and select "Create EDU ACCOUNT" or click [this link](https://www.onshape.com/en/education/sign-up "Onshape Sign Up Page"){:target="_blank"}. Follow the slides below to finish registering.

<br>

<!-- Slideshow container -->
  <div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
      <figure>
          <img src="/img/learning-course/stage0/setup/signup.webp" style="width:90%; border:5px solid #ADADAD">
          <figcaption> Fill out the details in the sign up form. </figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/learning-course/stage0/setup/edusignup2.webp" style="width:90%; border:5px solid #ADADAD">
          <figcaption> On the next screen, select that you are a student and that you are in grade school.</figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/learning-course/stage0/setup/edusignup3.webp" style="width:60%; border:5px solid #ADADAD">
          <figcaption> Finally, fill the form with your school information. You may enter "Robotics" as the reason for using Onshape. </figcaption>
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

Onshape will proceed to check your information (which may take some time), then send a verification email to activate your account. You'll be asked to set a password, then you'll enter your dashboard.

### Account Setup

The first time you enter Onshape, it will prompt you to set up your account, including the default units and mouse controls used when doing CAD. You can also set a profile picture and a nickname (we recommend keeping this as your real name). Finally, Onshape will run a browser check, to ensure compatibility. 

!!! Note

    If the browser check fails, you may want to try a different browser. Currently, chromium browsers like Chrome, Edge, Opera, and Arc are the best supported browsers for Onshape, but Firefox usually works with no issues as well. Safari is not well supported.

!!! Warning "Chrome Browser Setup"
    If you are using Chrome, an additional setup step may be required.

    First, type `chrome://settings/` in your searchbar to navigate to chrome settings. Make sure that "Use graphics acceleration when available" is enabled. Relaunch chrome if you have updated it to enable it.

    <center><img src="/img/learning-course/stage0/setup/chrome/graphicsacceleration.webp" style="border:5px solid #ADADAD"></center>

    Next, go to `chrome://flags/` and enable these:

    <center><img src="/img/learning-course/stage0/setup/chrome/flags.webp" style="border:5px solid #ADADAD"></center>

If your team uses Onshape, contact your mentor/design lead for access to the Onshape classroom/team.
<br>

## OPTIONAL: Onshape Educator Plan 
Besides individual setup, if your team uses Onshape or are switching to it, one of your mentors or design leads should get the Educator plan and add all members to a "classroom". The Educator plan is free for FIRST teams and will make document management easier. It also provides a suite of features for all students added to the "classroom", such as simulation, release management, and classes/assignments. 

If you are interested, direct your design lead or mentors to read the ChiefDelphi post linked below for a better overview and walkthrough to set it up for your team.

[Onshape Educator Plan: What it Means for FRC Teams](https://www.chiefdelphi.com/t/onshape-educator-plan-what-it-means-for-frc-teams/446394 "Onshape Educator Plan Chief Delphi Thread"){:target="_blank"}

<!-- ------------------DO NOT TOUCH ANYTHING BELOW HERE------------------ -->

<script>
// Initialize slide index for each slideshow
let slideIndices = [];

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