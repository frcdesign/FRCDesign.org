<style>
* {box-sizing:border-box}

details {
        font-size: 0.7rem !important;
    }   

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


# 2E: Cascade Elevator

## Layout Sketches

Elevator master sketches usually start with an extended side view so you can drive the length of it based off of the extension limits and your required beginning and end position for whatever mechanism you're moving. 

Though this elevator doesn't have that context, it's still useful to follow the same workflow of starting with a side sketch, which will contain most important dimensions but can be hard to conceptualize at first.

Follow the instructions in the slides to create your elevator layout sketches.

<!-- Slideshow container -->
<div class="slideshow-container">
    <!-- Full-width images with number and caption text -->
    <div id="slide1" class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-elevator/master-sketch.webp" style="width:40%">
            <figcaption>A clean view of the front sketch of the elevator tubes.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-elevator/elevatorSideExtendedSketch.webp" style="width:75%" style="border:5px solid #ADADAD">
            <figcaption> As practice for stage 3, we'll start with defining the position of the elevator in relation to drivetrain side sketch. Use rectangles to represent the 2x2 tube and the length of the stages. Add rectangles to represent the bottom tubes of each stage and carriage as well. </figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-elevator/elevatorSideRetractedSketch.webp" style="width:70%" style="border:5px solid #ADADAD">
            <figcaption> Feel free to create a retracted side sketch (constraining it to the geometry of the first side sketch) to help double check geometry and integration. This especially helpful when designing a full robot. </figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-elevator/elevatorFrontSketch.webp" style="width:75%" style="border:5px solid #ADADAD">
            <figcaption> Now add the front sketch to define all the elevator tubes, the width of the elevator, and the distance between stages on the side.</figcaption>
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

!!! Tip
    Instead of creating "extended" and "retracted" views, you can separate the stages into their own individual side sketches to let you "animate" how it moves in the sketch. You can use configurations to do this.

<br>

