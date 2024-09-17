<style>
* {box-sizing:border-box}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

.mySlides {
    display:none;
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

# 2A: Full Detail Drivebase


## Exercise: Bellypan Pocketing

Some teams may choose to pocket their bellypan to reduce weight and make wiring easier. A pocketed bellypan can save around 3-4 lbs. However, this will add significant machining time if you are manufacturing the bellypan yourself or increase cost if you are purchasing the bellypan from a fabrication service (eg: [Fabworks](https://fabworks.com/ "Fabworks Sheet Metal Services"){:target="_blank"}). You should carefully consider the tradeoffs with your team.

### Instructions

**If you choose to pocket your bellypan for your Stage 1C Drivetrain**, you can **follow the instructions in the slides** which utilize the `Vent` [Featurescripts](../../../resources/featurescripts.md "Featurescripts Page"){:target="_blank"}. You could also use the `Lighten`, or `Part Lighten` [Featurescripts](../../../resources/featurescripts.md "Featurescripts Page"){:target="_blank"} to pocket the bellypan. While the workflow may vary slightly between each Featurescript, the general idea is the same. A diamond pattern is recommended for strength and ease of modeling.

<!-- <center>**Sample Bellypan Pocketing Slides**</center> -->
<!-- Slideshow container -->
<div class="slideshow-container">
    <!-- Full-width images with number and caption text -->
    <div id="slide1" class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/pocket/pocket1s0.webp" style="width:100%">
            <figcaption>0. Pocketed bellypan. </figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/pocket/pocket1s1.webp" style="width:100%">
            <figcaption>1. Draw two perpendicular lines that are offset 45 degrees from vertical. </figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/pocket/pocket1s2.webp" style="width:100%">
            <figcaption>2. Linear pattern the lines until they completely cover the bellypan. These will be the ribs for the bellypan.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/pocket/pocket1s3.webp" style="width:100%">
            <figcaption>3. Offset the outline of the bellypan 0.5”.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/pocket/pocket1s4.webp" style="width:100%">
            <figcaption>4.  Connect any islands that might result from mounting holes being too far from a rib. One way to fix this is to add a slot connecting the island to a rib.</figcaption>
        </figure>
    </div>
    <div class="mySlides fade">
        <figure>
            <img src="/img/learning-course/stage2-drivebase/pocket/pocket1s0.webp" style="width:100%">
            <figcaption>5. Use a pocketing Featurescript to pocket the bellypan. Recommended settings are 0.15” wide ribs and 3/16” tool radius.</figcaption>
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



<br>
