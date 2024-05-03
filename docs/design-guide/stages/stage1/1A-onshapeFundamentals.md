<style>
.right{
    float:right;
}
.center{
    text-align:center;
}
.left{
    float:left;
}
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

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  margin-top: -22px;
  padding: 16px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
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


# 1A: Onshape Fundamentals

<span class="left">[< 0D: Theory](../stage0/0D-theory.md)</span> <span class="right">[1B: Swerve Drivebase >](1B-swerveDrivebase.md)</span>
<br>

Welcome to stage 1! Through these projects you will learn how to use some of basic tools, as well as some of the core parts in FRC and how they go together. The focus on this guide is primarily to familiarize yourself and build CAD skills within an FRC context. Please use the discord if you have any questions!

!!! Note
    If you have a bit of prior experience using Onshape's tools, you can skip the learning courses and polish your sketching and part design using a few CADvent drawings. Otherwise, please do the learning courses first; they help set a very good foundation for an efficient workflow.

## Sketching and Part Design

The sketching and part design in Onshape is very similar to Inventor, but very different from SolidWorks. There are similarities in how it works, but if you just jump into designing things, you're likely to miss a crucial part of the workflow that will make your life much harder.

[Onshape's Learning Center](https://learn.onshape.com/) provides free learning courses and articles on the entire program, from document navigation and sketching all the way to advanced surface and sheet metal modeling. Its resources on specifically sketching and part design are incredibly useful for learning the fundamentals.

Please complete these courses on the learning center to learn the fundamentals of Onshape part design. 

- [Introduction to Sketching Course](https://learn.onshape.com/courses/introduction-to-sketching)
- [Part Design Course](https://learn.onshape.com/courses/fundamentals-part-design-using-part-studios)

!!! Note
    The structure of the courses includes a few short videos and a practice per set of concepts, and don't take long to finish.

These learning courses can help both old and new designers learn a good workflow for sketching and part design.

## CADvent Part Gallery
CADvent is an advent calendar where each day has a different CAD challenge, defined with a drawing (released by FRC Team 8724 on [ChiefDelphi](https://www.chiefdelphi.com/t/cadvent-2023-2024/446060)). We've picked some of these part drawings for extra sketching and part design practice, if you feel you need it. In the future, more FRC-specific part drawings will be added. 

In the drawing slideshow below are 16 CADvent drawings. To begin, make a copy of the [CADvent practice document](https://cad.onshape.com/documents/6af40b750516bfd9d86b2203/w/1a10c33aa547ad764e1c876c/e/d57a1b029a59e3fa8c410591). Each part you make will go into a separate part studio. Some have already been set up, but you may make more if you want to do more practice parts. Use the dimensions in each drawing to guide the part. Stop before the "Bonus: Gusset" part studio! (That will be used in the next section.)

!!! Tip
    Think about how to achieve the part in as little sketches and features as possible. Feel free to ask for tips (after trying it yourself) in the beginner channels in the DDS Discord Server.

<!-- Slideshow container -->
<div class="slideshow-container">

  <!-- Full-width images with number and caption text -->
  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent1.webp" style="width:100%">
  </div>

  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent2.webp" style="width:100%">
  </div>

  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent3.webp" style="width:100%">
  </div>
  
  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent4.webp" style="width:100%">
  </div>

  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent5.webp" style="width:100%">
  </div>

  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent6.webp" style="width:100%">
  </div>

  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent7.webp" style="width:100%">
  </div>

  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent8.webp" style="width:100%">
  </div>

  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent9.webp" style="width:100%">
  </div>

  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent10.webp" style="width:100%">
  </div>

  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent11.webp" style="width:100%">
  </div>
  
  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent12.webp" style="width:100%">
  </div>
  
  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent13.webp" style="width:100%">
  </div>
  
  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent14.webp" style="width:100%">
  </div>
  
  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent15.webp" style="width:100%">
  </div>

  <div class="mySlides fade">
    <img src="/img/design-guide/stage1a/cadvents/cadvent16.webp" style="width:100%">
  </div>

  <!-- Next and previous buttons -->
  <a class="prev" onclick="plusSlides(-1)">&#10094;</a>
  <a class="next" onclick="plusSlides(1)">&#10095;</a>
</div>
<br>

<!-- The dots/circles -->
<div style="text-align:center">
  <span class="dot" onclick="currentSlide(1)"></span>
  <span class="dot" onclick="currentSlide(2)"></span>
  <span class="dot" onclick="currentSlide(3)"></span>
  <span class="dot" onclick="currentSlide(4)"></span>
  <span class="dot" onclick="currentSlide(5)"></span>
  <span class="dot" onclick="currentSlide(6)"></span>
  <span class="dot" onclick="currentSlide(7)"></span>
  <span class="dot" onclick="currentSlide(8)"></span>
  <span class="dot" onclick="currentSlide(9)"></span>
  <span class="dot" onclick="currentSlide(10)"></span>
  <span class="dot" onclick="currentSlide(11)"></span>
  <span class="dot" onclick="currentSlide(12)"></span>
  <span class="dot" onclick="currentSlide(13)"></span>
  <span class="dot" onclick="currentSlide(14)"></span>
  <span class="dot" onclick="currentSlide(15)"></span>
  <span class="dot" onclick="currentSlide(16)"></span>
</div>
<br>


## Multi-Part Modeling Practice

Now that you've had practice with sketching and part modeling, we’ll be introducing a new concept: multi-part part studios.

When designing in Onshape, you typically have 1 part studio for subassembly. The next couple of projects will slowly introduce you to this concept. Take a look at [this page](../../../design-standards/pages/sub-document-setup.md) about sub-document best practices.

Here is an example of one of the future projects that you’ll be working on. Notice how there are multiple parts inside of this one part studio, and how it “almost” looks like the completed product.

<center>![Example](\img\design-guide\stage1b\1a-Swerve.webp){width=45% height=45%}</center>

In the "bonus" part studio from the CADvent document you copied earlier, two aluminum box tubes have already been modeled for you. A new sketch has been created on top of the tubes that is ready for you to create the part profile.

For this project, you have to design a part called a "gusset" that connects two tubes. This gusset will be created in the same part studio as the tubes that it is connecting! Here's an example of a gusset:

<center>![Example](\img\design-guide\stage1a\8033-000-2024C_8.png){width=45% height=45%}</center>

Use the techniques you have learned to design this part in-context. This time you do not have a direct part drawing, so you'll have to reference the other parts in the part studio. Remember the ```Use``` tool: it's key here. Good luck!

!!! Tip
    When extruding a sketch in a part studio, you can decide whether to "add" to existing geometry, or to create a "new" part. Make sure that when you extrude your gusset, you tell Onshape to create a new part.

## Assembly Mates
The last thing to go over before we get into stage 1B, where you model a swerve drivebase, is the basic function of defining the position and motion of parts in an assembly. This section doesn't have a project but you'll use what you learn in the next projects.

When parts are inserted into an assembly, they free float. You can drag them around. The goal is to constrain the motion of all parts. There are few different ways to do this:

- **Group**: Limits the relative motion between a group of parts to none
- **Fix**: Fixes a part in space in the assembly (not recommended to use, not parametric)
- **Mates**: Tools to limit degrees of freedom between parts, using "mate connectors", automatically generated (or manually created) points with axes on parts. You can align the axes or offset in any direction or rotation you want, and different types of mates constrain different degrees of freedom. The "Fasten" mate is the most common and easy one, and limits all degrees of freedom between two parts with a single mate.

<center><img src="\img\design-guide\stage1a\mateConnectors.webp"></center>

The best practices for constraining an assembly using group, mates, and fix, as well as other tools used for assembly, such as replicate, pattern, standard content, etc. will be discovered through the projects. The best practices are also defined [here](../../../design-standards/pages/assembly-setup.md).


<br>
<center>1A: Fundamentals</center> 
<span class="left">[< 0D: Theory](../stage0/0D-theory.md)</span> <span class="right">[1B: Swerve Drivebase >](1B-swerveDrivebase.md)</span>
<br>
<br>

<script>
let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
</script>
