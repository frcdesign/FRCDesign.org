---
hide:
  - navigation
  - toc
---

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


# Website Feature Guide

Different features of the website are vital to the different sections, and can be easy to miss.

## Across the Website

- [Links](learning-course/index.md "Learning Course Landing Page"){:target="_blank"} are shown with green text
- Clicking on an image enlarges it and shows a caption, if applicable
- The website has a [glossary](resources/glossary.md "Glossary Page"){:target="_blank"} of terms related to the content. Whenever a word in that glossary is mentioned in the website, it will be underlined. You can hover over these underlined words to get a quick definition. Useful when you want to know what COTS or OTB means.
- Some information is hidden in dropdowns. Try to check most of them!
    
    ??? Example
        Information is hidden here to clean up pages.

### Admonitions

!!! Tip
    Quick tips are shown in a "Tip" box like this one.

!!! Note 
    Any extra notes about things are shown in a "Note" box like this one.

!!! Warning
    Pay attention to anything in a "Warning" box like this one.

!!! Example
    Examples for different concepts are shown in an "Example" box like this one.


## Learning Course

### Buttons
Important Onshape documents for the page will be shown as a button like the one below:

<center>[1A Exercises Document](https://cad.onshape.com/documents/812b2974ed32b9c89e8f1e25/w/747e47444b6c685bd0bee334/e/58894354f0152cd6485fe45e?renderMode=0&uiState=663d81b7afce5246f0309e28 "1A Exercises Onshape Document"){:target="_blank"  .md-button .md-button--primary}</center>

### Slideshows

<!-- Slideshow container -->
<div class="slideshow-container">

<!-- Full-width images with number and caption text -->
<div id="slide1" class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage1b/Exercise 2 Assembly.webp" style="width:65%">
        <figcaption> Navigate the slideshows by pressing the arrows on the sides. </figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <img src="/img/learning-course/stage1b/Exercise 3 Assembly.webp" style="width:65%">
        <figcaption> The dots below the slideshow indicate the slide you're on. They can also be clicked to navigate to slides. </figcaption>
    </figure>
</div>

<div class="mySlides fade">
    <figure>
        <video width="1920" controls>
            <source src="/img/learning-course/stage1b/shiftSelectEdited.webm" type="video/webm">
            Your browser does not support the video tag.
        </video>
        <figcaption> Some slideshows contain videos.</figcaption>
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


!!! Warning
    While you can click on an image to enlarge it, do not use this to navigate slideshows! Videos are not shown using this method and can be missed.


!!! Tip
    If a slideshow has issues loading, reload the webpage and it should be fixed.


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