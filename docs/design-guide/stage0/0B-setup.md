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

## Registering for Onshape

Onshape offers a free education license for students to use their software. It is highly recommended to use the education plan, as it allows for the creation of private documents, as well as other useful features.

To start registering, go to the [Onshape for Education](https://onshape.com/education-plan){:target="_blank"} page and select "Create EDU ACCOUNT" or click [this link](https://www.onshape.com/en/education/sign-up). Follow the slides below to finish registering.

<br>

<!-- Slideshow container -->
  <div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div id="slide1" class="mySlides fade">
      <figure>
          <img src="/img/design-guide/stage0/setup/signup.webp" style="width:90%; border:5px solid #ADADAD">
          <figcaption> Fill out the details in the sign up form. </figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/design-guide/stage0/setup/edusignup2.webp" style="width:90%; border:5px solid #ADADAD">
          <figcaption> On the next screen, select that you are a student and that you are in grade school.</figcaption>
      </figure>
  </div>

  <div class="mySlides fade">
      <figure>
          <img src="/img/design-guide/stage0/setup/edusignup3.webp" style="width:60%; border:5px solid #ADADAD">
          <figcaption> Finally, fill the form with your school information. You may enter "Robotics" as the reason for using Onshape. </figcaption>
      </figure>
  </div>


  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1,0)" style="background-color: #000; color: #fff;">&#10094;</a>
  <a class="next" onclick="plusSlides(1,0)" style="background-color: #000; color: #fff;">&#10095;</a>
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

??? Warning "Chrome Browser Setup"
    If you are using Chrome, an additional setup step may be required.

    First, type `chrome://settings/` in your searchbar to navigate to chrome settings. Make sure that "Use graphics acceleration when available" is enabled. Relaunch chrome if you have updated it to enable it.

    <center><img src="/img/design-guide/stage0/setup/chrome/graphicsacceleration.webp" style="border:5px solid #ADADAD"></center>

    Next, go to `chrome://flags/` and enable these:

    <center><img src="/img/design-guide/stage0/setup/chrome/flags.webp" style="border:5px solid #ADADAD"></center>

If your team uses Onshape, contact your mentor/design lead for access to the Onshape classroom/team.




## Setting up MKCad

MKCad is an Onshape plugin that contains a large library of parts that are often useful in FRC.

To install it, go to the [MKCad App](https://appstore.onshape.com/apps/Manufacturers%20Models/2ZT7X5D646R3LM3ZND7LGBTYRVM4SVH6CDDGM6I=/description){:target="_blank"} in the Onshape Appstore.

Press "Subscribe", then "Get for Free". This will automatically add MKCad to your Onshape account.

!!! Note
    After subscribing, the MKCAD inserter won't show up in already open documents until you reload. This is a first-time thing though.

??? Video "Video Tutorial"
    <video width="1920" controls="true" allowfullscreen="true" poster="/img/design-guide/stage0/setup/subscribe.webp">
      <source src="/img/design-guide/stage0/setup/MKCADsetup.webm" type="video/webm">
      Your browser does not support the video tag.
    </video>


## Featurescripts
Featurescripts are custom features coded by members of the community, and are often handy tools that assist with the FRC design process. For now, follow the instructions below to install just the featurescripts you'll use in stage 1A. More thorough instructions for installing featurescripts, a list of all recommended featurescripts, and some troubleshooting tips are found on the [featurescripts page](../../resources/featurescripts.md).

1. Open the document [Julia's Featurescripts](https://cad.onshape.com/documents/95c00401c440b44ad8799ef5/w/1f1ebce01a3b8eb6fa102975/e/b92d638809ae48771ecc7ad8){:target="_blank"}

2. Click "Custom Features" 

3. Click "Belts", "Chain Path", "Extrude Individual", "FilletXpert", "Shaft", "Spacer", and **"Tube Converter"** (this one is important)

??? Video "Video Tutorial"
    <video width="1920" controls="true" allowfullscreen="true" poster="../../../../img/design-guide/stage0/setup/addingJulia'sFeaturescripts.webp">
      <source src="../../../../img/design-guide/stage0/setup/addingJulia'sFeaturescripts.webm" type="video/webm">
      Your browser does not support the video tag.
    </video>

Once you have that done, you are ready for the next stage!

## OPTIONAL: Onshape Educator Plan 
Besides individual setup, if your team uses Onshape or are switching to it, one of your mentors or design leads should get the Educator plan and add all members to a "classroom". The Educator plan is free for FIRST teams and will make document management easier. It also provides a suite of features for all students added to the "classroom", such as simulation, release management, and classes/assignments. 

We recommend you read the ChiefDelphi post linked below for a better overview and walkthrough to set it up for your team.

[Onshape Educator Plan: What it Means for FRC Teams](https://www.chiefdelphi.com/t/onshape-educator-plan-what-it-means-for-frc-teams/446394)

<br>

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